# Exchange cells with a push: orientation, small deviations, mutual costs

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-26

## Changes from previous version

- I1, Step 11: the finite-size change of the R2 check is now stated for each geometry as `code/v2/output/spinwave_mutual.txt` gives it (perpendicular links at even $`r\ge8`$ change by up to $`0.045`$), together with what those values confirm and what they do not.
- I2, Step 12(ii): the R1 check ($`r\gg\ell_b`$) now reports the drift from $`L=64`$ to $`128`$ and the Aitken values with the range of $`r`$ where the extrapolation is meaningful, and says what the check confirms.
- I3, Result (8.14), (8.16): the cell factor is stated as $`c_{\rm cell}=c_1c_2`$; Step 10 now says the same.
- I4, Step 12(i), (8.18), Result, Open issues: the Result names the results that rest on Assumption E. Step 12(i) now derives the vertex factor $`\nu^2/(\nu^2+g'^2S^2)`$. The remainder $`O(r/\ell_b)`$ of the first line of (8.18) is marked, in the display and in the Result, as an estimate that rests on Step 12(i).
- Code: all three scripts were run again unchanged under `code/v2/`; every cited number comes from `code/v2/output/`.

## Setup and assumptions

**Field** (M8). One object with $`2S+1`$ places at each place $`x`$ of $`X_f`$, a cubic torus ($`D=3`$) or a ring ($`D=1`$) of even side $`L\ge4`$; $`N=L^D`$ objects, $`DN`$ links, coordination $`z=2D`$. $`C_{\rm ex}=J\sum_{\langle xy\rangle}\mathbf S_x\cdot\mathbf S_y`$, $`J>0`$ unless stated. $`\Delta`$ is the graph Laplacian, $`\Delta^+:=2z-\Delta`$ (the adjacency plus $`z`$), $`P_x`$ the projector onto place $`x`$, $`E={\rm diag}(\epsilon_x)`$; $`E\Delta E=\Delta^+`$ because every link joins the two classes. The class labels are chosen so that $`\epsilon_h=+1`$ (the other choice flips the sign of every $`m(x)`$). $`\hat g`$ is the pseudo-inverse of $`\Delta`$, so that the $`g`$ of 05-anchor is $`\hat g/\kappa_h`$; on the cubic torus $`\hat g\to\hat g_\infty`$, $`\hat g_\infty(0)=\gamma_3=0.2527310`$, $`\hat g_\infty(x)=\frac1{4\pi\lvert x\rvert}+O(\lvert x\rvert^{-3})`$ (quoted with 05-anchor).

**Push, sources, state** (M8, M9, A11, A15): as in the question: push $`-h_p\,\mathbf n\cdot\mathbf S_h`$; direction sources $`g\,\mathbf m\cdot\mathbf S_x`$ or $`g\,\mathbf m\cdot(\mathbf S_x-\mathbf S_{x'})`$ ($`x'`$ a neighbour of $`x`$; $`\epsilon_x`$ below is the class of the object with the sign $`+`$); relation sources R1 ($`g'\,\mathbf S_b\cdot\mathbf S_x`$, spin $`s_b`$) and R2 (link coefficient $`J+\delta`$). State: the lowest eigenvector of the stated total contract. $`\mathbf e_1,\mathbf e_2`$ complete $`\mathbf n`$ to a right-handed frame; $`\mathbf m^\perp:=\mathbf m-(\mathbf m\cdot\mathbf n)\mathbf n`$.

**Small numbers.** $`1/S`$; $`\eta:=h_p/(JS)`$ (not assumed small); $`\lvert g\rvert/h_p`$ and $`\lvert g\rvert/(JS)`$; $`\lvert g'\rvert/J`$, $`\lvert\delta\rvert/J`$. $`\lvert g\rvert\ll JS`$ does not make $`\lvert g\rvert/h_p`$ small; this is a separate condition (Step 6).

**Assumption E (expansion in $`1/S`$).** Each $`\mathbf S_x`$ is written exactly through one oscillator (Holstein–Primakoff, on its lowest $`2S+1`$ levels) about the classical minimum selected by the push, and the contract is truncated at quadratic order in the oscillator operators. As usual for this expansion we take its lowest eigenvector to give the quantities of the true lowest eigenvector asymptotically in $`1/S`$ as long as every occupation $`\langle n_x\rangle`$ stays $`\ll S`$; where this fails, it is said.

**Inputs** (08-ilang-propagation/05-anchor@v3; field $`H=\frac12p^{\rm T}p+\frac12q^{\rm T}Aq+b^{\rm T}q+c_0`$, $`A=\kappa_h\Delta+\kappa_aP_h`$ without bodies): the criterion (5.3) (lowest eigenvector iff $`A>0`$), the body criteria (5.4)–(5.6), (5.10), the negative result (5.7), the made field (5.11), and

```math
G_a(x,y)=(K_a^{-1})_{xy}=\frac1{\kappa_a}+g(x-y)-g(x-h)-g(y-h)+g(0),\qquad \mathcal E_{12}=-g_1g_2\,G_a(x_1,x_2),\qquad\text{(5.8), (5.14)}
```

```math
\mathcal E_{12}=-g_1g_2\,c_\phi-\frac{g_1g_2}{4\pi\kappa_h}\Bigl[\frac1{\lvert x_1-x_2\rvert}-\frac1{\lvert x_1-h\rvert}-\frac1{\lvert x_2-h\rvert}\Bigr]+O(\ell^{-3}).\qquad\text{(5.15)}
```

## Derivation

### Step 1. The field alone (item 1(a), standard)

$`J>0`$: the graph is connected and bipartite with classes of equal size $`N/2`$. By the Marshall–Lieb–Mattis theorem (Perron–Frobenius after the Marshall sign change in each sector of $`\sum_xS^3_x`$, and Lieb–Mattis ordering) the lowest eigenvalue is simple and its eigenvector has total spin $`\lvert SN/2-SN/2\rvert=0`$. A total-spin singlet satisfies $`U\lvert\Psi_0\rangle=\lvert\Psi_0\rangle`$ for every common rotation, and the expectation of the vector operator $`\mathbf S_x`$ vanishes in it:

```math
J>0:\quad \lvert\Psi_0\rangle\ \text{unique},\qquad U(\theta,\mathbf u)\lvert\Psi_0\rangle=\lvert\Psi_0\rangle\ \ \forall\,\theta,\mathbf u,\qquad \langle\mathbf S_x\rangle=0,\quad\text{both graphs, every }S.\qquad\text{(8.1)}
```

$`J<0`$: the eigenvalues of $`\mathbf S_x\cdot\mathbf S_y=\frac12[(\mathbf S_x+\mathbf S_y)^2-2S(S+1)]`$ are $`\le S^2`$, with equality only on the pair spin $`2S`$; so $`C_{\rm ex}\ge JS^2DN`$ with equality exactly on the multiplet of total spin $`NS`$ (connected graph):

```math
J<0:\quad \text{lowest eigenvalue }JS^2DN,\ (2NS+1)\text{-fold};\ U\ \text{acts irreducibly on it, so no lowest eigenvector is unchanged by all }U.\qquad\text{(8.2)}
```

### Step 2. Exact statements with the push

$`\mathbf n\cdot\sum_x\mathbf S_x`$ commutes with $`C=C_{\rm ex}-h_p\mathbf n\cdot\mathbf S_h`$.

(a) $`J<0`$. $`C\ge JS^2DN-h_pS`$, since $`-h_p\mathbf n\cdot\mathbf S_h\ge-h_pS`$. The product state $`\lvert F\rangle`$ with $`\mathbf n\cdot\mathbf S_x=S`$ at every $`x`$ attains the bound; any state attaining it lies in the multiplet of spin $`NS`$ and has $`\mathbf n\cdot\mathbf S_h=S`$, which in that multiplet leaves only $`\lvert F\rangle`$:

```math
J<0,\ h_p>0:\quad \lvert\Psi_0\rangle=\lvert F\rangle\ \text{unique},\qquad \langle\mathbf n\cdot\mathbf S_x\rangle=S\ \text{exactly, every }x,L,S,h_p>0,\ \text{both graphs and both orders of limits}.\qquad\text{(8.3)}
```

