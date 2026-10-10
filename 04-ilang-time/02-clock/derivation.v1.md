# Clock parts: self-driven evolution, ticking, ring clock, reading and resolution

- **Subproject:** 04-ilang-time
- **Package:** 02-clock
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-09

## Setup and assumptions

The setting and the definitions are those of question.md: a clock part $`K`$ with companion $`R\neq\emptyset`$, $`C=C_K\otimes\mathbb 1_R+\mathbb 1_K\otimes C_R+C_\partial`$ with $`C_\partial=\sum_nA_n\otimes B_n`$, readings on $`K`$ with $`p(r;\lambda)=\mathrm{Tr}(\Pi_rV_K(\lambda))`$, and the notions self-driven, ticking, index, clock, uniform ring clock, $`L_K`$, $`\Delta C_K`$. There are no inputs from other packages.

- **S1.** $`\mathcal H`$ is finite-dimensional (A1) and the contracts do not depend on $`\lambda`$ (A5). The evolution keeps states admissible (A3, A6), so $`C`$ maps $`\mathcal H_{\rm adm}`$ into itself. "Every start" means every unit vector of $`\mathcal H_{\rm adm}`$ at $`\lambda=0`$. If no two objects have the same type, then $`\mathcal H_{\rm adm}=\mathcal H`$ by (1.11).
- **S2.** Items 1–3 and 5 use (1.9) without readings. In item 4 a place reading with outcome $`m`$ is applied at a stated $`\lambda`$ through (1.3) with projector $`\Pi_m\otimes\mathbb 1_R`$ (A4, A8), and (1.9) holds between readings. We assume the state after a reading is admissible, so that the self-driven property applies to it. This holds when no object of $`R`$ has the type of $`k`$; otherwise $`\Pi_m\otimes\mathbb 1_R`$ would violate (1.11).
- **Notation.** $`V_0:=V_K(0)`$. The imaginary unit is $`i`$, so the spectral index of $`C_K`$ is written $`j,l`$: $`C_K=\sum_jE_jP_j`$. For ring clocks we write $`x:=\lambda/\lambda_0`$, the shift $`S\lvert m\rangle=\lvert m+1\rangle`$, and the Fourier vectors $`\lvert f_k\rangle=N^{-1/2}\sum_{m\in\mathbb Z_N}e^{2\pi ikm/N}\lvert m\rangle`$ with $`S\lvert f_k\rangle=e^{-2\pi ik/N}\lvert f_k\rangle`$, $`k\in\mathbb Z_N`$.
- **Partial trace (standard).** $`\mathrm{Tr}_R[(Y\otimes\mathbb 1)X]=Y\mathrm{Tr}_RX`$, $`\mathrm{Tr}_R[X(Y\otimes\mathbb 1)]=(\mathrm{Tr}_RX)Y`$, $`\mathrm{Tr}_R[(\mathbb 1\otimes W)X]=\mathrm{Tr}_R[X(\mathbb 1\otimes W)]`$.
- **Units.** By (1.9), $`C\lambda`$ is dimensionless, so $`C_K`$, $`E_j`$ and $`\Delta C_K`$ carry the units of $`1/\lambda`$.

## Derivation

### Step 1. Self-driven parts (item 1)

Let $`\rho(\lambda)=\lvert\Psi(\lambda)\rangle\langle\Psi(\lambda)\rvert`$. By (1.9), $`\dot\rho=-i[C,\rho]`$. The partial-trace rules give $`\mathrm{Tr}_R[\mathbb 1\otimes C_R,\rho]=0`$ and $`\mathrm{Tr}_R[C_K\otimes\mathbb 1,\rho]=[C_K,V_K]`$, hence
```math
\frac{\mathrm dV_K}{\mathrm d\lambda}=-i[C_K,V_K]-i\mathrm{Tr}_R[C_\partial,\rho(\lambda)] .
```

**Sufficient condition.** Suppose the cross terms act on $`K`$ as the identity:
```math
C_\partial=\mathbb 1_K\otimes B,\qquad B=B^\dagger\ \text{on}\ \mathcal H_R\quad(\text{in particular } C_\partial=0).
\qquad\text{(2.1)}
```
Then $`\mathrm{Tr}_R[C_\partial,\rho]=0`$ for every $`\rho`$, so $`\dot V_K=-i[C_K,V_K]`$. The unique solution of this linear equation is $`e^{-iC_K\lambda}V_0e^{iC_K\lambda}`$. Condition (2.1) does not depend on the pair term in which a single-object term of $`R`$ is booked (A5, M6). Shifting $`C_K\to C_K+c\mathbb 1`$ does not change self-drivenness.

