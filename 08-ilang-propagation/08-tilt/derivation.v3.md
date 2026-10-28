# Exchange cells with a push: orientation, small deviations, mutual costs

- **Subproject:** 08-ilang-propagation
- **Package:** 08-tilt
- **Version:** v3
- **Mode:** external regeneration
- **Date:** 2026-10-26

## Changes from previous version

- Step 13, (8.19), Result: without a push the orientation is now the minimum of the cost of the orientation (8.19). The non-cancelling regime and its positivity are stated. The nearly balanced collinear case is solved: the orientation cants below a threshold $`H_c`$, and the $`1/r`$ part follows from that (I1).
- Step 12, (8.18), Result: the projection onto a multiplet of the pair $`b,x`$ is removed. The held spin is eliminated at second order in its transverse coupling, in the exchange background, which gives a retarded vertex with its antisymmetric part. (8.18) is now one formula for every $`r`$; its two limits are derived, with their remainders, and the old second line comes out as the limit $`r\gg\ell_b`$ (I2, I6).
- Step 6, (8.10): the push's mixed term, which couples the copies, is included, and the lowest-derivative limit in which the copies are independent is stated (I3).
- Setup, Steps 8 and 10: separations are those of the midpoints, and the remainders of (8.14) and (8.16) hold for them (I4).
- Step 11, (8.17): the coefficient is given for all four pairs of link orientations with the separation along an axis, with signs; no pair has a vanishing coefficient (I5).
- Step 5, (8.9): exact diagonalization now searches every sector of $`\sum_xS^3_x`$ and checks that the lowest eigenvector is unique; the statements are restricted to the sampled $`h_p`$ (I7).
- Code: `ed_push.py` was changed to search all sectors. `spinwave_mutual.py` was changed: R2 in four orientation pairs at midpoint separations; a single object against a cell; R1 with the retarded vertex in the frequency domain on tori up to $`L=256`$, against (8.18) with its off-diagonal part (Step 12(ii)), which also extends the check of (8.16) in Step 10. `spinwave_tilt.py` is unchanged. All three were run again under `code/v3/`, and every cited number comes from `code/v3/output/`.

## Response to verification

- I1: Accepted and fixed in Step 13 and (8.19). The orientation minimizes $`E(\hat{\mathbf n})`$ of (8.19). $`-\hat{\mathbf h}_{\rm eff}`$ is the orientation in two cases: for non-cancelling sources, $`SJ\lvert\mathbf h_{\rm eff}\rvert\gg\gamma_3\lvert\mathbf h_i\rvert^2`$, where positivity follows from (5.6), and for parallel $`\mathbf m_i`$ exactly when $`H\ge H_c`$. For parallel $`\mathbf m_i`$ the orientation cants for $`H<H_c`$, which is the range where the verifier's determinant is negative, and the $`1/r`$ part is $`-h_1h_2(1-u^{*2})/(4\pi J\lvert\mathbf r\rvert)`$; it is absent only for $`H\ge H_c`$.
- I2: Accepted and fixed in Step 12. The projection onto a multiplet is gone. $`b`$ is eliminated at second order in its transverse coupling; the exchange of $`x`$ with its neighbours enters through the propagator of $`q_x`$. The resulting retarded vertex contains the antisymmetric response, whose low-frequency limit is the precession term of the spin $`\sigma`$; it does not depend on $`g'`$. The omitted terms are of relative order $`1/S`$, $`\lvert g'\rvert/(JS)`$ and $`\lvert g'\rvert s_b/(JS)`$, and $`s_b`$ needs no scaling with $`S`$ beyond $`\lvert g'\rvert s_b\ll JS`$. The $`r\gg\ell_b`$ law of v2 is the limit of (8.18).
- I3: Accepted and fixed in Step 6 and (8.10). The mixed term is included. It is smaller than the anchor by $`O(\nu/T_0)`$, and the lowest-derivative limit that discards it and the kinetic term is stated. The exact static identification is kept separate.
- I4: Accepted and fixed in Setup and Steps 8 and 10. Separations are those of the midpoints, and with them the remainders are $`O(\lvert\mathbf r\rvert^{-3})`$ in (8.14) and relative $`O(r^{-2})`$ in (8.16). With end points a term $`O(\lvert\mathbf r\rvert^{-2})`$ (relative $`O(r^{-1})`$) remains; the code checks this.
- I5: Accepted and fixed in Step 11 and (8.17). All four orientation pairs are given: $`a=\frac1{12}`$ for two links perpendicular to $`\mathbf r`$ and to each other, and $`a=-\frac12`$, repulsive for $`\delta_1\delta_2>0`$, for one link parallel and one perpendicular to $`\mathbf r`$, as the verifier states. No pair has a vanishing leading coefficient. All four are checked on the lattice at the midpoint separation.
- I6: Accepted and fixed in Step 12. The antisymmetric contraction is evaluated exactly in (8.18), over all frequencies; the low-frequency region gives the explicit term of order $`r/\ell_b`$ in its first limit.
- I7: Accepted and fixed in Step 5 and (8.9). Every sector $`M=-NS,\dots,NS`$ is searched. Uniqueness follows from Perron–Frobenius in each sector together with the computed gap, and the statements hold at the sampled $`h_p`$ only.

## Setup and assumptions

**Field** (M8). One object with $`2S+1`$ places at each place $`x`$ of $`X_f`$, a cubic torus ($`D=3`$) or a ring ($`D=1`$) of even side $`L\ge4`$; $`N=L^D`$ objects, $`DN`$ links, coordination $`z=2D`$. $`C_{\rm ex}=J\sum_{\langle xy\rangle}\mathbf S_x\cdot\mathbf S_y`$, $`J>0`$ unless stated. $`\Delta`$ is the graph Laplacian, $`\Delta^+:=2z-\Delta`$ (the adjacency plus $`z`$), $`P_x`$ the projector onto place $`x`$, $`E={\rm diag}(\epsilon_x)`$; $`E\Delta E=\Delta^+`$ because every link joins the two classes. The class labels are chosen so that $`\epsilon_h=+1`$ (the other choice flips the sign of every $`m(x)`$). $`\hat g`$ is the pseudo-inverse of $`\Delta`$, so that the $`g`$ of 05-anchor is $`\hat g/\kappa_h`$; on the cubic torus $`\hat g\to\hat g_\infty`$, $`\hat g_\infty(0)=\gamma_3=0.2527310`$, $`\hat g_\infty(x)=\frac1{4\pi\lvert x\rvert}+O(\lvert x\rvert^{-3})`$ (quoted with 05-anchor).

**Push, sources, state** (M8, M9, A11, A15): as in the question: push $`-h_p\,\mathbf n\cdot\mathbf S_h`$; direction sources $`g\,\mathbf m\cdot\mathbf S_x`$ or $`g\,\mathbf m\cdot(\mathbf S_x-\mathbf S_{x'})`$ ($`x'`$ a neighbour of $`x`$; $`\epsilon_x`$ below is the class of the object with the sign $`+`$); relation sources R1 ($`g'\,\mathbf S_b\cdot\mathbf S_x`$, spin $`s_b`$) and R2 (link coefficient $`J+\delta`$). State: the lowest eigenvector of the stated total contract. $`\mathbf e_1,\mathbf e_2`$ complete $`\mathbf n`$ to a right-handed frame; $`\mathbf m^\perp:=\mathbf m-(\mathbf m\cdot\mathbf n)\mathbf n`$. **Separations:** the separation $`\mathbf r`$ of two sources is that of their midpoints (the place of a single object, the midpoint of a two-object cell or of a link), $`r=\lvert\mathbf r\rvert`$.

**Small numbers.** $`1/S`$; $`\eta:=h_p/(JS)`$ (not assumed small); $`\lvert g\rvert/h_p`$ and $`\lvert g\rvert/(JS)`$; $`\lvert g'\rvert/J`$ and $`\lvert g'\rvert s_b/(JS)`$, $`\lvert\delta\rvert/J`$. $`\lvert g\rvert\ll JS`$ does not make $`\lvert g\rvert/h_p`$ small; this is a separate condition (Step 6).

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

The value ($`0.07836`$) is computed in `code/v3/output/spinwave_tilt.txt`; the same file gives $`\Delta S`$ at the far place of tori $`L=8,12,16`$ with the push: for $`\eta=1`$, $`\Delta S-\Delta S_3=0.0736,0.0412,0.0272`$ against the zero-mode term $`0.0766,0.0417,0.0271`$ of (8.6); for $`\eta=10`$ the excess $`0.033,0.019,0.013`$ also falls with $`L`$.

