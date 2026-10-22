# Weight of a bond made through the field

- **Subproject:** 07-ilang-weight
- **Package:** 04-weight-of-bond
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-20

## Setup and assumptions

- **Field (assumption, M8).** $`N_f\ge1`$ identical field objects ($`c=+1`$) without pair terms among them, on $`X_f`$: a ring ($`D=1`$), a square torus ($`D=2`$) or a cubic torus ($`D=3`$) of side $`L\ge3`$; $`\mathcal X:=\lvert X_f\rvert=L^D`$, $`n:=N_f/\mathcal X`$; own term $`C_1=-t_f\sum_{\{x,y\}}(\lvert x\rangle\langle y\rvert+\lvert y\rangle\langle x\rvert)`$, $`t_f>0`$; $`\Phi_x`$ the number of field objects at $`x`$. On one object $`C_1=t_f(\Lambda-2D)`$, $`\Lambda`$ the graph Laplacian. As in (4.4) of 06-ilang-source/04-profile,
```math
\ell(\mathbf x):=\Lambda^+(\mathbf x)=\frac1{\mathcal X}\sum_{\mathbf k\ne0}\frac{e^{i\mathbf k\cdot\mathbf x}}{\omega(\mathbf k)},\qquad \ell^{(2)}(\mathbf x):=(\Lambda^+)^2(\mathbf x)=\frac1{\mathcal X}\sum_{\mathbf k\ne0}\frac{e^{i\mathbf k\cdot\mathbf x}}{\omega(\mathbf k)^2},\qquad \omega(\mathbf k)=\sum_{\mu=1}^D4\sin^2\frac{k_\mu}2 ,
```
even functions of the displacement with $`\Lambda\ell=\delta_{\mathbf x,0}-\mathcal X^{-1}`$, $`\Lambda\ell^{(2)}=\ell`$, $`\sum_{\mathbf x}\ell=\sum_{\mathbf x}\ell^{(2)}=0`$; $`\ell_0:=\ell(0)`$.
- **Pair and source (assumption, M8, A15).** Two held Model D bodies ($`\tau=0`$) at $`x_1`$ and $`x_2=x_1+\mathbf r`$, on levels $`k_i`$ and branches $`\sigma_i`$ (half-gaps $`M^{(i)}_{k_i}`$), each coupled by coupling (a) or by the full grip with constant $`\gamma_i>0`$; no pair term between them; $`g_i:=\sigma_i\gamma_iM^{(i)}_{k_i}`$. One held source at $`x_s`$ with pair term $`g_s\Phi_{x_s}`$, first order in $`g_s`$. $`\mathbf R:=x_1-x_s`$, and $`d`$ is the length of the shortest representative of $`\mathbf R`$. Separations are those of field places; their relation to the distances of 03-ilang-space (M2) is not used.
- **State (assumption, M9, A11).** The eigenvector of the total contract connected, as the couplings go to zero, to the bodies in their internal states and every field object in the lowest one-object state. The mirrored highest state is treated in Step 7.
- **Regime (A13).** $`\eta:=\max(\lvert g_1\rvert,\lvert g_2\rvert)\,\ell_0/t_f\ll1`$, first order in $`g_s`$. Here $`\ell_0=(L^2-1)/(12L)`$ (ring), $`\ell_0\simeq\frac1{2\pi}\ln L+0.049`$ (square torus, value from the code), $`\ell_0\to0.2527`$ (cubic torus).
- **Inputs** (quoted in question.md): (4.2) of 06-ilang-source/04-profile, $`E=N_f\varepsilon_0(g)`$ and the bond $`M`$ as a combination of four descriptions; (4.4) there, $`M^{(2)}=-\frac{2ng_1g_2}{t_f}\Lambda^+(x_1,x_2)`$ with $`\sum_{x_2}M^{(2)}=0`$; (4.8) there, the third-order bond; (7.1)–(7.3) of 06-ilang-source/07-dressed-fall, the one-object contract $`h_x`$, the weight as the place dependence of $`N_f\varepsilon_0`$, and its expansion on the ring.
- **Standard mathematics (M5).** Rayleigh–Schrödinger perturbation theory for an isolated non-degenerate eigenvalue, the Hellmann–Feynman theorem, Fourier analysis on tori, asymptotics of the lattice Green functions of $`\mathbb Z^2`$ and $`\mathbb Z^3`$.

## Derivation

### Step 1. Reduction to one field object

With $`\tau=0`$ the total contract commutes with the position label of each body, with $`\sigma_3`$ and with $`D`$. In the sector of given $`(x_i,k_i,\sigma_i)`$ it acts as $`c+\sum_{j=1}^{N_f}h^{(j)}`$, with $`h^{(j)}`$ acting on field object $`j`$ as
```math
h=C_1+g_1P_{x_1}+g_2P_{x_2}+g_sP_{x_s},\qquad c=\sigma_1M^{(1)}_{k_1}+\sigma_2M^{(2)}_{k_2}\ \text{(coupling (a))},\qquad c=0\ \text{(full grip)},
```
up to the place-independent own term of the source. By (4.2) of 06-ilang-source/04-profile the eigenvalue of the stated state is $`E=c+N_f\varepsilon_0(h)`$, with $`\varepsilon_0`$ the lowest eigenvalue of $`h`$. Every quantity below is a difference of eigenvalues of total contracts, so it is fixed by them (M6), and A5 replacements do not change it. $`E`$ depends on the bodies only through the set $`\{(x_1,g_1),(x_2,g_2)\}`$. For bodies of one type it is therefore the eigenvalue of the (anti)symmetrized admissible state, and it does not depend on labels (Law 5). The two couplings differ only by the constant $`c`$. They give the same bond profile and the same weights, and differ in the costs of levels (Step 5).