(b) $`J>0`$, fixed $`L`$. At $`h_p=0`$ the lowest eigenvalue is simple (8.1) and isolated (finite dimension, A1), so the lowest eigenvector is analytic in $`h_p`$ near $`0`$ (standard perturbation theory) and $`m(x)=h_p\chi_L(x)+O(h_p^2)`$, $`\chi_L(x)=2\sum_{k\ne0}\epsilon_x\langle0\vert\mathbf n\cdot\mathbf S_x\vert k\rangle\langle k\vert\mathbf n\cdot\mathbf S_h\vert0\rangle/(E_k-E_0)`$, finite for each $`L`$:

```math
J>0:\qquad \lim_{L\to\infty}\,\lim_{h_p\to0}m(x)=0\qquad\text{every }S,\ \text{both graphs}.\qquad\text{(8.4)}
```

### Step 3. Expansion in $`1/S`$ about the orientation set by the push

The product state $`\mathbf S_x=\epsilon_xS\mathbf n`$ minimizes every link term classically, and the push selects $`\epsilon_h=+1`$. Holstein–Primakoff with a rotation by $`\pi`$ about $`\mathbf e_1`$ on class $`-`$: $`\epsilon_x\mathbf n\cdot\mathbf S_x=S-n_x`$, $`\mathbf e_1\cdot\mathbf S_x=\sqrt S\,Q_x+O(S^{-1/2})`$, $`\mathbf e_2\cdot\mathbf S_x=\epsilon_x\sqrt S\,P_x+O(S^{-1/2})`$, with $`[Q_x,P_y]=i\delta_{xy}`$, $`n_x=\frac12(Q_x^2+P_x^2-1)`$. Define the staggered transverse components

```math
q^{(1)}_x:=\epsilon_x\frac{\mathbf e_1\cdot\mathbf S_x}{\sqrt S}=\epsilon_xQ_x,\qquad q^{(2)}_x:=\epsilon_x\frac{\mathbf e_2\cdot\mathbf S_x}{\sqrt S}=P_x,\qquad [q^{(1)}_x,q^{(2)}_y]=i\epsilon_x\delta_{xy}.
```

For a link, $`\mathbf S_x\cdot\mathbf S_y=-(S-n_x)(S-n_y)+S(Q_xQ_y-P_xP_y)+O(1)=-S(S+1)+\frac S2\sum_\alpha(q^{(\alpha)}_x-q^{(\alpha)}_y)^2+O(1)`$, using $`\epsilon_y=-\epsilon_x`$; the push gives $`-h_p(S+\frac12)+\frac{h_p}2\sum_\alpha(q^{(\alpha)}_h)^2`$. Hence

```math
C=E_0+\frac12\sum_{\alpha=1,2}q^{(\alpha){\rm T}}V_a\,q^{(\alpha)}+C_4,\qquad V_a:=JS\Delta+h_pP_h,\qquad E_0=-JS(S+1)DN-h_p(S+\tfrac12),\qquad\text{(8.5)}
```

with $`C_4=O(J)`$ (quartic), of relative order $`1/S`$ while $`\langle n_x\rangle\ll S`$. With the canonical pair $`\tilde Q:=q^{(1)}`$, $`\tilde P:=Eq^{(2)}=\mathbf e_2\cdot\mathbf S/\sqrt S`$ the quadratic part reads $`C_2=\frac12\tilde P^{\rm T}T_a\tilde P+\frac12\tilde Q^{\rm T}V_a\tilde Q`$, $`T_a:=EV_aE=JS\Delta^++h_pP_h`$. For $`h_p>0`$ both $`V_a`$ and $`T_a`$ are positive definite, so $`C_2`$ has a unique Gaussian lowest eigenvector; for $`h_p=0`$ each has one zero mode (the constants, resp. $`\epsilon`$), the two common rotations about $`\mathbf e_1,\mathbf e_2`$. The canonical map $`\tilde Q\to E\tilde P`$, $`\tilde P\to-E\tilde Q`$ leaves $`C_2`$ unchanged, so $`\langle(q^{(1)}_x)^2\rangle=\langle(q^{(2)}_x)^2\rangle`$.

### Step 4. Orientation far from the push (item 1(b), orders $`S`$ and $`S^0`$)

From Step 3, $`m(x)=S-\Delta S(x)+O(1/S)`$ with $`\Delta S(x)=\langle n_x\rangle=\langle\tilde Q_x^2\rangle-\frac12`$, and the Gaussian covariance $`\langle\tilde Q\tilde Q^{\rm T}\rangle=\frac12T_a^{1/2}(T_a^{1/2}V_aT_a^{1/2})^{-1/2}T_a^{1/2}`$ depends only on $`\eta`$ and the graph. Leading order: $`m(x)=S`$.

*Zero modes.* The uniform mode $`\tilde Q_0=N^{-1/2}\sum_x\tilde Q_x`$ has potential weight $`h_p/N`$ and kinetic weight $`\simeq2zJS`$, so $`\langle\tilde Q_0^2\rangle\simeq\frac12\sqrt{2zJSN/h_p}`$; its share per place, and that of the staggered mode of $`\tilde P`$, adds $`\simeq\frac12\sqrt{2zJS/(Nh_p)}`$ to $`\Delta S(x)`$. The deviations stay small only if

```math
Nh_pS\gg zJ .\qquad\text{(8.6)}
```

The order $`L\to\infty`$ first satisfies (8.6) for every $`h_p>0`$; the order $`h_p\to0`$ at fixed $`L`$ violates it, and there the exact (8.4) holds instead.

*Cubic torus, $`L\to\infty`$, then $`R\to\infty`$.* Far from $`h`$ the covariance tends to that of the translation-invariant form without the zero modes: $`T(k)=JSz(1+\gamma_k)`$, $`V(k)=JSz(1-\gamma_k)`$, $`\gamma_k=\frac1D\sum_i\cos k_i`$, $`\omega_k=JSz\sqrt{1-\gamma_k^2}`$, and $`\langle\tilde Q_x^2\rangle\to\int\frac{T(k)}{2\omega_k}=\frac12\int(1-\gamma_k^2)^{-1/2}`$ (pair $`k`$ with $`k+(\pi,\pi,\pi)`$). The push enters only through the zero modes and the propagators between $`x`$ and $`h`$, which vanish as $`R\to\infty`$. Hence, for every $`h_p>0`$ (so also after $`h_p\to0`$),

```math
m(x)\to\epsilon_h\bigl[S-\Delta S_3+O(1/S)\bigr],\qquad \Delta S_3=\frac12\Bigl[\int_{\rm BZ}\frac{d^3k}{(2\pi)^3}\frac1{\sqrt{1-\gamma_k^2}}-1\Bigr]=0.0784.\qquad\text{(8.7)}
```

The value ($`0.07836`$) is computed in `code/v2/output/spinwave_tilt.txt`; the same file gives $`\Delta S`$ at the far place of tori $`L=8,12,16`$ with the push: for $`\eta=1`$, $`\Delta S-\Delta S_3=0.0736,0.0412,0.0272`$ against the zero-mode term $`0.0766,0.0417,0.0271`$ of (8.6); for $`\eta=10`$ the excess $`0.033,0.019,0.013`$ also falls with $`L`$.

*Ring.* $`(1-\gamma_k^2)^{-1/2}=1/\lvert\sin k\rvert`$ is not integrable; the pinning at $`h`$ cuts it off at the distance $`R`$. With $`T/(2\omega)\simeq1/\lvert k\rvert`$ near $`k=0`$ (and likewise for $`\tilde P`$ near $`\pi`$), $`G(r)=\frac1{2\pi}\int dk\,e^{ikr}/\lvert k\rvert`$; at long wavelengths the pinned place acts as a fixed value, and by the image at $`h`$, $`\langle\tilde Q_R^2\rangle\simeq G(0)-G(2R)=\frac1{2\pi}\int_{-\pi}^{\pi}dk\,\frac{1-\cos 2kR}{\lvert k\rvert}\simeq\frac1\pi\ln R`$:

```math
\text{ring:}\qquad m(R)=S-\frac1\pi\ln R+O(1)+O(1/S),\qquad\text{(8.8)}
```