**General criterion.** $`K`$ is self-driven if and only if
```math
\mathrm{Tr}_R[C_\partial,X]=0\quad\text{for every operator } X \text{ on } \mathcal H_{\rm adm}.
\qquad\text{(2.2)}
```
*Sufficiency.* $`\rho(\lambda)`$ stays on $`\mathcal H_{\rm adm}`$ (S1), and the argument above applies. *Necessity.* Differentiating the self-driven identity at $`\lambda=0`$ gives $`\mathrm{Tr}_R[C_\partial,\lvert\Psi\rangle\langle\Psi\rvert]=0`$ for every admissible unit $`\Psi`$. By polarization, the operators $`\lvert\Psi\rangle\langle\Psi\rvert`$ span all operators on $`\mathcal H_{\rm adm}`$.

**(2.1) is necessary when $`\mathcal H_{\rm adm}=\mathcal H`$.** Expand $`C_\partial=\mathbb 1_K\otimes G_0+\sum_{\alpha\ge1}F_\alpha\otimes G_\alpha`$, where the $`F_\alpha`$ form a basis of the traceless operators on $`\mathcal H_K`$. For $`X=Y\otimes Z`$, (2.2) reads $`\bigl[\mathrm{Tr}(G_0Z)\mathbb 1+\sum_\alpha\mathrm{Tr}(G_\alpha Z)F_\alpha,\;Y\bigr]=0`$ for all $`Y`$. The bracketed operator must therefore be a multiple of $`\mathbb 1`$, so $`\mathrm{Tr}(G_\alpha Z)=0`$ for all $`Z`$, i.e. $`G_\alpha=0`$. This gives (2.1) with $`B=G_0`$, which is self-adjoint because $`C_\partial`$ is.

**(2.1) is not necessary in general.** Take objects $`1\in K`$ and $`2\in R`$ of the same type $`T`$, with $`d_T\ge2`$ and either family $`c_T`$, and a single contract
```math
C=D\otimes\mathbb 1+\mathbb 1\otimes D+g\,P_{12},\qquad D=D^\dagger,\quad g\neq0,
\qquad\text{(2.3)}
```
with the single-object terms booked into it (A5), so that $`C_K=C_R=D`$ and $`C_\partial=gP_{12}`$. $`C`$ commutes with $`P_{12}`$, and $`P_{12}=c_T`$ on $`\mathcal H_{\rm adm}`$. Hence $`[C_\partial,X]=0`$ for every $`X`$ on $`\mathcal H_{\rm adm}`$, (2.2) holds, and $`K`$ is self-driven: $`e^{-iC\lambda}\Psi=e^{-igc_T\lambda}(e^{-iD\lambda}\otimes e^{-iD\lambda})\Psi`$. Yet $`\mathrm{Tr}_2[P_{12},Y\otimes Z]=[Z,Y]\neq0`$ for non-commuting $`Y,Z`$, so $`gP_{12}\neq\mathbb 1\otimes B`$. On admissible states the views of $`\{1\}`$ and $`\{2\}`$ coincide, so the view of $`K`$ does not depend on the labels (M6).

**Dependence on $`R`$.** For a self-driven $`K`$,
```math
p(r;\lambda)=\mathrm{Tr}\bigl(\Pi_r\,e^{-iC_K\lambda}V_0\,e^{iC_K\lambda}\bigr),
\qquad\text{(2.4)}
```
so the statistics depend on the state of $`R`$ only through $`V_0`$: **no** further dependence. Sequences of readings are treated in Step 6.

### Step 2. Statistics and ticking (item 2a)