### Step 2. Perturbation series

$`C_1`$ has the isolated lowest eigenvalue $`-2Dt_f`$, with eigenvector $`u=\mathcal X^{-1/2}\sum_x\lvert x\rangle`$ and gap $`4t_f\sin^2(\pi/L)`$; its reduced resolvent there is $`R=-\Lambda^+/t_f`$. Take $`V=\sum_ag_aP_{x_a}`$, $`a\in\{1,2,s\}`$, and $`\langle u\vert P_{x_a}=\mathcal X^{-1/2}\langle x_a\rvert`$. Insert these into the standard Rayleigh–Schrödinger terms $`\langle u\vert V\vert u\rangle`$, $`\langle u\vert VRV\vert u\rangle`$ and $`\langle u\vert VRVRV\vert u\rangle-\langle u\vert V\vert u\rangle\langle u\vert VR^2V\vert u\rangle`$:
```math
\varepsilon_0=-2Dt_f+\frac{\sum_ag_a}{\mathcal X}-\frac{1}{t_f\mathcal X}\sum_{a,b}g_ag_b\,\ell_{ab}+\frac{1}{t_f^2\mathcal X}\Big[\sum_{a,b,c}g_ag_bg_c\,\ell_{ab}\ell_{bc}-\frac{\sum_cg_c}{\mathcal X}\sum_{a,b}g_ag_b\,\ell^{(2)}_{ab}\Big]+O(g^4),\qquad\text{(4.1)}
```
with $`\ell_{ab}:=\ell(x_a-x_b)`$ and $`\ell^{(2)}_{ab}:=\ell^{(2)}(x_a-x_b)`$. The series converges for $`\sum_a\lvert g_a\rvert<2t_f\sin^2(\pi/L)`$ (Kato). Beyond that bound we use it as an expansion in η. Each further order adds one $`V`$ and one $`R`$, that is, a factor $`g\ell_{ab}/t_f`$ or $`g\ell^{(2)}_{ab}/(t_f\mathcal X\ell_{ab})`$. On the three graphs both factors are at most of order η, since $`\ell^{(2)}_0/(\mathcal X\ell_0)\le\ell_0`$ (ring: $`L/60`$). The code confirms that each truncation error scales as the next power of η (Code). The $`g_1g_2`$ and $`g_1g_2(g_1+g_2)`$ terms of (4.1) are (4.4) and (4.8) of 06-ilang-source/04-profile. Its $`g_sg_b`$ and $`g_sg_b^2`$ terms are (7.3) of 06-ilang-source/07-dressed-fall (there $`\mathcal X=L`$).

### Step 3. The bond profile (item 1)

Without the source, through second order the only $`\mathbf r`$-dependent term of (4.1) is the $`g_1g_2`$ term. By translation invariance it does not depend on $`x_1`$:
```math
E(x_1,\mathbf r)-E(x_1,\mathbf r')=\big[B(\mathbf r)-B(\mathbf r')\big]\big(1+O(\eta)\big),\qquad B(\mathbf r):=-\frac{2ng_1g_2}{t_f}\,\ell(\mathbf r).\qquad\text{(4.2)}
```
The relative $`O(\eta)`$ is the third-order bond, (4.8) of 06-ilang-source/04-profile, and $`B`$ is $`M^{(2)}`$ of (4.4) there.
- *Fixed by the total contract:* the whole profile (4.2), which is a difference of two eigenvalues of one total contract. It is the same for both couplings and every A5 split, and at second order it contains the couplings only through $`g_1g_2`$.
- *Not fixed by one total contract:* the $`\mathbf r`$-independent part of $`E`$. This is the zero of $`B`$ (the normalization $`\sum_{\mathbf r}B=0`$ refers to the four descriptions of (4.2) of 06-ilang-source/04-profile), together with the split of $`E`$ into rest costs, own marks ($`-ng_i^2\ell_0/t_f`$) and bond.

*Ring.* Let $`r`$ be the label difference mod $`L`$. The quadratic below has second difference $`1/L`$ for $`0<r<L`$, a kink of $`1`$ at $`r=0`$ and zero sum, so it is the zero-mean solution of $`\Lambda\ell=\delta-1/L`$, that is $`\Lambda^+`$:
```math
\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L},\qquad E(r)-E(r')=\frac{ng_1g_2}{t_fL}\big[r(L-r)-r'(L-r')\big]\big(1+O(\eta)\big).\qquad\text{(4.3)}
```

