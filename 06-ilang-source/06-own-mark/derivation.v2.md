# The own mark of a body: dressed levels, clock spacings, inertia at second order

- **Subproject:** 06-ilang-source
- **Package:** 06-own-mark
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-19

## Changes from previous version

- Steps 5, 6, 7 and Result (6.8)–(6.13): every perturbative result now carries the isolation condition (6.4) for the levels it uses, with the sufficient conditions of Step 3 ($`2t_fN_f<M_k`$ for one level, $`2t_fN_f<m`$ for all levels at $`\sigma=+`$, $`P=0`$). In v1 they were stated only under $`2t_f<m`$, $`4t_f\le m`$ or $`2t_f<M_k`$, which do not imply (6.4) for $`N_f\ge2`$ (review v1, I1).
- Step 6 and Result (6.12), (6.13): the second-order inequality of inertia and cost for (a) and (a′) is stated on an explicit region, $`0<\tau<\tau_0(L,M_k,t_f)`$ inside the isolation condition, in place of "at leading order in $`\tau^2`$". This follows the restriction of items 2 and 3 in the question's note of 2026-10-19.
- Open issues: the two items settled by that note are removed: the sign of $`\Delta''_{k,+}`$ beyond leading order in $`\tau^2`$, and the non-necessity of $`4t_f\le m`$ for (a).
- Code: paths moved to `code/v2/`, and the section notes that the parameters of the check satisfy $`2t_fN_f<m`$. The script is unchanged except for its version label, and it was re-run; its numbers are identical to those of v1.

## Setup and assumptions

**Field** (assumption, M8; the class of 04-profile). A ring of places $`x\in\mathbb Z_L`$, $`L\ge3`$; $`N_f\ge1`$ identical field objects with $`c=+1`$, no pair terms among them, own terms $`C_1=-t_f\sum_x(\lvert x\rangle\langle x+1\rvert+\lvert x+1\rangle\langle x\rvert)`$ with $`t_f>0`$ (assumption of the class); $`\Phi_x`$ is the number of field objects at $`x`$, $`n:=N_f/L`$, $`C_f`$ the sum of the own terms. One object has the eigenvectors $`\lvert q\rangle=L^{-1/2}\sum_xe^{iqx}\lvert x\rangle`$, $`q\in\frac{2\pi}L\mathbb Z_L`$, with eigenvalues $`-2t_f\cos q`$. In $`\mathcal H_{\rm adm}`$ (symmetric states) the field eigenstates are occupation states. The lowest one, $`\lvert\Omega_f\rangle`$ (all objects at $`q=0`$), is unique, with eigenvalue $`-2t_fN_f`$. An excited state has the label $`Q=\sum_jq_j`$ and the excitation energy $`E_{\rm exc}=\sum_j\varepsilon_{q_j}>0`$, where $`\varepsilon_q:=2t_f(1-\cos q)\in(0,4t_f]`$ for $`q\ne0`$.

**Body** (assumption). One Model D body on the same ring, with $`\tau>0`$, $`m>0`$, clock levels $`\lvert f_k\rangle`$, $`M_k=m+d_k`$ and $`\delta_c:=M_{k+1}-M_k=\frac{2\pi}{N\lambda_0}`$. The couplings (a) and (c), with constant $`\gamma`$, are those of the question. Records are taken at $`\kappa\to0`$. For $`\kappa>0`$ the record term $`\kappa xX`$ is not invariant under the joint translation of the ring, so the sectors below do not exist; this case is not treated.

**Inputs** (quoted). (5.5) and (5.6) of 04-ilang-time/05-moving-clock, with normalized plane waves $`\lvert p\rangle\to L^{-1/2}\lvert p\rangle`$:
```math
C_k(p)=-\tau\sin p\,\sigma_1+\mu_k\sigma_3,\quad \omega_k(p)=\sqrt{\mu_k^2+\tau^2\sin^2p},\quad \beta_{k,+}=\begin{pmatrix}\cos\frac{\theta_k}2\\ \sin\frac{\theta_k}2\end{pmatrix},\ \beta_{k,-}=\begin{pmatrix}-\sin\frac{\theta_k}2\\ \cos\frac{\theta_k}2\end{pmatrix},\ \tan\theta_k=-\frac{\tau\sin p}{\mu_k},
```
with $`\mu_k=M_k`$. (6.7) of 04-ilang-time/06-inertia-internal-energy: $`M_k=m+d_k`$, gap $`2M_k`$, $`\omega_k''(0)=\tau^2/M_k`$. (4.2) of 04-profile: $`E(g)=N_f\,\varepsilon_0(g)`$, where $`\varepsilon_0(g)`$ is the lowest eigenvalue of the one-object contract $`h(g)`$ with the held sources.

**Notation.** $`M_\sigma:=\sigma M_k`$, $`b_q:=\tau\lvert\sin q\rvert`$, $`K_\sigma(q):=\varepsilon_q(2M_\sigma-\varepsilon_q)+b_q^2`$, and $`S_0:=\sum_{q\ne0}\varepsilon_q^{-1}=\frac{L^2-1}{12t_f}`$ (standard sum $`\sum_{j=1}^{L-1}(1-\cos\frac{2\pi j}L)^{-1}=\frac{L^2-1}6`$).

**Regime** (A13). Expansion in $`\gamma`$ at fixed $`L,N_f,t_f,\tau,m,N,\lambda_0`$; every $`O(\gamma^3)`$ is meant at fixed $`L`$. We use perturbation theory for an isolated eigenvalue, with its conditions stated in Step 3.

## Derivation

### Step 1. Sectors, continuation in $`P`$, invariance

Let $`T`$ shift the position label of the body and of every field object by $`+1`$, and let $`Q_k=\lvert f_k\rangle\langle f_k\rvert`$ act on the clock label. Both operators are built from places alone, commute with every swap of field objects, and commute with $`C`$. Every term of $`C`$ is invariant under a common shift on the ring, and the clock label enters $`C`$ only through $`D`$ (in $`B`$ and in the couplings), which is diagonal in $`\lvert f_k\rangle`$. The sector $`(k,P)`$ is $`Q_k=1`$, $`T=e^{-iP}`$, $`P\in\frac{2\pi}L\mathbb Z_L`$, inside $`\mathcal H_{\rm adm}`$; it contains the start $`(p=P,\sigma,k)\otimes\lvert\Omega_f\rangle`$.