Insert $`e^{-iC_K\lambda}=\sum_je^{-iE_j\lambda}P_j`$ into (2.4):
```math
V_K(\lambda)=\sum_{j,l}e^{-i(E_j-E_l)\lambda}P_jV_0P_l,\qquad
p(r;\lambda)=\sum_{j,l}e^{-i(E_j-E_l)\lambda}\mathrm{Tr}\bigl(\Pi_rP_jV_0P_l\bigr).
\qquad\text{(2.5)}
```
Group the terms by gap: $`V_\omega:=\sum_{E_j-E_l=\omega}P_jV_0P_l`$, so that $`p(r;\lambda)=\sum_\omega e^{-i\omega\lambda}\mathrm{Tr}(\Pi_rV_\omega)`$. The functions $`e^{-i\omega\lambda}`$ with distinct $`\omega`$ are linearly independent on $`\mathbb R`$, so $`p(r;\cdot)`$ is constant if and only if $`\mathrm{Tr}(\Pi_rV_\omega)=0`$ for every $`\omega\neq0`$. Every $`\Pi_r`$ is a sum of place projectors $`\lvert m\rangle\langle m\rvert`$, $`m\in S_r`$, and the place reading is itself a reading. Hence
```math
\text{some reading on } K \text{ ticks}\iff \exists\,m,\ \exists\,\omega\neq0:\ \sum_{E_j-E_l=\omega}\langle m\vert P_jV_0P_l\vert m\rangle\neq0 ,
\qquad\text{(2.6)}
```
and in that case the place reading ticks. Two conditions each exclude ticking: $`[C_K,V_0]=0`$, which gives $`V_\omega=0`$ for $`\omega\neq0`$; and $`C_K`$ diagonal in the place basis, since then each $`\lvert m\rangle`$ lies in one eigenspace and $`\langle m\vert P_jV_0P_l\vert m\rangle=0`$ for $`j\neq l`$.

### Step 3. Recurrences and index (item 2b)

Let $`\Omega:=\{E_j-E_l:\ P_jV_0P_l\neq0\}`$ be the set of active gaps. It satisfies $`\Omega=-\Omega`$ because $`(P_jV_0P_l)^\dagger=P_lV_0P_j`$. The blocks $`P_j(\cdot)P_l`$ in (2.5) are independent: multiply by $`P_j`$ on the left and by $`P_l`$ on the right. Hence
```math
\{\lambda':V_K(\lambda')=V_K(\lambda)\}=\lambda+\mathcal T,\qquad
\mathcal T:=\{s\in\mathbb R:\ \omega s\in2\pi\mathbb Z\ \ \forall\,\omega\in\Omega\}.
\qquad\text{(2.7)}
```
$`\mathcal T`$ is a closed subgroup of $`\mathbb R`$ and does not depend on $`\lambda`$. There are three cases.
- $`\Omega\subseteq\{0\}`$, equivalently $`[C_K,V_0]=0`$. Then $`\mathcal T=\mathbb R`$ and $`V_K`$ is constant.
- $`\Omega\neq\{0\}`$ and all nonzero gaps are pairwise commensurate. The group $`\mathbb Z\Omega`$ generated by $`\Omega`$ lies in a cyclic group $`(\omega_1/q)\mathbb Z`$, so it is cyclic: $`\mathbb Z\Omega=\omega_*\mathbb Z`$ with $`\omega_*>0`$. Since $`\omega_*`$ is an integer combination of gaps and every gap is a multiple of $`\omega_*`$, $`\mathcal T=\tau\mathbb Z`$ with $`\tau=2\pi/\omega_*`$.
- Some $`\omega_1,\omega_2\in\Omega\setminus\{0\}`$ have $`\omega_1/\omega_2\notin\mathbb Q`$. A nonzero $`s\in\mathcal T`$ would give $`\omega_1s=2\pi n_1`$ and $`\omega_2s=2\pi n_2`$ with $`n_2\neq0`$, so $`\omega_1/\omega_2=n_1/n_2`$, a contradiction. Hence $`\mathcal T=\{0\}`$.

The view is injective on $`\Lambda`$ if and only if $`(\Lambda-\Lambda)\cap\mathcal T=\{0\}`$. Therefore
```math
V_K \text{ indexes } \lambda \text{ on all of } \mathbb R\iff \Omega \text{ contains two nonzero gaps with irrational ratio}.
\qquad\text{(2.8)}
```
If instead $`\mathcal T=\tau\mathbb Z`$, the maximal indexing intervals are the half-open intervals $`[a,a+\tau)`$ and $`(a,a+\tau]`$, $`a\in\mathbb R`$: any longer interval, or a closed one of length $`\tau`$, contains two points a distance $`\tau`$ apart. If $`\mathcal T=\mathbb R`$, no interval of positive length is indexed.

### Step 4. Uniform ring clocks (item 3a)