*Tori.* As $`L\to\infty`$ at fixed $`\mathbf r`$, $`\ell(0)-\ell(\mathbf r)`$ tends to the potential kernel of $`\mathbb Z^D`$. Its standard asymptotics, plus the smooth background forced by $`\Lambda\ell=-\mathcal X^{-1}`$ away from $`0`$, give
```math
\ell(0)-\ell(\mathbf r)=\begin{cases}\dfrac{\ln\lvert\mathbf r\rvert}{2\pi}+\dfrac{2\gamma_E+3\ln2}{4\pi}+O(\lvert\mathbf r\rvert^{-2})-\dfrac{\lvert\mathbf r\rvert^2}{4L^2}, & D=2,\\[2mm] G_0-\dfrac1{4\pi\lvert\mathbf r\rvert}+O(\lvert\mathbf r\rvert^{-3})-\dfrac{\lvert\mathbf r\rvert^2}{6L^3},\quad G_0=\Lambda^{-1}_{\mathbb Z^3}(0)=0.2527310, & D=3,\end{cases}\qquad\text{(4.4)}
```
up to higher terms in $`\lvert\mathbf r\rvert/L`$ (code: deviations scale as $`\lvert\mathbf r\rvert^{-2}`$, $`\lvert\mathbf r\rvert^{-3}`$ and as the stated background). For $`1\ll\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll L`$, therefore, $`E(\mathbf r)-E(\mathbf r')\simeq\frac{ng_1g_2}{\pi t_f}\ln\frac{\lvert\mathbf r\rvert}{\lvert\mathbf r'\rvert}`$ ($`D=2`$) and $`\simeq-\frac{ng_1g_2}{2\pi t_f}\big(\frac1{\lvert\mathbf r\rvert}-\frac1{\lvert\mathbf r'\rvert}\big)`$ ($`D=3`$). For $`g_1g_2>0`$ (equal branches) $`E`$ grows with the separation: on the ring with the graph distance, on the tori for $`1\ll\lvert\mathbf r\rvert\ll L`$. For $`g_1g_2<0`$ it falls.

### Step 4. Weight of a body and of the pair (item 2)

The weight at first order in $`g_s`$ is the $`g_s`$-linear part of $`E`$ as a function of the place, as in (7.2) of 06-ilang-source/07-dressed-fall, up to a place-independent constant. Collect the $`g_s`$-linear terms of (4.1) and put $`\phi(x):=-\frac{2g_s}{t_f}\ell(x-x_s)`$. A body alone then has
```math
W_i(x)=ng_i\,\phi(x)+\frac{ng_sg_i^2}{t_f^2}\Big[2\ell_0\,\ell(x-x_s)+\ell(x-x_s)^2-\frac2{\mathcal X}\,\ell^{(2)}(x-x_s)\Big]\qquad(\text{relative error }O(\eta^2)),\qquad\text{(4.5)}
```
which is (7.3) of 06-ilang-source/07-dressed-fall, now on all three graphs. For the pair, $`W_{\rm pair}(x_1;\mathbf r)=W_1(x_1)+W_2(x_1+\mathbf r)+W_b(x_1;\mathbf r)`$ with
```math
W_b=\frac{2ng_sg_1g_2}{t_f^2}\,S,\qquad S:=\ell(\mathbf r)\big(\ell_{1s}+\ell_{2s}\big)+\ell_{1s}\ell_{2s}-\frac{\ell^{(2)}_{1s}+\ell^{(2)}_{2s}}{\mathcal X}\qquad(\text{relative error }O(\eta)),\qquad\text{(4.6)}
```
up to the place-independent $`-\frac{2ng_sg_1g_2}{t_f^2\mathcal X}\ell^{(2)}(\mathbf r)`$. $`W_b`$ collects the $`g_sg_1g_2`$ terms of (4.1). The orderings with $`s`$ at an end of $`\ell_{ab}\ell_{bc}`$ give $`2\ell(\mathbf r)(\ell_{1s}+\ell_{2s})`$, those with $`s`$ in the middle give $`2\ell_{1s}\ell_{2s}`$, and the $`1/\mathcal X`$ terms give the rest. It is the $`g_s`$-linear, place-dependent part of $`E(g_1,g_2)-E(g_1,0)-E(0,g_2)+E(0,0)`$ with the source present. This is the bond of (4.2) of 06-ilang-source/04-profile weighed in the field of the source, and it is fixed by the four total contracts as that bond is. With $`\phi(x_a)=-\frac{2g_s}{t_f}\ell_{as}`$,
```math
W_b(x_1;\mathbf r)=\tfrac12B(\mathbf r)\big[\phi(x_1)+\phi(x_2)\big]+\frac{ng_1g_2}{2g_s}\,\phi(x_1)\phi(x_2)-\frac{2ng_sg_1g_2}{t_f^2\mathcal X}\big[\ell^{(2)}_{1s}+\ell^{(2)}_{2s}\big].\qquad\text{(4.7)}
```
By (4.5) the first-order cost $`ng_i`$ of a body is weighed by $`\phi`$ at its place. By (4.7) the bond is weighed by the same $`\phi`$, half at the place of each body. The second term of (4.7) is the change of the propagation between the bodies caused by the source ($`\ell_{12}\to\ell_{12}-\frac{g_s}{t_f}\ell_{1s}\ell_{s2}`$, the first-order change of the reduced resolvent), and the third is the normalization of the lowest state.