*Ring.* $`(1-\gamma_k^2)^{-1/2}=1/\lvert\sin k\rvert`$ is not integrable; the pinning at $`h`$ cuts it off at the distance $`R`$. With $`T/(2\omega)\simeq1/\lvert k\rvert`$ near $`k=0`$ (and likewise for $`\tilde P`$ near $`\pi`$), $`G(r)=\frac1{2\pi}\int dk\,e^{ikr}/\lvert k\rvert`$; at long wavelengths the pinned place acts as a fixed value, and by the image at $`h`$, $`\langle\tilde Q_R^2\rangle\simeq G(0)-G(2R)=\frac1{2\pi}\int_{-\pi}^{\pi}dk\,\frac{1-\cos 2kR}{\lvert k\rvert}\simeq\frac1\pi\ln R`$:

```math
\text{ring:}\qquad m(R)=S-\frac1\pi\ln R+O(1)+O(1/S),\qquad\text{(8.8)}
```

confirmed in `code/v3/output/spinwave_tilt.txt` (slope $`0.3156`$ of $`\Delta S(L/2)`$ in $`\ln L`$ for $`L=256`$–$`1024`$, $`\eta=1`$, against $`1/\pi=0.3183`$). The first correction is not uniform in $`R`$ and exceeds $`S`$ for $`\ln R\gtrsim\pi S`$: on the ring the expansion in $`1/S`$ does not decide the order $`L\to\infty`$, $`R\to\infty`$ at any $`S`$. The ring is the control of (8.7).

### Step 5. Exact diagonalization, $`S=\frac12`$ and $`S=1`$ (item 1(b))

`code/v3/ed_push.py` (output `code/v3/output/ed_push.txt`), $`J=1`$, push at $`h=0`$. $`C`$ commutes with $`M=\sum_xS^3_x`$, and the two lowest eigenvalues are computed in every sector $`M=-NS,\dots,NS`$; without full rotation symmetry no sector can be skipped. In each sector the lowest eigenvalue is simple: after the Marshall sign change the off-diagonal elements are $`\le0`$ and the matrix is irreducible, and the push is diagonal (Perron–Frobenius). So the lowest eigenvector of $`C`$ is unique iff the lowest sector value lies strictly below all others, which the code checks. Clusters: rings $`L=8,12,16,20`$ ($`S=\frac12`$) and $`L=6,8,10,12`$ ($`S=1`$); the cubic cluster $`\mathbb Z^3/\Lambda`$ with $`\Lambda`$ spanned by $`(2,2,0),(2,0,2),(0,2,2)`$: 16 objects, links $`x`$–$`x\pm\mathbf e_i`$, 48 links, 6 distinct neighbours each, bipartite, far places at graph distance 3. Without push every cluster has a unique singlet lowest eigenvector (check of (8.1)). With the push, at the sampled strengths $`h_p/J=0.01,0.1,0.3,1,3,10`$ on every cluster, the lowest eigenvector is unique and lies in the sector $`M=0`$; its gap to the next level over all sectors is at least $`0.185J`$ (ring $`L=20`$, $`h_p=10J`$). Between the sampled strengths nothing is claimed. The values are

```math
\begin{aligned}&m_{\rm far}(h_p=10J)=0.224,\ 0.190,\ 0.169,\ 0.154\quad(S=\tfrac12\text{ rings }L=8,12,16,20),\\&m_{\rm far}(h_p=10J)=0.695,\ 0.609,\ 0.551,\ 0.488\quad(S=1\text{ rings }L=6,8,10,12),\qquad m_{\rm far}(h_p=10J)=0.330\quad(\text{cubic cluster }16),\\&m_{\rm far}/h_p=0.29\text{–}0.32\ (S=\tfrac12\text{ rings}),\ 0.24\ (\text{cubic }16)\ \text{at }h_p=0.01J,\ \text{linear in }h_p\text{ at }h_p=0.01J,0.1J.\end{aligned}\qquad\text{(8.9)}
```

What this decides, at the sampled $`h_p`$: at fixed size $`m_{\rm far}`$ is linear in $`h_p`$ at the two smallest strengths on every cluster (as (8.4)); on rings with $`h_p\ge J`$ (and for $`S=1`$ at every $`h_p`$ computed) $`m_{\rm far}`$ falls monotonically with $`L`$, without sign of saturation, while for $`S=\frac12`$ and $`h_p\le0.1J`$ the linear response $`\chi_L`$ still rises slowly with $`L`$; this is consistent with the control (8.8) but no proof of $`m_{\rm far}\to0`$; with one cubic cluster of 16 objects the order $`L\to\infty`$, $`R\to\infty`$ for $`S=\frac12`$ on the cubic torus is **undecided**.

### Step 6. Identification with the oscillator field of 05-anchor (item 2)

*Static identification.* For any positive definite kinetic matrix $`T`$, the shift $`q\to q-A^{-1}b`$ shows that the lowest eigenvalue of $`\frac12p^{\rm T}Tp+\frac12q^{\rm T}Aq+b^{\rm T}q+c_0`$ is $`c_0+\frac12{\rm Tr}(T^{1/2}AT^{1/2})^{1/2}-\frac12b^{\rm T}A^{-1}b`$ and $`\langle q\rangle=-A^{-1}b`$; a lowest eigenvector exists iff $`A>0`$. So every source-dependent static result of 05-anchor depends on $`A`$ and $`b`$ only. A direction source gives, at the order of (8.5), $`g\,\mathbf m\cdot\mathbf S_x=g(\mathbf m\cdot\mathbf n)\epsilon_x(S-n_x)+g\sqrt S\epsilon_x\sum_\alpha(\mathbf m\cdot\mathbf e_\alpha)q^{(\alpha)}_x`$, and a cell $`g\,\mathbf m\cdot(\mathbf S_x-\mathbf S_{x'})=g(\mathbf m\cdot\mathbf n)\epsilon_x(2S-n_x-n_{x'})+g\sqrt S\epsilon_x\sum_\alpha(\mathbf m\cdot\mathbf e_\alpha)(q^{(\alpha)}_x+q^{(\alpha)}_{x'})`$. Comparing with (8.5):

```math
q_x\leftrightarrow q^{(\alpha)}_x=\epsilon_x\frac{\mathbf e_\alpha\cdot\mathbf S_x}{\sqrt S},\qquad \kappa_h=JS,\qquad \kappa_a=h_p,\qquad g_s=\epsilon_{x_s}\sqrt S\,g\,(\mathbf m\cdot\mathbf e_\alpha),\qquad c_0=E_0+\textstyle\sum_s g(\mathbf m\cdot\mathbf n)\epsilon_{x_s}S,\qquad\text{(8.10)}
```

two copies $`\alpha=1,2`$ with the same $`A=V_a`$ (no pinning, the push as the anchor), each with its own sources. The copies are not independent fields: they are conjugate to each other, and as one oscillator field ($`q=q^{(1)}`$, $`p=\tilde P`$) the kinetic matrix is $`T_a=EV_aE`$ instead of $`\mathbb 1`$. *Long-wavelength identification* (needed for dynamics; an approximation, separate from the exact static identification above). $`T_a(k)\to T_0:=2zJS`$ near $`k=0`$ and $`\to0`$ near $`k=(\pi,\dots)`$, where $`q^{(2)}`$ takes the role of coordinate. With the smooth coordinates and momenta $`\phi_\alpha,\pi_\alpha`$ of the two points, $`\tilde Q=\phi_1-\epsilon\pi_2`$, $`\tilde P=\pi_1+\epsilon\phi_2`$ (used again in Step 11), and $`q_\alpha=\phi_\alpha/\sqrt{T_0}`$, $`p_\alpha=\sqrt{T_0}\pi_\alpha`$, the bulk is two copies of the 05-anchor field with $`\frac12p^2`$: $`\kappa_h=2zJ^2S^2`$, $`g_s=\epsilon_{x_s}S\sqrt{2zJ}\,g(\mathbf m\cdot\mathbf e_\alpha)`$, speed $`c=\sqrt{\kappa_h}=JS\sqrt{2z}`$. The push $`\frac{h_p}2(\tilde Q_h^2+\tilde P_h^2)`$ gives three local terms at $`h`$: the anchor $`\frac{\kappa_a}2(q_1^2+q_2^2)_h`$, $`\kappa_a=2zJSh_p`$; the kinetic term $`\frac{h_p}{2T_0}(p_1^2+p_2^2)_h`$; and the mixed term $`-h_p\epsilon_h(q_1p_2-q_2p_1)_h`$. The mixed term couples the copies: it is $`-h_p\epsilon_h`$ times the local generator of rotations about $`\mathbf n`$, and it commutes with the total generator. At imaginary frequency $`\nu`$ ($`p\sim\nu q`$) the mixed term is smaller than the anchor by $`2\nu/T_0`$ and the kinetic term by $`\nu^2/T_0^2`$. For a wave number $`k`$, $`\nu=ck`$ gives $`\nu/T_0=k/\sqrt{2z}`$. In the *lowest-derivative limit* $`k\ll1`$ both terms are discarded, and only there are the copies two independent 05-anchor fields; the mixed term is the first correction, of relative order $`k`$. Both dictionaries give the same $`\kappa_a/\kappa_h=\eta`$ and $`g_s^2/\kappa_h=g^2(\mathbf m\cdot\mathbf e_\alpha)^2/J`$, the combinations that enter (5.8)–(5.15).