Let $`U=e^{-iC_K\lambda_0}`$, so $`U\lvert m\rangle=e^{i\theta_m}\lvert m+1\rangle`$, and let $`\bar\theta:=N^{-1}\sum_m\theta_m`$. Set $`\alpha_0=0`$ and $`\alpha_{m+1}=\alpha_m+\theta_m-\bar\theta`$. Summing gives $`\alpha_{N-1}+\theta_{N-1}-\bar\theta=\alpha_0`$, so with $`\lvert\tilde m\rangle:=e^{i\alpha_m}\lvert m\rangle`$ we have $`U\lvert\tilde m\rangle=e^{i\bar\theta}\lvert\widetilde{m+1}\rangle`$ for every $`m\in\mathbb Z_N`$. The orthonormal vectors $`\lvert v_k\rangle=N^{-1/2}\sum_me^{2\pi ikm/N}e^{i\alpha_m}\lvert m\rangle`$ satisfy $`U\lvert v_k\rangle=e^{i\bar\theta}e^{-2\pi ik/N}\lvert v_k\rangle`$, so $`U`$ has $`N`$ distinct eigenvalues. $`C_K`$ commutes with $`U`$ and therefore leaves each one-dimensional eigenspace invariant: $`C_K=\sum_kE_k\lvert v_k\rangle\langle v_k\rvert`$ with $`e^{-iE_k\lambda_0}=e^{i\bar\theta-2\pi ik/N}`$.

Conversely, take any data of the form below. Using $`\lvert m\rangle=e^{-i\alpha_m}N^{-1/2}\sum_ke^{-2\pi ikm/N}\lvert v_k\rangle`$, a direct computation gives $`e^{-iC_K\lambda_0}\lvert m\rangle=e^{i(\alpha_{m+1}-\alpha_m-\varepsilon\lambda_0)}\lvert m+1\rangle`$. Hence $`K`$ is a uniform ring clock with tick $`\lambda_0`$ if and only if
```math
C_K=\sum_{k\in\mathbb Z_N}E_k\lvert v_k\rangle\langle v_k\rvert,\quad
\lvert v_k\rangle=\frac{1}{\sqrt N}\sum_{m}e^{2\pi ikm/N}e^{i\alpha_m}\lvert m\rangle,\quad
E_k=\varepsilon+\frac{2\pi\ell_k}{N\lambda_0},\quad \ell_k\in\mathbb Z,\ \ell_k\equiv k\ (\mathrm{mod}\ N),
\qquad\text{(2.9)}
```
where the $`\alpha_m`$ and $`\varepsilon`$ are arbitrary reals. The phases are then $`\theta_m=\alpha_{m+1}-\alpha_m-\varepsilon\lambda_0`$ (mod $`2\pi`$, with $`\alpha_N:=\alpha_0`$). If $`\theta_m=0`$ for all $`m`$, then $`e^{-iC_K\lambda_0}=S`$. The same argument applied to $`S`$, whose eigenvalues $`e^{-2\pi ik/N}`$ on $`\lvert f_k\rangle`$ are distinct, gives exactly $`C_K=\sum_k\frac{2\pi\ell_k}{N\lambda_0}\lvert f_k\rangle\langle f_k\rvert`$ with $`\ell_k\equiv k`$. This $`C_K`$ commutes with $`S`$.

### Step 5. Ring-clock statistics and cost spread (item 3b)

Start at $`\lvert0\rangle`$, i.e. $`V_0=\lvert0\rangle\langle0\rvert`$. Then $`V_K(\lambda)`$ is the projector onto $`e^{-iC_K\lambda}\lvert0\rangle`$ by (2.4). We use $`\lvert0\rangle=e^{-i\alpha_0}N^{-1/2}\sum_k\lvert v_k\rangle`$, $`\langle m\vert v_k\rangle=N^{-1/2}e^{2\pi ikm/N}e^{i\alpha_m}`$, and $`e^{2\pi ikm/N}=e^{2\pi i\ell_km/N}`$. This gives $`\langle m\vert e^{-iC_K\lambda}\vert0\rangle=e^{i(\alpha_m-\alpha_0)-i\varepsilon\lambda}G(m;\lambda)`$, and hence
```math
p(m;\lambda)=\lvert G(m;\lambda)\rvert^2,\qquad G(m;\lambda):=\frac1N\sum_{k\in\mathbb Z_N}e^{2\pi i\ell_k(m-\lambda/\lambda_0)/N}.
\qquad\text{(2.10)}
```
This depends only on the $`\ell_k`$, not on the $`\theta_m`$. At $`\lambda=j\lambda_0`$, $`p(m)=\delta_{m,\,j\bmod N}`$.