*Distance large against $`\lvert\mathbf r\rvert`$.* Let $`\mathcal C_{\rm p}(\mathbf r):=n(g_1+g_2)-\frac n{t_f}\big[(g_1^2+g_2^2)\ell_0+2g_1g_2\ell(\mathbf r)\big]`$ be the coupling-made cost of the pair through second order ((4.1) without source). Rearranging (4.5)–(4.7) exactly gives
```math
W_{\rm pair}=\mathcal C_{\rm p}(\mathbf r)\,\phi(x_1)+\frac{ng_s(g_1+g_2)^2}{t_f^2}\Big[\ell(\mathbf R)^2-\frac{2\ell^{(2)}(\mathbf R)}{\mathcal X}\Big]+\big[W_2(x_2)-W_2(x_1)\big]+\frac{2ng_sg_1g_2}{t_f^2}\,\delta S,\qquad \delta S:=\big(\ell(\mathbf r)+\ell_{1s}\big)\big(\ell_{2s}-\ell_{1s}\big)-\frac{\ell^{(2)}_{2s}-\ell^{(2)}_{1s}}{\mathcal X}.\qquad\text{(4.8)}
```
The last two terms are of first order in $`\mathbf r\cdot\nabla\ell(\mathbf R)`$. For $`\lvert\mathbf r\rvert\ll d`$ the pair is therefore weighed like one body of coupling $`g_1+g_2`$, except that its cost $`\mathcal C_{\rm p}`$ contains the bond $`B`$, and this cost is weighed by $`\phi`$ as a whole. On the ring $`\phi`$ is the quadratic (4.3). For $`1\ll d\ll L`$, by (4.4), $`\phi(x)=\text{const}+\frac{g_s}{\pi t_f}\ln d`$ ($`D=2`$) and $`\phi(x)=\text{const}-\frac{g_s}{2\pi t_fd}`$ ($`D=3`$).

### Step 5. How the weight of a single body follows its cost

Compare two internal states $`(k,\sigma)`$ and $`(k',\sigma')`$ of body $`i`$ alone. By (4.1) without the source, their cost difference is $`\Delta\mathcal C_i=n\gamma_i(\sigma M_k-\sigma'M_{k'})`$ for the full grip and $`(1+n\gamma_i)(\sigma M_k-\sigma'M_{k'})`$ for coupling (a), each times $`1+O(\eta)`$. By (4.5) their weight difference is $`n\gamma_i(\sigma M_k-\sigma'M_{k'})\,\phi`$ in both couplings. Hence
```math
\Delta W_i(x)-\Delta W_i(x')=\Delta\mathcal C_i\,\big[F_i(x)-F_i(x')\big]\big(1+O(\eta)\big),\qquad F_i=\phi\ \ \text{(full grip)},\qquad F_i=\frac{n\gamma_i}{1+n\gamma_i}\,\phi\ \ \text{(coupling (a))}.\qquad\text{(4.9)}
```
For the full grip $`F`$ is the same for every level, branch and body. For coupling (a) it depends on the body through $`n\gamma_i`$, because the rest term of the body's own contract is not weighed at this order.

### Step 6. Is the bond weighed? (item 3)

Let $`\Delta_{\mathbf e}f(y):=f(y+\mathbf e)-f(y)`$ for a unit step $`\mathbf e`$ of the pair as a whole, and $`\Delta_{\mathbf r\mathbf r'}f:=f(\mathbf r)-f(\mathbf r')`$. Beyond the weights of the bodies at their own places, the part of the weight of the pair that depends on $`\mathbf r`$ is $`W_b`$. Its profile is compared with the bond profile (4.2) times the function (4.9):
```math
\rho_i:=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}W_b(x_1;\cdot)}{\Delta_{\mathbf r\mathbf r'}B\;\Delta_{\mathbf e}F_i(x_1)},\qquad \rho_i^{\rm fg}=\rho_0\big(1+O(\eta)\big),\qquad \rho_0=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}S}{2\,\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)}=1+\kappa,\qquad \kappa=\frac{\Delta_{\mathbf e}\Delta_{\mathbf r\mathbf r'}\delta S}{2\,\Delta_{\mathbf r\mathbf r'}\ell\;\Delta_{\mathbf e}\ell(\mathbf R)} .\qquad\text{(4.10)}
```
This holds for $`\ell(\mathbf r)\ne\ell(\mathbf r')`$ and $`\Delta_{\mathbf e}\ell(\mathbf R)\ne0`$; "fg" means full grip. The value $`1`$ comes from $`S-\delta S=2\ell(\mathbf r)\ell_{1s}+(\text{terms without }\mathbf r)`$. The configurations used, $`\{x_1,x_1+\mathbf r\}`$ and $`\{x_1,x_1+\mathbf r'\}`$ and their translates, share the body at $`x_1`$, so $`\rho_i`$ does not depend on labels. Neither $`\rho_0`$ nor $`\kappa`$ contains a coupling. At leading order in η the ratio is therefore exactly the same for every level, branch, $`\gamma_i`$, $`N_f`$, $`t_f`$ and sign of $`g_s`$, and for both signs of the bond ($`g_1g_2<0`$ reverses $`W_b`$ and $`B`$ together). The class contains no control at this order. At order η the exact ratio depends on levels and bodies (code).