*Small deviations.* The tilt of the object at $`y`$ by a transverse source at $`x_s`$ is $`\lvert\langle\mathbf e_1\cdot\mathbf S_y\rangle\rvert/S=\lvert g\,(\mathbf m\cdot\mathbf e_1)\rvert\,G_a(y,x_s)\le\lvert g\rvert\,\Gamma(x_s)`$, $`\Gamma(x)=G_a(x,x)=\frac1{h_p}+\frac{2[\hat g(0)-\hat g(x-h)]}{JS}`$, by (5.11) with (8.10). The identification holds at leading order in $`1/S`$ under

```math
\Delta S_3\ll S\ \text{and (8.6)};\qquad \lvert g\rvert\ll h_p\ \text{and}\ \lvert g\rvert\ll JS\ \ (\text{cubic torus: }\Gamma\le\tfrac1{h_p}+\tfrac{2\gamma_3}{JS});\qquad \text{ring: also }\tfrac1\pi\ln d\ll S\ \text{and}\ \lvert g\rvert d\ll JS\ \text{at the distances }d\text{ used}.\qquad\text{(8.11)}
```

### Step 7. Which results of 05-anchor carry over (item 2, short argument)

By Step 6 and (8.11): (5.8) holds exactly as a matrix identity for $`V_a^{-1}`$ with $`\kappa_h=JS`$, $`\kappa_a=h_p`$ (checked against a direct inverse in `code/v3/output/spinwave_mutual.txt`, error $`5\times10^{-14}`$); (5.3) with the push holds ($`V_a>0`$, $`T_a>0`$); (5.11) and (5.14), (5.15) hold for the transverse components (Step 8). An along-$`\mathbf n`$ source adds $`-g\epsilon_xP_x`$ to both $`V_a`$ and $`T_a`$, i.e. it is a body with $`\alpha=-g\epsilon_x`$ in both copies; with this reading (5.4)–(5.6), (5.10) hold as positivity criteria for $`V_a-\sum_ig_i\epsilon_{x_i}P_{x_i}`$, and a source with $`g\epsilon_x<0`$ is itself a push (the analogue of the first statement of (5.7)). What changes: (i) *boundedness of the common rotation* (A1): the zero mode of 05-anchor (a free particle on $`\mathbb R`$) is here a rotation of the orientation on the sphere, quantized with discrete levels; therefore the "no lowest eigenvector" outcomes of (5.3)–(5.6) are replaced by a lowest eigenvector that exists (A1) and, for the field alone, is the unique singlet (8.1); the outcome "$`-\infty`$" is replaced by a finite rotation of the orientation, and the uniform shift $`-g_s/\kappa_a`$ of (5.11) is the small-angle form of a rotation by $`\arctan(g/h_p)`$ (classical uniform rotation in the plane of $`\mathbf n,\mathbf e_1`$: energy $`-S(h_p\cos\theta-g\epsilon_x\sin\theta)`$); (ii) *next order in $`1/S`$*: $`C_4`$ and the $`O(S^{-1/2})`$ terms of the transverse components change the coefficients by relative $`O(1/S)`$ (not computed); (iii) on the ring, (5.8) and (5.14) hold with $`r=\frac{s(L-s)}{\kappa_hL}`$, but only at distances allowed by (8.11).

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

For cells, $`G_a(x_1,x_2)`$ in (8.13) becomes $`\sum_{a\in{\rm cell}_1,\,b\in{\rm cell}_2}G_a(a,b)`$, with the weight $`g\epsilon_x\sqrt S`$ on each object. The two objects of a cell lie symmetrically about its midpoint, so with the midpoint separation $`\mathbf r`$ the dipole terms of $`\sum\frac1{4\pi\lvert a-b\rvert}`$ cancel, and the pair terms give $`c_{\rm cell}/(4\pi\lvert\mathbf r\rvert)`$ up to $`O(\lvert\mathbf r\rvert^{-3})`$. This holds also for a single object against a cell. With the end-point separation a term $`O(\lvert\mathbf r\rvert^{-2})`$ remains. The separation part $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)c_{\rm cell}/(4\pi J\lvert\mathbf r\rvert)`$ is a long-range mark of order $`S^0`$ (the uniform part is of order $`S`$); it is attractive iff $`\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)>0`$, so for single objects its sign alternates with the class of the separation, and for cells written with $`+`$ on the class-$`+`$ object ($`\epsilon_{x_1}\epsilon_{x_2}=1`$) it is fixed. `code/v3/output/spinwave_mutual.txt`: $`4\pi r\hat g_\infty(r)=1.078,1.020,1.008,1.004`$ at $`r=2,4,6,8`$ and $`\pi r\sum\hat g_\infty=0.991,1.0005,1.0001,1.0000`$ for cells. For a single object against a cell along $`\mathbf r`$, $`2\pi R[\hat g_\infty(r)+\hat g_\infty(r+1)]=1.029,1.013,1.007`$ at the midpoint separation $`R=4.5,6.5,8.5`$, against $`0.915,0.935,0.948`$ with the end-point separation $`R=r=4,6,8`$. On tori $`L=16,32,64`$ the separation dependence $`\hat g_L(r)-\hat g_L(8)`$ converges to that of $`\hat g_\infty`$. *Vanishing members* (excluded): a source at $`h`$ ($`G_a(h,\cdot)=1/h_p`$), $`\mathbf m_1^\perp\cdot\mathbf m_2^\perp=0`$ (e.g. $`\mathbf m_i=\mathbf n`$, or $`\mathbf m_1\perp\mathbf m_2`$ both transverse: different copies), sources on the same object or cell.

### Step 9. Sources quadratic in the deviations: the second-order formula

Along-$`\mathbf n`$ sources and relation sources add, at the order of (8.5), local quadratic terms $`\delta H_i=\frac12\tilde Q^{\rm T}A_i\tilde Q+\frac12\tilde P^{\rm T}B_i\tilde P`$ and constants linear in the strengths. Their mutual cost is of second order; Rayleigh–Schrödinger perturbation theory of the Gaussian lowest eigenvector of $`C_2`$ gives, with $`\delta H(\tau)=e^{C_2\tau}\delta He^{-C_2\tau}`$ and Wick's theorem,

```math
\mathcal E_{12}=-\int_{-\infty}^{\infty}d\tau\,\langle T\,\delta H_1(\tau)\,\delta H_2(0)\rangle_c .\qquad\text{(8.15)}
```

At large separation only the low modes matter: per copy, the coordinate ($`q^{(1)}`$ near $`k=0`$, $`q^{(2)}`$ near $`k=0`$, i.e. $`\tilde P`$ near $`(\pi,\dots)`$) has the imaginary-time covariance $`\frac{T_0}{4\pi^2c}\frac1{r^2+c^2\tau^2}`$ with $`T_0=2zJS`$, $`c=JS\sqrt{2z}`$; covariances with momenta carry extra derivatives. Far from $`h`$ the push enters only through the zero modes, whose contribution vanishes as $`L\to\infty`$ (as $`N^{-1/2}`$ with (8.6)). `code/v3/spinwave_mutual.py` evaluates (8.15) on the lattice (exact $`T(k),V(k)`$, zero modes left out) on tori $`L=32,64,128`$, $`r=2,\dots,12`$ along an axis.

### Step 10. Along-$`\mathbf n`$ direction sources

$`g\,\mathbf n\cdot\mathbf S_x=g\epsilon_xS-\frac{g\epsilon_x}2\sum_\alpha(q^{(\alpha)}_x)^2+\text{const}`$: $`A=B=-g\epsilon_xP_x`$. Wick's theorem gives $`\langle T\,q^2(\tau)\,q^2(0)\rangle_c=2G^2`$ per copy, $`G=\frac{T_0}{4\pi^2c\rho^2}`$, so (8.15) is $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2\int d\tau\,G^2`$, and $`\int d\tau\,\rho^{-4}=\pi/(2cr^3)`$:

```math
\mathcal E^\parallel_{12}=-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1\cdot\mathbf n)(\mathbf m_2\cdot\mathbf n)\,\frac{c_{\rm cell}\,\kappa_\parallel}{JS\,r^3}\bigl[1+O(r^{-2})\bigr],\qquad \kappa_\parallel=\frac{\sqrt{2z}}{32\pi^3}=\frac{\sqrt3}{16\pi^3}=0.0034913,\qquad\text{(8.16)}
```