Every matrix element of $`C`$ either keeps the body label $`x_b`$ or changes it by $`\pm1`$: the motion term does, and so does the bond factor of (c). For $`L\ge3`$ these three classes are distinct, so the split $`C=C^{(0)}+C^{(+)}+C^{(-)}`$ by the change of $`x_b`$ is fixed by $`C`$ alone. On the states $`L^{-1/2}\sum_xe^{iPx}\lvert x,s,f_k\rangle\otimes\lvert x+\vec r\rangle`$ (relative field positions $`\vec r`$, symmetrized), a step $`x_b\to x_b+1`$ at fixed field positions lowers every $`r_j`$ by one and gives a factor $`e^{-iP}`$. Hence
```math
C_k(P)=\hat C^{(0)}+e^{-iP}\hat C^{(+)}+e^{iP}\hat C^{(+)\dagger},\qquad\text{(6.1)}
```
where the $`\hat C`$ are independent of $`P`$ and act on (branch)$`\otimes`$(relative field configurations). For real $`P`$, (6.1) is a Hermitian family analytic in $`P`$, and at $`P\in\frac{2\pi}L\mathbb Z_L`$ it is $`C`$ on the sector $`(k,P)`$. The quantities $`E_{k,\sigma}(P)`$ and $`E''_{k,\sigma}(0)`$ refer to its eigenvalue branch.

**Invariance (M6, Law 5, (1.2)).**
- The sectors are fixed by places, types and families. The matrix (6.1) is fixed by the matrix elements of the total contract, and the dressed level by the family $`C(\gamma)`$ and its limit at $`\gamma\to0`$.
- Any replacement of listed terms that leaves $`C(\gamma)`$ unchanged therefore leaves unchanged: the eigenvalues of (6.1), their differences between levels, their $`P`$-derivatives, and their Taylor coefficients in $`\gamma`$.
- Relabelling the field objects maps each sector onto itself, and eigenvalues do not see the common phase.
- The splits used below (body, field and coupling; mean field and fluctuation) are only means of computation. For example, $`\gamma M_k\sigma_3\Phi_{x_b}=\gamma nM_k\sigma_3+\gamma M_k\sigma_3(\Phi_{x_b}-n)`$ moves a term diagonal in the body's places between a pair term and an own term (A5). This changes the body's "rest term" but not $`C`$. Only eigenvalue data of $`C`$ are reported.
- The parameters in the results are eigenvalue data of $`C(0)`$:
  - $`M_k=\frac12[E_{k,+}(0)-E_{k,-}(0)]_{\gamma=0}`$ and $`\delta_c=M_{k+1}-M_k`$;
  - $`\tau^2=M_kE''_{k,+}(0)|_{\gamma=0}`$;
  - $`\varepsilon_q`$ are the field's excitation energies;
  - $`n`$ counts objects and places.

### Step 2. The contract on a clock level; mean field and vertex

On $`Q_k=1`$, $`D`$ acts as $`d_k`$, so
```math
\begin{aligned}\text{(a)}:\ C\big|_k&=A+M_k\sigma_3\textstyle\sum_x\lvert x\rangle\langle x\rvert(1+\gamma\Phi_x)+C_f,\\ \text{(c)}:\ C\big|_k&=\text{(a)}+\gamma\tfrac\tau2\textstyle\sum_x\bigl(\lvert x+1\rangle\langle x\rvert(-i\sigma_1)+\lvert x\rangle\langle x+1\rvert(i\sigma_1)\bigr)\tfrac12(\Phi_x+\Phi_{x+1}).\end{aligned}\qquad\text{(6.2)}
```
The level enters only through $`M_k`$. Hence, exactly and at every order in $`\gamma`$, $`E_{k,\sigma}(P)=\mathcal E_\sigma(P;M_k)`$ with one function $`\mathcal E_\sigma`$ for all levels. A clock level is dressed like a body without clock label whose $`m`$ is replaced by $`M_k`$.

**Mean field.** Write $`\Phi_x=n+\delta\Phi_x`$, and let $`\gamma W`$ be the part of (6.2) that contains $`\delta\Phi_x`$. The mean-field part is $`A+(1+\gamma n)M_k\sigma_3+C_f`$ for (a) and $`(1+\gamma n)(A+M_k\sigma_3)+C_f`$ for (c). By (5.5)–(5.6) of 04-ilang-time/05-moving-clock its body eigenvalues are $`\sigma\tilde\omega_k(p)`$, with $`\tilde\omega_k^{(a)}=[(1+\gamma n)^2M_k^2+\tau^2\sin^2p]^{1/2}`$ and $`\tilde\omega_k^{(c)}=(1+\gamma n)\omega_k(p)`$.

**Vertex.** $`\Phi_x`$ is a sum of one-object operators. It has $`\langle\Omega_f\vert\delta\Phi_x\vert\Omega_f\rangle=0`$ and $`\delta\Phi_x\lvert\Omega_f\rangle=\frac{\sqrt{N_f}}L\sum_{q\ne0}e^{-iqx}\lvert q\rangle_f`$, where $`\lvert q\rangle_f`$ is the normalized symmetric state with one object at $`q`$ (excitation $`\varepsilon_q`$). The sum over $`x`$ enforces $`p'=P-q`$. For (c), the bond factor gives $`\frac\tau2\cdot\frac{1+e^{-iq}}2\cdot i(e^{iP}-e^{-i(P-q)})\sigma_1=-\frac\tau2(\sin P+\sin(P-q))\sigma_1`$. With (5.5) this yields
```math
\langle P-q,\sigma';q\vert\,\gamma W\,\vert P,\sigma;\Omega_f\rangle=\gamma\frac{\sqrt{N_f}}L\langle\beta_{\sigma'}(P-q)\vert\hat V_q\vert\beta_\sigma(P)\rangle,\qquad \hat V_q=\begin{cases}M_k\sigma_3&\text{(a)}\\ \tfrac12[C_k(P)+C_k(P-q)]&\text{(c)},\end{cases}\qquad\text{(6.3)}
```
and all other matrix elements of $`W`$ from $`\lvert P,\sigma;\Omega_f\rangle`$ vanish.