*Expansion in $`\lvert\mathbf r\rvert/d`$.* For $`d\gg1`$, expand $`\ell_{2s}=\ell(\mathbf R+\mathbf r)`$ in δS by Taylor's theorem, with $`\partial_{\mathbf e}:=\mathbf e\cdot\nabla`$:
```math
\kappa=\frac{\big[(\ell(\mathbf r)+\ell(\mathbf R))\,\mathbf r-(\ell(\mathbf r')+\ell(\mathbf R))\,\mathbf r'\big]\cdot\nabla\partial_{\mathbf e}\ell+(\mathbf r-\mathbf r')\cdot\nabla\ell\;\partial_{\mathbf e}\ell-\mathcal X^{-1}(\mathbf r-\mathbf r')\cdot\nabla\partial_{\mathbf e}\ell^{(2)}}{2\,[\ell(\mathbf r)-\ell(\mathbf r')]\,\partial_{\mathbf e}\ell}\bigg\rvert_{\mathbf R}+\big(\text{second order in }\mathbf r/d,\ \mathbf r'/d\big).\qquad\text{(4.11)}
```
The sizes below assume $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$, $`\lvert\mathbf r'\rvert/\lvert\mathbf r\rvert`$ of order 2, and a place where $`\partial_{\mathbf e}\ell(\mathbf R)`$ is not anomalously small. Using (4.4):
- $`D=3`$: $`\kappa=O(\lvert\mathbf r'\rvert/d)`$. The code finds $`d\kappa\approx1.0`$ and $`2.0`$ for non-collinear $`\mathbf r,\mathbf r'`$, and smaller values for collinear ones.
- $`D=2`$: here $`\ell(\mathbf r)+\ell(\mathbf R)\simeq\frac1{2\pi}\ln\frac{L^2}{\lvert\mathbf r\rvert d}`$, so $`\kappa=O\big(\frac{\lvert\mathbf r-\mathbf r'\rvert}{d}\ln\frac{L^2}{\lvert\mathbf r\rvert d}\big)`$, which grows like $`\ln L`$ at fixed places. The code finds $`d\kappa\approx3.1,\,5.7,\,8.6`$ for $`L=128,512,2048`$.

The first-order κ consists only of relocations. When $`\mathbf r`$ changes at fixed $`x_1`$, the midpoint at which the absolute bond $`B`$ is weighed (4.7) moves by $`(\mathbf r-\mathbf r')/2`$. The $`\mathbf r`$-independent $`g_1g_2`$ terms of (4.7) taken at the midpoint, $`\frac{ng_1g_2}{2g_s}\phi^2`$ and the normalization term, move with it. Expanding these displacements reproduces (4.11) term by term.

*Midpoint as the place.* Take $`\bar x:=x_1+\mathbf r/2`$ as the place, with $`\mathbf r,\mathbf r'`$ having even components, change $`\mathbf r`$ at fixed $`\bar x`$, and define $`\rho^{\rm mid}_i`$ as in (4.10) with $`x_1\to\bar x`$. $`S`$ is symmetric in the two bodies, so expanded about $`\bar x`$ it contains only even powers of $`\mathbf r`$, and $`\rho^{\rm mid}_0=1+\kappa^{\rm mid}`$ has no first-order term. On the ring, put $`d_{1,2}=\bar d\mp r/2`$. Besides the main term $`2\ell(r)\ell(\bar d)`$, the only terms of $`S`$ that depend on both $`r`$ and $`\bar d`$ are $`\frac{r^2}{4L}\big[2\ell(\bar d)-L\ell'(\bar d)^2\big]`$, using $`\ell''=1/L`$ and $`\ell^{(2)\prime\prime}=-\ell+\text{const}`$ from $`\Lambda\ell^{(2)}=\ell`$. For the quadratic (4.3), $`2\ell-L\ell'^2=\frac{L^2-1}{6L}-\frac L4`$ is constant. For the same steps, evaluating (4.10) with (4.3) gives the ring value of $`\rho_0`$. Altogether:
```math
\kappa^{\rm mid}_{D=3}=O\Big(\frac{\lvert\mathbf r\rvert\lvert\mathbf r'\rvert}{d^2}\Big),\qquad \kappa^{\rm mid}_{D=2}=O\Big(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d}\Big),\qquad \kappa^{\rm mid}_{\rm ring}=0,\qquad \rho_0^{\rm ring}=\frac{2(1-w)(1-2w)}{(1-2u)(1-2v)}.\qquad\text{(4.12)}
```
- On the ring, $`u=d_1/L`$, $`v=r/L`$ and $`w=u+v`$, where $`d_1<d_2=d_1+r`$ are the arc lengths from $`x_s`$ to the bodies, taken in the sense in which the arc from $`x_1`$ to $`x_2`$ does not contain $`x_s`$.
- Both ring statements hold for $`x_s`$ outside that arc. $`\rho_0^{\rm ring}`$ is for unit steps in that sense and $`r'=r-1`$.
- The code confirms these statements on the lattice, with $`u=(d_1+\frac12)/L`$ and $`v=(r-\frac12)/L`$:
  - both ring statements hold to rounding error;
  - on the tori, $`d^2\kappa^{\rm mid}\approx-2`$ to $`-3`$ ($`D=3`$) and $`\approx-15,-30,-47`$ ($`D=2`$, $`L=128,512,2048`$).