order $`g_1g_2/(JS)`$, one order in $`1/S`$ below the separation part of (8.14); $`c_{\rm cell}=c_1c_2`$ as in (8.14): a cell has $`A=B=-g\epsilon_x(P_x+P_{x'})`$, at large $`r`$ a vertex of twice the strength at the cell midpoint ($`c_i=2`$), so $`c_{\rm cell}=2`$ for a single object and a cell and $`4`$ for two cells. With midpoint separations the dipole terms of $`\sum\lvert a-b\rvert^{-3}`$ cancel, as in Step 8, and the remainder is relative $`O(r^{-2})`$; with end points it would be $`O(r^{-1})`$. In the code both cells are $`(x,x+\mathbf e_2)`$, so the two separations coincide. It falls as $`r^{-3}`$: no long-range mark. Lattice/continuum ratio (`code/v3/output/spinwave_mutual.txt`): on $`L=128`$, $`1.02,1.00,0.96,0.94`$ at $`r=4,\dots,7`$, rising with $`L`$ at fixed $`r`$; the Aitken extrapolation from $`L=32,64,128`$ (meaningful for $`r\le7`$, where $`L=32\ge4r`$) gives $`1.06,1.06,1.05,1.07`$ (single objects) and $`1.01,1.02,1.03,1.05`$ (cells) at $`r=4,\dots,7`$: (8.16) up to corrections of a few per cent at these $`r`$. The same quantity is the case $`\lvert g'\rvert=0`$ of block (3) (Step 12(iii)). There, with $`L`$ up to $`256`$ and extrapolated from $`L=64,128,256`$, the ratios are $`1.02`$–$`1.04`$ at $`r=6,\dots,12`$; the off-diagonal factor $`1-\gamma^2`$ of Step 12(ii) changes the continuum value by at most $`0.4\%`$ at these $`r`$. For a general $`\mathbf m`$ the transverse part (8.14) dominates unless $`\mathbf m_1^\perp\cdot\mathbf m_2^\perp=0`$; cross terms transverse–along vanish at order $`g_1g_2`$ (odd in the deviations).

### Step 11. Relation source R2 (changed link)

$`\delta\,\mathbf S_x\cdot\mathbf S_y=-\delta S(S+1)+\frac{\delta S}2\sum_\alpha(q^{(\alpha)}_x-q^{(\alpha)}_y)^2`$: $`A=\delta S(e_x-e_y)(e_x-e_y)^{\rm T}`$, $`B=\delta S(e_x+e_y)(e_x+e_y)^{\rm T}`$, which vanish on the zero modes (unchanged by the common rotation). With $`\tilde Q=\phi_1-\epsilon\pi_2`$, $`\tilde P=\pi_1+\epsilon\phi_2`$ ($`\phi_\alpha,\pi_\alpha`$ the smooth coordinate and momentum of copy $`\alpha`$), $`\phi_\alpha=\sqrt{T_0}\chi_\alpha`$, $`\pi_\alpha=\partial_t\chi_\alpha/\sqrt{T_0}`$, $`t'=ct`$ and $`\mathbf e`$ the unit vector from $`y`$ to $`x`$:

```math
\delta H=\frac{\delta ST_0}2\Bigl[\sum_\alpha\Bigl((\mathbf e\cdot\nabla\chi_\alpha)^2+\frac2z(\partial_{t'}\chi_\alpha)^2\Bigr)-\epsilon_x\sqrt{\tfrac8z}\bigl(\mathbf e\cdot\nabla\chi_1\,\partial_{t'}\chi_2-\partial_{t'}\chi_1\,\mathbf e\cdot\nabla\chi_2\bigr)\Bigr].
```

Every term carries two derivatives, so each contraction in (8.15) is $`\propto\rho^{-4}`$, $`\rho^2=r^2+c^2\tau^2`$, and $`\mathcal E\propto\int d\tau\,\rho^{-8}\propto r^{-7}`$. With the Euclidean covariance $`\frac1{4\pi^2c\rho^2}`$ of $`\chi`$ ($`\partial_{t'}\to i\partial_{\tau'}`$, $`\tau'=c\tau`$), $`I_{\mu\nu}=\delta_{\mu\nu}-4n_\mu n_\nu`$, $`n=(\tau',\mathbf r)/\rho`$, $`M_i=\mathbf e_i\mathbf e_i^{\rm T}-\frac2z\hat 0\hat 0^{\rm T}`$:

```math
\mathcal E^{R2}_{12}=-\frac{\delta_1\delta_2S\sqrt{2z}}{16\pi^4J}\int\frac{d\tau'}{\rho^8}\Bigl\{4{\rm Tr}(M_1IM_2I)-\frac{16}z\epsilon_1\epsilon_2\bigl[I_{00}\,\mathbf e_1\!\cdot\! I\mathbf e_2-(I\mathbf e_1)_0(I\mathbf e_2)_0\bigr]\Bigr\}=-\frac{\sqrt3}{8\pi^3}\frac{\delta_1\delta_2S}{J\,r^7}\,a\,\bigl[1+O(r^{-2})\bigr],\qquad a=\begin{cases}\frac{43}6+\frac52\epsilon_1\epsilon_2 & \text{both links}\parallel\mathbf r,\\ \frac43-\frac5{12}\epsilon_1\epsilon_2 & \text{both}\perp\mathbf r,\ \text{parallel to each other},\\ \frac1{12} & \text{both}\perp\mathbf r,\ \perp\text{ each other},\\ -\frac12 & \text{one}\parallel\mathbf r,\ \text{one}\perp\mathbf r,\end{cases}\qquad\text{(8.17)}
```

for the separation along an axis ($`\epsilon_i`$ is the class of the endpoint $`x`$ of link $`i`$, $`\mathbf e_i`$ points from $`y`$ to $`x`$; order $`\delta_1\delta_2S/J`$). Derivation of $`a`$: with $`\mathbf r=r\hat{\mathbf e}_1`$ and $`u=r^2/\rho^2`$, one has $`n=(\tau',\mathbf r)/\rho`$, $`I_{00}=4u-3`$, $`I_{0\mathbf e_i}=-4\frac{\tau'r}{\rho^2}p_i`$ and $`\mathbf e_1\cdot I\mathbf e_2=\mathbf e_1\cdot\mathbf e_2-4up_1p_2`$, where $`p_i=1`$ if link $`i\parallel\mathbf r`$ and $`0`$ otherwise. The braces are polynomials in $`u`$, and $`\int d\tau'\rho^{-8}u^k=r^{-7}C_{3+k}`$ with $`C_n=\int_{-\pi/2}^{\pi/2}\cos^{2n}\theta\,d\theta`$ ($`C_3,C_4,C_5=\frac{5\pi}{16},\frac{35\pi}{128},\frac{63\pi}{256}`$). The cross term equals $`-3`$ for two links $`\parallel\mathbf r`$, equals $`4u-3`$ for two parallel links $`\perp\mathbf r`$, and vanishes in the last two cases. In the last two cases the braces are $`\frac49(4u-3)^2`$ and $`4-32u+\frac{256}9u^2`$, so $`a=\frac1{12}`$ and $`-\frac12`$ independent of $`\epsilon_1\epsilon_2`$. Sign: for $`\delta_1\delta_2>0`$ the cost is attractive in the first three cases and repulsive for one link parallel and one perpendicular to $`\mathbf r`$. The values of $`a`$ are $`\frac{29}3,\frac{14}3,\frac{11}{12},\frac74,\frac1{12},-\frac12`$, so **no** pair of orientations has a vanishing leading coefficient (excluded only: $`\delta_i=0`$, links that share an object). In the last two cases the midpoints are not exactly on an axis: their separation is $`r\hat{\mathbf e}_1`$ plus an offset of order $`1`$, and the axis formula has a relative remainder $`O(r^{-1})`$; at the midpoint vector the remainder is $`O(r^{-2})`$. Lattice check (`code/v3/output/spinwave_mutual.txt`, continuum at the midpoint separation; odd $`r`$ gives $`\epsilon_1\epsilon_2=-1`$). The closed forms of $`a`$ agree with the numerical $`\tau'`$-integral in all four cases. The lattice/continuum ratios on $`L=128`$ at $`r=8,\dots,12`$ are:

| orientation pair | ratios at $`r=8,\dots,12`$ | largest change from $`L=64`$ |
|---|---|---|
| both links $`\parallel\mathbf r`$ | $`1.112,1.066,1.067,1.042,1.046`$ | $`0.014`$ |
| both $`\perp\mathbf r`$, parallel to each other | $`1.123,1.079,1.072,1.051,1.046`$ | $`0.045`$ (at $`r=12`$, member $`\epsilon_1\epsilon_2=+1`$; at most $`0.004`$ for $`r=9,11`$) |
| both $`\perp\mathbf r`$, $`\perp`$ each other | $`0.958,1.020,0.988,1.010,0.996`$ | $`0.015`$ |
| one $`\parallel\mathbf r`$, one $`\perp\mathbf r`$ | $`1.054,0.958,1.034,0.987,1.023`$ | $`0.015`$ |