### Step 3. Existence and isolation

At $`\gamma=0`$ the eigenvalues of the sector $`(k,P)`$ are $`\sigma'\omega_k(P-Q)+E_{\rm exc}-2t_fN_f`$. The dressed level starts at $`\sigma\omega_k(P)-2t_fN_f`$, and it is a simple eigenvalue iff
```math
\sigma\omega_k(P)\neq\sigma'\omega_k(P-Q)+E_{\rm exc}\quad\text{for every excited field eigenstate }(Q,E_{\rm exc})\text{ and }\sigma'=\pm\qquad\text{(6.4)}
```
(the case $`\lvert\Omega_f\rangle`$, $`\sigma'=-\sigma`$ is excluded by $`\omega_k\ge M_k>0`$). Under (6.4) the eigenvalue of the analytic Hermitian family (6.1), (6.2) is simple and isolated. By Rellich's theorem the dressed level exists, is analytic in $`\gamma`$ and $`P`$, and has the Rayleigh–Schrödinger expansion. This holds for $`\lvert\gamma\rvert`$ small against the distance of the level from the rest of the sector spectrum, divided by the vertex scale $`M_k(n/L)^{1/2}`$ of (6.3). That distance is at most $`\varepsilon_{2\pi/L}+\omega_k(2\pi/L)-M_k=O(L^{-2})`$: consider the state with the body at $`-2\pi/L`$ in the same branch and one field object at $`2\pi/L`$. The range therefore shrinks as $`L`$ grows. A level that is simple at $`P=0`$ stays simple for real $`P`$ near $`0`$, which is all that $`E''(0)`$ needs.

At $`P=0`$:
- **$`\sigma=+`$.** $`\omega_k(Q)+E_{\rm exc}>M_k`$ for every excited state, so only $`\sigma'=-`$ can coincide, at $`E_{\rm exc}=M_k+\omega_k(Q)\ge2M_k`$. Since $`E_{\rm exc}\le4t_fN_f`$, (6.4) holds if $`2t_fN_f<M_k`$. The one-object excitations, the only ones that enter the second order, stay below the gap if $`2t_f<M_k`$. When field excitations reach $`M_k+\omega_k(Q)`$, the level lies among states "lower branch plus excited field". On the finite ring it is then isolated only away from exact coincidences, with a range in $`\gamma`$ set by the nearest one. For $`L\to\infty`$ these states become dense (decay through the field); this case is not treated.
- **$`\sigma=-`$.** Only $`\sigma'=-`$ can coincide, at $`E_{\rm exc}=\omega_k(Q)-M_k<(M_k^2+\tau^2)^{1/2}-M_k`$. So (6.4) holds if $`\varepsilon_{2\pi/L}>(M_k^2+\tau^2)^{1/2}-M_k`$. For one-object excitations it holds if $`\tau^2\le2t_fM_k`$, since $`\omega_k(q)-M_k<\tau^2\sin^2q/(2M_k)\le\varepsilon_q\tau^2/(2t_fM_k)`$ when $`\sin q\ne0`$, and $`\omega_k(q)-M_k=0<\varepsilon_q`$ when $`\sin q=0`$.

For $`N_f=1`$ the one-object excitations are all the excitations.

### Step 4. The dressed level through second order

We take the mean-field contract as unperturbed and $`\gamma W`$ as the perturbation. The first order vanishes. The second order involves only $`\lvert P-q,\sigma';q\rangle`$, $`q\ne0`$, with denominators $`\sigma\omega_k(P)-\sigma'\omega_k(P-q)-\varepsilon_q`$; bare values suffice, since mean-field values change only $`O(\gamma^3)`$. The sum over $`\sigma'`$ uses $`\sum_{\sigma'}\frac{\lvert\beta_{\sigma'}\rangle\langle\beta_{\sigma'}\rvert}{z-\sigma'\omega'}=(z-C_k(p'))^{-1}=\frac{z+C_k(p')}{z^2-\omega'^2}`$, which holds because $`C_k(p')^2=\omega_k(p')^2`$. The result is
```math
E_{k,\sigma}(P)=\sigma\tilde\omega_k(P)-2t_fN_f+\gamma^2\frac nL\sum_{q\ne0}G_{k,\sigma}(P,q)+O(\gamma^3),\qquad G_{k,\sigma}=\langle\beta_\sigma(P)\vert\hat V_q\,(z_q-C_k(P-q))^{-1}\hat V_q\vert\beta_\sigma(P)\rangle,\qquad\text{(6.5)}
```
with $`z_q=\sigma\omega_k(P)-\varepsilon_q`$. To make $`G`$ explicit, set $`\Omega:=\sigma\omega_k(P)`$, $`\omega'^2:=M_k^2+\tau^2\sin^2(P-q)`$ and $`s_\pm:=M_k^2\pm\tau^2\sin P\sin(P-q)`$. From (5.6), $`\langle\sigma_1\rangle=-\tau\sin P/\Omega`$ and $`\langle\sigma_3\rangle=M_k/\Omega`$ in $`\beta_\sigma(P)`$. This gives $`\langle\sigma_3C_k(p')\sigma_3\rangle=s_-/\Omega`$ and $`\langle C_k(p')\rangle=s_+/\Omega`$. For (c), $`\hat V_q\beta_\sigma(P)=\frac12(\Omega+C_k(p'))\beta_\sigma(P)`$, and functions of $`C_k(p')`$ commute. Hence
```math
G^{(a)}=\frac{M_k^2(z_q+s_-/\Omega)}{z_q^2-\omega'^2},\qquad G^{(c)}=\frac{z_q(\Omega^2+\omega'^2)+2\Omega\omega'^2+(s_+/\Omega)(\Omega^2+\omega'^2+2\Omega z_q)}{4(z_q^2-\omega'^2)}.
```
$`G`$ depends on $`\sigma`$ only through $`\Omega`$, and $`\sigma\tilde\omega_k`$ likewise. The $`\sigma=-`$ results therefore follow from the $`\sigma=+`$ ones by $`M_k\to-M_k`$, with $`\omega_k(P)`$ read as $`M_k(1+\tau^2\sin^2P/M_k^2)^{1/2}`$.