confirmed in `code/v2/output/spinwave_tilt.txt` (slope $`0.3156`$ of $`\Delta S(L/2)`$ in $`\ln L`$ for $`L=256`$–$`1024`$, $`\eta=1`$, against $`1/\pi=0.3183`$). The first correction is not uniform in $`R`$ and exceeds $`S`$ for $`\ln R\gtrsim\pi S`$: on the ring the expansion in $`1/S`$ does not decide the order $`L\to\infty`$, $`R\to\infty`$ at any $`S`$. The ring is the control of (8.7).

### Step 5. Exact diagonalization, $`S=\frac12`$ and $`S=1`$ (item 1(b))

`code/v2/ed_push.py` (output `code/v2/output/ed_push.txt`), $`J=1`$, push at $`h=0`$, lowest eigenvector searched in $`\sum_xS^3_x=0,1,2`$. Clusters: rings $`L=8,12,16,20`$ ($`S=\frac12`$) and $`L=6,8,10,12`$ ($`S=1`$); the cubic cluster $`\mathbb Z^3/\Lambda`$ with $`\Lambda`$ spanned by $`(2,2,0),(2,0,2),(0,2,2)`$: 16 objects, links $`x`$–$`x\pm\mathbf e_i`$, 48 links, 6 distinct neighbours each, bipartite, far places at graph distance 3. Without push every cluster has a unique singlet lowest eigenvector (check of (8.1)). With the push the lowest eigenvector lies in the sector $`0`$ for all $`h_p\le10J`$, and

```math
\begin{aligned}&m_{\rm far}(h_p=10J)=0.224,\ 0.190,\ 0.169,\ 0.154\quad(S=\tfrac12\text{ rings }L=8,12,16,20),\\&m_{\rm far}(h_p=10J)=0.695,\ 0.609,\ 0.551,\ 0.488\quad(S=1\text{ rings }L=6,8,10,12),\qquad m_{\rm far}(h_p=10J)=0.330\quad(\text{cubic cluster }16),\\&m_{\rm far}/h_p=0.29\text{–}0.32\ (S=\tfrac12\text{ rings}),\ 0.24\ (\text{cubic }16)\ \text{at }h_p=0.01J,\ \text{linear in }h_p\text{ for }h_p\le0.1J.\end{aligned}\qquad\text{(8.9)}
```

What this decides: at fixed size $`m_{\rm far}\to0`$ linearly as $`h_p\to0`$ on every cluster (as (8.4)); on rings with $`h_p\ge J`$ (and for $`S=1`$ at every $`h_p`$ computed) $`m_{\rm far}`$ falls monotonically with $`L`$, without sign of saturation, while for $`S=\frac12`$ and $`h_p\le0.1J`$ the linear response $`\chi_L`$ still rises slowly with $`L`$; this is consistent with the control (8.8) but no proof of $`m_{\rm far}\to0`$; with one cubic cluster of 16 objects the order $`L\to\infty`$, $`R\to\infty`$ for $`S=\frac12`$ on the cubic torus is **undecided**.

### Step 6. Identification with the oscillator field of 05-anchor (item 2)

*Static identification.* For any positive definite kinetic matrix $`T`$, the shift $`q\to q-A^{-1}b`$ shows that the lowest eigenvalue of $`\frac12p^{\rm T}Tp+\frac12q^{\rm T}Aq+b^{\rm T}q+c_0`$ is $`c_0+\frac12{\rm Tr}(T^{1/2}AT^{1/2})^{1/2}-\frac12b^{\rm T}A^{-1}b`$ and $`\langle q\rangle=-A^{-1}b`$; a lowest eigenvector exists iff $`A>0`$. So every source-dependent static result of 05-anchor depends on $`A`$ and $`b`$ only. A direction source gives, at the order of (8.5), $`g\,\mathbf m\cdot\mathbf S_x=g(\mathbf m\cdot\mathbf n)\epsilon_x(S-n_x)+g\sqrt S\epsilon_x\sum_\alpha(\mathbf m\cdot\mathbf e_\alpha)q^{(\alpha)}_x`$, and a cell $`g\,\mathbf m\cdot(\mathbf S_x-\mathbf S_{x'})=g(\mathbf m\cdot\mathbf n)\epsilon_x(2S-n_x-n_{x'})+g\sqrt S\epsilon_x\sum_\alpha(\mathbf m\cdot\mathbf e_\alpha)(q^{(\alpha)}_x+q^{(\alpha)}_{x'})`$. Comparing with (8.5):

```math
q_x\leftrightarrow q^{(\alpha)}_x=\epsilon_x\frac{\mathbf e_\alpha\cdot\mathbf S_x}{\sqrt S},\qquad \kappa_h=JS,\qquad \kappa_a=h_p,\qquad g_s=\epsilon_{x_s}\sqrt S\,g\,(\mathbf m\cdot\mathbf e_\alpha),\qquad c_0=E_0+\textstyle\sum_s g(\mathbf m\cdot\mathbf n)\epsilon_{x_s}S,\qquad\text{(8.10)}
```

two copies $`\alpha=1,2`$ with the same $`A=V_a`$ (no pinning, the push as the anchor), each with its own sources. The copies are not independent fields: they are conjugate to each other, and as one oscillator field ($`q=q^{(1)}`$, $`p=\tilde P`$) the kinetic matrix is $`T_a=EV_aE`$ instead of $`\mathbb 1`$. *Long-wavelength identification* (needed for dynamics): $`T_a(k)\to2zJS`$ near $`k=0`$ and $`\to0`$ near $`k=(\pi,\dots)`$, where $`q^{(2)}`$ takes the role of coordinate; for wavelengths $`\gg1`$ the low modes near the two points form two independent copies of the 05-anchor field with $`\frac12p^2`$, after $`q=q^{(\alpha)}/\sqrt{2zJS}`$: $`\kappa_h=2zJ^2S^2`$, $`\kappa_a=2zJSh_p`$, $`g_s=\epsilon_{x_s}S\sqrt{2zJ}\,g(\mathbf m\cdot\mathbf e_\alpha)`$, speed $`\sqrt{\kappa_h}=JS\sqrt{2z}`$, plus a local kinetic term $`\frac{h_p}{4zJS}p_h^2`$ of relative size $`\eta/(2z)`$ absent in 05-anchor. Both dictionaries give the same $`\kappa_a/\kappa_h=\eta`$ and $`g_s^2/\kappa_h=g^2(\mathbf m\cdot\mathbf e_\alpha)^2/J`$, the combinations that enter (5.8)–(5.15).

*Small deviations.* The tilt of the object at $`y`$ by a transverse source at $`x_s`$ is $`\lvert\langle\mathbf e_1\cdot\mathbf S_y\rangle\rvert/S=\lvert g\,(\mathbf m\cdot\mathbf e_1)\rvert\,G_a(y,x_s)\le\lvert g\rvert\,\Gamma(x_s)`$, $`\Gamma(x)=G_a(x,x)=\frac1{h_p}+\frac{2[\hat g(0)-\hat g(x-h)]}{JS}`$, by (5.11) with (8.10). The identification holds at leading order in $`1/S`$ under

```math
\Delta S_3\ll S\ \text{and (8.6)};\qquad \lvert g\rvert\ll h_p\ \text{and}\ \lvert g\rvert\ll JS\ \ (\text{cubic torus: }\Gamma\le\tfrac1{h_p}+\tfrac{2\gamma_3}{JS});\qquad \text{ring: also }\tfrac1\pi\ln d\ll S\ \text{and}\ \lvert g\rvert d\ll JS\ \text{at the distances }d\text{ used}.\qquad\text{(8.11)}
```

### Step 7. Which results of 05-anchor carry over (item 2, short argument)