These confirm the sign, the decay $`r^{-7}`$ and the coefficient at the midpoint separation. The corrections alternate with the parity of $`r`$, with $`\lvert\text{ratio}-1\rvert\,r^2\lesssim8`$, consistent with $`O(r^{-2})`$. The perpendicular member at even $`r=10,12`$ is confirmed only to within its finite-size change. At small $`r`$ the last two cases, whose coefficients are small, take the continuum sign only from $`r=5`$ resp. $`r=6`$ on: the ratio is $`-1.42`$ at $`r=4`$ and $`-0.68`$ at $`r=5`$, respectively. No long-range mark.

### Step 12. Relation source R1 (held spin)

(i) *Retarded vertex.* Conditions: $`\lvert g'\rvert\ll J`$ and $`\lvert g'\rvert s_b\ll JS`$; $`s_b`$ needs no scaling with $`S`$ beyond the second. With (8.5) and $`S^\alpha_b:=\mathbf e_\alpha\cdot\mathbf S_b`$,

```math
g'\mathbf S_b\cdot\mathbf S_x=g'\epsilon_x(S-n_x)\,\mathbf n\cdot\mathbf S_b+g'\sqrt S\,\epsilon_x\textstyle\sum_\alpha S^\alpha_b\,q^{(\alpha)}_x+O(g').
```

The first term splits the levels of $`b`$ by $`\Delta_b=\lvert g'\rvert S`$. The lowest level is $`\mathbf n\cdot\mathbf S_b=m_b:=\sigma\epsilon_x`$, with $`\sigma:=-s_b\,{\rm sgn}\,g'`$. In it, $`-g'\epsilon_xm_bn_x=\lvert g'\rvert s_bn_x`$ is the along-$`\mathbf n`$ vertex $`\frac12\lvert g'\rvert s_b\sum_\alpha(q^{(\alpha)}_x)^2`$ (Step 10 with $`g=-\epsilon_x\lvert g'\rvert s_b`$). Next, $`b`$ is eliminated at second order in the transverse term: this is the cumulant of the imaginary-time action, with $`b`$ in its lowest level and the field Gaussian (8.5). Only $`S^\mp_b`$ connects $`m_b`$ to the next level, with squared matrix element $`2s_b`$, so the time-ordered correlator of $`b`$ is $`\chi_{\alpha\beta}(\tau)=\frac{s_b}2e^{-\Delta_b\lvert\tau\rvert}[\delta_{\alpha\beta}+i\frac{m_b}{s_b}{\rm sgn}(\tau)\varepsilon_{\alpha\beta}]`$, with $`\varepsilon_{12}=-\varepsilon_{21}=1`$. Adding the along vertex, the field at $`x`$ receives the term $`\frac12\int\frac{d\nu}{2\pi}q_x^{\rm T}(-\nu)K(\nu)q_x(\nu)`$, where $`\nu`$ is the imaginary frequency and

```math
K(\nu)=\lvert g'\rvert s_b\,\frac{\nu^2}{\nu^2+\Delta_b^2}\,\mathbb 1+\lvert g'\rvert\sigma\epsilon_x\,\frac{\Delta_b\nu}{\nu^2+\Delta_b^2}\,\varepsilon .
```

$`K(0)=0`$: $`b`$ follows the orientation. This holds at every order, since a static tilt of the field near $`x`$ together with $`b`$ is a joint rotation, which leaves the R1 term unchanged. For $`\nu\ll\Delta_b`$ the antisymmetric part is $`\frac{\sigma\epsilon_x}S\nu\,\varepsilon`$, independent of $`g'`$. With $`q=\sqrt S\theta`$ it is the precession term $`\frac\sigma2(\theta_1\dot\theta_2-\theta_2\dot\theta_1)`$ of the spin $`\sigma`$ that follows the orientation. No multiplet of the pair $`b,x`$ is used: the exchange of $`x`$ with its neighbours is contained in the propagator of $`q_x`$. Three kinds of term are omitted. Higher orders in the transverse term are of relative order $`\langle(q^{(\alpha)}_x)^2\rangle/S=O(1/S)`$. The reaction of the field on $`b`$ is of relative order $`O(\lvert g'\rvert/(JS))`$, since its self-energy $`\sim g'^2S\,\hat g(0)/(JS)`$ is small against $`\Delta_b`$. Higher orders in each vertex are of relative order $`O(\lvert g'\rvert s_b\gamma_3/(JS))`$.

(ii) *Mutual cost.* With two such vertices, the second-order formula (8.15) becomes $`\mathcal E_{12}=-\frac12\int\frac{d\nu}{2\pi}{\rm Tr}[K_1G_{12}K_2G_{21}]`$, where $`G_{12}(\nu)`$ is the matrix of the $`\tau`$-transforms of $`\langle T\,q^{(\alpha)}_{x_1}(\tau)q^{(\beta)}_{x_2}(0)\rangle`$. At large $`r`$, $`G_{12}=G\,\mathbb 1`$ with $`G(\nu)=\frac{T_0}{4\pi c^2r}e^{-\lvert\nu\rvert r/c}`$, the transform of the covariance of Step 9. The off-diagonal part comes from the momenta in $`q^{(\alpha)}`$ and is treated below. For $`K_i=a_i\mathbb 1+b_i\varepsilon`$, $`{\rm Tr}(K_1K_2)=2(a_1a_2-b_1b_2)`$. With $`\int\frac{d\nu}{2\pi}G^2=\frac{\kappa_\parallel}{JSr^3}`$ (Step 10), $`u=2\lvert\nu\rvert r/c`$, $`\ell_b:=c/\Delta_b=\sqrt{2z}J/\lvert g'\rvert`$ and $`\beta_i:=2r/\ell_{b_i}`$:

```math
\mathcal E^{R1}_{12}=-\frac{\lvert g'_1g'_2\rvert\,\kappa_\parallel}{JS\,r^3}\,\mathcal F_{12},\qquad \mathcal F_{12}=\int_0^\infty du\,e^{-u}\,\frac{u^2\bigl(s_{b_1}s_{b_2}u^2-\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}\beta_1\beta_2\bigr)}{(u^2+\beta_1^2)(u^2+\beta_2^2)}.\qquad\text{(8.18)}
```

The relative remainder of (8.18) is $`O(r^{-2})`$ (lattice), $`O(1/S)`$, $`O(\lvert g'\rvert/J)`$ and $`O(\lvert g'\rvert s_b/(JS))`$. *Off-diagonal part.* The continuum covariance is $`G_{12}=G(\mathbb 1+\gamma'\varepsilon)`$ with $`\gamma'=-(\epsilon_{x_1}+\epsilon_{x_2})\nu/T_0`$, and $`G_{21}=G_{12}`$. Matrices $`x\mathbb 1+y\varepsilon`$ multiply like complex numbers $`x+iy`$, so $`{\rm Tr}[K_1G_{12}K_2G_{21}]=2{\rm Re}[k_1k_2g^2]`$. With it the integrand of (8.18), $`a_1a_2-b_1b_2`$ in units of $`\lvert g'_1g'_2\rvert`$, becomes $`(a_1a_2-b_1b_2)(1-\gamma^2)+2\gamma(a_1b_2+a_2b_1)`$, where $`\gamma=(\epsilon_{x_1}+\epsilon_{x_2})cu/(2rT_0)`$. The added term is nonzero only for $`{\rm sgn}\,\sigma_1={\rm sgn}\,\sigma_2`$ and $`\epsilon_{x_1}=\epsilon_{x_2}`$. Then it adds to $`\mathcal F_{12}`$ an amount of order $`s_{b_1}s_{b_2}\Delta_b/T_0`$ for $`r\lesssim\ell_b`$, which shifts the zero of $`\mathcal F_{12}`$ below. For $`r\gg\ell_b`$ (equal $`\ell_b`$) it is a relative correction $`-{\rm sgn}(\sigma_1)\frac{24}{\sqrt{2z}}\frac{\ell_b}{r^2}`$. Both lie within the stated remainders, the first relative to the scale $`s_{b_1}s_{b_2}`$ of $`\mathcal F_{12}`$. Write $`\varsigma:={\rm sgn}(\sigma_1\sigma_2)\epsilon_{x_1}\epsilon_{x_2}`$. The integrals $`\int_0^\infty\frac{u^2du}{(u^2+\beta_1^2)(u^2+\beta_2^2)}=\frac\pi{2(\beta_1+\beta_2)}`$ and $`\int_0^\infty\frac{du}{(u^2+\beta_1^2)(u^2+\beta_2^2)}=\frac\pi{2\beta_1\beta_2(\beta_1+\beta_2)}`$, and $`\int_0^\infty u^{2n}e^{-u}du=(2n)!`$, give the two limits:

```math
\mathcal F_{12}=\begin{cases}s_{b_1}s_{b_2}\Bigl[1-\dfrac\pi2\,\dfrac{\beta_1^2+\beta_1\beta_2+\beta_2^2+\varsigma\beta_1\beta_2}{\beta_1+\beta_2}+O(\beta^2\ln\beta)\Bigr], & r\ll\ell_b,\\[2ex] -\dfrac{2\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}}{\beta_1\beta_2}\Bigl[1-\dfrac{12}{\beta_1\beta_2}\Bigl(\varsigma+\dfrac{\beta_1}{\beta_2}+\dfrac{\beta_2}{\beta_1}\Bigr)+O(\beta^{-4})\Bigr], & r\gg\ell_b,\end{cases}
```

i.e. $`\mathcal E^{R1}_{12}=-\lvert g'_1g'_2\rvert s_{b_1}s_{b_2}\frac{\kappa_\parallel}{JSr^3}[1+O(r/\ell_b)]`$ for $`1\ll r\ll\ell_b`$ (order $`g'_1g'_2`$; the term of order $`r/\ell_b`$ includes the antisymmetric part, whose low-frequency region gives the term $`\varsigma\beta_1\beta_2`$), and

```math
\mathcal E^{R1}_{12}=\frac{3\sqrt3}{8\pi^3}\,\frac JS\,\frac{\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}}{r^5}\bigl[1+O(\ell_b^2/r^2)\bigr]\quad(r\gg\ell_b),
```

independent of $`\lvert g'\rvert`$ (with $`\beta_1\beta_2=4r^2\lvert g'_1g'_2\rvert S^2/c^2`$ and $`c^2=2zJ^2S^2`$, the prefactor is $`z\kappa_\parallel=\frac{3\sqrt3}{8\pi^3}=0.020948`$). This is the law in the order of the question ($`r\to\infty`$ last at fixed $`g'`$); it is not analytic in $`g'`$, because its range $`r\gg\ell_b\propto1/\lvert g'\rvert`$ recedes as $`g'\to0`$. Sign: for $`\varsigma=-1`$ the integrand of (8.18) is positive, so the cost is negative at every $`r`$. For equal $`\ell_b`$ the integrand is $`u^2/(u^2+\beta^2)`$, which decreases in $`\beta`$, so the cost rises monotonically to zero: attractive at every $`r`$. For $`\varsigma=+1`$ it is attractive for $`r\ll\ell_b`$ and repulsive for $`r\gg\ell_b`$; for equal $`\ell_b`$, (8.18) changes sign at $`\beta_0=1.698`$, i.e. $`r_0=0.849\,\ell_b`$ (computed). No term of R1 is linear in $`q^{(\alpha)}`$: the lowest eigenvector can be taken as an eigenvector of the conserved $`\mathbf n\cdot\mathbf S_{\rm tot}`$, and in it $`\langle S^\alpha_b\rangle=0`$. So there is no $`1/r`$ part.

(iii) *Lattice check* (`code/v3/output/spinwave_mutual.txt`, block (3)). Settings: equal spins with $`{\rm sgn}\,\sigma_1={\rm sgn}\,\sigma_2`$, so $`\varsigma=(-1)^r`$; $`\lvert g'\rvert/J=0,0.2,0.5,2`$, i.e. $`\ell_b=\infty,17.3,6.93,1.73`$; tori $`L=32,64,128,256`$; $`r=2,\dots,12`$. The code evaluates the formula of (ii) with the exact lattice propagators $`G_{12}(\nu)`$ and compares it with the continuum including the off-diagonal part. The ratios, extrapolated from $`L=64,128,256`$, lie between $`1.01`$ and $`1.05`$ at $`r=6,\dots,12`$ for all four values. The exceptions are $`1.07`$ and $`0.94`$ at $`r=6,8`$ for $`\lvert g'\rvert/J=0.5`$, next to the change of sign at $`r_0=5.9`$. On $`L=256`$ the ratio at $`r=9,11`$ is $`1.008,0.999`$ ($`\lvert g'\rvert/J=0.2`$), $`1.015,1.006`$ ($`0.5`$) and $`1.025,1.012`$ ($`2`$). The value $`\lvert g'\rvert/J=0.2`$ tests the regime $`r\lesssim\ell_b`$ ($`\beta\le1.39`$) with its term of order $`r/\ell_b`$. The value $`\lvert g'\rvert/J=2`$ (where $`\beta=1.15r`$, outside the condition $`\lvert g'\rvert\ll J`$, as a test of the formula only) tests the decay $`r^{-5}`$ and the sign of the limit $`r\gg\ell_b`$. Without the off-diagonal part the ratios at even $`r`$ are off, e.g. $`1.74`$ at $`r=12`$ for $`\lvert g'\rvert/J=0.2`$, near the zero of $`\mathcal F_{12}`$, and $`0.92`$ for $`\lvert g'\rvert/J=2`$, as stated in (ii). At $`\lvert g'\rvert=0`$ the frequency-domain code reproduces the time-domain along-$`\mathbf n`$ values to $`1.3\times10^{-4}`$.


### Step 13. Without a push (item 3(c), short argument)

*Direction sources* (cubic torus, order $`L\to\infty`$ first, $`\lvert g_i\rvert\ll JS`$). Let $`\mathbf h_i:=c_ig_i\epsilon_{x_i}\mathbf m_i`$ ($`c_i=1`$ single object, $`2`$ cell), $`\mathbf h_{\rm eff}=\mathbf h_1+\mathbf h_2`$, and let $`\hat{\mathbf n}`$ be the orientation far from the sources (Step 3 with $`\mathbf n\to\hat{\mathbf n}`$, no push; $`\perp`$ is now relative to $`\hat{\mathbf n}`$). At fixed $`\hat{\mathbf n}`$ the along parts of the sources are anchors $`a_i=-\mathbf h_i\cdot\hat{\mathbf n}`$, which change the response by relative $`O(g/(JS))`$. The transverse parts are linear sources $`\sqrt S\,g_i\epsilon_{x_i}\mathbf m_i^\perp`$ on each object of source $`i`$. The deviations vanish far away, and the shift of Step 6 with $`(JS\Delta)^+`$ ($`\hat g_L\to\hat g_\infty`$) gives the cost of the orientation

```math
E(\hat{\mathbf n})=S\,\hat{\mathbf n}\cdot\mathbf h_{\rm eff}-\frac1{2J}\sum_{i,j=1,2}w_{ij}\,\mathbf h_i^\perp\cdot\mathbf h_j^\perp\,\bigl[1+O(g/(JS))\bigr],\qquad w_{ij}=\frac1{c_ic_j}\sum_{a\in i,\,b\in j}\hat g_\infty(a-b),
```

with $`w_{ii}=\gamma_3`$ for a single object and $`w_{12}=\frac1{4\pi r}+O(r^{-3})`$ (Step 8). The lowest eigenvector takes the minimizing $`\hat{\mathbf n}`$ (the sources pin the zero modes as the push does in (8.6); rotor levels of order $`J/N`$ aside). By the envelope theorem the $`r`$-dependence of the minimum is $`\partial E/\partial w_{12}`$ at fixed $`\hat{\mathbf n}`$, so the separation part is $`-\mathbf h_1^\perp\cdot\mathbf h_2^\perp/(4\pi Jr)`$ at the minimizing $`\hat{\mathbf n}`$. This is the form of (8.14), where the push fixes $`\hat{\mathbf n}=\mathbf n`$.

(α) *Non-cancelling sources,* $`SJ\lvert\mathbf h_{\rm eff}\rvert\gg\gamma_3\lvert\mathbf h_i\rvert^2`$. The first term dominates: the minimum lies within an angle $`O(\gamma_3\lvert\mathbf h_i\rvert^2/(SJ\lvert\mathbf h_{\rm eff}\rvert))`$ of $`-\hat{\mathbf h}_{\rm eff}`$, where $`\mathbf h_1^\perp=-\mathbf h_2^\perp`$. The quadratic form there is positive by (5.6) with $`\alpha_i\to a_i`$, $`\kappa_h\to JS`$. Indeed $`a_1+a_2=\lvert\mathbf h_{\rm eff}\rvert>0`$, and $`a_1a_2+\lvert\mathbf h_{\rm eff}\rvert/r_{12}>0`$ because $`\lvert a_1a_2\rvert r_{12}\le2\gamma_3\lvert\mathbf h_1\rvert\lvert\mathbf h_2\rvert/(JS)`$ (single objects, $`r_{12}=2[\gamma_3-\hat g(\mathbf r)]/(JS)`$). The separation part is $`+\lvert\mathbf h_1^\perp\rvert^2/(4\pi Jr)`$: repulsive.

