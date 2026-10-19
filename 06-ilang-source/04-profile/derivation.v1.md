# Profile of the mutual cost of two held sources on a hopping field

- **Subproject:** 06-ilang-source
- **Package:** 04-profile
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-19

## Setup and assumptions

- **Field (assumption, M8).** $`N_f\ge1`$ identical field objects, family $`c=+1`$, no pair terms among them. Each has the places $`X_f`$ of a finite connected graph $`\Gamma`$ with adjacency matrix $`A_\Gamma`$, own term $`C_1=-t_fA_\Gamma`$, $`t_f>0`$, and $`\Phi_x=\sum_{j}\lvert x\rangle\langle x\rvert_j`$. Graphs: ring of $`L\ge3`$ places, square torus $`L\times L`$, cubic torus $`L^3`$ ($`L\ge3`$), nearest-neighbour edges. They are regular of degree $`z=2D`$ ($`D=1,2,3`$) and vertex-transitive. $`\Lambda:=z\mathbb 1-A_\Gamma`$ is the graph Laplacian, so $`C_1=t_f(\Lambda-z\mathbb 1)`$; $`\Lambda^+`$ is its pseudo-inverse ($`\Lambda^+\mathbf 1=0`$); $`n:=N_f/\lvert X_f\rvert`$.
- **Sources (A15, M8).** Held bodies at $`x_1\neq x_2`$ in eigenvectors of their $`G`$ with eigenvalues $`g_1,g_2`$. A held body has no motion term and its state is an eigenvector of every operator by which it enters $`C`$, so its state is conserved and $`C`$ acts on the field as $`\sum_j h_j(g)`$ with $`h(g):=C_1+V`$, $`V:=g_1\lvert x_1\rangle\langle x_1\rvert+g_2\lvert x_2\rangle\langle x_2\rvert`$. Two bodies of one type in the swap-symmetrized state give the same $`V`$ in both terms; nothing changes.
- **State (assumption, M9).** Lowest state: the eigenvector of the field contract with sources connected to the lowest one without them. Control: the highest state.
- **Distance.** $`d`$ is the graph distance; on the tori $`\mathbf d=x_1-x_2`$ with components in $`(-L/2,L/2]`$, and $`\lvert\mathbf d\rvert`$ is its Euclidean length. On the ring $`w:=d(L-d)/L^2\in[0,\tfrac14]`$.
- **Mutual cost** (as in 03-held-sources). With $`E(g_1,g_2)`$ the field cost (1.8) in the stated state, the part depending on both $`g_1`$ and $`g_2`$ is
```math
M(g_1,g_2):=E(g_1,g_2)-E(g_1,0)-E(0,g_2)+E(0,0).\qquad\text{(4.1)}
```
It is computed from the total contract and the state only (M6). $`M^{(k)}`$ denotes its part of order $`k`$ in $`(g_1,g_2)`$.
- **Input** (item 4), (17.15) of 03-ilang-space/17-motion: for the chain $`h_m`$ with $`K_{h_m}=mX`$, $`d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X`$.
- **Tools.** Perron–Frobenius; Rayleigh–Schrödinger perturbation theory for a simple isolated eigenvalue (convergent at least while $`\lVert V\rVert`$ is below half the gap, Kato); Fourier diagonalization on tori; standard lattice and continuum Green-function asymptotics. $`\Lambda`$ is the explicit matrix of $`C_1`$; no field equation is used (M4, M5). $`g_i,t_f,J,\Delta`$ are costs.

## Derivation

### Step 1. Exact reduction to one field object

$`h(g)`$ has off-diagonal entries $`-t_f\le0`$ on the edges of a connected graph. By Perron–Frobenius its lowest eigenvalue $`\varepsilon_0(g)`$ is simple for every real $`(g_1,g_2)`$, with a positive eigenvector $`\varphi_0(g)`$. Since $`\sum_jh_j\ge N_f\varepsilon_0(g)`$, with equality only on $`\varphi_0(g)^{\otimes N_f}`$, and this vector is symmetric (admissible for $`c=+1`$) and continuous in $`g`$, it is the lowest state for every real $`g`$ (no level crossing):
```math
E(g)=N_f\,\varepsilon_0(g),\qquad M=N_f\bigl[\varepsilon_0(g_1,g_2)-\varepsilon_0(g_1,0)-\varepsilon_0(0,g_2)+\varepsilon_0(0,0)\bigr].\qquad\text{(4.2)}
```
For $`c=-1`$ and $`N_f\ge2`$ the lowest admissible state fills $`N_f`$ distinct orbitals, so $`E\neq N_f\varepsilon_0`$, and (4.2) fails (control).

### Step 2. Second order in terms of the single-object contract