By Step 6 and (8.11): (5.8) holds exactly as a matrix identity for $`V_a^{-1}`$ with $`\kappa_h=JS`$, $`\kappa_a=h_p`$ (checked against a direct inverse in `code/v2/output/spinwave_mutual.txt`, error $`5\times10^{-14}`$); (5.3) with the push holds ($`V_a>0`$, $`T_a>0`$); (5.11) and (5.14), (5.15) hold for the transverse components (Step 8). An along-$`\mathbf n`$ source adds $`-g\epsilon_xP_x`$ to both $`V_a`$ and $`T_a`$, i.e. it is a body with $`\alpha=-g\epsilon_x`$ in both copies; with this reading (5.4)–(5.6), (5.10) hold as positivity criteria for $`V_a-\sum_ig_i\epsilon_{x_i}P_{x_i}`$, and a source with $`g\epsilon_x<0`$ is itself a push (the analogue of the first statement of (5.7)). What changes: (i) *boundedness of the common rotation* (A1): the zero mode of 05-anchor (a free particle on $`\mathbb R`$) is here a rotation of the orientation on the sphere, quantized with discrete levels; therefore the "no lowest eigenvector" outcomes of (5.3)–(5.6) are replaced by a lowest eigenvector that exists (A1) and, for the field alone, is the unique singlet (8.1); the outcome "$`-\infty`$" is replaced by a finite rotation of the orientation, and the uniform shift $`-g_s/\kappa_a`$ of (5.11) is the small-angle form of a rotation by $`\arctan(g/h_p)`$ (classical uniform rotation in the plane of $`\mathbf n,\mathbf e_1`$: energy $`-S(h_p\cos\theta-g\epsilon_x\sin\theta)`$); (ii) *next order in $`1/S`$*: $`C_4`$ and the $`O(S^{-1/2})`$ terms of the transverse components change the coefficients by relative $`O(1/S)`$ (not computed); (iii) on the ring, (5.8) and (5.14) hold with $`r=\frac{s(L-s)}{\kappa_hL}`$, but only at distances allowed by (8.11).

```math
\text{(5.3) with anchor, (5.8), (5.10), (5.11), (5.14), (5.15) hold under (8.10), (8.11); the outcome “no lowest eigenvector” of (5.3)–(5.6) fails: one exists.}\qquad\text{(8.12)}
```

### Step 8. Transverse direction sources (item 3(a))

At the order of (8.5), the sources are linear in $`q^{(\alpha)}`$ with $`b^{(\alpha)}=\sum_i g_i\epsilon_{x_i}\sqrt S(\mathbf m_i\cdot\mathbf e_\alpha)e_{x_i}`$; the shift of Step 6 in each copy, summed over $`\alpha`$, is (5.14) with (8.10):

```math
\mathcal E^\perp_{12}=-S\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)G_a(x_1,x_2)=-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)\Bigl[\frac S{h_p}+\frac{\hat g(x_1-x_2)-\hat g(x_1-h)-\hat g(x_2-h)+\hat g(0)}{J}\Bigr],\qquad\text{(8.13)}
```

at order $`g_1g_2`$, exact at this order in $`1/S`$ for every $`L`$ on both graphs. In the order $`L\to\infty`$, distances to $`h\to\infty`$ at fixed $`\mathbf r=x_2-x_1`$, then $`\lvert\mathbf r\rvert\to\infty`$, (5.15) gives

```math
\mathcal E^\perp_{12}=-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)\,c_{\rm cell}\Bigl[\frac S{h_p}+\frac{\gamma_3}J+\frac1{4\pi J\lvert\mathbf r\rvert}+O(\lvert\mathbf r\rvert^{-3})\Bigr],\qquad c_{\rm cell}=c_1c_2,\ c_i=1\ (\text{single object}),\ 2\ (\text{two-object cell}).\qquad\text{(8.14)}
```

For cells, $`G_a(x_1,x_2)`$ in (8.13) becomes $`\sum_{a\in{\rm cell}_1,\,b\in{\rm cell}_2}G_a(a,b)`$; $`b`$ is a monopole $`2g\epsilon_x\sqrt S`$ at the cell, so the pair terms give the factor $`c_{\rm cell}`$ up to $`O(\lvert\mathbf r\rvert^{-3})`$. The separation part $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)c_{\rm cell}/(4\pi J\lvert\mathbf r\rvert)`$ is a long-range mark of order $`S^0`$ (the uniform part is of order $`S`$); it is attractive iff $`\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)>0`$, so for single objects its sign alternates with the class of the separation, and for cells written with $`+`$ on the class-$`+`$ object ($`\epsilon_{x_1}\epsilon_{x_2}=1`$) it is fixed. `code/v2/output/spinwave_mutual.txt`: $`4\pi r\hat g_\infty(r)=1.078,1.020,1.008,1.004`$ at $`r=2,4,6,8`$ and $`\pi r\sum\hat g_\infty=0.991,1.0005,1.0001,1.0000`$ for cells; on tori $`L=16,32,64`$ the separation dependence $`\hat g_L(r)-\hat g_L(8)`$ converges to that of $`\hat g_\infty`$. *Vanishing members* (excluded): a source at $`h`$ ($`G_a(h,\cdot)=1/h_p`$), $`\mathbf m_1^\perp\cdot\mathbf m_2^\perp=0`$ (e.g. $`\mathbf m_i=\mathbf n`$, or $`\mathbf m_1\perp\mathbf m_2`$ both transverse: different copies), sources on the same object or cell.

### Step 9. Sources quadratic in the deviations: the second-order formula

Along-$`\mathbf n`$ sources and relation sources add, at the order of (8.5), local quadratic terms $`\delta H_i=\frac12\tilde Q^{\rm T}A_i\tilde Q+\frac12\tilde P^{\rm T}B_i\tilde P`$ and constants linear in the strengths. Their mutual cost is of second order; Rayleigh–Schrödinger perturbation theory of the Gaussian lowest eigenvector of $`C_2`$ gives, with $`\delta H(\tau)=e^{C_2\tau}\delta He^{-C_2\tau}`$ and Wick's theorem,

```math
\mathcal E_{12}=-\int_{-\infty}^{\infty}d\tau\,\langle T\,\delta H_1(\tau)\,\delta H_2(0)\rangle_c .\qquad\text{(8.15)}
```

At large separation only the low modes matter: per copy, the coordinate ($`q^{(1)}`$ near $`k=0`$, $`q^{(2)}`$ near $`k=0`$, i.e. $`\tilde P`$ near $`(\pi,\dots)`$) has the imaginary-time covariance $`\frac{T_0}{4\pi^2c}\frac1{r^2+c^2\tau^2}`$ with $`T_0=2zJS`$, $`c=JS\sqrt{2z}`$; covariances with momenta carry extra derivatives. Far from $`h`$ the push enters only through the zero modes, whose contribution vanishes as $`L\to\infty`$ (as $`N^{-1/2}`$ with (8.6)). `code/v2/spinwave_mutual.py` evaluates (8.15) on the lattice (exact $`T(k),V(k)`$, zero modes left out) on tori $`L=32,64,128`$, $`r=2,\dots,12`$ along an axis.

### Step 10. Along-$`\mathbf n`$ direction sources

$`g\,\mathbf n\cdot\mathbf S_x=g\epsilon_xS-\frac{g\epsilon_x}2\sum_\alpha(q^{(\alpha)}_x)^2+\text{const}`$: $`A=B=-g\epsilon_xP_x`$. Wick's theorem gives $`\langle T\,q^2(\tau)\,q^2(0)\rangle_c=2G^2`$ per copy, $`G=\frac{T_0}{4\pi^2c\rho^2}`$, so (8.15) is $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2\int d\tau\,G^2`$, and $`\int d\tau\,\rho^{-4}=\pi/(2cr^3)`$:

```math
\mathcal E^\parallel_{12}=-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1\cdot\mathbf n)(\mathbf m_2\cdot\mathbf n)\,\frac{c_{\rm cell}\,\kappa_\parallel}{JS\,r^3}\bigl[1+O(r^{-2})\bigr],\qquad \kappa_\parallel=\frac{\sqrt{2z}}{32\pi^3}=\frac{\sqrt3}{16\pi^3}=0.0034913,\qquad\text{(8.16)}
```

order $`g_1g_2/(JS)`$, one order in $`1/S`$ below the separation part of (8.14); $`c_{\rm cell}=c_1c_2`$ as in (8.14): a cell has $`A=B=-g\epsilon_x(P_x+P_{x'})`$, at large $`r`$ a vertex of twice the strength at the cell ($`c_i=2`$), so $`c_{\rm cell}=2`$ for a single object and a cell and $`4`$ for two cells. It falls as $`r^{-3}`$: no long-range mark. Lattice/continuum ratio (`code/v2/output/spinwave_mutual.txt`): on $`L=128`$, $`1.02,1.00,0.96,0.94`$ at $`r=4,\dots,7`$, rising with $`L`$ at fixed $`r`$; the Aitken extrapolation from $`L=32,64,128`$ (meaningful for $`r\le7`$, where $`L=32\ge4r`$) gives $`1.06,1.06,1.05,1.07`$ (single objects) and $`1.01,1.02,1.03,1.05`$ (cells) at $`r=4,\dots,7`$: (8.16) up to corrections of a few per cent at these $`r`$. For a general $`\mathbf m`$ the transverse part (8.14) dominates unless $`\mathbf m_1^\perp\cdot\mathbf m_2^\perp=0`$; cross terms transverse–along vanish at order $`g_1g_2`$ (odd in the deviations).