(β) *Parallel* $`\mathbf m_1\parallel\mathbf m_2`$, every ratio of the strengths: $`\mathbf h_i=h_i\mathbf m`$, $`H:=\lvert h_1+h_2\rvert`$, $`u:=\lvert\hat{\mathbf n}\cdot\mathbf m\rvert`$. Then $`E=-SHu-\frac Q{2J}(1-u^2)`$ with $`Q=w_{11}h_1^2+w_{22}h_2^2+2w_{12}h_1h_2>0`$, minimal at $`u^*=\min(1,SJH/Q)`$; define $`H_c:=Q/(SJ)`$. For $`H\ge H_c`$ the orientation is $`-\hat{\mathbf h}_{\rm eff}`$, there is no $`1/r`$ part, and (8.16) applies. For $`H<H_c`$ it cants: it lies on the cone $`u=u^*`$ about $`\mathbf m`$ and is fixed only up to rotations about $`\mathbf m`$. At $`u=1`$, (5.6) reads $`H/r_{12}+h_1h_2>0`$, i.e. $`H>H_c`$ up to relative $`O(g/(JS))`$, so the canted range is exactly the range in which $`-\hat{\mathbf h}_{\rm eff}`$ is unstable. $`H<H_c`$ needs $`h_1h_2<0`$: for $`h_1h_2>0`$, $`H_c\le\gamma_3H^2/(SJ)\ll H`$. So

```math
\text{no push:}\quad \mathcal E_{12}\big|_{\mathbf r}=-\frac{\mathbf h_1^\perp\cdot\mathbf h_2^\perp}{4\pi Jr}\Big|_{\hat{\mathbf n}=\arg\min E};\quad\text{(α): }+\frac{\lvert\mathbf h_1^\perp\rvert^2}{4\pi Jr};\quad\text{(β): }-\frac{h_1h_2\,(1-u^{*2})}{4\pi Jr},\ u^*=\min\Bigl(1,\frac{SJH}Q\Bigr);\quad\text{relation sources fix no orientation.}\qquad\text{(8.19)}
```

In (β) the separation part is repulsive for $`H<H_c`$, equals $`+h_1^2/(4\pi Jr)`$ at $`\mathbf h_{\rm eff}=0`$, and vanishes for $`H\ge H_c`$. For non-parallel $`\mathbf m_i`$ near cancellation the minimization of $`E`$ is not carried out.

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
- **(8.9)** Exact diagonalization ($`S=\frac12`$: rings $`L\le20`$ and one cubic cluster of 16 objects; $`S=1`$: rings $`L\le12`$), with every sector of $`\sum_xS^3_x`$ searched, at the sampled $`h_p/J=0.01,0.1,0.3,1,3,10`$. The lowest eigenvector is unique and lies in $`M=0`$. At fixed size $`m_{\rm far}`$ is linear in $`h_p`$ at the two smallest strengths. On rings with $`h_p\ge J`$ it decreases with $`L`$ over the computed sizes (values in (8.9)). For $`S=\frac12`$ on the cubic torus the order $`L\to\infty`$, $`R\to\infty`$ is undecided at these sizes.
- **(8.10)** Under Assumption E, identification at leading order in $`1/S`$: two conjugate copies $`q^{(\alpha)}`$ with the 05-anchor matrix $`A=V_a`$, $`\kappa_h=JS`$, $`\kappa_a=h_p`$, $`g_s=\epsilon_{x_s}\sqrt Sg(\mathbf m\cdot\mathbf e_\alpha)`$, exact for all static results of the quadratic expansion; kinetic matrix $`EV_aE`$ instead of $`\mathbb 1`$. Separately, as an approximation for dynamics: in the lowest-derivative limit (wave numbers $`k\ll1`$) two independent copies of the 05-anchor field with $`\kappa_h=2zJ^2S^2`$, $`\kappa_a=2zJSh_p`$, $`g_s=\epsilon_{x_s}S\sqrt{2zJ}g(\mathbf m\cdot\mathbf e_\alpha)`$. Beyond it the push adds a mixed term $`-h_p\epsilon_h(q_1p_2-q_2p_1)_h`$ that couples the copies, smaller than the anchor by $`2\nu/T_0`$ (relative order $`k`$), and a kinetic term smaller by $`\nu^2/T_0^2`$, with $`T_0=2zJS`$.
- **(8.11)** Under Assumption E, conditions of (8.10): $`\Delta S_3\ll S`$, $`Nh_pS\gg zJ`$, $`\lvert g\rvert\ll h_p`$, $`\lvert g\rvert\ll JS`$; on the ring also $`\frac1\pi\ln d\ll S`$ and $`\lvert g\rvert d\ll JS`$ at the distances used.
- **(8.12)** Under (8.10), (8.11) and Assumption E: (5.3) with the anchor, (5.8), (5.10), (5.11), (5.14), (5.15) hold, and "$`-\infty`$" becomes a finite rotation; the uniform shift of (5.11) is the small-angle form of a bounded rotation; at the next order in $`1/S`$ the coefficients change by relative $`O(1/S)`$. Exact (A1, (8.1)): the outcome "no lowest eigenvector" of (5.3)–(5.6) fails, because a lowest eigenvector exists.
- **(8.13)** Under Assumption E, transverse direction sources, order $`g_1g_2`$, leading order in $`1/S`$, every $`L`$, both graphs: $`\mathcal E^\perp_{12}=-S\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)G_a(x_1,x_2)`$.
- **(8.14)** Under Assumption E, cubic torus, order $`L\to\infty`$, distances to $`h\to\infty`$, then $`r\to\infty`$: separation part $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1^\perp\cdot\mathbf m_2^\perp)c_{\rm cell}/(4\pi J r)`$, with $`c_{\rm cell}=c_1c_2`$, where $`c_i=1`$ for a single object and $`2`$ for a two-object cell (so $`1`$, $`2`$ or $`4`$), $`r`$ the midpoint separation, remainder $`O(r^{-3})`$; long range, order $`S^0`$; it vanishes for a source at $`h`$ or for $`\mathbf m_1^\perp\cdot\mathbf m_2^\perp=0`$.
- **(8.16)** Under Assumption E, along-$`\mathbf n`$ direction sources: $`-\epsilon_{x_1}\epsilon_{x_2}g_1g_2(\mathbf m_1\cdot\mathbf n)(\mathbf m_2\cdot\mathbf n)c_{\rm cell}\kappa_\parallel/(JSr^3)[1+O(r^{-2})]`$ ($`r`$ the midpoint separation), $`c_{\rm cell}=c_1c_2`$ as in (8.14), $`\kappa_\parallel=\sqrt3/(16\pi^3)`$, order $`g_1g_2/(JS)`$; no long-range mark.
- **(8.17)** Under Assumption E, R2, separation along an axis: $`-\frac{\sqrt3}{8\pi^3}\frac{\delta_1\delta_2S}{Jr^7}a`$, order $`\delta_1\delta_2S/J`$. Here $`a=\frac{43}6+\frac52\epsilon_1\epsilon_2`$ for both links $`\parallel\mathbf r`$, $`\frac43-\frac5{12}\epsilon_1\epsilon_2`$ for both $`\perp\mathbf r`$ and parallel to each other, $`\frac1{12}`$ for both $`\perp\mathbf r`$ and $`\perp`$ each other, and $`-\frac12`$ for one link $`\parallel\mathbf r`$ and one $`\perp\mathbf r`$. For $`\delta_1\delta_2>0`$ the cost is attractive in the first three cases and repulsive in the last. No pair of orientations has a vanishing coefficient. The remainder is relative $`O(r^{-2})`$ at the midpoint separation, and $`O(r^{-1})`$ for the last two cases if the axis value is used. No long-range mark.
- **(8.18)** Under Assumption E, R1, cubic torus, order of item 3, at leading order in $`1/S`$, $`\lvert g'_i\rvert/J`$ and $`\lvert g'_i\rvert s_{b_i}/(JS)`$ (no other condition on $`s_b`$): $`\mathcal E^{R1}_{12}=-\frac{\lvert g'_1g'_2\rvert\kappa_\parallel}{JSr^3}\mathcal F_{12}`$, with $`\mathcal F_{12}`$ the integral of (8.18) in $`\beta_i=2r/\ell_{b_i}`$, $`\ell_b=\sqrt{2z}J/\lvert g'\rvert`$, $`\sigma_i=-s_{b_i}{\rm sgn}\,g'_i`$, and relative remainder $`O(r^{-2})`$. For $`1\ll r\ll\ell_b`$ it is $`-\lvert g'_1g'_2\rvert s_{b_1}s_{b_2}\kappa_\parallel/(JSr^3)[1+O(r/\ell_b)]`$, of order $`g'_1g'_2`$, with the term of order $`r/\ell_b`$ given in Step 12. For $`r\gg\ell_b`$, the law for $`r\to\infty`$ last, it is $`\frac{3\sqrt3}{8\pi^3}\frac JS\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}r^{-5}[1+O(\ell_b^2/r^2)]`$, of order $`g'^0`$. Sign: for $`\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}<0`$ it is negative at every $`r`$, and for equal $`\ell_b`$ attractive at every $`r`$ (rising monotonically to zero). For $`\sigma_1\sigma_2\epsilon_{x_1}\epsilon_{x_2}>0`$ it is attractive for $`r\ll\ell_b`$ and repulsive for $`r\gg\ell_b`$, changing sign at $`r_0=0.849\,\ell_b`$ for equal $`\ell_b`$. No long-range mark (no $`1/r`$ part).
- **(8.19)** Without a push. Under Assumption E, cubic torus, order $`L\to\infty`$ first, $`\lvert g_i\rvert\ll JS`$, with $`\mathbf h_i=c_ig_i\epsilon_{x_i}\mathbf m_i`$: the orientation $`\hat{\mathbf n}`$ minimizes $`E(\hat{\mathbf n})`$ of Step 13, and the separation part of the mutual cost is $`-\mathbf h_1^\perp\cdot\mathbf h_2^\perp/(4\pi Jr)`$ at that $`\hat{\mathbf n}`$. For non-cancelling sources, $`SJ\lvert\mathbf h_{\rm eff}\rvert\gg\gamma_3\lvert\mathbf h_i\rvert^2`$, the orientation is $`-\hat{\mathbf h}_{\rm eff}`$ up to an angle $`O(\gamma_3\lvert\mathbf h_i\rvert^2/(SJ\lvert\mathbf h_{\rm eff}\rvert))`$, and the part is $`+\lvert\mathbf h_1^\perp\rvert^2/(4\pi Jr)`$ at leading order in that angle (repulsive). For $`\mathbf m_1\parallel\mathbf m_2`$ it is $`-h_1h_2(1-u^{*2})/(4\pi Jr)`$ with $`u^*=\min(1,SJH/Q)`$. This vanishes for $`H\ge H_c=Q/(SJ)`$, where the orientation is $`-\hat{\mathbf h}_{\rm eff}`$ and (8.16) applies. For $`H<H_c`$, which needs $`h_1h_2<0`$, it is repulsive; the orientation cants and is fixed only up to rotations about $`\mathbf m`$, and the part equals $`+h_1^2/(4\pi Jr)`$ at $`\mathbf h_{\rm eff}=0`$. (8.17) and (8.18) are unchanged as $`L\to\infty`$. Exact (Lieb–Mattis): relation sources fix no orientation; the lowest eigenvalue is a multiplet of total spin $`\lvert\sum_i\epsilon_{x_i}\sigma_i\rvert`$, a unique singlet with $`\langle\mathbf S_x\rangle=0`$ when this is $`0`$, always for R2.