At $`P=0`$ we have $`\Omega=M_\sigma`$ and $`z_q^2-\omega'^2=-K_\sigma(q)`$:
```math
G^{(a)}_{k,\sigma}(0,q)=-\frac{M_k^2(2M_\sigma-\varepsilon_q)}{K_\sigma(q)},\qquad G^{(c)}_{k,\sigma}(0,q)=-\frac{M_k^2(2M_\sigma-\varepsilon_q)+b_q^2(M_\sigma-\varepsilon_q/4)}{K_\sigma(q)}.\qquad\text{(6.6)}
```
For both couplings $`\sigma\tilde\omega_k(0)=(1+\gamma n)M_\sigma`$ exactly. The $`\gamma^2`$ coefficient of $`E_{k,\sigma}(0)`$, the cost of the own mark, is therefore $`\Delta_{k,\sigma}:=\gamma^2\frac nL\sum_{q\ne0}G_{k,\sigma}(0,q)`$.

- **Sign, $`\sigma=+`$.** If $`2t_f<M_k`$, then $`2M_k-\varepsilon_q>0`$, so $`K_+>0`$ and both numerators are positive: $`\Delta_{k,+}<0`$, for every $`\tau`$.
- **Sign, $`\sigma=-`$.** If $`\tau^2\le2t_fM_k`$, then $`K_-=-[(M_k+\varepsilon_q)^2-\omega_k(q)^2]<0`$ (Step 3), while $`M_k^2(2M_k+\varepsilon_q)`$ and $`M_k^2(2M_k+\varepsilon_q)+b_q^2(M_k+\varepsilon_q/4)`$ are positive: $`\Delta_{k,-}<0`$.
- **Dependences.** $`\Delta`$ is linear in $`N_f`$ at fixed $`L`$ (the squared vertex is proportional to $`N_f`$, the denominators do not depend on it). It depends on $`k`$ only through $`M_k`$ and on $`\sigma`$ through $`M_\sigma`$; $`t_f`$ and $`L`$ enter through $`\varepsilon_q`$ and the set of labels.

**Held body, $`\tau=0`$.** The body label is conserved, and the field sees the held source $`g=\sigma\gamma M_k`$ at $`x_b`$. $`\varepsilon_0`$ is simple (Perron–Frobenius, $`t_f>0`$), hence analytic in $`g`$. By (4.2) of 04-profile,
```math
E_{k,\sigma}(P)\big|_{\tau=0}=\sigma M_k+N_f\,\varepsilon_0(\sigma\gamma M_k)\ \ \text{for all }P\ \text{and all }\gamma,\qquad N_f\varepsilon_0(g)=-2t_fN_f+gn-g^2\tfrac nLS_0+O(g^3).\qquad\text{(6.7)}
```
The second expression uses $`\lvert\langle q\vert x_b\rangle\langle x_b\vert0\rangle\rvert^2=L^{-2}`$. Hence $`\Delta_{k,\sigma}|_{\tau=0}=-\gamma^2M_k^2N_f(L^2-1)/(12t_fL^2)`$ for both branches and both couplings. It is proportional to $`M_k^2`$ and to $`1/t_f`$, and at fixed $`n`$ it grows like $`L`$.

### Step 5. Clock spacings

Let $`G_+(M,q)`$ denote $`G_{k,+}(0,q)`$ of (6.6) as a function of $`M_k=M`$ (by (6.2)). Assume (6.4) for $`\sigma=+`$, $`P=0`$ at the levels $`k`$ and $`k+1`$; since $`M_{k+1}>M_k`$, $`2t_fN_f<M_k`$ suffices (Step 3). Then (6.5) gives
```math
E_{k+1,+}(0)-E_{k,+}(0)=(1+\gamma n)\,\delta_c+\gamma^2\frac nL\sum_{q\ne0}\bigl[G_+(M_{k+1},q)-G_+(M_k,q)\bigr]+O(\gamma^3).\qquad\text{(6.8)}
```
The first order is a common rescaling by $`1+\gamma n`$ for both couplings. The second-order change is a common rescaling iff $`F(M):=\sum_qG_+(M,q)`$ is affine on $`\{M_k\}`$; this is a condition only for $`N\ge3`$, since $`N=2`$ has a single spacing.

At fixed $`\varepsilon=\varepsilon_q`$, $`b=b_q`$, set $`K=\varepsilon(2M-\varepsilon)+b^2`$. Then $`G^{(a)}_+=-\frac{M^2}\varepsilon+\frac{M^2b^2}{\varepsilon^2(2M+a)}`$ with $`a:=\frac{b^2}\varepsilon-\varepsilon`$, $`\frac{M^2}{2M+a}=\frac M2-\frac a4+\frac{a^2}{4(2M+a)}`$, and $`G^{(c)}_+=G^{(a)}_+-\frac{b^2}{2\varepsilon}\bigl[1+\frac{\varepsilon^2/2-b^2}K\bigr]`$. Differentiating twice in $`M`$:
```math
\partial_M^2G^{(a)}_+=-\frac2\varepsilon\Bigl[1-\frac{b^2(b^2-\varepsilon^2)^2}{K^3}\Bigr],\qquad \partial_M^2G^{(c)}_+=-\frac2\varepsilon\Bigl[1-\frac{b^6}{K^3}\Bigr].\qquad\text{(6.9)}
```
- **(c).** $`K>b^2`$ whenever $`\varepsilon<2M`$, so $`\partial_M^2G^{(c)}_+<0`$.
- **(a).** If $`\varepsilon\le M`$, then $`K>\varepsilon^2`$ and $`K>b^2`$. For $`b\ge\varepsilon`$, $`b^2(b^2-\varepsilon^2)^2<b^6<K^3`$; for $`b<\varepsilon`$, $`b^2(\varepsilon^2-b^2)^2<b^2\varepsilon^4<K^3`$. So $`\partial_M^2G^{(a)}_+<0`$.