Let $`\varphi_0`$ be the simple isolated lowest eigenvector of a single-object contract, and $`R:=\sum_{k\neq0}\lvert\varphi_k\rangle\langle\varphi_k\rvert/(\varepsilon_k-\varepsilon_0)`$ its reduced resolvent. Rayleigh–Schrödinger gives $`\varepsilon_0(g)=\varepsilon_0+\langle V\rangle-\langle VRV\rangle+O(V^3)`$. The first-order term is additive. With $`V=g_1\Phi^{(1)}_{x_1}+g_2\Phi^{(1)}_{x_2}`$ (single-object coupled operators), the $`g_1g_2`$ part of the second-order term is, by (4.2),
```math
M^{(2)}=-2N_fg_1g_2\,\mathrm{Re}\langle\varphi_0\vert\Phi^{(1)}_{x_1}R\,\Phi^{(1)}_{x_2}\vert\varphi_0\rangle=-2N_fg_1g_2\,\varphi_0(x_1)\varphi_0(x_2)R(x_1,x_2),\qquad\text{(4.3)}
```
the second form for $`\Phi^{(1)}_x=\lvert x\rangle\langle x\rvert`$ and real $`C_1`$. On the three graph families, $`\varphi_0=\lvert X_f\rvert^{-1/2}\mathbf 1`$, $`\varepsilon_0=-zt_f`$, and $`C_1-\varepsilon_0=t_f\Lambda`$, so $`R=\Lambda^+/t_f`$. Fourier diagonalization then gives
```math
M^{(2)}(x_1,x_2)=-\frac{2n\,g_1g_2}{t_f}\,\Lambda^+(x_1,x_2),\qquad \Lambda^+(x,y)=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\neq0}\frac{e^{i\mathbf k\cdot(x-y)}}{\omega(\mathbf k)},\quad \omega(\mathbf k)=\sum_{\mu=1}^{D}4\sin^2\frac{k_\mu}2,\qquad \sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0,\qquad\text{(4.4)}
```
with $`\mathbf k\in(2\pi/L)\mathbb Z_L^D`$. The sum rule follows from $`\Lambda^+\mathbf 1=0`$. Since $`\Lambda^+(x,x)>0`$, for $`g_1g_2>0`$ the value at $`x_2=x_1`$ is negative, so $`M^{(2)}(x_1,x_2)>0`$ for some $`x_2\neq x_1`$, on every graph of the class.

### Step 3. Ring: closed form

Let $`f(d):=\frac{L^2-1}{12L}-\frac{d(L-d)}{2L}`$, $`f(L)=f(0)`$. Since $`2p(d)-p(d+1)-p(d-1)=2`$ for $`p(d)=d(L-d)`$, we get $`(\Lambda f)(d)=-1/L`$ for $`1\le d\le L-1`$ and $`(\Lambda f)(0)=2f(0)-2f(1)=1-1/L`$. Also $`\sum_{d=0}^{L-1}p(d)=L(L^2-1)/6`$ gives $`\sum_df(d)=0`$. Hence $`f=\Lambda^+\delta_0`$, i.e. $`\Lambda^+(x_1,x_2)=f(d)`$, and
```math
M^{(2)}_{\rm ring}(d)=\frac{N_f\,g_1g_2}{t_f\,L^2}\Bigl[d(L-d)-\frac{L^2-1}6\Bigr]=\frac{n\,g_1g_2}{t_f}\Bigl[d\Bigl(1-\frac dL\Bigr)-\frac{L^2-1}{6L}\Bigr].\qquad\text{(4.5)}
```
For $`g_1g_2\neq0`$ it is strictly monotone on $`0\le d\le L/2`$, and increasing for $`g_1g_2>0`$. At fixed $`N_f`$ it equals $`(N_fg_1g_2/t_f)(w-\tfrac16+\tfrac1{6L^2})`$, a function of $`d/L`$. At fixed $`n`$ its $`d`$-dependent part tends to $`(ng_1g_2/t_f)\,d`$ for $`d\ll L`$, while its constant part $`-ng_1g_2L/(6t_f)`$ diverges. Code (i): (4.3) evaluated numerically from $`C_1`$ agrees with (4.5) for $`L\in\{3,4,16,101,400\}`$, $`t_f\in\{1,2\}`$ and all $`d`$, to $`\le1.5\times10^{-12}`$ relative (`code/v1/output/second_order.txt`).

### Step 4. Tori: leading forms for $`1\ll\lvert\mathbf d\rvert\ll L`$