Controls: for (8.7) the ring (8.8), the order (8.4) and $`J<0`$ (8.3); for the long range of (8.14) the along-$`\mathbf n`$ sources (8.16), the relation sources (8.17), (8.18), and parallel sources without push with $`H\ge H_c`$ (8.19).

## Consistency checks

1. **$`S\to\infty`$ of item 1(b).** (8.7) gives $`m/S\to1`$: the product state with the staggered orientation $`\epsilon_x\mathbf n`$; for $`J<0`$ the product state (8.3) is exact at every $`S`$. Passed.
2. **Identification against (5.15).** With $`\kappa_h=JS`$, $`g_s^2=Sg^2`$ the coefficient $`g_{s1}g_{s2}/(4\pi\kappa_h)=g_1g_2/(4\pi J)`$ of (5.15) equals the lattice limit: $`4\pi r\hat g_\infty(r)\to1`$ (Step 8). In (8.17), the sum of the vertex over the three link directions is $`T_0[(\nabla\chi)^2+(\partial_{t'}\chi)^2]`$, the energy density of the copy (a uniform change of $`J`$), as it must be. Passed.
3. **Dimensions.** $`\mathcal E^\perp\sim g^2/J`$, $`\mathcal E^\parallel\sim g^2/(JS)`$, $`\mathcal E^{R1}\sim J/S`$ or $`g'^2/(JS)`$, $`\mathcal E^{R2}\sim\delta^2S/J`$: energies, and each scales as (vertex)$`^2`$/(level spacing $`JS`$). Passed.

## Open issues

- For $`S=\frac12`$ on the cubic torus the persistence of the orientation (order $`L\to\infty`$, $`R\to\infty`$) is undecided: one cluster of 16 objects.
- On the ring the methods used here do not decide $`m(x)`$ far from the push; exact diagonalization only shows a decrease with $`L`$ for $`L\le20`$.
- The next order in $`1/S`$ of (8.13)–(8.18) is not computed; that the $`1/r`$ law of (8.14) survives at all orders is not proven.
- The corrections near the push to (8.16)–(8.18) are not computed. (8.17) is classified only for separations along an axis; for other directions it is the stated integral.
- Without a push, the minimum of $`E(\hat{\mathbf n})`$ (Step 13) for non-parallel $`\mathbf m_i`$ near cancellation is not computed.
- The rotor regime $`Nh_pS\sim zJ`$ between the two orders of item 1(b) is not computed.

## Code

- `code/v3/ed_push.py` (check): exact diagonalization of $`C_{\rm ex}-h_pS^3_h`$, $`J=1`$, in every sector $`\sum_xS^3_x=-NS,\dots,NS`$ (two lowest eigenvalues per sector); $`S=\frac12`$ rings $`L=8,12,16,20`$ and the 16-object cubic cluster (links listed in the output), $`S=1`$ rings $`L=6,8,10,12`$; at $`h_p=0`$ and $`h_p/J=0.01,0.1,0.3,1,3,10`$: sector, energy and uniqueness (gap to the next level over all sectors) of the lowest eigenvector, $`m`$ at the far places and at $`h`$. Output `code/v3/output/ed_push.txt`.
- `code/v3/spinwave_tilt.py` (check, unchanged from v2): leading order in $`1/S`$; $`\Delta S_3`$ by midpoint sums ($`L=64,128,256`$, Richardson); exact Gaussian $`\Delta S`$ at the far place with the push on cubic tori $`L=8,12,16`$ for $`\eta=0.1,1,10`$, with the zero-mode estimate; rings $`L=64,\dots,1024`$ for (8.8). Output `code/v3/output/spinwave_tilt.txt`.
- `code/v3/spinwave_mutual.py` (check): (5.8) with (8.10) against a direct inverse; transverse separation parts from $`\hat g_\infty`$ (Bessel integral) and on tori $`L=16,32,64`$, including a single object against a cell (midpoint against end point); continuum coefficients of (8.16), of the limit $`r\gg\ell_b`$ of (8.18) and of (8.17) for four orientation pairs (closed forms against the numerical $`\tau'`$-integral); (8.15) on tori $`L=32,64,128`$ for along-$`\mathbf n`$ sources (single objects, cells) and R2 in four orientation pairs (continuum at the midpoint separation), $`r=2,\dots,12`$, with the extrapolation $`L\to\infty`$; R1: the function $`\mathcal F`$ of (8.18) with its two limits and its change of sign; the lattice evaluation with the retarded vertex in the frequency domain (propagators at $`(r,0,0)`$ by summing over $`(k_2,k_3)`$ for each $`k_1`$) for $`\lvert g'\rvert/J=0,0.2,0.5,2`$ on tori $`L=32,64,128,256`$, against (8.18) without and with the off-diagonal part, with the extrapolation from $`L=64,128,256`$, and a cross-check of the frequency against the time domain. Output `code/v3/output/spinwave_mutual.txt`.

## Methods used

- Marshall–Lieb–Mattis and Lieb–Mattis theorems; Perron–Frobenius; analytic perturbation theory
- Holstein–Primakoff representation and expansion in $`1/S`$; quadratic forms, normal modes, Gaussian lowest eigenvectors
- Lattice Green functions on tori and their asymptotics; Wick's theorem; imaginary-time second-order perturbation theory
- Elimination of a held spin at second order (retarded vertex, imaginary frequency); dimension counting of local vertices
- Cost of the orientation as a collective coordinate; envelope theorem; positivity of a Kron-reduced form
- Exact diagonalization (Lanczos) in all sectors of $`\sum_xS^3_x`$; Perron–Frobenius per sector