### Step 11. Relation source R2 (changed link)

$`\delta\,\mathbf S_x\cdot\mathbf S_y=-\delta S(S+1)+\frac{\delta S}2\sum_\alpha(q^{(\alpha)}_x-q^{(\alpha)}_y)^2`$: $`A=\delta S(e_x-e_y)(e_x-e_y)^{\rm T}`$, $`B=\delta S(e_x+e_y)(e_x+e_y)^{\rm T}`$, which vanish on the zero modes (unchanged by the common rotation). With $`\tilde Q=\phi_1-\epsilon\pi_2`$, $`\tilde P=\pi_1+\epsilon\phi_2`$ ($`\phi_\alpha,\pi_\alpha`$ the smooth coordinate and momentum of copy $`\alpha`$), $`\phi_\alpha=\sqrt{T_0}\chi_\alpha`$, $`\pi_\alpha=\partial_t\chi_\alpha/\sqrt{T_0}`$, $`t'=ct`$ and $`\mathbf e`$ the unit vector from $`y`$ to $`x`$:

```math
\delta H=\frac{\delta ST_0}2\Bigl[\sum_\alpha\Bigl((\mathbf e\cdot\nabla\chi_\alpha)^2+\frac2z(\partial_{t'}\chi_\alpha)^2\Bigr)-\epsilon_x\sqrt{\tfrac8z}\bigl(\mathbf e\cdot\nabla\chi_1\,\partial_{t'}\chi_2-\partial_{t'}\chi_1\,\mathbf e\cdot\nabla\chi_2\bigr)\Bigr].
```

Every term carries two derivatives, so each contraction in (8.15) is $`\propto\rho^{-4}`$, $`\rho^2=r^2+c^2\tau^2`$, and $`\mathcal E\propto\int d\tau\,\rho^{-8}\propto r^{-7}`$. With the Euclidean covariance $`\frac1{4\pi^2c\rho^2}`$ of $`\chi`$ ($`\partial_{t'}\to i\partial_{\tau'}`$, $`\tau'=c\tau`$), $`I_{\mu\nu}=\delta_{\mu\nu}-4n_\mu n_\nu`$, $`n=(\tau',\mathbf r)/\rho`$, $`M_i=\mathbf e_i\mathbf e_i^{\rm T}-\frac2z\hat 0\hat 0^{\rm T}`$:

```math
\mathcal E^{R2}_{12}=-\frac{\delta_1\delta_2S\sqrt{2z}}{16\pi^4J}\int\frac{d\tau'}{\rho^8}\Bigl\{4{\rm Tr}(M_1IM_2I)-\frac{16}z\epsilon_1\epsilon_2\bigl[I_{00}\,\mathbf e_1\!\cdot\! I\mathbf e_2-(I\mathbf e_1)_0(I\mathbf e_2)_0\bigr]\Bigr\}=-\frac{\sqrt3}{8\pi^3}\frac{\delta_1\delta_2S}{J\,r^7}\,a\,\bigl[1+O(r^{-2})\bigr],\qquad\text{(8.17)}
```

$`a=\frac{43}6+\frac52\epsilon_1\epsilon_2`$ for both links parallel to $`\mathbf r`$, $`a=\frac43-\frac5{12}\epsilon_1\epsilon_2`$ for both links parallel to each other and perpendicular to $`\mathbf r`$ ($`\epsilon_i`$ the class of the endpoint $`x`$ of link $`i`$); attractive in both for $`\delta_1\delta_2>0`$; order $`\delta_1\delta_2S/J`$. `code/v2/output/spinwave_mutual.txt`: the closed forms agree with the numerical $`\tau'`$-integral. The lattice/continuum ratio on $`L=128`$ is $`1.112,1.067,1.046`$ (parallel) and $`1.123,1.072,1.046`$ (perpendicular) at $`r=8,10,12`$, and $`1.066,1.042`$ (parallel) and $`1.079,1.051`$ (perpendicular) at $`r=9,11`$. Odd $`r`$ gives $`\epsilon_1\epsilon_2=-1`$ and even $`r`$ gives $`\epsilon_1\epsilon_2=+1`$. From $`L=64`$ to $`128`$ the ratio changes as follows. Parallel links: by at most $`0.002`$ for $`r\le9`$ and by $`0.007,0.005,0.014`$ at $`r=10,11,12`$. Perpendicular links: by at most $`0.004`$ for $`r\le7`$ and at $`r=9,11`$, but by $`0.010,0.023,0.045`$ at $`r=8,10,12`$ (the member $`\epsilon_1\epsilon_2=+1`$, $`a=\frac{11}{12}`$). There, from $`L=32`$ to $`64`$ the ratio rises from $`0.81`$ to $`1.05`$ ($`r=10`$) and from $`0.66`$ to $`1.00`$ ($`r=12`$), and its $`L=32`$ values alternate between $`0.66`$ and $`1.21`$ at $`r\ge8`$. So the values that change by at most $`0.014`$ (parallel links at $`r=8,\dots,12`$, perpendicular links at $`r=8,9,11`$) confirm the coefficient and the approach $`1+O(r^{-2})`$: for them $`(\text{ratio}-1)\,r^2=5`$–$`8`$. The perpendicular values at $`r=10,12`$ ($`1.072,1.046`$ on $`L=128`$) confirm the sign, the decay $`r^{-7}`$ and the coefficient only to within their finite-size change of up to $`0.045`$; they do not resolve the correction $`O(r^{-2})`$ there. No long-range mark.

### Step 12. Relation source R1 (held spin)