For $`\lvert\mathbf d\rvert\gg1`$, (4.4) is fixed by $`\lvert\mathbf k\rvert\ll1`$, where $`\omega(\mathbf k)=\lvert\mathbf k\rvert^2(1+O(\lvert\mathbf k\rvert^2))`$. By standard lattice–continuum matching, $`\Lambda^+(\mathbf d)=G_L(\mathbf d)+O(\lvert\mathbf d\rvert^{-D})`$, where $`G_L`$ is the zero-mean Green function of $`-\nabla^2`$ on the continuum torus of side $`L`$ ($`-\nabla^2G_L=\delta-L^{-D}`$). There is no constant offset: both functions have zero mean and the same small-$`\mathbf k`$ coefficients. Scaling gives $`G_L(\mathbf r)=L^{2-D}G_1(\mathbf r/L)`$. The square and cubic symmetry excludes quadratic harmonic terms, so near $`0`$:
- $`D=2`$ (Kronecker's second limit formula, $`G_1=-\frac1{2\pi}\ln\lvert\theta_1(z\vert i)/\eta(i)\rvert+\frac{v^2}2`$, $`z=u+iv`$, $`\theta_1'(0)=2\pi\eta^3`$): $`G_1(r)=-\frac1{2\pi}(\ln r+\kappa_2)+\frac{r^2}4+O(r^4)`$, with $`\kappa_2=\ln(2\pi\eta(i)^2)=\ln\frac{\Gamma(1/4)^2}{2\sqrt\pi}=1.31053`$;
- $`D=3`$ (Ewald sum of the simple cubic lattice): $`G_1(r)=\frac1{4\pi r}-\frac{c_3}{4\pi}+\frac{r^2}6+O(r^4)`$, with $`c_3=2.837297`$.

With (4.4):
```math
M^{(2)}_{\rm sq}=-\frac{n\,g_1g_2}{\pi t_f}\Bigl[\ln\frac L{\lvert\mathbf d\rvert}-\kappa_2\Bigr]-\frac{n\,g_1g_2}{t_f}\Bigl[\frac{\lvert\mathbf d\rvert^2}{2L^2}+O(\lvert\mathbf d\rvert^{-2})+O\Bigl(\frac{\lvert\mathbf d\rvert^4}{L^4}\Bigr)\Bigr],\qquad\text{(4.6)}
```
```math
M^{(2)}_{\rm cub}=-\frac{n\,g_1g_2}{2\pi t_f}\Bigl[\frac1{\lvert\mathbf d\rvert}-\frac{c_3}L\Bigr]-\frac{n\,g_1g_2}{t_f}\Bigl[\frac{\lvert\mathbf d\rvert^2}{3L^3}+O(\lvert\mathbf d\rvert^{-3})+O\Bigl(\frac{\lvert\mathbf d\rvert^4}{L^5}\Bigr)\Bigr].\qquad\text{(4.7)}
```
In the regime $`1\ll\lvert\mathbf d\rvert\ll L`$ and for $`g_1g_2>0`$, both are negative and increasing in $`\lvert\mathbf d\rvert`$. Their leading brackets are positive for $`\lvert\mathbf d\rvert<e^{-\kappa_2}L=0.270L`$ (square) and for $`\lvert\mathbf d\rvert<L/c_3=0.352L`$ (cubic). At fixed $`n`$, the $`d`$-dependent part of (4.6), $`(ng_1g_2/\pi t_f)\ln\lvert\mathbf d\rvert`$, does not depend on $`L`$, and its constant part diverges like $`\ln L`$. (4.7) tends to $`-ng_1g_2/(2\pi t_f\lvert\mathbf d\rvert)`$ as $`L\to\infty`$. At fixed $`N_f`$ both carry the factor $`N_f/L^D`$. Code (i), with $`m:=M^{(2)}t_f/(ng_1g_2)`$ computed from $`C_1`$ by conjugate gradients, compared with the bracket terms of (4.6) and (4.7):
- square, $`L=64,128,256`$: $`\lvert m-m_{\rm lead}\rvert\le8.3\times10^{-3}`$ on $`4\le\lvert\mathbf d\rvert\le L/8`$ (at $`L=256`$, $`m`$ runs there from $`-0.91`$ to $`-0.25`$); the largest deviation is at $`\lvert\mathbf d\rvert=L/8`$ and is close to $`\lvert\mathbf d\rvert^2/2L^2=7.8\times10^{-3}`$;
- cubic, $`L=32,48,64`$: $`\lvert m-m_{\rm lead}\rvert\le9.6\times10^{-4}`$ on $`4\le\lvert\mathbf d\rvert\le L/8`$, where $`\lvert m\rvert\ge0.013`$.

All three families give a dependence on $`d`$ that is not exponentially small (linear, logarithmic, $`1/\lvert\mathbf d\rvert`$). The reason is that in (4.4) the states a source excites reach down to the lowest one as $`L\to\infty`$: $`t_f\,\omega_{\min}=4t_f\sin^2(\pi/L)\to0`$.

### Step 5. Range of the second-order form

The third-order term $`\langle VRVRV\rangle-\langle V\rangle\langle VR^2V\rangle`$ has the $`g_1g_2`$ part (vertex-transitive $`\Gamma`$, $`\ell_d:=\Lambda^+(x_1,x_2)`$, $`\ell_0:=\Lambda^+(x,x)`$, $`\ell^{(2)}`$ the entries of $`(\Lambda^+)^2`$)
```math
M^{(3)}=\frac{N_f\,g_1g_2(g_1+g_2)}{\lvert X_f\rvert\,t_f^2}\Bigl[2\ell_0\ell_d+\ell_d^2-\frac{\ell^{(2)}_0+2\ell^{(2)}_d}{\lvert X_f\rvert}\Bigr].\qquad\text{(4.8)}
```
- **Ring.** $`\ell_d=L(\tfrac1{12}-\tfrac w2)-\tfrac1{12L}`$ by Step 3. Further, $`\ell^{(2)}_d=L^3c+O(L)`$, where $`c`$ is the zero-mean periodic solution of $`-\mathrm d^2c/\mathrm du^2=\tfrac1{12}-\tfrac w2`$ with $`u=d/L`$, i.e. $`c=(\tfrac1{30}-w^2)/24`$. The bracket is $`\tfrac{L^2}{60}(1-10w+20w^2)`$, and $`M^{(3)}/M^{(2)}=-\frac{(g_1+g_2)L}{10t_f}\frac{1-10w+20w^2}{1-6w}`$.
- **Square torus.** $`2\ell_0+\ell_d=\frac1{2\pi}(3\ln L-\ln\lvert\mathbf d\rvert)+O(1)`$, and the last term of (4.8) is $`O(1)\ell_d`$.
- **Cubic torus.** $`\ell_0=W_3+O(1/L)`$, with Watson's integral $`W_3=0.252731`$; $`\ell_d=1/(4\pi\lvert\mathbf d\rvert)+O(1/L)`$; the last term is $`O(\lvert\mathbf d\rvert/L^2)\,\ell_d`$.

On the ring $`\lvert1-10w+20w^2\rvert\le1`$ and $`\max_d\lvert M^{(2)}\rvert=N_f\lvert g_1g_2\rvert(L^2-1)/(6t_fL^2)`$. To leading order, the second-order form therefore has relative accuracy $`\epsilon\ll1`$ under
```math
\text{ring: }\frac{(\lvert g_1\rvert+\lvert g_2\rvert)L}{10\,t_f}\le\epsilon\ \ (\text{relative to }\max_d\lvert M^{(2)}\rvert);\quad \text{square: }\frac{(\lvert g_1\rvert+\lvert g_2\rvert)(3\ln L-\ln\lvert\mathbf d\rvert)}{4\pi t_f}\lesssim\epsilon;\quad \text{cubic: }\frac{(\lvert g_1\rvert+\lvert g_2\rvert)\bigl(W_3+\frac1{8\pi\lvert\mathbf d\rvert}\bigr)}{t_f}\lesssim\epsilon.\qquad\text{(4.9)}
```
By (4.2) these conditions do not involve $`N_f`$ or $`n`$. At fixed $`n`$ and $`g`$ they bound $`L=(N_f/n)^{1/D}`$: the second-order form fails for $`L\gtrsim t_f/\lvert g\rvert`$ on the ring and for $`\ln L\gtrsim t_f/\lvert g\rvert`$ on the square torus; the cubic condition does not involve $`L`$. On the ring, near the zero $`w=\tfrac16`$ of $`M^{(2)}`$ only the condition relative to $`\max_d\lvert M^{(2)}\rvert`$ holds: the zero itself moves at third order.

### Step 6. Exact lowest eigenvalue on the ring (one field object)

For $`\varepsilon\notin\mathrm{spec}C_1`$, $`(C_1+V)\psi=\varepsilon\psi`$ is equivalent to $`\psi=\mathcal G(\varepsilon)V\psi`$ with $`\mathcal G=(\varepsilon-C_1)^{-1}`$. Taking components at $`x_1,x_2`$:
```math
\bigl(1-g_1\mathcal G_0(\varepsilon)\bigr)\bigl(1-g_2\mathcal G_0(\varepsilon)\bigr)=g_1g_2\,\mathcal G_d(\varepsilon)^2,\qquad \mathcal G_d:=\mathcal G(x,x+d).\qquad\text{(4.10)}
```
On the ring, for $`\varepsilon=-2t_f\cos q`$,
```math
\mathcal G_d(\varepsilon)=\frac{\cos\bigl(q(L/2-d)\bigr)}{2t_f\sin q\,\sin(qL/2)},\qquad 0\le d\le L,\qquad\text{(4.11)}
```
because $`\varepsilon\mathcal G_d+t_f(\mathcal G_{d+1}+\mathcal G_{d-1})=\delta_{d,0}`$: for $`d\neq0`$ by $`\cos(a+q)+\cos(a-q)=2\cos q\cos a`$, and at $`d=0`$ by $`\cos(qL/2-q)-\cos q\cos(qL/2)=\sin q\sin(qL/2)`$. Here $`q\in(0,2\pi/L)`$ above $`-2t_f`$ and $`q=i\theta`$, $`\theta>0`$, below. A rank-2 perturbation keeps $`\varepsilon_0\le-2t_f\cos(2\pi/L)`$ (Weyl), so $`\varepsilon_0`$ is given by the largest root $`\theta`$ if one exists, and otherwise by the smallest root $`q`$. For $`g_1=g_2=g`$ the unique positive lowest eigenvector is even under the reflection exchanging $`x_1,x_2`$, so $`1=g(\mathcal G_0+\mathcal G_d)`$:
```math
t_f\sin q\,\sin\frac{qL}2=g\cos\frac{qd}2\cos\frac{q(L-d)}2,\qquad\text{one source: }\ 2t_f\sin q\tan\frac{qL}2=g,\qquad\varepsilon_0=-2t_f\cos q.\qquad\text{(4.12)}
```
For $`g<0`$, $`q=i\theta`$: $`t_f\sinh\theta\sinh\frac{\theta L}2=\lvert g\rvert\cosh\frac{\theta d}2\cosh\frac{\theta(L-d)}2`$ and $`\varepsilon_0=-2t_f\cosh\theta`$. For bounded $`\gamma:=gL/t_f`$ one has $`q=O(1/L)`$. With $`q=y/L`$ and $`u=d/L`$, (4.12) becomes $`Y\sin\frac Y2=\gamma\cos\frac{Yu}2\cos\frac{Y(1-u)}2`$ and $`y\tan\frac y2=\frac\gamma2`$, up to relative $`O(L^{-2})`$, and $`M=\frac{t_f}{L^2}\bigl(Y^2-2y^2\bigr)`$. Expanding gives $`Y^2-2y^2=\gamma^2(w-\tfrac16)+\tfrac{\gamma^3}{30}(1-10w+20w^2)+O(\gamma^4)`$, which is (4.5) and (4.8) at $`N_f=1`$. So $`ML^2/t_f`$ depends only on $`\gamma`$ and $`d/L`$, and $`\gamma`$ is the expansion parameter.

Code (ii), $`L=64,256`$, $`d\in\{1,L/8,L/4,L/2\}`$, $`\gamma\in\{0.03,0.1,0.3,1,3,-0.3,-1\}`$:
- the roots of (4.10)–(4.12) agree with exact diagonalization to $`\le4.4\times10^{-16}`$; this includes $`g_2=2g_1`$;
- the residual $`\lvert(M-M^{(2)}-M^{(3)})/M^{(2)}\rvert`$ is $`\le3.1\times10^{-4}`$ for $`\lvert\gamma\rvert\le0.1`$, $`\le2.9\times10^{-3}`$ for $`\lvert\gamma\rvert\le0.3`$ and $`\le3.3\times10^{-2}`$ for $`\lvert\gamma\rvert\le1`$ (it is $`O(\gamma^2)`$);
- at $`\gamma=3`$ the second-order form is off by $`42`$–$`43\%`$ at $`d=1`$ and by $`59\%`$ at $`d=L/4`$ (`code/v1/output/exact_ring.txt`).

### Step 7. Control state and control field

**Highest state.** Let $`L`$ be even, so that $`\Gamma`$ is bipartite. With $`S:=\mathrm{diag}((-1)^{\sum_\mu x_\mu})`$, $`SA_\Gamma S=-A_\Gamma`$ and $`SVS=V`$, hence $`Sh(g)S=-h(-g)`$. The highest eigenvalue $`\varepsilon_{\rm top}(g)=-\varepsilon_0(-g)`$ is therefore simple for all real $`g`$, and Step 1 with the inequality reversed gives
```math
M_{\rm top}(g_1,g_2)=-M_0(-g_1,-g_2),\qquad M^{(2)}_{\rm top}=+\frac{2n\,g_1g_2}{t_f}\Lambda^+(x_1,x_2).\qquad\text{(4.13)}
```
For odd $`L`$ the highest eigenvalue of $`C_1`$ is degenerate (ring: $`k=\pi(L\pm1)/L`$), and the highest state is not fixed by connection. Code (i): $`\lvert M^{(2)}_0+M^{(2)}_{\rm top}\rvert\le2.8\times10^{-15}`$ on rings $`L=4,16,64`$; degeneracy at $`L=15`$.

**Control field (assumption, M8).** $`N_f`$ objects ($`c=+1`$, no pair terms among them) with the places $`\{\varnothing\}\cup X_f`$, $`X_f`$ a chain. The own term is $`C^{c}_1=\Delta\sum_x\lvert x\rangle\langle x\rvert-J\sum_{\langle xy\rangle}(\lvert x\rangle\langle y\rvert+{\rm h.c.})`$ with $`\Delta>2J>0`$, and the coupled operator is $`\Phi^c_x=\sum_j(\lvert x\rangle\langle\varnothing\rvert+\lvert\varnothing\rangle\langle x\rvert)_j`$. The lowest eigenvector is $`\lvert\varnothing\rangle`$ (eigenvalue $`0`$). Its gap is $`\ge\Delta-2J`$, since the block $`K:=C^c_1\vert_{X_f}`$ has spectrum in $`[\Delta-2J,\Delta+2J]`$. It is not sharp, since $`\Phi^c_x\lvert\varnothing\rangle=\lvert x\rangle`$. The reduction of Step 1 holds near $`g=0`$, and (4.3) gives $`M^{(2)}_c=-2N_fg_1g_2K^{-1}(x_1,x_2)`$. On an infinite chain, $`f(d)=e^{-\theta\lvert d\rvert}/(2J\sinh\theta)`$ with $`\cosh\theta=\Delta/2J`$ solves $`Kf=\delta_0`$: for $`d\ne0`$ $`\Delta-2J\cosh\theta=0`$, and at $`d=0`$ $`\Delta-2Je^{-\theta}=2J\sinh\theta`$. It is the bounded solution, so
```math
M^{(2)}_c(d)=-\frac{N_f\,g_1g_2}{J\sinh(1/\xi)}\,e^{-d/\xi},\qquad \xi=\frac1{\mathrm{arccosh}(\Delta/2J)},\qquad\text{(4.14)}
```
valid for $`\lvert g_1\rvert+\lvert g_2\rvert\ll\Delta-2J`$; $`\xi\to\infty`$ as $`\Delta\to2J^+`$. On a finite chain the ends add relative corrections $`O(e^{-2\delta/\xi})`$, with $`\delta`$ the distance of the sources from the ends. Code (iii): open chain of $`400`$ places, $`x_1=100`$, $`d=1,\dots,160`$, $`\Delta/J\in\{2.02,2.1,2.5,3\}`$. Numerical (4.3) from $`C^c_1`$ equals (4.14) to $`\le5.7\times10^{-13}`$ relative wherever $`\lvert M\rvert>10^{-12}\lvert M(1)\rvert`$. The fitted decay lengths $`7.07695,3.17536,1.44270,1.03904`$ equal $`\xi`$ to all digits shown (`code/v1/output/control_decay.txt`).

### Step 8. Field places and body positions

Body $`b`$ couples by $`\sum_m\lvert h_m\rangle\langle h_m\rvert\otimes G\otimes\Phi_{\pi(m)}`$, with $`\pi`$ a map from chain labels to ring places (assumption, M8). A held body at $`h_{m_i}`$ acts on the field as $`g_i\Phi_{\pi(m_i)}`$. By the rotation and reflection symmetry of the ring, $`M(m_1,m_2)=F_L\bigl(d_\Gamma(\pi(m_1),\pi(m_2))\bigr)`$ exactly, with $`F_L`$ the ring mutual cost; at second order $`F_L`$ is (4.5), which for $`g_1g_2\neq0`$ is strictly monotone on $`\{0,\dots,\lfloor L/2\rfloor\}`$. Let the positions used be $`S=\{m_0,\dots,m_0+K\}`$, $`K\ge1`$. Requiring $`M=F_L(d_0/a)`$ on $`S`$ for a constant $`a>0`$, with $`d_0=\lvert m_1-m_2\rvert\sigma_X`$ (17.15), is (by monotonicity) the same as requiring $`d_\Gamma(\pi(m),\pi(m'))=\lvert m-m'\rvert\sigma_X/a`$. For adjacent $`m`$ this makes $`k:=\sigma_X/a`$ a positive integer. Hence
```math
d_\Gamma\bigl(\pi(m),\pi(m')\bigr)=k\lvert m-m'\rvert\ \ \forall m,m'\in S\iff \pi(m)=\pi(m_0)+s\,k\,(m-m_0)\bmod L,\ s=\pm1,\ kK\le\lfloor L/2\rfloor,\qquad\text{(4.15)}
```
and then $`M=F_L(k\,d_0/\sigma_X)`$. Proof. ($`\Leftarrow`$) The ring distance of a difference $`r\le\lfloor L/2\rfloor`$ is $`r`$. ($`\Rightarrow`$) $`kK=d_\Gamma(\pi(m_0),\pi(m_0+K))\le\lfloor L/2\rfloor`$. Then $`\pi(m_0+1)=\pi(m_0)+sk`$, and inductively, of the two places at distance $`k`$ from $`\pi(m)`$, only $`\pi(m)+sk`$ is at distance $`k(m+1-m_0)`$ from $`\pi(m_0)`$; the other is at $`k(m-1-m_0)`$. Sufficiency holds at all orders, and necessity at second order. A map that fails:
```math
\pi(m)=m\bmod L\ \text{on}\ S=\{0,\dots,K\},\ \lfloor L/2\rfloor<K\le L-1:\quad d_\Gamma(\pi(0),\pi(K))=L-K<K,\ \text{e.g. } M(0,L-1)=M(0,1)\ \text{while}\ d_0=(L-1)\sigma_X.\qquad\text{(4.16)}
```
The tie between field places and body positions is the coupling map $`\pi`$ alone, a choice of the description; whether anything enforces (4.15) is not asked here (M10).

## Result

- **(4.1)** Definition: the mutual cost is the double difference of the field cost $`E(g_1,g_2)`$ in the stated state.
- **(4.2)** Theorem (exact, all real $`g_1,g_2`$; every finite connected $`\Gamma`$, $`N_f\ge1`$, $`c=+1`$, no pair terms among field objects): the lowest state is $`\varphi_0(g)^{\otimes N_f}`$, connected to the lowest state without sources without level crossing, and $`E=N_f\varepsilon_0(g)`$, so $`M`$ is exactly $`N_f`$ times the one-object mutual cost. Control: $`c=-1`$, $`N_f\ge2`$.
- **(4.3)** Formula (second order, remainder $`O(N_f\lvert g_1g_2\rvert(\lvert g_1\rvert+\lvert g_2\rvert))`$; simple isolated lowest eigenvector of the single-object contract): $`M^{(2)}=-2N_fg_1g_2\mathrm{Re}\langle\varphi_0\vert\Phi^{(1)}_{x_1}R\Phi^{(1)}_{x_2}\vert\varphi_0\rangle`$, which for the class is $`-2N_fg_1g_2\varphi_0(x_1)\varphi_0(x_2)R(x_1,x_2)`$.
- **(4.4)** Formula (second order; ring and tori, lowest state): $`M^{(2)}=-(2ng_1g_2/t_f)\Lambda^+(x_1,x_2)`$, and $`\sum_{x_2\in X_f}M^{(2)}(x_1,x_2)=0`$. Hence, for $`g_1g_2>0`$, $`M^{(2)}(x_1,x_2)>0`$ for some $`x_2\neq x_1`$.
- **(4.5)** Formula (second order; ring, every $`L\ge3`$, every $`d`$): $`M^{(2)}=\frac{N_fg_1g_2}{t_fL^2}[d(L-d)-\frac{L^2-1}6]`$. For $`g_1g_2>0`$ it is strictly increasing on $`0\le d\le L/2`$ and negative iff $`d(L-d)<(L^2-1)/6`$. At fixed $`N_f`$ it is a function of $`d/L`$. At fixed $`n`$ it is linear in $`d`$ for $`d\ll L`$, with a constant part $`\propto L`$.
- **(4.6)** Formula (second order; square torus, $`1\ll\lvert\mathbf d\rvert\ll L`$, corrections $`\lvert\mathbf d\rvert^2/2L^2`$ and $`O(\lvert\mathbf d\rvert^{-2})`$): $`M^{(2)}=-\frac{ng_1g_2}{\pi t_f}[\ln\frac L{\lvert\mathbf d\rvert}-\kappa_2]`$, $`\kappa_2=1.31053`$. For $`g_1g_2>0`$ it is negative and increasing in $`\lvert\mathbf d\rvert`$. At fixed $`n`$ the $`d`$-dependence is $`\frac{ng_1g_2}{\pi t_f}\ln\lvert\mathbf d\rvert`$. Checked to $`8.3\times10^{-3}`$ in $`m`$ ($`L=64,128,256`$; $`4\le\lvert\mathbf d\rvert\le L/8`$).
- **(4.7)** Formula (second order; cubic torus, $`1\ll\lvert\mathbf d\rvert\ll L`$, corrections $`\lvert\mathbf d\rvert^2/3L^3`$ and $`O(\lvert\mathbf d\rvert^{-3})`$): $`M^{(2)}=-\frac{ng_1g_2}{2\pi t_f}[\frac1{\lvert\mathbf d\rvert}-\frac{c_3}L]`$, $`c_3=2.837297`$. For $`g_1g_2>0`$ it is negative and increasing in $`\lvert\mathbf d\rvert`$. At fixed $`n`$ it tends to $`-ng_1g_2/(2\pi t_f\lvert\mathbf d\rvert)`$. Checked to $`9.6\times10^{-4}`$ in $`m`$ ($`L=32,48,64`$; $`4\le\lvert\mathbf d\rvert\le L/8`$). At fixed $`L`$ and $`g_i`$, all of (4.4)–(4.7) scale as $`N_f/t_f`$.
- **(4.8)** Formula (third order; vertex-transitive $`\Gamma`$, lowest state): the $`g_1g_2`$ part of third order, $`\propto g_1g_2(g_1+g_2)`$.
- **(4.9)** Criterion (leading order in the small parameter; lowest state): the second-order form holds to relative accuracy $`\epsilon`$ under $`(\lvert g_1\rvert+\lvert g_2\rvert)L/10t_f\le\epsilon`$ on the ring (relative to $`\max_d\lvert M^{(2)}\rvert`$), under $`(\lvert g_1\rvert+\lvert g_2\rvert)(3\ln L-\ln\lvert\mathbf d\rvert)/4\pi t_f\lesssim\epsilon`$ on the square torus, and under $`(\lvert g_1\rvert+\lvert g_2\rvert)(W_3+1/8\pi\lvert\mathbf d\rvert)/t_f\lesssim\epsilon`$ on the cubic torus. These conditions do not involve $`N_f`$ or $`n`$.
- **(4.10)–(4.12)** Formula (exact; one field object on the ring, lowest state): the eigenvalue equation (4.10) with the ring Green function (4.11), and for $`g_1=g_2=g`$ the closed equation (4.12). For $`g_1=g_2`$ and $`L\gg1`$, $`ML^2/t_f`$ is a function of $`\gamma=gL/t_f`$ and $`d/L`$ alone, up to relative $`O(L^{-2})`$. Its expansion in $`\gamma`$ reproduces (4.5) and (4.8).
- **(4.13)** Theorem (exact, all orders; ring and tori with even $`L`$, highest state): $`M_{\rm top}(g_1,g_2)=-M_0(-g_1,-g_2)`$, so $`M^{(2)}_{\rm top}=-M^{(2)}_0`$. The sign and monotonicity statements of (4.5)–(4.7) reverse in the highest state.
- **(4.14)** Example (second order, $`\lvert g_1\rvert+\lvert g_2\rvert\ll\Delta-2J`$; gapped control field on a chain, lowest state $`\lvert\varnothing\rangle^{\otimes N_f}`$): $`M^{(2)}_c=-\frac{N_fg_1g_2}{J\sinh(1/\xi)}e^{-d/\xi}`$ with $`\xi=1/\mathrm{arccosh}(\Delta/2J)`$. It falls off faster than any power of $`d`$.
- **(4.15)** Criterion (bodies recorded on a chain, ring field, coupling map $`\pi`$; sufficiency at all orders, necessity at second order): the mutual cost is the same function of $`d_0`$ as of the graph distance, up to a constant factor, iff $`\pi`$ is the scaled embedding $`\pi(m)=\pi(m_0)\pm k(m-m_0)\bmod L`$ with $`k\in\mathbb Z_{>0}`$ and $`kK\le\lfloor L/2\rfloor`$. Then $`M=F_L(kd_0/\sigma_X)`$.
- **(4.16)** Negative: the wrapping map $`\pi(m)=m\bmod L`$ on more than $`\lfloor L/2\rfloor+1`$ positions fails (4.15).

## Consistency checks

1. **Dimensions.** $`g_i,t_f,J,\Delta`$ are costs. $`M^{(2)}\propto g_1g_2/t_f`$ and $`M^{(3)}\propto g^3L/t_f^2`$ are costs; $`\gamma=gL/t_f`$ and $`(\lvert g_1\rvert+\lvert g_2\rvert)L/t_f`$ are pure numbers.
2. **Ring $`L=3`$** (complete graph). $`C_1`$ has eigenvalues $`-2t_f,t_f,t_f`$, and $`R=(\mathbb 1-\mathbf 1\mathbf 1^{\!\top}/3)/(3t_f)`$, so $`R(x_1,x_2)=-1/(9t_f)`$ and (4.3) gives $`M^{(2)}=2N_fg_1g_2/(27t_f)`$. (4.5) at $`L=3`$, $`d=1`$ gives $`\frac{N_fg_1g_2}{9t_f}(2-\tfrac43)`$, the same.
3. **Sum over the two ends, ring $`L=4`$.** From the eigenvectors $`(1,\pm1,1,\pm1)/2`$, $`(1,0,-1,0)/\sqrt2`$ and $`(0,1,0,-1)/\sqrt2`$: $`M^{(2)}_{\rm top}(1)=-N_fg_1g_2/(32t_f)`$ and $`M^{(2)}_{\rm top}(2)=-3N_fg_1g_2/(32t_f)`$. (4.5) gives $`M^{(2)}_0(1)=N_fg_1g_2/(32t_f)`$ and $`M^{(2)}_0(2)=3N_fg_1g_2/(32t_f)`$. The sums vanish, as (4.13) requires.

## Open issues

- Odd $`L`$: the highest state is degenerate and is not determined by connection; (4.13) is derived only for even $`L`$.
- The tori conditions in (4.9) are leading-order estimates with $`O(1)`$ terms not computed; no rigorous remainder bound is given beyond Kato's sufficient radius $`\max_i\lvert g_i\rvert<2t_f\sin^2(\pi/L)`$.
- Long range is shown for the hopping class and short range for one gapped field; a general criterion over field contracts is not derived.
- Field objects with $`c=-1`$, or with pair terms among them, are outside the class.
- Necessity in (4.15) is shown at second order only.

## Code

- `code/v1/check_second_order.py` (check, item 1 and (4.13)). It evaluates (4.3) from the matrix $`C_1`$: by dense diagonalization on rings $`L\in\{3,4,16,101,400\}`$, compared with (4.5); and by conjugate gradients for $`R(\cdot,x_2)`$ on square tori $`L\in\{64,128,256\}`$ and cubic tori $`L\in\{32,48,64\}`$, compared with (4.6) and (4.7) along axis and diagonal directions with components $`\le L/4`$. It also evaluates lowest plus highest state on even rings and the top degeneracy at $`L=15`$. Output: `code/v1/output/second_order.txt`.
- `code/v1/check_exact_ring.py` (check, item 2). One field object on rings $`L=64,256`$: the exact lowest eigenvalue by diagonalization and by the roots of (4.10)–(4.12), and $`M`$ against $`M^{(2)}`$ (4.5) and $`M^{(3)}`$ (4.8), for several $`\gamma=gL/t_f`$ and $`d`$, plus a case $`g_2=2g_1`$. Output: `code/v1/output/exact_ring.txt`.
- `code/v1/check_control_decay.py` (check, item 3). The control field on an open chain of $`400`$ places: (4.3) from $`C^c_1`$ against (4.14), and the fitted decay length against $`\xi`$. Output: `code/v1/output/control_decay.txt`.

## Methods used

- Perron–Frobenius theorem; bosonic product states of non-interacting objects
- Rayleigh–Schrödinger perturbation theory (second and third order), reduced resolvent
- Graph Laplacian and its pseudo-inverse; Fourier diagonalization on tori
- Lattice–continuum Green-function matching; Kronecker's second limit formula; Ewald constant; Watson's integral
- Rank-two secular equation; ring Green function
- Bipartite sublattice symmetry
- Exact diagonalization, conjugate gradients (code checks)