$`V_K(\lambda)`$ is conjugated by a function of $`C_K`$, so $`L_K`$ and $`\Delta C_K`$ do not depend on $`\lambda`$. The weights are $`\lvert\langle v_k\vert0\rangle\rvert^2=1/N`$, so
```math
\Delta C_K=\frac{2\pi}{N\lambda_0}\Bigl[\frac1N\sum_k\ell_k^2-\Bigl(\frac1N\sum_k\ell_k\Bigr)^2\Bigr]^{1/2}.
\qquad\text{(2.11)}
```
The $`\ell_k`$ are $`N`$ distinct integers, since they are distinct mod $`N`$. Sort them as $`\ell_{(1)}<\dots<\ell_{(N)}`$. Their variance is $`N^{-2}\sum_{a<b}(\ell_{(b)}-\ell_{(a)})^2\ge N^{-2}\sum_{a<b}(b-a)^2=(N^2-1)/12`$, with equality if and only if all consecutive gaps equal $`1`$. $`N`$ consecutive integers form a complete residue system mod $`N`$, so the equality case lies in the family:
```math
\min\Delta C_K=\frac{2\pi}{\lambda_0}\sqrt{\frac{N^2-1}{12N^2}},\quad\text{attained iff } \{\ell_k\}=\{c,c+1,\dots,c+N-1\},\ c\in\mathbb Z .
\qquad\text{(2.12)}
```
Equivalently, the spectrum of $`C_K`$ consists of $`N`$ levels equally spaced by $`2\pi/(N\lambda_0)`$. For these minimal members, (2.10) is a geometric sum whose modulus does not depend on $`c`$:
```math
p(m;\lambda)=\frac{\sin^2(\pi\lambda/\lambda_0)}{N^2\sin^2\bigl(\pi(\lambda/\lambda_0-m)/N\bigr)}\qquad(\text{value }1\text{ where the denominator vanishes}).
\qquad\text{(2.13)}
```
For a minimal member every pair of eigenvectors is active and the gaps generate $`(2\pi/(N\lambda_0))\mathbb Z`$. By (2.7)–(2.8), $`\tau=N\lambda_0`$: the view indexes $`\lambda`$ on half-open intervals of length $`N\lambda_0`$.

### Step 6. Reading the clock (item 4a)

A place reading with outcome $`m`$ acts by $`\Pi_m\otimes\mathbb 1_R`$ (1.3). The partial-trace rules give the new view
```math
V_K\ \longmapsto\ \frac{\Pi_mV_K\Pi_m}{\mathrm{Tr}(\Pi_mV_K)}=\lvert m\rangle\langle m\rvert .
\qquad\text{(2.14)}
```
By S2 and (2.4), the statistics of a sequence of readings on a self-driven $`K`$ are fixed by $`C_K`$ and $`V_0`$, and after outcome $`m`$ the clock restarts from $`\lvert m\rangle`$. For $`\theta_m=0`$, $`C_K`$ commutes with $`S`$ (Step 4), so $`\langle m'\vert e^{-iC_K\lambda}\vert m\rangle=G(m'-m;\lambda)`$ with $`G`$ from (2.10) and no phase prefactor. Write $`\Delta:=\lambda_2-\lambda_1`$. The joint distribution of the two outcomes is
```math
P(m_1,m_2)=p(m_1;\lambda_1)\,p(m_2-m_1;\Delta).
\qquad\text{(2.15)}
```
Without the first reading, $`p(m_2;\lambda_2)=\bigl\lvert\sum_{m_1}G(m_2-m_1;\Delta)G(m_1;\lambda_1)\bigr\rvert^2`$, because $`e^{-iC_K\lambda_2}=e^{-iC_K\Delta}e^{-iC_K\lambda_1}`$. With the first reading applied but not recorded,
```math
P_2(m_2)=\sum_{m_1}p(m_1;\lambda_1)\,p(m_2-m_1;\Delta),\qquad
p(m_2;\lambda_2)-P_2(m_2)=\sum_{m_1\neq m_1'}G(m_2-m_1;\Delta)G(m_1;\lambda_1)\,G(m_2-m_1';\Delta)^*G(m_1';\lambda_1)^* .
\qquad\text{(2.16)}
```
The unrecorded reading removes the interference terms. **When this matters.**
- *No change, for every member,* if $`\lambda_1\in\lambda_0\mathbb Z`$ or $`\Delta\in\lambda_0\mathbb Z`$. Then $`e^{-iC_K\lambda_1}`$ or $`e^{-iC_K\Delta}`$ is a power of $`S`$, so $`G(\cdot;\lambda_1)`$ or $`G(\cdot;\Delta)`$ is a Kronecker delta and only the terms with $`m_1=m_1'`$ survive.
- *Minimal member: no other case.* Shifting $`c`$ adds a constant to $`C_K`$, so take $`c=0`$, $`\ell_k=k`$. Write $`D(m):=p(m;\lambda_2)-P_2(m)=\langle m\vert U_\Delta V_{\rm off}U_\Delta^\dagger\vert m\rangle`$, where $`U_\Delta=e^{-iC_K\Delta}`$, $`V=\lvert\psi(\lambda_1)\rangle\langle\psi(\lambda_1)\rvert`$ and $`V_{\rm off}=V-\sum_m\Pi_mV\Pi_m`$. Let $`Z:=\sum_me^{2\pi im/N}\lvert m\rangle\langle m\rvert`$, so $`Z^{-1}\lvert f_k\rangle=\lvert f_{k-1}\rangle`$, and set $`x_1=\lambda_1/\lambda_0`$, $`x_\Delta=\Delta/\lambda_0`$. Then $`\hat D:=\sum_me^{-2\pi im/N}D(m)=\mathrm{Tr}(U_\Delta^\dagger Z^{-1}U_\Delta V_{\rm off})`$. Since $`E_k-E_{k-1}=2\pi/(N\lambda_0)`$ for $`k\ge1`$ and $`E_0-E_{N-1}=-2\pi(N-1)/(N\lambda_0)`$, we get $`U_\Delta^\dagger Z^{-1}U_\Delta=e^{-2\pi ix_\Delta/N}\bigl[Z^{-1}+(e^{2\pi ix_\Delta}-1)\lvert f_{N-1}\rangle\langle f_0\rvert\bigr]`$, and $`\mathrm{Tr}(Z^{-1}V_{\rm off})=0`$. With $`\psi(\lambda_1)=N^{-1/2}\sum_ke^{-2\pi ikx_1/N}\lvert f_k\rangle`$ we have $`\langle f_0\vert V\vert f_{N-1}\rangle=N^{-1}e^{2\pi ix_1}e^{-2\pi ix_1/N}`$, and $`\langle f_0\vert\sum_m\Pi_mV\Pi_m\vert f_{N-1}\rangle=N^{-1}\langle\psi\vert Z^{-1}\vert\psi\rangle=N^{-2}e^{-2\pi ix_1/N}(N-1+e^{2\pi ix_1})`$. Hence
```math
\hat D=\frac{N-1}{N^2}\,e^{-2\pi i(x_1+x_\Delta)/N}\,(e^{2\pi ix_1}-1)(e^{2\pi ix_\Delta}-1),\qquad
\lvert\hat D\rvert=\frac{4(N-1)}{N^2}\,\lvert\sin\pi x_1\,\sin\pi x_\Delta\rvert .
\qquad\text{(2.17)}
```
So for the minimal member the first reading changes the distribution of the second outcome **if and only if** $`\lambda_1\notin\lambda_0\mathbb Z`$ and $`\lambda_2-\lambda_1\notin\lambda_0\mathbb Z`$.