(i) *Lowest order in $`g'`$ at fixed $`r`$.* The places of $`b`$ are split by $`g'\langle\mathbf S_x\rangle\cdot\mathbf S_b=g'\epsilon_x(S-\Delta S)\,\mathbf n\cdot\mathbf S_b`$; its lowest level is $`\mathbf n\cdot\mathbf S_b=-\epsilon_xs_b\,{\rm sgn}\,g'`$, gap $`\Delta_b\simeq\lvert g'\rvert S`$. In it the part $`g'(\mathbf n\cdot\mathbf S_b)(\mathbf n\cdot\mathbf S_x)`$ acts on the field as $`-\lvert g'\rvert s_b\,\epsilon_x\mathbf n\cdot\mathbf S_x`$. This is an along-$`\mathbf n`$ source with $`g=-\epsilon_x\lvert g'\rvert s_b`$, whose vertex is $`\frac12\lvert g'\rvert s_b\sum_\alpha(q^{(\alpha)}_x)^2`$ (Step 10). The transverse part is $`g'\mathbf S_b^\perp\cdot\mathbf S_x^\perp=g'\sqrt S\,\epsilon_x\sum_\alpha(\mathbf e_\alpha\cdot\mathbf S_b)\,q^{(\alpha)}_x`$. In the lowest level of $`b`$, $`\mathbf e_\alpha\cdot\mathbf S_b`$ connects only to the next level, with squared matrix element $`s_b/2`$. So $`\langle T(\mathbf e_\alpha\cdot\mathbf S_b)(\tau)(\mathbf e_\beta\cdot\mathbf S_b)(0)\rangle`$ has a symmetric part $`\delta_{\alpha\beta}\frac{s_b}2e^{-\Delta_b\lvert\tau\rvert}`$, with Fourier transform $`\delta_{\alpha\beta}s_b\Delta_b/(\nu^2+\Delta_b^2)`$, and an antisymmetric part $`\propto{\rm sgn}(\tau)\,e^{-\Delta_b\lvert\tau\rvert}`$ that couples $`\alpha=1`$ to $`\alpha=2`$. Eliminating $`b`$ at second order in the transverse part, the symmetric part adds $`-\frac12g'^2S\,\frac{s_b\Delta_b}{\nu^2+\Delta_b^2}\sum_\alpha\lvert q^{(\alpha)}_x(\nu)\rvert^2`$ ($`\nu`$ the imaginary frequency). Together with the vertex above, the vertex becomes $`\frac12\lvert g'\rvert s_b\,f(\nu)\sum_\alpha\lvert q^{(\alpha)}_x(\nu)\rvert^2`$ with $`f(\nu)=\nu^2/(\nu^2+\Delta_b^2)`$. Its static limit cancels the vertex: $`b`$ follows the orientation. Relative to the vertex, the antisymmetric part has the weight $`\Delta_b\lvert\nu\rvert/(\nu^2+\Delta_b^2)\le\Delta_b/\lvert\nu\rvert`$, and it is not evaluated. In (8.15) the two vertices and the two coordinate covariances form one frequency loop. The $`\tau`$-transform of $`1/(r^2+c^2\tau^2)`$ is $`\frac\pi{cr}e^{-\lvert\nu\rvert r/c}`$, so the factors $`f_1f_2`$ multiply the $`f=1`$ result by $`\int_0^\infty du\,e^{-u}f_1f_2`$, with $`u=2\lvert\nu\rvert r/c`$. Since $`1-f_1f_2\le(1-f_1)+(1-f_2)`$ and $`\int_0^\infty du\,(1-f_i)=\frac\pi2\cdot\frac{2r}{\ell_{b_i}}`$, this multiplier lies between $`1-\pi r(\ell_{b_1}^{-1}+\ell_{b_2}^{-1})`$ and $`1`$, where $`\ell_b:=c/\Delta_b=\sqrt{2z}J/\lvert g'\rvert`$. So for $`1\ll r\ll\ell_b`$, (8.16) applies with a correction of relative order $`r/\ell_b`$ from $`f`$. The antisymmetric part has the relative weight $`\le\Delta_b/\lvert\nu\rvert\sim r/\ell_b`$ at $`\nu\sim c/r`$. That its contribution is also $`O(r/\ell_b)`$ is an estimate, not derived; the remainder $`O(r/\ell_b)`$ of (8.18) rests on it.

(ii) *$`r\gg\ell_b`$.* For $`\nu\ll\lvert g'\rvert S`$ the pair $`b,x`$ stays in its lowest multiplet, total spin $`S+\sigma`$, $`\sigma=-s_b\,{\rm sgn}\,g'`$; by the projection theorem $`\mathbf S_x=\frac{S(S+1)+J_t(J_t+1)-s_b(s_b+1)}{2J_t(J_t+1)}\mathbf J_t`$ there ($`J_t=S+\sigma`$), i.e. a spin $`S+\sigma`$ with link coefficient $`J'`$, $`J'(S+\sigma)=JS+O(J/S)`$. In (8.5) this changes $`V_a`$ by $`J\sigma[-zP_x+\frac12\sum_{y\sim x}(e_xe_y^{\rm T}+e_ye_x^{\rm T})]`$ and $`T_a`$ by $`J\sigma[-zP_x-\frac12\sum_{y\sim x}(e_xe_y^{\rm T}+e_ye_x^{\rm T})]`$. In the smooth fields the leading term has one derivative, $`\lambda_x(\phi_1\pi_2-\phi_2\pi_1)`$ with $`\lambda_x=zJ\sigma\epsilon_x`$: the rotation generator about $`\mathbf n`$ of the two copies, i.e. the uncompensated spin $`\sigma`$ following the orientation; terms with two derivatives give $`r^{-7}`$, and their cross terms with it vanish (odd in $`\tau`$). Evaluating (8.15), $`\int d\tau'(r^2-\tau'^2)\rho^{-8}=\pi/(4r^5)`$:

```math
\mathcal E^{R1}_{12}=\begin{cases}-\lvert g'_1g'_2\rvert s_{b_1}s_{b_2}\,\dfrac{\kappa_\parallel}{JS\,r^3}\bigl[1+O(r/\ell_b)+O(r^{-2})\bigr], & 1\ll r\ll\ell_b\ (\text{remainder }O(r/\ell_b)\text{: estimate of Step 12(i)}),\\[2ex] \dfrac{\lambda_1\lambda_2}{16\pi^3c\,r^5}=\dfrac{3\sqrt3}{8\pi^3}\,\dfrac JS\,\sigma_1\sigma_2\,\epsilon_{x_1}\epsilon_{x_2}\,\dfrac1{r^5}\bigl[1+O(r^{-2})\bigr], & r\gg\ell_b,\end{cases}\qquad \frac{3\sqrt3}{8\pi^3}=0.020948.\qquad\text{(8.18)}
```

The first line is attractive for both signs of $`g'`$; the second is independent of $`\lvert g'\rvert`$ (not analytic in $`g'`$: its range $`r\gg\ell_b\propto1/\lvert g'\rvert`$ recedes as $`g'\to0`$), repulsive iff $`\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}>0`$, and is the law in the order of the question ($`r\to\infty`$ last at fixed $`g'`$). Lattice check of the second line (spin-length model above, `code/v2/output/spinwave_mutual.txt`; ratio lattice/continuum, odd $`r`$ gives $`\epsilon_{x_1}\epsilon_{x_2}=-1`$). On $`L=128`$ the ratio is $`1.011,1.046,0.994,1.012,0.978,0.986,0.959`$ at $`r=6,\dots,12`$. It has not converged in $`L`$: from $`L=64`$ to $`128`$ it still rises by $`0.04,0.06,0.08,0.11,0.14,0.17,0.21`$ at $`r=6,\dots,12`$ (at $`r=10`$ from $`0.841`$ to $`0.978`$). The $`L=32`$ values fall from $`0.76`$ to $`0.25`$ over the same $`r`$. The Aitken extrapolation from $`L=32,64,128`$ is meaningful for $`r\le7`$, as in Step 10. There it gives $`1.051,1.125,1.020,1.060`$ at $`r=4,\dots,7`$, so $`(\text{ratio}-1)\,r^2=0.8,3.1,0.7,2.9`$, which depends on the parity of $`r`$. For $`r\ge8`$ the extrapolated values ($`1.017,1.047,1.032,1.071,1.103`$ at $`r=8,\dots,12`$) rest on $`L=32`$ values far from the limit and are not used. What the check confirms: in the range $`r=4,\dots,7`$, the sign, the decay $`r^{-5}`$ and the coefficient of the second line of (8.18) to within $`6\%`$ at $`r=6,7`$, with lattice corrections consistent with $`1+O(r^{-2})`$ that depend on the parity of $`r`$. At $`r\ge8`$ the $`L=128`$ values lie between $`0.96`$ and $`1.02`$, but they still drift by $`0.08`$ to $`0.21`$, so they do not test the coefficient there. No long-range mark.

### Step 13. Without a push (item 3(c), short argument)

*Direction sources.* The classical cost of the orientation $`\hat{\mathbf n}`$ is $`S\hat{\mathbf n}\cdot\mathbf h_{\rm eff}`$, $`\mathbf h_{\rm eff}=\sum_ic_ig_i\epsilon_{x_i}\mathbf m_i`$ ($`c_i=1`$ single, $`2`$ cell). If $`\mathbf h_{\rm eff}\ne0`$ the sources fix $`\hat{\mathbf n}^*=-\mathbf h_{\rm eff}/\lvert\mathbf h_{\rm eff}\rvert`$ (order $`L\to\infty`$ first; they pin the zero modes as the push does, (8.6) with $`\lvert\mathbf h_{\rm eff}\rvert`$). Relative to $`\hat{\mathbf n}^*`$ the along parts are anchors $`a_i=-c_ig_i\epsilon_{x_i}(\mathbf m_i\cdot\hat{\mathbf n}^*)`$ at the source places ($`a_1+a_2=\lvert\mathbf h_{\rm eff}\rvert>0`$), and the transverse parts $`b_i=c_ig_i\epsilon_{x_i}\sqrt S\,\mathbf m_i^\perp`$ obey $`b_1+b_2=0`$ (no linear uniform term at the minimum). Kron reduction of $`JS\Delta+\sum_ia_iP_{x_i}`$ to $`\{x_1,x_2\}`$ gives the matrix $`\bigl(\begin{smallmatrix}\ell+a_1&-\ell\\-\ell&\ell+a_2\end{smallmatrix}\bigr)`$, $`\ell=1/r_{12}`$, $`r_{12}=2[\gamma_3-\hat g(\mathbf r)]/(JS)`$, and the cost $`-\frac12\lvert b_1\rvert^2\frac{a_1+a_2}{\ell(a_1+a_2)+a_1a_2}=-\frac{r_{12}}2\lvert b_1\rvert^2[1+O(g/J)]`$, i.e. $`-\frac{c_1^2g_1^2\lvert\mathbf m_1^\perp\rvert^2}J[\gamma_3-\hat g(\mathbf r)]`$. If $`\mathbf h_{\rm eff}=0`$ ($`\mathbf m_1\parallel\mathbf m_2`$, $`c_1g_1\epsilon_{x_1}=-c_2g_2\epsilon_{x_2}`$), orientations $`\perp\mathbf m`$ win (this cost, of order $`g^2/J`$, against $`O(g^2/(JS))`$ for orientations along $`\mathbf m`$) and the orientation is fixed only up to rotations about $`\mathbf m`$. So