- For $`v\to0`$, $`\rho_0^{\rm ring}\to2(1-u)\in(0,2)`$.

*Answer for the full grip.* The bond is weighed like the costs of the bodies, by the same function $`\phi`$ placed at the midpoint of the pair:
- On the ring this is exact at leading order in η ($`\rho^{\rm mid}_0=1`$). Referred to $`x_1`$, the question's place, the ratio is $`\rho_0^{\rm ring}\neq1`$ at generic places, entirely through the relocation.
- On the cubic torus, $`\rho_0=1+O(\lvert\mathbf r'\rvert/d)`$ and $`\rho_0^{\rm mid}=1+O(\lvert\mathbf r\rvert\lvert\mathbf r'\rvert/d^2)`$.
- On the square torus the same holds only for $`d`$ large against $`\lvert\mathbf r-\mathbf r'\rvert\ln(L^2/(\lvert\mathbf r\rvert d))`$, respectively against $`\lvert\mathbf r'\rvert\ln^{1/2}(L^2/(\lvert\mathbf r'\rvert d))`$. At fixed places it fails as $`L\to\infty`$.

*Coupling (a).* By (4.9), with the same $`W_b`$ and $`B`$,
```math
\rho_i^{(a)}=\frac{1+n\gamma_i}{n\gamma_i}\,\rho_i^{\rm fg},\qquad \rho_i^{{\rm mid},(a)}=\frac{1+n\gamma_i}{n\gamma_i}\,\rho_i^{\rm mid,fg}.\qquad\text{(4.13)}
```
Wherever the full-grip ratio is near 1, this ratio is near $`(1+n\gamma_i)/(n\gamma_i)>1`$, on every graph. The bond, which is made entirely through the field, is weighed per unit cost $`(1+n\gamma_i)/(n\gamma_i)`$ times as strongly as the level costs of body $`i`$. For unequal $`\gamma_1\ne\gamma_2`$ the two bodies' functions also differ. The ratio approaches the full-grip value only for $`n\gamma_i\to\infty`$.

*Controls (M9).*
- For "yes" (full grip): coupling (a) of the same class, by (4.13); the square torus at fixed places with $`L\to\infty`$; and the ring referred to $`x_1`$, by (4.12).
- For "no" (coupling (a)): the full grip on the cubic torus.
- For the independence of levels and branches: none in the class at leading order in η; at order η the code shows a dependence.

### Step 7. The mirrored highest state

For even $`L`$ the graphs are bipartite. The sublattice sign $`U`$ is diagonal in places with $`U^2=1`$, $`UC_1U=-C_1`$ and $`UP_xU=P_x`$, so $`\max\mathrm{spec}(C_1+V)=-\min\mathrm{spec}(C_1-V)`$, and the highest state has $`E^{\max}(g)=c-N_f\varepsilon_0(-g)`$. Terms of odd total order in $`(g_1,g_2,g_s)`$ are unchanged and terms of even order are reversed:
```math
B\to-B,\qquad \phi\to-\phi,\qquad F_i\to-F_i,\qquad W_b\to W_b,\qquad \rho_i,\ \rho_i^{\rm mid}\ \text{unchanged}.\qquad\text{(4.14)}
```
The code checks the mirror identity to rounding error. For odd $`L`$ the highest one-object level of $`C_1`$ is degenerate, so this construction does not define a mirrored state.

## Result

Class: both couplings, every $`N_f\ge1`$, all levels and branches, equal and unequal bodies, ring and square and cubic tori of side $`L\ge3`$, held bodies, field in the stated lowest state (Step 7: highest, for even $`L`$), first order in $`g_s`$.

- **(4.1)** Through third order in the point couplings, the lowest one-object eigenvalue is given by Rayleigh–Schrödinger with reduced resolvent $`-\Lambda^+/t_f`$. Each further order is smaller by a factor of order $`\eta=\max\lvert g_i\rvert\ell_0/t_f`$.
- **(4.2)** The bond profile is $`E(x_1,\mathbf r)-E(x_1,\mathbf r')=[B(\mathbf r)-B(\mathbf r')](1+O(\eta))`$ with $`B=-\frac{2ng_1g_2}{t_f}\ell(\mathbf r)`$, independent of $`x_1`$.
  - It is fixed by one total contract, and is the same for both couplings and for every A5 split.
  - The zero of $`B`$ and the split into rest costs, own marks and bond are fixed only by comparing descriptions.