Hence $`F`$ is strictly concave for $`M\ge m`$ if $`\varepsilon_q<2m`$ for all $`q`$ (c), sufficient $`2t_f<m`$, or if $`\varepsilon_q\le m`$ for all $`q`$ (a), sufficient $`4t_f\le m`$. Take the region $`2t_fN_f<m`$ for (c), and $`2t_fN_f<m`$, $`4t_f\le m`$ for (a). There (6.4) holds for $`\sigma=+`$, $`P=0`$ at every level, since $`M_k\ge m`$ (Step 3), so (6.8) holds for every $`k`$; and $`F`$ is strictly concave, for (c) because $`2t_fN_f<m`$ implies $`2t_f<m`$. In this region the second-order change of the spacing, $`\gamma^2[F(M_{k+1})-F(M_k)]`$, strictly decreases with $`k`$. It is not $`\delta_c`$ times one factor for all $`k`$. At $`\tau=0`$ the change is $`-\gamma^2\frac nLS_0\,\delta_c(M_k+M_{k+1})`$ by (6.7), for every $`t_f`$.

### Step 6. Curvature and inertia

$`\sigma\tilde\omega''_k(0)`$ is $`\sigma\tau^2/((1+\gamma n)M_k)`$ for (a) and $`\sigma(1+\gamma n)\tau^2/M_k`$ for (c). Differentiating (6.5) twice at $`P=0`$, where $`G`$ is analytic under (6.4), gives
```math
E''_{k,\sigma}(0)=\sigma\frac{\tau^2}{M_k}\times\begin{cases}1-\gamma n+\gamma^2n^2&\text{(a)}\\ 1+\gamma n&\text{(c)}\end{cases}+\Delta''_{k,\sigma}+O(\gamma^3),\qquad \Delta''_{k,\sigma}:=\gamma^2\frac nL\sum_{q\ne0}\partial_P^2G_{k,\sigma}(P,q)\big|_{P=0}.\qquad\text{(6.10)}
```

**Leading order in $`\tau^2`$.** Take (a), $`\sigma=+`$, and expand to first order in $`\tau^2`$ and second order in $`P`$:
- $`z_q+s_-/\Omega=2M-\varepsilon+Z`$, with $`Z=\frac{\tau^2P^2}{2M}-\frac{\tau^2}M[\sin P\sin(P-q)+\frac{P^2}2]`$;
- $`z_q^2-\omega'^2=-K_0+Y`$, with $`K_0:=\varepsilon(2M-\varepsilon)`$ and $`Y=\frac{\tau^2P^2(M-\varepsilon)}M-\tau^2\sin^2(P-q)`$.

So $`G=-\frac{M^2}\varepsilon-\frac{M^2}{K_0}[Z+Y/\varepsilon]`$, with $`Z''=-2\tau^2c/M`$, $`Y''=2\tau^2\frac{M-\varepsilon}M-2\tau^2\cos2q`$, $`c:=\cos q`$, and $`4\sin^2q/\varepsilon_q=2(1+c)/t_f`$. For (c), the same expansion turns the numerator of $`G^{(c)}`$ into $`4M^2(2M-\varepsilon)+4Mu(3M-\varepsilon)+w(4M-\varepsilon)+2Mv(2M-\varepsilon)`$, with $`u=\frac{\tau^2P^2}{2M}`$, $`w=\tau^2\sin^2(P-q)`$, $`v=\frac{\tau^2}M[\sin P\sin(P-q)-\frac{P^2}2]`$. With $`\varepsilon=\varepsilon_q`$:
```math
\partial_P^2G^{(a)}_{k,+}\big|_0=\frac{2M_k\tau^2(1+c)(1-M_k/t_f)}{\varepsilon(2M_k-\varepsilon)},\qquad \partial_P^2G^{(c)}_{k,+}\big|_0=-\frac{\tau^2(1+c)\bigl[2M_k^2/t_f+2M_k(2c-1)-\varepsilon c\bigr]}{\varepsilon(2M_k-\varepsilon)}.\qquad\text{(6.11)}
```
The relative corrections are $`O(\tau^2/M_k^2)`$ and $`O(\tau^2/(M_kt_fq_1^2))`$ with $`q_1=2\pi/L`$; the latter comes from the term $`2\tau^2\sin q\cos q\,P`$ of the denominator. For $`\sigma=-`$, replace $`M_k\to-M_k`$.

**Sign for $`2t_f<M_k`$.** Every term of (6.11) is $`\le0`$, and $`<0`$ for $`c\ne-1`$:
- (a): because $`1-M_k/t_f<0`$;
- (c): set $`\mu:=M_k/t_f>2`$. The bracket divided by $`t_f`$ is $`2\mu^2+2\mu(2c-1)-2c(1-c)`$. It increases with $`c`$ on $`[-1,1]`$ (its derivative is $`\ge4\mu-6>0`$) and equals $`2(\mu-1)(\mu-2)>0`$ at $`c=-1`$.

So $`\Delta''_{k,+}<0`$ at leading order in $`\tau^2`$.

