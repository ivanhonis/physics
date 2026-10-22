# Weight of a body with its own mark against its cost

- **Subproject:** 07-ilang-weight
- **Package:** 03-weight-of-mark
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-20

## Setup and assumptions

- **Field** (assumption, M8). $`N_f\ge1`$ identical field objects ($`c=+1`$), no pair terms among them, on $`X_f`$: a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L\ge3`$, $`\lvert X_f\rvert=L^D`$. Own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$; $`n=N_f/\lvert X_f\rvert`$. $`C_1+2Dt_f=t_f\Lambda`$, $`\Lambda`$ the graph Laplacian, with eigenvalues $`\omega(\mathbf k)`$ of (4.4); $`\omega_{\min}:=\min_{\mathbf k\ne0}\omega(\mathbf k)`$.
- **State** (assumption, M9, A11). In each sector the lowest state of the field; the highest state for even $`L`$ through the mirror (3.18).
- **Body** (A15, M8). One held Model D body at $`x`$ ($`\tau=0`$), in the eigenvector $`\lvert\sigma\rangle\lvert f_k\rangle`$ of $`S:=\sigma_3\otimes(m\mathbb 1_N+D)`$, eigenvalue $`\sigma M_k`$, $`M_k=m+2\pi k/(N\lambda_0)>0`$. Coupling (a): $`C_{\rm D}+\gamma\sum_x\lvert x\rangle\langle x\rvert\otimes S\otimes\Phi_x`$; at $`\tau=0`$ the motion term vanishes, so (c) equals (a). Full grip: the body's own term is $`A=0`$, the pair term is the same. $`\theta:=1`$ for (a), $`\theta:=0`$ for the full grip; $`g_b:=\sigma\gamma M_k`$.
- **Source.** Held at $`x_s`$ in an eigenvector of its coupled operator, pair term $`g_s\Phi_{x_s}`$; its own eigenvalue $`c_s`$ does not depend on $`x`$. First order in $`g_s`$.
- **Cost, weight:** as defined in the question. $`r:=x_s-x`$, $`r':=x_s-x'`$ (displacements; $`\lvert r\rvert`$ the distance); $`[f]:=f(r)-f(r')`$.
- **Notation.** $`\ell(y):=\Lambda^+(x,x+y)`$, $`\ell_0:=\ell(0)`$, $`\ell^{(j)}:=(\Lambda^+)^j`$ in the same way ($`\ell^{(2)}`$ as in (4.8)). For $`\delta/t_f<\omega_{\min}`$:
```math
\ell_\delta(y):=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\ne0}\frac{e^{i\mathbf k\cdot y}}{\omega(\mathbf k)-\delta/t_f},\qquad \ell^{(2)}_\delta:=\sum_y\ell_\delta(y)^2=\frac1{\lvert X_f\rvert}\sum_{\mathbf k\ne0}\frac1{(\omega(\mathbf k)-\delta/t_f)^2},
```
and $`\ell_\delta=\sum_{j\ge1}(\delta/t_f)^{j-1}\ell^{(j)}`$ for $`\lvert\delta\rvert/t_f<\omega_{\min}`$.
- **Inputs** (as quoted): (4.2), (4.4), (4.8) of 06-ilang-source/04-profile; (6.7) of 06-ilang-source/06-own-mark; (7.1), (7.2), (7.6) of 06-ilang-source/07-dressed-fall, with $`\delta N(x)=-\frac{2ng_s}{t_f}\ell(r)`$.
- **Regime** (A13). Exact statements hold for all $`\gamma`$. Expansions in $`\gamma`$ need $`\lvert g_b\rvert\ell_0/t_f\ll1`$; large-distance forms hold for $`1\ll\lvert r\rvert,\lvert r'\rvert\ll L`$. Standard mathematics: rank-one perturbations, Hellmann–Feynman for a nondegenerate eigenvalue, Perron–Frobenius, Fourier analysis on tori, asymptotics of lattice Green functions (constants evaluated by the code).

## Derivation

### Step 1. Reduction to one field object

At $`\tau=0`$ the body has no motion term, so its position label $`x`$ is conserved. Every term that contains body labels contains them through $`S`$, so the eigenbasis of $`S`$ is conserved too. In the sector $`(x,k,\sigma)`$, with the source in its eigenvector, the total contract is $`\theta\sigma M_k+c_s+\sum_{j=1}^{N_f}h_x^{(j)}`$ with $`h_x=C_1+g_bP_x+g_sP_{x_s}`$ (7.1). There are no pair terms among the field objects, so this is a sum of one-object operators on the symmetric subspace. $`-h_x`$ has nonnegative off-diagonal entries on a connected graph, so by Perron–Frobenius its lowest eigenvector is nondegenerate. The product of $`N_f`$ copies of it is symmetric, so (4.2) gives
```math
E_{k,\sigma}(x)=\theta\sigma M_k+c_s+N_f\,\varepsilon_0(x),\qquad \varepsilon_0(x)=\min\mathrm{spec}h_x .\qquad\text{(3.1)}
```
For (a) this is (7.2). The code (check R) diagonalizes the full contract with branch and clock labels and finds that its spectrum is the union of the sector spectra, to $`4\times10^{-14}`$, for both couplings.

### Step 2. Lowest eigenpair of one object with one point term

Let $`h_g:=C_1+gP_x`$, with lowest eigenvalue $`-2Dt_f+\delta`$. From $`(E-C_1)\psi=g\psi(x)\lvert x\rangle`$ we get $`\psi\propto(E-C_1)^{-1}\lvert x\rangle`$ and $`1=g\langle x\vert(E-C_1)^{-1}\vert x\rangle`$. Separating the $`\mathbf k=0`$ term gives $`\lvert X_f\rvert\delta\,\langle x+y\vert(E-C_1)^{-1}\vert x\rangle=1-\eta\ell_\delta(y)`$ with $`\eta:=\lvert X_f\rvert\delta/t_f`$. Hence
```math
\psi(x+y)\propto1-\eta\,\ell_\delta(y),\qquad \frac g{t_f}=\frac{\eta}{1-\eta\,\ell_\delta(0)},\qquad\text{(3.2)}
```
and, since $`\sum_y\ell_\delta(y)=0`$,
```math
\rho_g(y):=\frac{\lvert\psi(x+y)\rvert^2}{\lVert\psi\rVert^2}=\frac{(1-\eta\ell_\delta(y))^2}{\lvert X_f\rvert+\eta^2\ell^{(2)}_\delta}.\qquad\text{(3.3)}
```
The function $`1/(\lvert X_f\rvert\delta)-\ell_\delta(0)/t_f`$, which equals $`1/g`$, decreases strictly on $`(-\infty,0)`$, where it runs over $`(-\infty,0)`$, and on $`(0,t_f\omega_{\min})`$, where it runs over $`\mathbb R`$. So the lowest eigenvalue is the unique root on $`(0,t_f\omega_{\min})`$ for $`g>0`$ and on $`(-\infty,0)`$ for $`g<0`$: $`\mathrm{sign}\delta=\mathrm{sign}g`$ and $`\delta/t_f<\omega_{\min}`$. With $`\delta/t_f=\eta/\lvert X_f\rvert`$ and $`\hat g:=g/t_f`$, (3.2) gives $`\eta=\hat g-\ell_0\hat g^2+(\ell_0^2-\ell^{(2)}_0/\lvert X_f\rvert)\hat g^3+O(\hat g^4)`$. Code checks B and C: (3.3) agrees with the diagonalized density to $`4\times10^{-10}/\lvert X_f\rvert`$, and $`N_f\delta`$ agrees with the eigenvalue to $`5\times10^{-13}`$.

### Step 3. Cost (item 1)

Without the source, the description without the body (the field alone) has lowest eigenvalue $`-2Dt_fN_f`$. By (3.1) and (3.2):
```math
\mathrm{Cost}_{k,\sigma}=\theta\sigma M_k+C^{\rm mark}_{k,\sigma},\qquad C^{\rm mark}_{k,\sigma}:=N_f\bigl[\varepsilon_0(g_b)-\varepsilon_0(0)\bigr]=n\,t_f\,\eta(g_b),\qquad\text{(3.4)}
```
```math
C^{\rm mark}_{k,\sigma}=n g_b-\frac{n\ell_0}{t_f}g_b^2+\frac n{t_f^2}\Bigl(\ell_0^2-\frac{\ell^{(2)}_0}{\lvert X_f\rvert}\Bigr)g_b^3+O(g_b^4),\qquad g_b=\sigma\gamma M_k .\qquad\text{(3.5)}
```
$`C^{\rm mark}`$ does not depend on $`x`$ (translations). It increases strictly in $`g_b`$ ($`\mathrm d\varepsilon_0/\mathrm dg=\rho_g(0)>0`$) and has the sign of $`g_b`$. Values of $`\ell_0`$:
- ring: $`\ell_0=(L^2-1)/(12L)`$, which reproduces (6.7);
- square torus: $`\ell_0=\frac1{2\pi}\ln L+c_\square+o(1)`$ with $`c_\square=0.04877`$;
- cubic torus: $`\ell_0=G_3-\xi_3/L+o(1/L)`$ with $`G_3=0.252731`$ and $`\xi_3=2.837297/(4\pi)`$ (code check S).

Code check D: the remainder of (3.5) truncated at $`g_b^2`$ scales as $`\gamma^{2.98\text{–}2.99}`$.

What the total contract fixes (M6):
- (i) $`E_{k,\sigma}-E_{k',\sigma'}=\theta(\sigma M_k-\sigma'M_{k'})+C^{\rm mark}_{k,\sigma}-C^{\rm mark}_{k',\sigma'}`$ is fixed by the total contract of the description with the body alone.
- (ii) $`C^{\rm mark}`$ is the difference between the descriptions with and without the coupling, so it is fixed by those two total contracts.
- (iii) $`\mathrm{Cost}`$ itself needs the reference description without the body. It shifts by $`c`$ if $`c\mathbb 1`$ is added to the body's own term. That change alters the evolution of the description with the body only by a common phase (1.2), so it changes no reading. $`\theta\sigma M_k`$ is what this comparison adds to $`C^{\rm mark}`$.
- (iv) The costs of single contract terms are not fixed: listing $`B`$ inside the pair term (A5) changes them and leaves $`C`$ unchanged.

In the full grip, $`\mathrm{Cost}=C^{\rm mark}\to0`$ for $`\gamma\to0`$ at every level.

### Step 4. Weight, exact in γ (item 2)

$`h_x=h_{g_b}+g_sP_{x_s}`$, and the lowest eigenvalue of $`h_{g_b}`$ is nondegenerate (Step 1). By Hellmann–Feynman, $`\varepsilon_0(x)=\varepsilon_0(g_b)+g_s\rho_{g_b}(x_s-x)+O(g_s^2)`$, where $`\varepsilon_0(g_b)`$, $`\theta\sigma M_k`$ and $`c_s`$ do not depend on $`x`$. For both couplings, therefore,
```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=N_fg_s\bigl[\rho_{g_b}(r)-\rho_{g_b}(r')\bigr]+O(g_s^2):\qquad\text{(3.6)}
```
the source weighs the body by the field density that the body makes at the source's place. With (3.3):
```math
W_{k,\sigma}(x)-W_{k,\sigma}(x')=\frac{n g_s\bigl[(1-\eta\ell_\delta(r))^2-(1-\eta\ell_\delta(r'))^2\bigr]}{1+\eta^2\ell^{(2)}_\delta/\lvert X_f\rvert}+O(g_s^2),\qquad \eta=\eta(g_b),\ \ \delta=\frac{t_f\eta}{\lvert X_f\rvert}.\qquad\text{(3.7)}
```
Code check A compares the lowest eigenvalue of $`h_x`$ with both point terms ($`\pm g_s`$, symmetric difference) with (3.6). The maximal relative deviation is $`\le2.3\times10^{-5}`$ at $`g_s=10^{-3}`$ and falls by 4 when $`g_s`$ is halved (ring, square torus); on the cubic torus it is $`\le6.5\times10^{-8}`$, at the noise floor for $`L=12`$.

### Step 5. Weight through second order and at large distance (item 2)

With the expansions of Step 2, (3.3) gives $`\lvert X_f\rvert\rho_g(y)=1-2\hat g\ell(y)+\hat g^2\bigl[\ell(y)^2+2\ell_0\ell(y)-\tfrac{2\ell^{(2)}(y)+\ell^{(2)}_0}{\lvert X_f\rvert}\bigr]+O(\hat g^3)`$. In (3.6) this gives
```math
\Delta W_{k,\sigma}=\sigma\gamma M_k[\delta N]+\gamma^2M_k^2[\Theta_D]+O(g_s^2)+O(g_s\gamma^3M_k^3),\qquad \Theta_D(x):=\frac{ng_s}{t_f^2}\Bigl[\ell(r)^2+2\ell_0\ell(r)-\frac{2\ell^{(2)}(r)}{\lvert X_f\rvert}\Bigr],\qquad\text{(3.8)}
```
with $`\Delta W_{k,\sigma}:=W_{k,\sigma}(x)-W_{k,\sigma}(x')`$. Code check E: the remainder scales as $`\gamma^{2.98\text{–}3.00}`$.

**Ring.** $`\ell=\frac{L^2-1}{12L}-\frac u{2L}`$ and $`\ell^{(2)}=\mathrm{const}-\frac{u^2+2u}{24L}`$, with $`u=r(L-r)`$. The second follows from $`\Lambda u=2`$ and $`\Lambda u^2=12u-2L^2-2`$. Exactly in $`r`$:
```math
\Delta W_{k,\sigma}\big|_{\rm ring}=\sigma\gamma M_k\frac{ng_s}{Lt_f}(u-u')+\gamma^2M_k^2\frac{ng_s}{3L^2t_f^2}\Bigl[u^2-u'^2-\frac{L^2-2}2(u-u')\Bigr].\qquad\text{(3.9)}
```
For $`1\ll r,r'\ll L`$ this is $`\simeq\frac{ng_s}{t_f}(r-r')\bigl[\sigma\gamma M_k-\gamma^2M_k^2\frac L{6t_f}\bigr]`$, a uniform pull.

**Square torus.** $`\ell(r)=\frac1{2\pi}\bigl[\ln\frac L{\lvert r\rvert}+\kappa_\square\bigr]+O(\lvert r\rvert^{-2})+O(\lvert r\rvert^2/L^2)`$ with $`\kappa_\square=2\pi c_\square-\gamma_E-\tfrac32\ln2=-1.3105`$. The $`\ell^{(2)}`$ term is $`O(\lvert r\rvert^2\ln L/L^2)`$. Then
```math
\Delta W_{k,\sigma}\big|_{\square}\simeq\frac{ng_s}{\pi t_f}\ln\frac{\lvert r\rvert}{\lvert r'\rvert}\Bigl[\sigma\gamma M_k-\frac{\gamma^2M_k^2}{2t_f}\bigl(\ell(r)+\ell(r')+2\ell_0\bigr)\Bigr].\qquad\text{(3.10)}
```

**Cubic torus.** $`\ell(r)=\frac1{4\pi\lvert r\rvert}-\frac{\xi_3}L+O(\lvert r\rvert^{-3})+O(\lvert r\rvert^2/L^3)`$. The $`\ell^{(2)}`$ term is $`O(\lvert r\rvert/L^3)`$. Then
```math
\Delta W_{k,\sigma}\big|_{\rm cubic}\simeq-\frac{ng_s}{2\pi t_f}\Bigl(\frac1{\lvert r\rvert}-\frac1{\lvert r'\rvert}\Bigr)\Bigl[\sigma\gamma M_k-\frac{\gamma^2M_k^2}{2t_f}\bigl(\ell(r)+\ell(r')+2\ell_0\bigr)\Bigr].\qquad\text{(3.11)}
```
Code check S confirms the asymptotic forms of $`\ell`$: the deviation falls as $`\lvert r\rvert^{-2}`$ on the square torus and as $`\lvert r\rvert^{-3}`$ on the cubic torus, and $`\ell_0+\xi_3/L=0.252731`$ at $`L=32,64,96`$.

### Step 6. Weight against cost (item 3)

**(a) The weight is a function of the mark cost.** By (3.4), $`\eta=C^{\rm mark}/(nt_f)`$ and $`\delta=t_f\eta/\lvert X_f\rvert`$. So (3.7) depends on $`k`$, $`\sigma`$, $`\gamma`$ and the coupling only through $`C^{\rm mark}`$:
```math
\Delta W_{k,\sigma}=\mathcal W_{x,x'}\bigl(C^{\rm mark}_{k,\sigma}\bigr)+O(g_s^2),\qquad\text{(3.12)}
```
where $`\mathcal W`$ is (3.7) at $`\eta=C/(nt_f)`$: one function for all levels, both branches, every $`\gamma`$ and both couplings. Expanding (3.3) in $`\eta`$ instead of $`\hat g`$ gives
```math
\mathcal W(C)=FC+F_2C^2+F_3C^3+O(C^4),\qquad F=-\frac{2g_s}{t_f}[\ell]=\frac{[\delta N]}n,\quad F_2=\frac{g_s}{nt_f^2}\Bigl[\ell^2-\frac{2\ell^{(2)}}{\lvert X_f\rvert}\Bigr],\quad F_3=\frac{2g_s}{n^2t_f^3\lvert X_f\rvert}\Bigl[\ell\,\ell^{(2)}+\ell^{(2)}_0\ell-\frac{\ell^{(3)}}{\lvert X_f\rvert}\Bigr].\qquad\text{(3.13)}
```
Code check H: the remainder after $`F_3`$ scales as $`\gamma^{3.8\text{–}4.05}`$.

**(b) Full grip.** Here $`\mathrm{Cost}=C^{\rm mark}`$, so
```math
\Delta W_{k,\sigma}=\mathrm{Cost}_{k,\sigma}F\bigl[1+B^{\rm fg}_{k,\sigma}\bigr],\qquad B^{\rm fg}_{k,\sigma}=-\frac{\eta}2\Bigl[\ell(r)+\ell(r')-\frac{2[\ell^{(2)}]}{\lvert X_f\rvert[\ell]}\Bigr]+O(\eta^2\ell^2),\quad \eta=\frac{\mathrm{Cost}_{k,\sigma}}{nt_f}=\frac{g_b}{t_f}+O(g_b^2).\qquad\text{(3.14)}
```
Criterion, for a pair with $`F\ne0`$: a factor $`G(x,x')`$ independent of $`(k,\sigma)`$ with $`\Delta W=\mathrm{Cost}\,G+O(\gamma^3)`$ exists iff $`F_2(x,x')=0`$. Proof: the order $`\gamma`$ forces $`G=F+\gamma G_1+O(\gamma^2)`$. At order $`\gamma^2`$, $`\Delta W-\mathrm{Cost}\,G`$ is $`-\sigma\gamma^2nM_kG_1+\gamma^2n^2M_k^2F_2`$. The first part is odd in $`\sigma`$ and the second even, so both vanish. The first breaking term is $`F_2\mathrm{Cost}^2`$: even in $`\sigma`$, $`\propto M_k^2`$, with parameter $`\eta\ell`$.

**(c) Coupling (a).** Here $`\mathrm{Cost}=\sigma M_k(1+\gamma n)+O(\gamma^2)`$. By (3.8) and (3.5):
```math
\Delta W_{k,\sigma}=\mathrm{Cost}_{k,\sigma}F^{(a)}\bigl[1+B^{(a)}_{k,\sigma}\bigr],\quad F^{(a)}:=\frac{\gamma[\delta N]}{1+\gamma n},\quad B^{(a)}_{k,\sigma}=\frac{g_b[\Theta_D]}{[\delta N]}+O(\gamma^2)=-\frac{g_b}{2t_f}\Bigl[\ell(r)+\ell(r')+2\ell_0-\frac{2[\ell^{(2)}]}{\lvert X_f\rvert[\ell]}\Bigr]+O(\gamma^2).\qquad\text{(3.15)}
```
By the same odd/even argument, a universal $`G`$ with $`\Delta W=\mathrm{Cost}\,G+O(\gamma^3)`$ exists iff $`[\Theta_D]=0`$; otherwise the first breaking term is $`\gamma^2M_k^2[\Theta_D]`$. In (a) only the mark is weighed, $`\mathcal W(C^{\rm mark})`$, while the cost also contains $`\sigma M_k`$. The term $`2\ell_0`$, the mark's own second-order cost in (3.5), is compensated in the full grip and not in (a).

Code check I: $`\lvert B\rvert\propto\gamma^{0.98\text{–}0.99}`$, and $`\lvert B-(\text{first order of (3.14), (3.15)})\rvert\propto\gamma^{1.96\text{–}1.98}`$, on all six graphs, for both couplings.

**(d) Dependence on the graph and the distance.** These forms are at first order, from (3.14), (3.15), (3.9)–(3.11):
```math
\begin{aligned}
&\text{ring (all }r,r'):&&B^{\rm fg}=-\tfrac{\eta}{12L}\bigl[L^2-3-4(u+u')\bigr],&&B^{(a)}=\tfrac{g_b}{3Lt_f}\bigl[u+u'-\tfrac{L^2-2}2\bigr];\\
&\text{square }(1\ll\lvert r\rvert,\lvert r'\rvert\ll L):&&B^{\rm fg}\simeq-\tfrac{\eta}{4\pi}\bigl[\ln\tfrac{L^2}{\lvert r\rvert\lvert r'\rvert}+2\kappa_\square\bigr],&&B^{(a)}\simeq-\tfrac{g_b}{4\pi t_f}\bigl[\ln\tfrac{L^4}{\lvert r\rvert\lvert r'\rvert}+2\kappa_\square+4\pi c_\square\bigr];\\
&\text{cubic }(1\ll\lvert r\rvert,\lvert r'\rvert\ll L):&&B^{\rm fg}\simeq-\tfrac{\eta}{8\pi}\bigl(\tfrac1{\lvert r\rvert}+\tfrac1{\lvert r'\rvert}\bigr)+\tfrac{\eta\xi_3}L,&&B^{(a)}\simeq-\tfrac{g_b}{t_f}\bigl[G_3+\tfrac1{8\pi}\bigl(\tfrac1{\lvert r\rvert}+\tfrac1{\lvert r'\rvert}\bigr)-\tfrac{2\xi_3}L\bigr].
\end{aligned}\qquad\text{(3.16)}
```
Errors are $`O(\eta\lvert r\rvert^{-2})`$ (square), $`O(\eta\lvert r\rvert^{-3})`$ (cubic), $`O(\eta\lvert r\rvert^2/L^2)`$ and $`O(\eta^2\ell^2)`$.
- On the ring, for $`r,r'\ll L`$: $`B^{\rm fg}\simeq-\eta L/12`$ and $`B^{(a)}\simeq-g_bL/(6t_f)`$. Both are independent of the distance and grow with $`L`$.
- The full grip has no ring pair with $`F\ne0`$ and $`F_2=0`$: $`F_2\propto[\ell]\,[L^2-3-4(u+u')]`$, and $`L^2-3\not\equiv0\pmod 4`$. For (a), $`[\Theta_D]=0`$ on the ring pairs with $`u+u'=L^2/2-1`$ (even $`L`$, the antipode and its neighbour).

Code check K (break against distance along an axis, $`r'`$ the antipode, $`\lvert g_b\rvert\ell_0/t_f=0.05`$) confirms the first-order breaks of (3.14) and (3.15) at all distances. Cubic torus, $`L=20`$: $`B^{\rm fg}=-6.99\times10^{-3}`$ at $`\lvert r\rvert=1`$ and $`8.6\times10^{-4}`$ at $`\lvert r\rvert=10`$; $`B^{(a)}`$ lies between $`-0.054`$ and $`-0.047`$ ($`\sigma=+1`$), against $`-g_b\ell_0/t_f=-0.05`$. Ring, $`L=64`$: $`B^{\rm fg}`$ rises from $`2.5\times10^{-3}`$ to $`4.8\times10^{-2}`$ and $`B^{(a)}`$ from $`-4.6\times10^{-2}`$ to $`-1.9\times10^{-3}`$.

**(e) Differences between levels and branches (M6).** For two internal states 1 and 2, with $`C_i:=C^{\rm mark}_i`$, (3.12)–(3.13) give
```math
\frac{\Delta W_1-\Delta W_2}{\mathrm{Cost}_1-\mathrm{Cost}_2}=\frac{C_1-C_2}{\theta(\sigma_1M_{k_1}-\sigma_2M_{k_2})+C_1-C_2}\Bigl[F+F_2(C_1+C_2)+F_3(C_1^2+C_1C_2+C_2^2)+O(C^3)\Bigr].\qquad\text{(3.17)}
```
- **Two levels, same branch.** The relative break is $`\sigma\gamma n(M_k+M_{k'})F_2/F+O(\gamma^2)`$ (full grip) and $`\sigma\gamma(M_k+M_{k'})[\Theta_D]/[\delta N]+O(\gamma^2)`$ (a): first order, as for one level.
- **Two branches of one level.** $`C_++C_-=-2n\ell_0\gamma^2M_k^2/t_f+O(\gamma^4)`$ and $`C_+^2+C_+C_-+C_-^2=n^2\gamma^2M_k^2+O(\gamma^4)`$. The ratio (3.17) is
  - full grip: $`F\bigl[1+\gamma^2M_k^2\,\tfrac{n^2F_3-2n\ell_0F_2/t_f}{F}+O(\gamma^4)\bigr]`$;
  - (a): $`F^{(a)}\bigl[1+\gamma^2M_k^2\bigl(\tfrac{\ell_0^2-\ell^{(2)}_0/\lvert X_f\rvert}{t_f^2}+\tfrac{n^2F_3-2n\ell_0F_2/t_f}{F}\bigr)+O(\gamma^3)\bigr]`$.

  Branch differences are universal through first order and break at second order wherever the coefficient is nonzero. On the cubic torus at large distance the full-grip break is $`\gamma^2M_k^2\ell_0(\ell(r)+\ell(r'))/t_f^2+O(\gamma^2M_k^2/(t_f^2L^2))`$, which decays like $`1/\lvert r\rvert`$ down to $`O(\gamma^2M_k^2/(t_f^2L))`$. The break of (a) keeps $`\gamma^2M_k^2G_3^2/t_f^2`$.

Code check J: the predicted breaks agree with the diagonalization to relative $`\le6\times10^{-5}`$ (branch pairs, both couplings), $`4\times10^{-5}`$–$`2.5\times10^{-3}`$ (level pairs, full grip) and $`5\times10^{-3}`$–$`8\times10^{-3}`$ (level pairs, (a)) at the smallest $`\gamma`$. The residuals grow with $`\gamma`$ as the next order.

**(f) Highest state (mirror).** For even $`L`$ the graph is bipartite. $`U=(-1)^{\sum_\mu x_\mu}`$ gives $`UC_1U=-C_1`$ and $`UP_yU=P_y`$, so $`\max\mathrm{spec}h(g_b,g_s)=-\min\mathrm{spec}h(-g_b,-g_s)`$; the reference value is $`+2Dt_fN_f`$. Since $`\Delta W`$ is linear in $`g_s`$, (3.12) gives
```math
\Delta W^{\rm high}_{k,\sigma}(g_b)=\Delta W_{k,\sigma}(-g_b)=\sum_{j\ge1}(-1)^jF_j\bigl(C^{\rm mark,high}_{k,\sigma}\bigr)^j,\qquad C^{\rm mark,high}(g_b)=-C^{\rm mark}(-g_b)=ng_b+\frac{n\ell_0}{t_f}g_b^2+O(g_b^3).\qquad\text{(3.18)}
```
So (3.14)–(3.17) carry over with $`F\mapsto-F`$ and $`F^{(a)}\mapsto-F^{(a)}`$. The first-order relative breaks change sign; the second-order ones (branch pairs, which are even in $`g_b`$) do not. Code check M: the eigenvalue identity holds to machine precision.

## Result

Class for all results (unless stated otherwise):
- the field class of the setting (ring, square torus or cubic torus, every $`N_f\ge1`$, $`t_f>0`$);
- one held Model D body at $`\tau=0`$, every level $`k`$ and both branches, with coupling (a) ($`=`$(c)) or the full grip;
- one held source, at first order in $`g_s`$ (remainder $`O(g_s^2)`$);
- the lowest field state, and the highest for even $`L`$ by (3.18).

- **(3.1)** In each sector $`(x,k,\sigma)`$ the eigenvalue is $`\theta\sigma M_k+c_s+N_f\min\mathrm{spec}(C_1+g_bP_x+g_sP_{x_s})`$, $`g_b=\sigma\gamma M_k`$, exactly.
- **(3.2), (3.3)** The lowest eigenpair of $`C_1+gP_x`$ is given exactly by $`\psi\propto1-\eta\ell_\delta`$, with $`g/t_f=\eta/(1-\eta\ell_\delta(0))`$, $`\eta=\lvert X_f\rvert\delta/t_f`$, $`\mathrm{sign}\delta=\mathrm{sign}g`$; its density is (3.3).
- **(3.4), (3.5)** Item 1 (cost):
  - $`\mathrm{Cost}_{k,\sigma}=\theta\sigma M_k+C^{\rm mark}_{k,\sigma}`$ with $`C^{\rm mark}=N_f[\varepsilon_0(g_b)-\varepsilon_0(0)]=nt_f\eta(g_b)`$, exact for every $`\gamma`$;
  - through $`g_b^3`$: $`C^{\rm mark}=ng_b-n\ell_0g_b^2/t_f+n(\ell_0^2-\ell^{(2)}_0/\lvert X_f\rvert)g_b^3/t_f^2`$, with remainder $`O(g_b^4)`$ for $`\lvert g_b\rvert\ell_0/t_f\ll1`$.
  - The total contract with the body fixes the level and branch differences of $`E`$. $`C^{\rm mark}`$ is fixed as a difference between the descriptions with and without the coupling. $`\mathrm{Cost}`$ needs the reference description and shifts with a constant in the body's own term, which changes no reading. The costs of single contract terms are not fixed.
- **(3.6), (3.7)** Item 2 (weight), exact in $`\gamma`$, both couplings: $`W_{k,\sigma}(x)-W_{k,\sigma}(x')=N_fg_s[\rho_{g_b}(r)-\rho_{g_b}(r')]`$, the field density made by the body read at the source, in the closed form (3.7).
- **(3.8)** Through $`\gamma^2`$: $`\Delta W=\sigma\gamma M_k[\delta N]+\gamma^2M_k^2[\Theta_D]`$, with $`\Theta_D=\frac{ng_s}{t_f^2}[\ell^2+2\ell_0\ell-2\ell^{(2)}/\lvert X_f\rvert]`$; remainder $`O(g_s\gamma^3M_k^3)`$; same for both couplings.
- **(3.9)–(3.11)** Large-distance forms:
  - ring: (3.9), exact in $`r`$, which is (7.6) (a uniform pull for $`r\ll L`$);
  - square torus: $`\ln(\lvert r\rvert/\lvert r'\rvert)`$ law (3.10);
  - cubic torus: $`1/\lvert r\rvert`$ law (3.11).

  On both tori the second-order coefficient is $`-\frac{\gamma^2M_k^2}{2t_f}(\ell(r)+\ell(r')+2\ell_0)`$ relative to $`\sigma\gamma M_k`$. (3.10) and (3.11) hold for $`1\ll\lvert r\rvert,\lvert r'\rvert\ll L`$, up to the errors stated in Step 5.
- **(3.12), (3.13)** Exactly in $`\gamma`$, $`\Delta W_{k,\sigma}=\mathcal W_{x,x'}(C^{\rm mark}_{k,\sigma})`$, with one function $`\mathcal W`$ for all levels, branches, $`\gamma`$ and both couplings. $`\mathcal W(C)=FC+F_2C^2+F_3C^3+O(C^4)`$, with $`F=[\delta N]/n`$ and $`F_2`$, $`F_3`$ as in (3.13). $`\mathcal W`$ is not linear wherever $`F_2(x,x')\ne0`$: on the ring for every pair with $`F\ne0`$, and on the tori for generic pairs (3.16).
- **(3.14)** Item 3, full grip:
  - weight $`=`$ cost $`\times F`$ at leading order, with the universal $`F=[\delta N]/n`$ (remainder $`O(\gamma^2)`$);
  - a universal factor exists at order $`\gamma^2`$ iff $`F_2(x,x')=0`$; otherwise the first breaking term is $`F_2\mathrm{Cost}^2`$, with relative size $`B^{\rm fg}=-\frac\eta2[\ell(r)+\ell(r')-2[\ell^{(2)}]/(\lvert X_f\rvert[\ell])]`$, $`\eta=\mathrm{Cost}/(nt_f)`$.
- **(3.15)** Item 3, coupling (a):
  - weight $`=`$ cost $`\times F^{(a)}`$, $`F^{(a)}=\gamma[\delta N]/(1+\gamma n)`$, at leading order (remainder $`O(\gamma^2)`$);
  - a universal factor exists at order $`\gamma^2`$ iff $`[\Theta_D]=0`$; otherwise the first breaking term is $`\gamma^2M_k^2[\Theta_D]`$, with relative size $`B^{(a)}=-\frac{g_b}{2t_f}[\ell(r)+\ell(r')+2\ell_0-2[\ell^{(2)}]/(\lvert X_f\rvert[\ell])]`$.
- **(3.16)** Dependence on the graph (first order in $`\gamma`$):
  - ring: $`\lvert B^{\rm fg}\rvert\simeq\lvert\eta\rvert L/12`$ and $`\lvert B^{(a)}\rvert\simeq\lvert g_b\rvert L/(6t_f)`$ for $`r,r'\ll L`$; no ring pair with $`F\ne0`$ has $`F_2=0`$;
  - square torus: both breaks grow like $`\ln L`$;
  - cubic torus: the full-grip break decays like $`(1/\lvert r\rvert+1/\lvert r'\rvert)`$ down to $`O(\eta/L)`$, while that of (a) tends to $`-g_bG_3/t_f`$, $`G_3=0.252731`$, at every large distance.

  Of the six combinations of coupling and graph, only the full grip on the cubic torus makes weight and cost proportional for all levels and branches to a relative accuracy that improves with distance: $`O(\eta(1/\lvert r\rvert+1/\lvert r'\rvert))+O(\eta/L)+O(\eta^2)`$.
- **(3.17)** Differences, for every pair of internal states, exactly in $`\gamma`$ through the divided difference of $`\mathcal W`$:
  - between two levels of one branch, universality breaks at first order in $`\gamma`$ wherever $`F_2\ne0`$ (full grip) or $`[\Theta_D]\ne0`$ (a), as for one level;
  - between the two branches of one level, it holds through first order and breaks at order $`\gamma^2M_k^2`$ wherever the coefficient given in Step 6(e) is nonzero.

  On the cubic torus at large distance the full-grip branch break decays like $`1/\lvert r\rvert`$ down to $`O(\gamma^2M_k^2/(t_f^2L))`$, while that of (a) tends to $`\gamma^2M_k^2G_3^2/t_f^2`$.
- **(3.18)** In the highest state (even $`L`$): $`\Delta W^{\rm high}(g_b)=\Delta W(-g_b)=\sum_j(-1)^jF_j(C^{\rm mark,high})^j`$, with $`C^{\rm mark,high}(g_b)=-C^{\rm mark}(-g_b)`$. (3.14)–(3.17) carry over with $`F\mapsto-F`$ and $`F^{(a)}\mapsto-F^{(a)}`$. The first-order relative breaks change sign; the second-order branch-pair breaks do not.
- **Controls (M9).**
  - For the positive answer (full grip, cubic torus), the failing descriptions are coupling (a) on the same graph and the full grip on the ring or square torus.
  - For the negative answers, the order-$`\gamma^2`$ criteria of (3.14) and (3.15) are exact, so the control of each is a pair on which its criterion holds. On the ring these are only the pairs with $`[\ell]=0`$ (where $`F=0`$) and, for (a), the pairs with $`u+u'=L^2/2-1`$ (even $`L`$). On the tori the zeros of $`F_2`$ and $`[\Theta_D]`$ are not classified.

## Consistency checks

1. **Dimensions.** $`g_b`$, $`g_s`$, $`t_f`$, $`M_k`$, Cost and $`W`$ have the dimension of $`C`$; $`\gamma`$, $`n`$, $`\ell^{(j)}`$, $`\eta`$ and $`F`$ are dimensionless; $`F_2\propto1/[C]`$ and $`F_3\propto1/[C]^2`$. Every term of (3.5), (3.8) and (3.13)–(3.17) is homogeneous.
2. **Special cases.** For $`\gamma\to0`$: $`\Delta W\to0`$ and $`\mathrm{Cost}\to\theta\sigma M_k`$. On the ring:
   - $`\ell_0=(L^2-1)/(12L)`$ turns (3.5) into (6.7);
   - the $`g_b^2g_s`$ coefficient of (3.8) equals the $`g_1^2g_2`$ term of (4.8);
   - $`\Theta_D-\Theta`$ of (7.6) is constant in $`x`$ (code check F: $`2\times10^{-15}`$).
3. **Sum rule.** $`\sum_x\rho_{g_b}(x_s-x)=1`$ for every $`\gamma`$, so the $`\gamma`$-dependent part of $`\sum_xW(x)`$ must vanish. At order $`\hat g`$: $`\sum_y\ell=0`$. At order $`\hat g^2`$: $`\sum_y[\ell^2+2\ell_0\ell-(2\ell^{(2)}+\ell^{(2)}_0)/\lvert X_f\rvert]=\ell^{(2)}_0-\ell^{(2)}_0=0`$. Passed.

## Open issues

- Results for $`N_f>1`$ rest on the reduction (4.2) and on the factor $`N_f`$ in (3.1); the code checks $`N_f=1`$ only.
- The highest state is covered for even $`L`$ only; for odd $`L`$ the top of the one-object band is degenerate, and it is not treated.
- Terms of order $`g_s^2`$ (the source's own mark and its nonlinearity) are not treated.
- The large-distance constants $`c_\square`$, $`G_3`$ and $`\xi_3`$ are evaluated numerically (code check S), not in closed form.
- On the square and cubic tori, the pairs where $`F_2`$ or $`[\Theta_D]`$ vanish are not classified.
- Whether a coupling other than the full grip removes the $`G_3`$ break of (a), and how special the full grip is, belongs to item 5. Moving bodies, inertia and bonds are out of scope.

## Code

- `code/v1/check_weight_of_mark.py` (role: check). For $`N_f=1`$, $`t_f=1`$, it covers the ring ($`L=32,64`$), the square torus ($`L=12,20`$) and the cubic torus ($`L=8,12`$, plus $`L=20`$ for the distance scan); two levels ($`M_k=1,1.5`$), both branches and both couplings, with $`\gamma`$ chosen so that $`\gamma M_k\ell_0/t_f\le0.04`$. It diagonalizes one field object with the point terms of the body and the source and compares the result with (3.1)–(3.18). The checks are:
  - R: full contract against (3.1);
  - A: eigenvalue weight against (3.6);
  - B, C: exact forms (3.2)–(3.4);
  - D, E: $`\gamma`$-scaling of the remainders of (3.5), (3.8);
  - F: (7.6);
  - H: (3.13);
  - I: single-level breaks (3.14), (3.15);
  - J: differences (3.17);
  - K: distance dependence;
  - M: mirror (3.18);
  - S: asymptotics of $`\ell`$ by FFT up to $`L=512`$ (2D) and $`L=96`$ (3D).

  Outputs: `code/v1/output/check_log.txt` (all numbers cited above) and `code/v1/output/check_results.json` (the same, machine-readable).

## Methods used

- sector reduction by conserved labels; Perron–Frobenius; one-object reduction for bosons without mutual pair terms
- rank-one (point-term) perturbation, secular equation, resolvent with the zero mode separated
- Hellmann–Feynman theorem; Rayleigh–Schrödinger expansion
- Fourier analysis on tori; pseudo-inverse of the graph Laplacian; asymptotics of lattice Green functions
- odd/even decomposition in the branch label
- bipartite (staggered) mirror
- numerical check by exact diagonalization (dense and Lanczos) and FFT