- **(4.3)** On the ring, $`\ell(r)=\frac{L^2-1}{12L}-\frac{r(L-r)}{2L}`$ and the profile is $`\frac{ng_1g_2}{t_fL}[r(L-r)-r'(L-r')]`$.
- **(4.4)** On the tori, $`\ell(0)-\ell(\mathbf r)`$ has the forms of (4.4). The profile is logarithmic ($`D=2`$) and of the form $`1/\lvert\mathbf r\rvert`$ ($`D=3`$) for $`1\ll\lvert\mathbf r\rvert\ll L`$.
- **(4.5)** A body alone has weight $`W_i=ng_i\phi+\frac{ng_sg_i^2}{t_f^2}[2\ell_0\ell+\ell^2-\frac2{\mathcal X}\ell^{(2)}]`$ with $`\phi=-\frac{2g_s}{t_f}\ell(x-x_s)`$, on all three graphs, with relative error $`O(\eta^2)`$.
- **(4.6)** The pair has weight $`W_1(x_1)+W_2(x_2)+W_b`$ with $`W_b=\frac{2ng_sg_1g_2}{t_f^2}S`$, with relative error $`O(\eta)`$ on $`W_b`$.
- **(4.7)** $`W_b=\frac12B(\mathbf r)[\phi(x_1)+\phi(x_2)]`$ plus the source-modified propagation term $`\frac{ng_1g_2}{2g_s}\phi(x_1)\phi(x_2)`$ plus a normalization term. The bond is weighed by the same $`\phi`$ as the first-order costs, half at each body.
- **(4.8)** This is an exact rearrangement: the pair is weighed as $`\mathcal C_{\rm p}(\mathbf r)\phi(x_1)`$ plus a term depending only on $`g_1+g_2`$, plus terms of first order in $`\mathbf r\cdot\nabla\ell(\mathbf R)`$.
- **(4.9)** For a body alone, level differences of weight equal level differences of cost times $`F_i`$, at leading order in η. $`F_i=\phi`$ for the full grip, the same for all levels, branches and bodies; $`F_i=\frac{n\gamma_i}{1+n\gamma_i}\phi`$ for coupling (a).
- **(4.10)** For the full grip the ratio of the bond's weight to bond profile times $`F`$ is $`\rho_0(1+O(\eta))`$, with $`\rho_0=1+\kappa`$. $`\rho_0`$ depends only on the graph and the places, and not on levels, branches, $`\gamma_i`$, $`N_f`$, $`t_f`$ or the sign of the bond.
- **(4.11)** For $`d\gg1`$, κ is of first order in $`\mathbf r/d`$, $`\mathbf r'/d`$, for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$ at generic places. It is $`O(\lvert\mathbf r'\rvert/d)`$ on the cubic torus and $`O(\frac{\lvert\mathbf r-\mathbf r'\rvert}{d}\ln\frac{L^2}{\lvert\mathbf r\rvert d})`$ on the square torus. It consists of relocations: when $`\mathbf r`$ changes at fixed $`x_1`$, the midpoint at which the bond is weighed moves, and the $`\mathbf r`$-independent $`g_1g_2`$ terms move with it.
- **(4.12)** Referred to the midpoint, $`\kappa^{\rm mid}`$ has no first-order term:
  - it is $`O(\lvert\mathbf r\rvert\lvert\mathbf r'\rvert/d^2)`$ on the cubic torus and $`O(\frac{\lvert\mathbf r'\rvert^2}{d^2}\ln\frac{L^2}{\lvert\mathbf r'\rvert d})`$ on the square torus;
  - on the ring it is $`0`$ at leading order in η, for $`x_s`$ outside the arc between the bodies; there the ratio referred to $`x_1`$ is $`\frac{2(1-w)(1-2w)}{(1-2u)(1-2v)}`$ (unit steps).
  - Answer, full grip: yes on the ring (midpoint, exact at leading order in η), and on the cubic torus for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d\ll L`$. On the square torus, yes only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$.
- **(4.13)** For coupling (a) the ratio is $`\frac{1+n\gamma_i}{n\gamma_i}`$ times the full-grip ratio. Answer: no, on every graph. Wherever the full-grip ratio is 1 (the ring with the midpoint place; the tori in the ranges of (4.11)–(4.12)), the ratio is $`\frac{1+n\gamma_i}{n\gamma_i}>1`$: the bond is weighed more strongly than the level costs of the bodies.
- **(4.14)** In the highest state (even $`L`$), $`B`$, $`\phi`$ and $`F_i`$ change sign, $`W_b`$ does not, and all ratios are unchanged.

## Consistency checks

1. **Dimensions.** $`g_a`$, $`t_f`$ and $`E`$ are costs, while $`\ell`$, $`\ell^{(2)}/\mathcal X`$ (per $`\ell`$) and $`\phi`$ are pure numbers. $`B\sim ng^2/t_f`$ and $`W_b\sim ng_sg^2/t_f^2`$ are costs, and $`\rho`$ and κ are pure numbers. Passed.
2. **One body and independent bodies.** For $`g_2\to0`$, $`B`$ and $`W_b`$ vanish and (4.8) reduces to (4.5) for body 1. On the cubic torus every term of $`S-\ell^{(2)}(\mathbf r)/\mathcal X`$ carries two factors of ℓ or a factor $`\ell^{(2)}/\mathcal X`$. It therefore vanishes as all separations grow, and the pair is weighed as the sum of its bodies. The code finds $`3.5\cdot10^{-5}`$, $`7.7\cdot10^{-6}`$ and $`1.9\cdot10^{-6}`$ at separations $`L/4`$ for $`L=16,32,64`$. Passed.
3. **Sum rule.** By Hellmann–Feynman, $`\partial_{g_s}\varepsilon_0=\lvert\psi_0(x_s)\rvert^2`$, so $`\sum_{x_s}\partial_{g_s}E=N_f`$ for every $`g_1,g_2`$. Every $`g_1g_2`$ term of the weight must therefore sum to zero over the place. Using $`\sum_x\ell=\sum_x\ell^{(2)}=0`$ and $`\sum_x\ell(a-x)\ell(x-b)=\ell^{(2)}(a-b)`$, $`\sum_{x_1}[S-\ell^{(2)}(\mathbf r)/\mathcal X]=\ell^{(2)}(\mathbf r)-\ell^{(2)}(\mathbf r)=0`$; the code finds at most $`10^{-15}`$. Passed.

## Open issues

- Separations are those of field places; how they relate to the distances of 03-ilang-space is not used here.
- The ratio depends on the place assigned to an extended pair. Referred to $`x_1`$ it has the first-order relocation κ; referred to the midpoint it has none. Which place the fall of a pair tests is for the packages on mutual motion and inertia.
- The $`O(\eta)`$ dependence of the ratio on levels, branches and bodies is shown only numerically (code), not derived.
- The estimates of κ and $`\kappa^{\rm mid}`$ on the tori are order estimates at generic places, checked numerically. They fail near places where $`\partial_{\mathbf e}\ell(\mathbf R)`$ vanishes.
- Only held bodies and the lowest (or mirrored highest) field state are treated; other field states (A11) are not.
- For coupling (a) the rest term is not weighed at this order. Whether a wider class of couplings or field contracts weighs it is not decided here (M10: nothing is said about what the language enforces).

## Code

- `code/v1/check_weight_of_bond.py` (role: check). For $`N_f=1`$, $`t_f=1`$ it builds the one-object contract $`h=C_1+g_1P_{x_1}+g_2P_{x_2}+g_sP_{x_s}`$ on a ring ($`L=30,60`$), a square torus ($`L=12,20`$) and a cubic torus ($`L=8,10`$), and takes its exact lowest eigenvalue by dense diagonalization. Setup:
  - couplings $`g_i=\sigma_i\gamma_iM_{k_i}`$ with $`M_k=1+0.5k`$, $`\gamma_2=0.6\gamma_1`$ and $`\gamma_1=\eta/(2.5\ell_0)`$, for $`\eta=0.08,0.04,0.02`$;
  - two choices of levels and branches, $`(k_1\sigma_1,k_2\sigma_2)=(0{+},1{+})`$ and $`(2{-},3{+})`$, the second with a repulsive bond;
  - $`g_s=0.01/\ell_0`$, with a symmetric difference in $`g_s`$;
  - the $`\ell`$, $`\ell^{(2)}`$ tables computed by FFT.

  It compares with the formulas:
  - the bond profile (4.2), the single-body weight (4.5), the bond part $`W_b`$ (4.6), and the ratios (4.10) (full grip, against both bodies), (4.13) (coupling (a)) and (4.12) (midpoint), all from exact eigenvalues;
  - the mirror identity (4.14) and the sum rule;
  - the ring form (4.3) and the torus forms (4.4) ($`D=2`$: $`L=256,1024`$; $`D=3`$: $`L=64,128`$);
  - the ring ratio (4.12) for $`L=40`$–$`320`$, and κ and $`\kappa^{\rm mid}`$ against $`d`$ ($`D=3`$: $`L=128`$; $`D=2`$: $`L=128,512,2048`$).

  Findings:
  - Every deviation from (4.2), (4.6), (4.10), (4.12) and (4.13) halves when η halves (ratio ≈ 2). The exceptions are entries at the $`10^{-4}`$ level of the $`O(g_s^2)`$ error, or entries crossing zero.
  - The deviation from (4.5) is at most $`4\cdot10^{-3}`$ and falls at least as fast as η.
  - The exact ratios tend to $`\rho_0`$, $`\rho_0^{\rm mid}`$ and $`\frac{1+n\gamma}{n\gamma}\rho_0`$. At $`\eta=0.08`$ they differ between the level choices and the two bodies, e.g. 1.234 against 1.181 on the ring with $`L=30`$. Output: `code/v1/output/check_weight_of_bond.txt`.

## Methods used

- Reduction of held-body sectors to one field object
- Rayleigh–Schrödinger perturbation theory (third order, isolated eigenvalue)
- Hellmann–Feynman theorem
- Pseudo-inverse of the graph Laplacian; Fourier analysis on tori
- Asymptotics of the lattice potential kernel ($`\mathbb Z^2`$, $`\mathbb Z^3`$)
- Taylor expansion in separation over distance; parity about the midpoint
- Bipartite sublattice symmetry
- Exact diagonalization (code check)