```math
\text{no push:}\quad \mathcal E_{12}\big|_{\mathbf r}=+\frac{c_1^2g_1^2\lvert\mathbf m_1^\perp\rvert^2}{4\pi J\lvert\mathbf r\rvert}\ (\text{repulsive; }\lvert\mathbf m^\perp_1\rvert=1\text{ if }\mathbf h_{\rm eff}=0),\qquad \text{(8.16) only, if }\mathbf m_1\parallel\mathbf m_2,\ \mathbf h_{\rm eff}\ne0;\qquad \text{relation sources fix no orientation.}\qquad\text{(8.19)}
```

*Relation sources.* R2 ($`J+\delta>0`$) keeps the bipartite antiferromagnetic structure; R1 too, with $`b`$ in the class $`-\epsilon_x`$ for $`g'>0`$ and $`\epsilon_x`$ (ferromagnetic within a class) for $`g'<0`$. By Lieb–Mattis (which allows ferromagnetic terms within a class) the lowest eigenvalue has total spin $`\lvert\sum_i\epsilon_{x_i}\sigma_i\rvert`$ (field and held objects) and is $`(2S_{\rm tot}+1)`$-fold degenerate; for $`S_{\rm tot}=0`$ the lowest eigenvector is unique, unchanged by every common rotation, with $`\langle\mathbf S_x\rangle=0`$. Relation sources therefore fix no orientation. Their vertices are unchanged by the common rotation, so without a push the separation dependence (8.17), (8.18) is unchanged as $`L\to\infty`$: only rotor levels of order $`J/N`$ differ.

## Result

All results: exchange cells, cubic torus or ring of even side $`L\ge4`$, the setting of the question; $`\epsilon_h=+1`$. **Assumption E** (Setup): the lowest eigenvector of the expansion (8.5), truncated at quadratic order, is taken to give the quantities of the true lowest eigenvector asymptotically in $`1/S`$ while every $`\langle n_x\rangle\ll S`$. The results that rest on it say so. (8.1)–(8.4) and the parts of (8.12) and (8.19) marked "Exact" do not rest on it; (8.9) is numerical.

- **(8.1)** $`J>0`$, field alone, every $`S`$, both graphs: the lowest eigenvector is unique, a singlet, unchanged by every common rotation, $`\langle\mathbf S_x\rangle=0`$.
- **(8.2)** $`J<0`$, field alone: lowest eigenvalue $`JS^2DN`$, $`(2NS+1)`$-fold degenerate; no lowest eigenvector is unchanged by all common rotations.
- **(8.3)** $`J<0`$ with push: unique lowest eigenvector, the product state; $`\langle\mathbf n\cdot\mathbf S_x\rangle=S`$ exactly for every $`x`$, $`L`$, $`S`$, $`h_p>0`$, both graphs and both orders of limits.
- **(8.4)** $`J>0`$, order $`h_p\to0`$ at fixed $`L`$, then $`L\to\infty`$: $`m(x)=O(h_p)\to0`$, every $`S`$, both graphs (exact).
- **(8.5)** The expansion on which Assumption E rests: at leading order in $`1/S`$ about the orientation set by the push, $`C=E_0+\frac12\sum_{\alpha=1,2}q^{(\alpha){\rm T}}(JS\Delta+h_pP_h)q^{(\alpha)}+O(J)`$, $`q^{(\alpha)}_x=\epsilon_x\mathbf e_\alpha\cdot\mathbf S_x/\sqrt S`$, $`[q^{(1)}_x,q^{(2)}_y]=i\epsilon_x\delta_{xy}`$; the quartic remainder is of relative order $`1/S`$ while $`\langle n_x\rangle\ll S`$.
- **(8.6)** Under Assumption E (its condition $`\langle n_x\rangle\ll S`$ with the push): $`Nh_pS\gg zJ`$ is required; it is met in the order $`L\to\infty`$ first and violated in the order $`h_p\to0`$ at fixed $`L`$.
- **(8.7)** Under Assumption E, cubic torus, $`J>0`$, order $`L\to\infty`$, $`R\to\infty`$, then $`h_p\to0`$: $`m(x)\to\epsilon_h[S-\Delta S_3+O(1/S)]`$, $`\Delta S_3=0.0784`$, independent of $`h_p>0`$; the expansion is taken at fixed $`L`$ under (8.6) and its coefficients have uniform limits as $`L\to\infty`$.
- **(8.8)** Under Assumption E, ring (control): $`m(R)=S-\frac1\pi\ln R+O(1)+O(1/S)`$; the first correction is not uniform in $`R`$, and the expansion in $`1/S`$ does not decide the order $`L\to\infty`$, $`R\to\infty`$ at any $`S`$.
- **(8.9)** Exact diagonalization ($`S=\frac12`$: rings $`L\le20`$ and one cubic cluster of 16 objects; $`S=1`$: rings $`L\le12`$): $`m_{\rm far}`$ is linear in $`h_p\to0`$ at fixed size, and on rings with $`h_p\ge J`$ falls monotonically with $`L`$ (values in (8.9)); for $`S=\frac12`$ on the cubic torus the order $`L\to\infty`$, $`R\to\infty`$ is undecided at these sizes.
- **(8.10)** Under Assumption E, identification at leading order in $`1/S`$: two conjugate copies $`q^{(\alpha)}`$ with the 05-anchor matrix $`A=V_a`$, $`\kappa_h=JS`$, $`\kappa_a=h_p`$, $`g_s=\epsilon_{x_s}\sqrt Sg(\mathbf m\cdot\mathbf e_\alpha)`$, exact for all static results of the quadratic expansion; kinetic matrix $`EV_aE`$ instead of $`\mathbb 1`$; for wavelengths $`\gg1`$ two independent copies of the 05-anchor field with $`\kappa_h=2zJ^2S^2`$, $`\kappa_a=2zJSh_p`$, $`g_s=\epsilon_{x_s}S\sqrt{2zJ}g(\mathbf m\cdot\mathbf e_\alpha)`$, plus a local kinetic term of relative size $`\eta/(2z)`$.
- **(8.11)** Under Assumption E, conditions of (8.10): $`\Delta S_3\ll S`$, $`Nh_pS\gg zJ`$, $`\lvert g\rvert\ll h_p`$, $`\lvert g\rvert\ll JS`$; on the ring also $`\frac1\pi\ln d\ll S`$ and $`\lvert g\rvert d\ll JS`$ at the distances used.
- **(8.12)** Under (8.10), (8.11) and Assumption E: (5.3) with the anchor, (5.8), (5.10), (5.11), (5.14), (5.15) hold, and "$`-\infty`$" becomes a finite rotation; the uniform shift of (5.11) is the small-angle form of a bounded rotation; at the next order in $`1/S`$ the coefficients change by relative $`O(1/S)`$. Exact (A1, (8.1)): the outcome "no lowest eigenvector" of (5.3)–(5.6) fails, because a lowest eigenvector exists.
- **(8.13)** Under Assumption E, transverse direction sources, order $`g_1g_2`$, leading order in $`1/S`$, every $`L`$, both graphs: $`\mathcal E^\perp_{12}=-S\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)G_a(x_1,x_2)`$.
- **(8.14)** Under Assumption E, cubic torus, order $`L\to\infty`$, distances to $`h\to\infty`$, then $`r\to\infty`$: separation part $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)c_{\rm cell}/(4\pi J r)`$, with $`c_{\rm cell}=c_1c_2`$, where $`c_i=1`$ for a single object and $`2`$ for a two-object cell (so $`1`$, $`2`$ or $`4`$); long range, order $`S^0`$; it vanishes for a source at $`h`$ or for $`\mathbf m_1^\perp\cdot\mathbf m_2^\perp=0`$.
- **(8.16)** Under Assumption E, along-$`\mathbf n`$ direction sources: $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1\cdot\mathbf n)(\mathbf m_2\cdot\mathbf n)c_{\rm cell}\kappa_\parallel/(JSr^3)`$, $`c_{\rm cell}=c_1c_2`$ as in (8.14), $`\kappa_\parallel=\sqrt3/(16\pi^3)`$, order $`g_1g_2/(JS)`$; no long-range mark.
- **(8.17)** Under Assumption E, R2: $`-\frac{\sqrt3}{8\pi^3}\frac{\delta_1\delta_2S}{Jr^7}a`$, $`a=\frac{43}6+\frac52\epsilon_1\epsilon_2`$ (links parallel to $`\mathbf r`$), $`\frac43-\frac5{12}\epsilon_1\epsilon_2`$ (links perpendicular), order $`\delta_1\delta_2S/J`$; attractive for $`\delta_1\delta_2>0`$ in both geometries; no long-range mark.
- **(8.18)** Under Assumption E, R1: $`-\lvert g'_1g'_2\rvert s_{b_1}s_{b_2}\kappa_\parallel/(JSr^3)\,[1+O(r/\ell_b)+O(r^{-2})]`$ for $`1\ll r\ll\ell_b=\sqrt{2z}J/\lvert g'\rvert`$ (order $`g'_1g'_2`$). The remainder $`O(r/\ell_b)`$ is an estimate that rests on Step 12(i): the part of $`b`$'s response that couples the two copies is not evaluated. For $`r\gg\ell_b`$ (order $`g'^0`$, the law for $`r\to\infty`$ last): $`\frac{3\sqrt3}{8\pi^3}\frac JS\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}r^{-5}[1+O(r^{-2})]`$, $`\sigma_i=-s_{b_i}{\rm sgn}\,g'_i`$. No long-range mark.
- **(8.19)** Without a push. Under Assumption E: direction sources with $`\mathbf h_{\rm eff}\ne0`$ fix the orientation $`-\mathbf h_{\rm eff}/\lvert\mathbf h_{\rm eff}\rvert`$; the $`1/r`$ part becomes $`+c_1^2g_1^2\lvert\mathbf m_1^\perp\rvert^2/(4\pi Jr)`$ (repulsive), and is absent for $`\mathbf m_1\parallel\mathbf m_2`$ with $`\mathbf h_{\rm eff}\ne0`$ (then (8.16)); for $`\mathbf h_{\rm eff}=0`$ the orientation is fixed only up to rotations about $`\mathbf m`$ and the $`1/r`$ part is $`+c_1^2g_1^2/(4\pi Jr)`$; (8.17), (8.18) are unchanged as $`L\to\infty`$. Exact (Lieb–Mattis): relation sources fix no orientation; the lowest eigenvalue is a multiplet of total spin $`\lvert\sum_i\epsilon_{x_i}\sigma_i\rvert`$, a unique singlet with $`\langle\mathbf S_x\rangle=0`$ when this is $`0`$, always for R2.