**Inertia against cost.** Assume (6.4) for $`\sigma=+`$ at $`P=0`$, sufficient $`2t_fN_f<M_k`$ (Step 3), so that (6.5) and (6.10) hold. $`E_{k,+}(0)`$ contains the field's eigenvalue $`-2t_fN_f`$, so the comparison is between changes. Write $`\delta X:=X(\gamma)-X(0)`$, a difference of eigenvalue data of two total contracts of the family, which M6 allows. The base value is $`1/E''_{k,+}(0)|_{\gamma=0}=M_k/\tau^2`$ ((6.7) of 04-ilang-time/06-inertia-internal-energy). Then $`\delta E_{k,+}(0)=\gamma nM_k+\Delta_{k,+}+O(\gamma^3)`$, while $`\delta(1/E''_{k,+}(0))`$ equals $`\frac{\gamma nM_k}{\tau^2}-\frac{M_k^2}{\tau^4}\Delta''_{k,+}`$ for (a) and $`\frac{M_k}{\tau^2}(-\gamma n+\gamma^2n^2)-\frac{M_k^2}{\tau^4}\Delta''_{k,+}`$ for (c), up to $`O(\gamma^3)`$. Hence
```math
\delta\Bigl(\frac1{E''_{k,+}(0)}\Bigr)-\frac{\delta E_{k,+}(0)}{\tau^2}=\begin{cases}-\dfrac1{\tau^2}\Bigl[\dfrac{M_k^2}{\tau^2}\Delta''_{k,+}+\Delta_{k,+}\Bigr]&\text{(a)}\\[2mm] \dfrac{M_k}{\tau^2}(-2\gamma n+\gamma^2n^2)-\dfrac1{\tau^2}\Bigl[\dfrac{M_k^2}{\tau^2}\Delta''_{k,+}+\Delta_{k,+}\Bigr]&\text{(c)}\end{cases}\ +O(\gamma^3).\qquad\text{(6.12)}
```
- **(a).** The first-order parts agree. The own-mark parts do not, in the region $`2t_fN_f<M_k`$, $`0<\tau<\tau_0`$, with some $`\tau_0>0`$ that depends on $`L`$, $`M_k`$, $`t_f`$. There (6.4) holds and $`2t_f<M_k`$, so $`\Delta_{k,+}<0`$ for every $`\tau`$ (Step 4). By (6.11), $`\Delta''_{k,+}/\tau^2`$ tends to a negative limit as $`\tau\to0^+`$. It is continuous in $`\tau`$, being a finite sum of functions analytic under (6.4), so $`\Delta''_{k,+}<0`$ on some interval $`0<\tau<\tau_0`$. On that interval the own mark lowers the cost and raises the inertia, and the bracket is negative.
- **(c).** The two sides differ already at first order. The uniform part multiplies the motion and rest terms alike: the curvature grows by the factor $`1+\gamma n`$, while the cost grows by $`\gamma nM_k`$.
- **Heavy body.** For $`M_k\gg t_f`$, at leading order in $`\tau^2`$ and for both couplings: $`-\frac{M_k^2}{\tau^4}\Delta''_{k,+}\approx\frac{\gamma^2nM_k^3(L-1)(L-2)}{6\tau^2t_f^2L}`$, using $`\sum_{q\ne0}\frac{1+\cos q}{\varepsilon_q}=\frac{(L-1)(L-2)}{6t_f}`$. By contrast $`\Delta_{k,+}/\tau^2\approx-\frac{\gamma^2nM_k^2(L^2-1)}{12\tau^2t_fL}`$. The relative changes therefore grow like $`+M_k^2`$ for the inertia and $`-M_k`$ for the cost.

By (6.2), for (a) and (c), $`1/E''_{k,\sigma}(0)`$ and $`\delta E_{k,\sigma}(0)`$ of every level are those of a clockless body with rest parameter $`M_k`$: one function of $`M_k`$ for all levels.

### Step 7. Controls

**(i) $`\tau\to0`$.** (6.7) holds for both couplings: $`E''_{k,\sigma}\equiv0`$ at every $`\gamma`$, so the curvature inertia is not defined, with or without the mark. Item 3 is void, and the mark changes only the cost. The spacings are $`\delta_c+N_f[\varepsilon_0(\gamma M_{k+1})-\varepsilon_0(\gamma M_k)]`$. $`\varepsilon_0`$ is strictly concave: $`\varepsilon_0''=2\sum_{j\ne0}\lvert\langle j\vert x_b\rangle\langle x_b\vert\varphi_0\rangle\rvert^2/(\varepsilon_0-\varepsilon_j)<0`$, because the lowest eigenvector $`\varphi_0`$ of $`h(g)`$ has positive components and so is not $`\lvert x_b\rangle`$. Hence, at every order, the spacing changes strictly decrease with $`k`$: there is no common rescaling for $`N\ge3`$.

**(ii) Rest-only coupling.** Replace the (a) term by $`\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes\sigma_3\otimes m\mathbb 1_N\otimes\Phi_x`$ (a′), and add the bond term of (c) to get (c′). The level-$`k`$ contract now depends on $`M_k`$ and on $`m`$ separately, so the analogue of (6.2) fails. At $`P=0`$ the mean field gives $`M_k+\gamma nm`$, and the vertex is $`m\sigma_3`$ (a′) or $`m\sigma_3+\frac\tau2\sin q\,\sigma_1`$ (c′). Repeating Step 4 gives
```math
G^{(a')}_{k,+}(0,q)=-\frac{m^2}{\varepsilon_q}+\frac{m^2b_q^2}{\varepsilon_qK_+(q)},\qquad G^{(c')}_{k,+}(0,q)=-\frac{m^2}{\varepsilon_q}+\frac{(m-\varepsilon_q/2)^2b_q^2}{\varepsilon_qK_+(q)}.\qquad\text{(6.13)}
```
The coupling vanishes at $`\gamma=0`$, so the start and the criterion (6.4) are those of Step 3. We work in the region $`2t_fN_f<m`$, where (6.4) holds for $`\sigma=+`$, $`P=0`$ at every level and $`2t_f<m`$. There $`1/K_+`$ is positive, strictly decreasing and strictly convex in $`M_k`$.
- **Spacings.** They are unchanged at first order. At $`\tau=0`$ they are unchanged at every order, for every $`t_f`$: the shift $`N_f\varepsilon_0(\gamma m)`$ is the same for all levels. For $`\tau>0`$ and $`2t_fN_f<m`$, their second-order changes are negative and strictly increasing in $`k`$, so there is no common factor for $`N\ge3`$.
- **Inertia, (a′).** $`G^{(a')}=(m^2/M_k^2)G^{(a)}`$ at every $`P`$, and the mean field gives $`1/E''=(M_k+\gamma nm)/\tau^2`$. So (6.12) holds with the bracket multiplied by $`m^2/M_k^2`$. The two changes are equal at first order. They are unequal at second order for $`2t_fN_f<m`$ and $`0<\tau<\tau_0`$, with $`\tau_0`$ as in Step 6.
- **Inertia, (c′).** $`E''=(1+\gamma n)^2\tau^2/(M_k+\gamma nm)`$ at first order, so $`\delta(1/E'')=\gamma n(m-2M_k)/\tau^2\ne\delta E/\tau^2=\gamma nm/\tau^2`$.
- **Dependence on $`M_k`$.** In neither control is level $`k`$ dressed like a clockless body with rest parameter $`M_k`$. At $`\tau=0`$ the own-mark cost $`-\gamma^2m^2\frac nLS_0`$ is the same for every level, whereas that body under (a) has $`-\gamma^2M_k^2\frac nLS_0`$.