### Step 7. Frequent reading (item 4b)

By (2.14), each outcome $`0`$ restarts the clock at $`\lvert0\rangle`$. Given outcome $`0`$ at the previous reading (or the start at $`\lambda=0`$), outcome $`0`$ at the next reading has probability $`p(0;\lambda/n)=\lvert\langle0\vert e^{-iC_K\lambda/n}\vert0\rangle\rvert^2`$. Hence
```math
P_n=\Bigl\lvert\frac1N\sum_ke^{-2\pi i\ell_k\lambda/(nN\lambda_0)}\Bigr\rvert^{2n}
\ \overset{\text{min.}}{=}\ \Bigl[\frac{\sin^2(\pi\lambda/(n\lambda_0))}{N^2\sin^2(\pi\lambda/(nN\lambda_0))}\Bigr]^{n},
\qquad P_n=e^{-\lambda^2\Delta C_K^2/n+O(n^{-3})}\xrightarrow[n\to\infty]{}1 .
\qquad\text{(2.18)}
```
For the expansion: $`\lvert\langle0\vert e^{-iC_K\delta}\vert0\rangle\rvert^2=1-\delta^2\Delta C_K^2+O(\delta^4)`$, which is even in $`\delta`$, so $`n\ln p(0;\lambda/n)=-\lambda^2\Delta C_K^2/n+O(n^{-3})`$. Frequent reading freezes the clock at $`\lvert0\rangle`$ (Law 1).

### Step 8. Rate and orthogonality bound (item 5a)