Controls: for (8.7) the ring (8.8), the order (8.4) and $`J<0`$ (8.3); for the long range of (8.14) the along-$`\mathbf n`$ sources (8.16), the relation sources (8.17), (8.18), and parallel sources without push (8.19).

## Consistency checks

1. **$`S\to\infty`$ of item 1(b).** (8.7) gives $`m/S\to1`$: the product state with the staggered orientation $`\epsilon_x\mathbf n`$; for $`J<0`$ the product state (8.3) is exact at every $`S`$. Passed.
2. **Identification against (5.15).** With $`\kappa_h=JS`$, $`g_s^2=Sg^2`$ the coefficient $`g_{s1}g_{s2}/(4\pi\kappa_h)=g_1g_2/(4\pi J)`$ of (5.15) equals the lattice limit: $`4\pi r\hat g_\infty(r)\to1`$ (Step 8). In (8.17), the sum of the vertex over the three link directions is $`T_0[(\nabla\chi)^2+(\partial_{t'}\chi)^2]`$, the energy density of the copy (a uniform change of $`J`$), as it must be. Passed.
3. **Dimensions.** $`\mathcal E^\perp\sim g^2/J`$, $`\mathcal E^\parallel\sim g^2/(JS)`$, $`\mathcal E^{R1}\sim J/S`$ or $`g'^2/(JS)`$, $`\mathcal E^{R2}\sim\delta^2S/J`$: energies, and each scales as (vertex)$`^2`$/(level spacing $`JS`$). Passed.

## Open issues

- For $`S=\frac12`$ on the cubic torus the persistence of the orientation (order $`L\to\infty`$, $`R\to\infty`$) is undecided: one cluster of 16 objects.
- On the ring the methods used here do not decide $`m(x)`$ far from the push; exact diagonalization only shows a decrease with $`L`$ for $`L\le20`$.
- The next order in $`1/S`$ of (8.13)–(8.18) is not computed; that the $`1/r`$ law of (8.14) survives at all orders is not proven.
- The crossover of (8.18) between $`r^{-3}`$ and $`r^{-5}`$ near $`r\sim\ell_b`$, and the corrections near the push, are not computed. The remainder $`O(r/\ell_b)`$ of its first line is an estimate (Step 12(i)), because the part of the response of $`b`$ that couples the two copies is not evaluated; (8.17) is evaluated for two link geometries only (general geometry as the stated integral).
- The rotor regime $`Nh_pS\sim zJ`$ between the two orders of item 1(b) is not computed.

## Code

- `code/v2/ed_push.py` (check): exact diagonalization of $`C_{\rm ex}-h_pS^3_h`$, $`J=1`$, in the sectors $`\sum_xS^3_x=0,1,2`$; $`S=\frac12`$ rings $`L=8,12,16,20`$ and the 16-object cubic cluster (links listed in the output), $`S=1`$ rings $`L=6,8,10,12`$; uniqueness of the singlet without push; $`m`$ at the far places and at $`h`$ for $`h_p/J=0.01,\dots,10`$. Output `code/v2/output/ed_push.txt`.
- `code/v2/spinwave_tilt.py` (check): leading order in $`1/S`$; $`\Delta S_3`$ by midpoint sums ($`L=64,128,256`$, Richardson); exact Gaussian $`\Delta S`$ at the far place with the push on cubic tori $`L=8,12,16`$ for $`\eta=0.1,1,10`$, with the zero-mode estimate; rings $`L=64,\dots,1024`$ for (8.8). Output `code/v2/output/spinwave_tilt.txt`.
- `code/v2/spinwave_mutual.py` (check): (5.8) with (8.10) against a direct inverse; transverse separation parts from $`\hat g_\infty`$ (Bessel integral) and on tori $`L=16,32,64`$; continuum coefficients of (8.16)–(8.18) (closed forms and numerical $`\tau'`$-integral); (8.15) on tori $`L=32,64,128`$ for along-$`\mathbf n`$ sources (single, cells), the spin-length model of R1 and R2 (two geometries), $`r=2,\dots,12`$, with the extrapolation $`L\to\infty`$. Output `code/v2/output/spinwave_mutual.txt`.

## Methods used

- Marshall–Lieb–Mattis and Lieb–Mattis theorems; Perron–Frobenius; analytic perturbation theory
- Holstein–Primakoff representation and expansion in $`1/S`$; quadratic forms, normal modes, Gaussian lowest eigenvectors
- Lattice Green functions on tori and their asymptotics; Wick's theorem; imaginary-time second-order perturbation theory
- Projection theorem for a multiplet; dimension counting of local vertices
- Exact diagonalization (Lanczos) in sectors of $`\sum_xS^3_x`$