## Result

Class: couplings (a), (c); every $`N_f\ge1`$, $`L\ge3`$, $`t_f>0`$, every level $`k`$, both branches; records at $`\kappa=0`$. Every $`O(\gamma^3)`$ is at fixed $`L`$. Every perturbative result, (6.5), (6.6) and (6.8)–(6.13) apart from their exact $`\tau=0`$ parts, holds under (6.4) for the levels and branches it uses.

- **(6.1), (6.2)** (definition and theorem, exact). The sectors $`(k,P)`$ and the continuation $`C_k(P)`$ are fixed by places and by the total contract, so the dressed levels, their differences, their $`P`$-curvature and their $`\gamma`$-coefficients are M6-invariant. For (a) and (c) the level-$`k`$ contract depends on $`k`$ only through $`M_k`$. At every order, therefore, $`E_{k,\sigma}(P)=\mathcal E_\sigma(P;M_k)`$, where $`\mathcal E_\sigma(P;M)`$ is the dressed level of a body without clock label and with rest parameter $`M`$ under the same coupling. This is one function for all levels, and it carries the cost, the spacings and the curvature inertia.
- **(6.4)** (criterion). The starting level is a simple eigenvalue of its sector at $`\gamma=0`$ iff (6.4) holds. Under (6.4) the dressed level exists, is isolated, and is analytic in $`\gamma`$ and $`P`$. Sufficient conditions at $`P=0`$:
  - $`\sigma=+`$: sufficient $`2t_fN_f<M_k`$; the one-object excitations stay off the gap if $`2t_f<M_k`$.
  - $`\sigma=-`$: sufficient $`\varepsilon_{2\pi/L}>(M_k^2+\tau^2)^{1/2}-M_k`$; for one-object excitations, $`\tau^2\le2t_fM_k`$.

  When field excitations reach $`M_k+\omega_k(Q)\ge2M_k`$, the upper level lies among lower-branch states with an excited field. It is then isolated on the finite ring only away from exact coincidences.
- **(6.5)** (formula, $`O(\gamma^3)`$, under (6.4)). $`E_{k,\sigma}(P)=\sigma\tilde\omega_k(P)-2t_fN_f+\gamma^2\frac nL\sum_{q\ne0}G_{k,\sigma}(P,q)`$ for real $`P`$ near $`0`$, with $`G`$ explicit for both couplings. The $`\sigma=-`$ result follows from $`\sigma=+`$ by $`M_k\to-M_k`$, with $`\omega_k`$ read as in Step 4.
- **(6.6)** (formula, $`O(\gamma^3)`$, under (6.4)). The own-mark cost at $`P=0`$ is $`\Delta_{k,\sigma}=\gamma^2\frac nL\sum_qG_{k,\sigma}(0,q)`$, with closed forms for (a) and (c).
  - Sign: $`\Delta_{k,+}<0`$ for $`2t_f<M_k`$ and every $`\tau`$; $`\Delta_{k,-}<0`$ for every $`\tau`$ with $`\tau^2\le2t_fM_k`$.
  - Dependences: linear in $`N_f`$ at fixed $`L`$; $`k`$ only through $`M_k`$; $`\sigma`$ through $`M_\sigma`$.
- **(6.7)** (formula, exact in $`\gamma`$, $`\tau=0`$). $`E_{k,\sigma}=\sigma M_k+N_f\varepsilon_0(\sigma\gamma M_k)`$, independent of $`P`$. Its second order is $`-\gamma^2M_k^2N_f(L^2-1)/(12t_fL^2)`$ for both branches and both couplings, growing like $`L`$ at fixed $`n`$.
- **(6.8), (6.9)** (negative, $`O(\gamma^3)`$, $`N\ge3`$). (6.8) holds under (6.4) for $`\sigma=+`$, $`P=0`$ at the levels $`k`$, $`k+1`$, sufficient $`2t_fN_f<M_k`$. The first-order change of the spacings is the common factor $`1+\gamma n`$. The second-order change strictly decreases with $`k`$, so it is not a common rescaling of the clock. This holds in the region $`2t_fN_f<m`$ for (c), and $`2t_fN_f<m`$, $`4t_f\le m`$ for (a); both regions lie inside (6.4) for every level. At $`\tau=0`$ the change is $`-\gamma^2\frac nLS_0\delta_c(M_k+M_{k+1})`$ for every $`t_f`$.
- **(6.10), (6.11)** (formula, $`O(\gamma^3)`$, under (6.4)). (6.10) gives the curvature at all $`\tau`$. (6.11) gives its leading order in $`\tau^2`$, with relative corrections $`O(\tau^2/M_k^2,\ \tau^2L^2/(M_kt_f))`$. There, for $`2t_f<M_k`$, $`\Delta''_{k,+}<0`$ for both couplings.
- **(6.12)** (negative, $`O(\gamma^3)`$, under (6.4) for $`\sigma=+`$ at $`P=0`$, sufficient $`2t_fN_f<M_k`$). The change of the curvature inertia is not the change of the cost divided by $`\tau^2`$:
  - (a): equal at first order; unequal at second order in the region $`2t_fN_f<M_k`$, $`0<\tau<\tau_0`$ with some $`\tau_0(L,M_k,t_f)>0`$, where the own mark raises the inertia and lowers the cost;
  - (c): unequal already at first order.

  For (a) and (c), by (6.2), the curvature inertia and the cost of level $`k`$ are those of a clockless body with rest parameter $`M_k`$, for every level.