Up to phases, $`\langle\psi(\lambda)\vert\psi(\lambda+s)\rangle=\langle\psi(\lambda)\vert e^{-iC_Ks}\vert\psi(\lambda)\rangle=1-is\langle C_K\rangle-\tfrac{s^2}{2}\langle C_K^2\rangle+\tfrac{is^3}{6}\langle C_K^3\rangle+O(s^4)`$. Therefore $`\cos^2\theta=1-s^2\Delta C_K^2+O(s^4)`$, where $`\Delta C_K`$ is computed from $`V_K(\lambda)`$ and does not depend on $`\lambda`$ (Step 5). Hence $`\sin^2\theta=s^2\Delta C_K^2+O(s^4)`$ and
```math
\lim_{\lambda'\to\lambda}\frac{\theta(\lambda,\lambda')}{\lvert\lambda'-\lambda\rvert}=\Delta C_K .
\qquad\text{(2.19)}
```
We use the standard fact that $`\theta`$ is the Fubini–Study distance on unit rays, which is a metric. Split $`[\lambda,\lambda']`$ into $`M`$ equal pieces. The triangle inequality and (2.19) give $`\theta(\lambda,\lambda')\le\Delta C_K\lvert\lambda'-\lambda\rvert+O(1/M)`$, because the remainder is uniform: $`\lvert\langle C_K^n\rangle\rvert\le\lVert C_K\rVert^n`$. Letting $`M\to\infty`$ and using $`\theta=\pi/2`$ at orthogonality:
```math
\theta(\lambda,\lambda')\le\Delta C_K\lvert\lambda'-\lambda\rvert,\qquad
\psi(\lambda')\perp\psi(\lambda)\ \Longrightarrow\ \lvert\lambda'-\lambda\rvert\ge\frac{\pi}{2\Delta C_K}.
\qquad\text{(2.20)}
```
This is the Mandelstam–Tamm inequality for the unitary group $`e^{-iC_K\lambda}`$. If $`\Delta C_K=0`$, $`\psi_0`$ is an eigenvector of $`C_K`$ and orthogonality never occurs.

### Step 9. Ring clock at the bound (item 5b)

Take $`\theta_m=0`$, the minimal member, and the start $`\lvert0\rangle`$. Then $`\langle\psi(0)\vert\psi(\lambda)\rangle=G(0;\lambda)=N^{-1}\sum_{j=0}^{N-1}e^{-2\pi i(c+j)x/N}`$. This vanishes if and only if $`e^{-2\pi ix}=1`$ and $`e^{-2\pi ix/N}\neq1`$, i.e. $`x\in\mathbb Z\setminus N\mathbb Z`$. The smallest such $`\lambda>0`$ is $`\lambda_\perp=\lambda_0`$ (for $`N\ge2`$). Inserting (2.12) into (2.20):
```math
\lambda_\perp=\lambda_0,\qquad \frac{\pi}{2\min\Delta C_K}=\frac{\sqrt3\,N\lambda_0}{2\sqrt{N^2-1}},\qquad
r_N:=\frac{\lambda_\perp}{\pi/(2\min\Delta C_K)}=\frac{2}{\sqrt3}\sqrt{1-\frac1{N^2}}\ \xrightarrow[N\to\infty]{}\ \frac{2}{\sqrt3}.
\qquad\text{(2.21)}
```
$`r_N`$ is strictly increasing in $`N`$ and $`r_2=1`$, so the bound is attained if and only if $`N=2`$.

## Result

- **(2.1)** Sufficient condition for a self-driven part: $`C_\partial=\mathbb 1_K\otimes B`$ (the cross terms act trivially on $`K`$).
- **(2.2)** Necessary and sufficient condition: $`\mathrm{Tr}_R[C_\partial,X]=0`$ for all $`X`$ on $`\mathcal H_{\rm adm}`$. It reduces to (2.1) when $`\mathcal H_{\rm adm}=\mathcal H`$, for example when no two objects share a type.
- **(2.3)** Counterexample to the necessity of (2.1): two identical-type objects coupled by a swap contract $`gP_{12}`$.
- **(2.4)** For a self-driven $`K`$, the statistics depend on $`R`$ only through $`V_K(0)`$.
- **(2.5)** Closed form of $`V_K(\lambda)`$ and $`p(r;\lambda)`$. **(2.6)** Ticking criterion: some active gap $`\omega\neq0`$ has a nonzero place-diagonal component.
- **(2.7)** The recurrence set is $`\lambda+\mathcal T`$, with period group $`\mathcal T`$ fixed by the active gaps $`\Omega`$. **(2.8)** The view indexes $`\lambda`$ on all of $`\mathbb R`$ if and only if $`\Omega`$ contains two nonzero gaps with irrational ratio. Otherwise the maximal indexing intervals are half-open of length $`\tau=2\pi/\omega_*`$.
- **(2.9)** All uniform ring clocks: phase-twisted Fourier eigenvectors with eigenvalues $`\varepsilon+2\pi\ell_k/(N\lambda_0)`$, $`\ell_k\equiv k`$ (mod $`N`$).
- **(2.10)** $`p(m;\lambda)`$ for every member. **(2.11)** $`\Delta C_K`$ over the family. **(2.12)** Its minimum, attained for equally spaced levels. **(2.13)** $`p(m;\lambda)`$ for minimal members.
- **(2.14)** A reading resets the view of $`K`$ to $`\lvert m\rangle\langle m\rvert`$. **(2.15)** Joint distribution of two readings. **(2.16)** The unrecorded first reading removes interference. **(2.17)** For the minimal member, the first reading changes the second distribution if and only if $`\lambda_1,\lambda_2-\lambda_1\notin\lambda_0\mathbb Z`$.
- **(2.18)** All-zero probability under $`n`$ readings, $`P_n\to1`$ (frequent reading stops the clock).
- **(2.19)** Angular rate $`=\Delta C_K`$. **(2.20)** Orthogonality needs $`\lvert\lambda'-\lambda\rvert\ge\pi/(2\Delta C_K)`$.
- **(2.21)** Ring clock: $`\lambda_\perp=\lambda_0`$, $`r_N=\frac{2}{\sqrt3}\sqrt{1-N^{-2}}\to2/\sqrt3`$, and the bound is attained only for $`N=2`$.

## Consistency checks

1. **Units and normalization.** $`\Delta C_K\propto1/\lambda_0`$ and the bound $`\propto\lambda_0`$, so $`r_N`$ is dimensionless. In (2.10), $`\sum_m p(m;\lambda)=1`$ because $`\sum_me^{2\pi i(\ell_k-\ell_{k'})m/N}=N\delta_{kk'}`$ (as $`\ell_k\equiv k`$). (2.15) sums to $`1`$, and $`\sum_mD(m)=0`$ in (2.16). Passed.
2. **$`N=2`$.** Take $`C_K=(\pi/\lambda_0)\lvert f_1\rangle\langle f_1\rvert`$. Directly, $`\langle0\vert\psi(\lambda)\rangle=(1+e^{-i\pi x})/2`$, so $`p(0;\lambda)=\cos^2(\pi x/2)`$, which agrees with (2.13). Also $`\Delta C_K=\pi/(2\lambda_0)`$, which agrees with (2.12). A direct computation gives $`D(0)=-\tfrac12\sin\pi x_1\sin\pi x_\Delta`$, which equals $`\hat D/2`$ from (2.17). Finally $`\lambda_\perp=\lambda_0=\pi/(2\Delta C_K)`$. Passed.
3. **Start commuting with $`C_K`$** ($`V_0=\lvert v_k\rangle\langle v_k\rvert`$ or $`\mathbb 1/d_K`$). Here $`\Omega\subseteq\{0\}`$: by (2.5)–(2.8), nothing ticks, $`\mathcal T=\mathbb R`$ and no interval is indexed. For $`\lvert v_k\rangle`$, $`\Delta C_K=0`$, and (2.20) correctly excludes orthogonality. Passed.

## Open issues

- The necessity of (2.1) is shown only for $`\mathcal H_{\rm adm}=\mathcal H`$. With identical-type objects on both sides of the cut, only (2.2) and the counterexample (2.3) are given; how such parts are specified without labels (A7, M6) is not treated.
- In item 4(a), the "only if" of (2.17) is proven for the minimal member only. Other members have additional no-change values of $`\Delta`$; for example, $`N=2`$ with $`\ell=(0,3)`$ gives $`e^{-iC_K\lambda_0/3}=S`$.
- Item 4 assumes that post-reading states are admissible, which holds when no object of $`R`$ has the type of $`k`$ (S2).
- Indexing on all of $`\mathbb R`$ in (2.8) is exact injectivity only; the quasi-periodic near-recurrences that limit a finite-resolution reading are not quantified.
- Out of scope: clock time versus other parts (criterion 2), comparison of clocks (criterion 3), readings represented by recording contracts (criterion 7), and clocks that are not self-driven.

## Methods used

- partial trace, Heisenberg-type equation for the view
- spectral decomposition, linear independence of exponentials
- closed subgroups of $`\mathbb R`$, commensurability
- circulant operators, discrete Fourier transform, geometric sums
- variance of distinct integers
- projective readings (1.3), interference and decoherence of the view
- Taylor expansion, frequent-reading (Zeno-type) limit
- Fubini–Study metric, Mandelstam–Tamm inequality