- **(6.13)** (control, $`O(\gamma^3)`$).
  - $`\tau\to0`$ (exact, every $`t_f`$): $`E''\equiv0`$, so the inertia is undefined. The spacing changes strictly decrease with $`k`$ at every order, so there is no common rescaling for $`N\ge3`$.
  - Rest-only coupling, in the region $`2t_fN_f<m`$ (inside (6.4) for $`\sigma=+`$, $`P=0`$, every level): the spacings are not changed at first order (nor at any order at $`\tau=0`$, for every $`t_f`$). For $`\tau>0`$ they change at second order without a common factor ($`N\ge3`$).
  - Rest-only coupling, inertia, in the same region: the change of the inertia equals the change of the cost$`/\tau^2`$ at first order for (a′) but not for (c′). Through second order it equals it for neither: for (a′) for $`0<\tau<\tau_0`$ as in (6.12); for (c′) already at first order.
  - Rest-only coupling, dependence on $`M_k`$: level $`k`$ is not dressed like a clockless body with rest parameter $`M_k`$.

## Consistency checks

1. **Dimensions.** $`\gamma`$ and $`\Phi_x`$ are numbers. $`G`$ has the dimension of a cost ($`M_k^2/\varepsilon_q`$), and so do $`E''`$ ($`P`$ is a number) and $`\tau^2/M_k`$. Both $`1/E''`$ and $`M_k/\tau^2`$ are inverse costs. Passed.
2. **Held body.** At $`\tau=0`$, (6.6) gives $`G=-M_k^2/\varepsilon_q`$ for both couplings and both branches, i.e. $`\Delta_{k,\sigma}=-\gamma^2M_k^2\frac nLS_0`$. This is the second order of $`N_f\varepsilon_0(\sigma\gamma M_k)`$ from (4.2) of 04-profile in (6.7). Passed.
3. **Branch sum rule.** $`\sum_{\sigma'}\lvert\langle\beta_{\sigma'}\vert\hat V_q\vert\beta_\sigma\rangle\rvert^2=\langle\hat V_q^2\rangle`$ requires $`G\to-\langle\hat V_q^2\rangle/\varepsilon_q`$ for large $`\varepsilon_q`$. (6.6) gives $`-M_k^2/\varepsilon_q`$ for (a) and $`-(M_k^2+b_q^2/4)/\varepsilon_q`$ for (c), which equal $`\langle M_k^2\rangle`$ and $`\langle\frac14(C_k(0)+C_k(-q))^2\rangle`$ at $`P=0`$. Passed.

## Open issues

- The upper level when field excitations reach the gap (embedded level, decay through the field as $`L\to\infty`$) is not treated, and neither is the limit $`L\to\infty`$ at fixed $`n`$, where the own-mark cost grows like $`L`$.
- Records with $`\kappa>0`$, which break the joint translation, and orders above $`\gamma^2`$ are not treated.
- The code checks only $`N_f=1`$, so multi-object coincidences in (6.4) are not tested numerically.
- The fall of the dressed body in the field of another source is left to a later package.

## Code

- `code/v2/check_own_mark.py` (role: check).
  - **Method.** Exact diagonalization of the sector matrix (6.1) for $`N_f=1`$ on rings $`L=6,10`$, with couplings (a) and (c), levels $`k=0,1,2`$ ($`t_f=1`$, $`m=3`$, $`\delta_c=0.5`$, so $`2t_fN_f<m`$ and (6.4) holds for $`\sigma=+`$), both branches, $`\tau=1,0.25`$ and $`\gamma=0.01,0.02,0.04,0.08`$. The exact curvature at $`P=0`$ comes from the second-order Hellmann–Feynman formula, cross-checked by a finite difference of (6.1). The second-order curvature is the exact $`P`$-derivative of (6.5), computed by a Cauchy integral.
  - **Outputs.** `code/v2/output/check_own_mark.log` (summary) and `code/v2/output/check_own_mark.csv` (all rows).
  - **Findings.**
    - (6.6) agrees with (6.5) at $`P=0`$ to $`6.7\times10^{-16}`$.
    - The deviation of the exact $`E_{k,\sigma}(0)`$, $`E''_{k,\sigma}(0)`$ and the spacings from (6.5), (6.10), (6.8) scales as $`\gamma^{p}`$ with $`p=2.91`$–$`3.11`$ in all cases.
    - The relative deviation of (6.11) from (6.10) decreases fourfold when $`\tau`$ is halved ($`\le1.6\times10^{-2}`$ at $`\tau=0.2`$).
    - The second-order spacing change per unit spacing is $`-0.505`$ ($`k=0`$) and $`-0.585`$ ($`k=1`$) for (a), $`L=6`$, $`\tau=1`$.
    - In all 24 cases of section D, $`\Delta_{k,+}<0`$ and $`\Delta''_{k,+}<0`$.

## Methods used

- Joint-translation sectors and relative coordinates (analytic continuation in the total label)
- Mean-field and fluctuation split; Rayleigh–Schrödinger perturbation theory to second order
- Analytic perturbation theory of a simple eigenvalue (Rellich); 2×2 resolvent identity
- Concavity of the lowest eigenvalue; Perron–Frobenius
- Exact diagonalization; Hellmann–Feynman second derivative; Cauchy-integral derivative
