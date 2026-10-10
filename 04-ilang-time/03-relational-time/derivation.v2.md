# Relational time: conditional states of a stationary global state relative to a ring clock

- **Subproject:** 04-ilang-time
- **Package:** 03-relational-time
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-10

## Changes from previous version

- Setup, Clock bullet: the minimal spread from (2.12) of 02-clock is now stated only for the localized clock start $`\lvert0\rangle`$ (I1).
- Setup, new bullet "Split of $`C`$" with the new tag (3.19). $`C_R`$ and $`C_\partial`$ are now defined from the total $`C`$ by a partial trace, so they do not depend on how terms are booked (I3). The invariance of $`\mathcal H_{R,\rm adm}`$ under $`C_R`$ is now shown for every $`C_\partial`$, not only for $`C_\partial=0`$.
- Step 3, (3.4) and Result item 1: the criterion now has the correct quantifier. A nonproduct joint place distribution means that *some* reading on $`R`$ depends on $`m`$. For a specified reading, the condition is on its class sums (I2).
- Step 7: in the split (3.19), (3.15) needs $`\sum_kB_k=0`$, which is no restriction. The example now has $`\sum_kn_k=0`$, and the object carrying $`P`$ has a type that occurs only once in $`R`$, so that $`C`$ keeps $`\mathcal H_{\rm adm}`$ invariant.
- Step 9: one sentence states that $`C_R`$ is the operator (3.19).
- All other steps, all tags (3.1)–(3.18) and their meanings are unchanged.

## Response to verification

- **I1:** Accepted and fixed in Setup, Clock bullet. Input (2.12) is stated for the start $`\lvert0\rangle`$. The text now says that this generator attains the minimum for that start, and it makes no claim for the clock views of the states used here. No step used the fact.
- **I2:** Accepted and fixed in Step 3 (display (3.4) and the text after it) and in Result item 1. For a specified partition $`\{S_r\}`$, $`p(\cdot\vert m)`$ depends on $`m`$ iff at least one class sum does. The one-class reading never does. A nonproduct joint place distribution is equivalent to the existence of *some* reading on $`R`$ with $`m`$-dependent statistics; the finest reading suffices. Example (3.5) is unchanged, since there the specified reading (the place reading of $`R`$) depends on $`m`$.
- **I3:** Accepted and fixed in Setup ("Split of $`C`$", (3.19)), Step 7 and Step 9. $`C_R:=N^{-1}\mathrm{Tr}_K(C-C_K\otimes\mathbb 1_R)`$ depends only on the total $`C`$ and the given $`C_K`$. Every $`R`$-only term enters $`C_R`$, whichever pair it is booked in, and (3.19) is the unique split with $`\mathrm{Tr}_KC_\partial=0`$. Steps 1–6 and 8 are unaffected: there $`C_\partial=0`$, or $`\mathrm{Tr}_KC_\partial=g\mathrm{Tr}(Z)\lvert0\rangle\langle0\rvert_R=0`$ in (3.16). Step 7 is adjusted as listed above.

## Setup and assumptions

- **Objects.** Clock object $`K`$ with places $`m\in\mathbb Z_N`$, $`N\ge2`$, and companion $`R\neq\emptyset`$, which contains no object of the clock's type. The swap conditions (1.11) therefore involve only pairs inside $`R`$, and $`\mathcal H_{\rm adm}=\mathcal H_K\otimes\mathcal H_{R,\rm adm}`$. The clock is the only object of its type, so $`K`$ is specified without labels (M6). All statistics below are invariant under the common phase (1.2).
- **Contracts.** $`C=C_K\otimes\mathbb 1_R+\mathbb 1_K\otimes C_R+C_\partial`$, $`C_\partial=\sum_nA_n\otimes B_n`$, all independent of $`\lambda`$ (A5), $`\lambda\in\mathbb R`$ (A9). By A3 the evolution (1.9) keeps $`\mathcal H_{\rm adm}`$ invariant, so $`C`$ maps $`\mathcal H_{\rm adm}`$ into itself.
- **Clock.** $`C_K=\frac{2\pi}{N\lambda_0}\sum_kk\lvert f_k\rangle\langle f_k\rvert`$. Input (2.9) of 02-clock@v2: "If $`\theta_m=0`$ for all $`m`$, then $`e^{-iC_K\lambda_0}=S`$", with $`C_K=\sum_k\frac{2\pi\ell_k}{N\lambda_0}\lvert f_k\rangle\langle f_k\rvert`$, $`\ell_k\equiv k`$. Our $`C_K`$ is the case $`\alpha_m=0`$, $`\varepsilon=0`$, $`\ell_k=k`$. Hence
```math
e^{-iC_K\lambda_0}=S=\sum_{k}e^{-2\pi ik/N}\lvert f_k\rangle\langle f_k\rvert,\qquad S\lvert m\rangle=\lvert m+1\rangle,\qquad \langle m+1\rvert S=\langle m\rvert .
```
By (2.12) of 02-clock@v2 ($`\{\ell_k\}=\{0,\dots,N-1\}`$, $`c=0`$), this generator attains the minimal spread $`\Delta C_K`$ for the localized clock start $`\lvert0\rangle`$. Nothing is claimed for the clock views of the states used below, whose Fourier weights need not be uniform. The fact is not needed below.
- **Split of $`C`$ (M6).** By A5, a single-object term on an object of $`R`$ may be booked in a pair with the clock, so a split by contract list would depend on that convention. The split is therefore fixed by the total $`C`$ and the given $`C_K`$:
```math
C_R:=\frac1N\mathrm{Tr}_K\bigl(C-C_K\otimes\mathbb 1_R\bigr),\qquad
C_\partial:=C-C_K\otimes\mathbb 1_R-\mathbb 1_K\otimes C_R,\qquad
\mathrm{Tr}_KC_\partial=0 .
\qquad\text{(3.19)}
```
This is the unique split of the stated form with $`\mathrm{Tr}_KC_\partial=0`$: moving some $`\mathbb 1_K\otimes B`$ between $`C_R`$ and $`C_\partial`$ changes $`\mathrm{Tr}_KC_\partial`$ by $`NB`$. Every $`R`$-only term $`\mathbb 1_K\otimes D`$ enters $`C_R`$ as $`D`$, whichever pair it is booked in. Hence $`C_R`$ and $`C_\partial`$ depend only on the total $`C`$, not on the booking. $`C_R`$ is self-adjoint. Since $`C-C_K\otimes\mathbb 1_R`$ maps $`\mathcal H_K\otimes\mathcal H_{R,\rm adm}`$ into itself, each map $`\psi\mapsto(\langle m\rvert\otimes\mathbb 1)(C-C_K\otimes\mathbb 1_R)(\lvert m\rangle\otimes\psi)`$ preserves $`\mathcal H_{R,\rm adm}`$. So $`C_R`$ preserves $`\mathcal H_{R,\rm adm}`$, and with it every $`Q_s`$. Spectral decomposition: $`C_R=\sum_se_sQ_s`$ with distinct $`e_s`$.
- **Conditional states.** $`\Phi(m)=(\langle m\rvert\otimes\mathbb 1_R)\Psi`$, so $`\Psi=\sum_m\lvert m\rangle\otimes\Phi(m)`$. A place reading on $`K`$ gives $`m`$ with $`p(m)=\lVert\Phi(m)\rVert^2`$ and leaves $`\lvert m\rangle\otimes\Phi(m)/\lVert\Phi(m)\rVert`$ (1.3).
- **Readings.** A reading is a partition of joint places (A4). A reading on $`R`$ has classes $`S_r`$ of joint places of $`R`$, with projector $`\Pi^R_r`$. If $`R`$ contains identical-type objects, one may restrict to partitions whose classes are unions of swap orbits of joint places, so that the readings keep states admissible and do not depend on labels (M6). For an admissible state, $`\lvert\Psi_K\rvert`$ is constant on each orbit by (1.11), so the place moduli carry the same information and nothing below changes.
- **Values of $`\lambda`$.** In item 1, a single reading (or a clock reading followed at once by a reading on $`R`$) is applied at a stated $`\lambda`$ to $`\Psi(\lambda)=e^{-iC\lambda}\Psi(0)`$ (A8). In items 2–4, $`\Psi`$ is an eigenvector, so $`\Psi(\lambda)=e^{-iE\lambda}\Psi`$ is the same state for every $`\lambda`$ (1.2), and the value of $`\lambda`$ does not matter.

## Derivation

### Step 1. Readings that do not depend on $`\lambda`$ (item 1)

Every reading, local on some part or not, is a partition of the joint places of the whole system. Its statistics are therefore $`p(r;\lambda)=\sum_{K\in S_r}p_K(\lambda)`$, with $`p_K(\lambda)=\lvert\langle K\vert\Psi(\lambda)\rangle\rvert^2`$. The finest partition is itself a reading. Hence all statistics are $`\lambda`$-independent iff every $`p_K`$ is. Let $`C=\sum_jE_jP_j`$ with distinct $`E_j`$, and let $`\rho=\lvert\Psi(0)\rangle\langle\Psi(0)\rvert`$. By (1.9), $`\Psi(\lambda)=\sum_je^{-iE_j\lambda}P_j\Psi(0)`$. Grouping the terms by Bohr frequency $`\omega\in\{E_j-E_l\}`$ gives
```math
\rho_\omega:=\sum_{E_j-E_l=\omega}P_j\,\rho\,P_l,\qquad
p_K(\lambda)=\sum_\omega e^{-i\omega\lambda}\langle K\vert\rho_\omega\vert K\rangle .
\qquad\text{(3.1)}
```
Exponentials with distinct real frequencies are linearly independent functions on $`\mathbb R`$. Therefore
```math
\text{all reading statistics are }\lambda\text{-independent}
\iff
\langle K\vert\rho_\omega\vert K\rangle=\sum_{E_j-E_l=\omega}\langle K\vert P_j\Psi(0)\rangle\langle P_l\Psi(0)\vert K\rangle=0\quad\forall K,\ \forall\omega\neq0 .
\qquad\text{(3.2)}
```
In that case $`p_K(\lambda)=\langle K\vert\rho_0\vert K\rangle`$.

### Step 2. Eigenvectors are sufficient but not necessary

If $`C\Psi(0)=E\Psi(0)`$, then only the $`P_j`$ with $`E_j=E`$ acts nontrivially, so $`\rho=\rho_0`$ and (3.2) holds. The converse fails because place readings do not detect relative phases between places. Take $`C_\partial=0`$ and let $`R`$ be one object with $`C_R=\sum_re_r\lvert r\rangle\langle r\rvert`$ and $`e_{r_1}\neq e_{r_2}`$. Since $`C_K\lvert f_0\rangle=0`$, the start below evolves as
```math
\Psi(0)=\lvert f_0\rangle\otimes(\alpha\lvert r_1\rangle+\beta\lvert r_2\rangle),\ \alpha\beta\neq0:\qquad
\Psi(\lambda)=\lvert f_0\rangle\otimes(\alpha e^{-ie_{r_1}\lambda}\lvert r_1\rangle+\beta e^{-ie_{r_2}\lambda}\lvert r_2\rangle) .
\qquad\text{(3.3)}
```
All $`p_K`$ are constant ($`\lvert\alpha\rvert^2/N`$, $`\lvert\beta\rvert^2/N`$, $`0`$), but $`\Psi(0)`$ is not an eigenvector of $`C`$.

### Step 3. The clock outcome and readings on $`R`$ (item 1, second part)

Assume that (3.2) holds. A place reading on $`K`$ at some $`\lambda`$ is followed at once (same $`\lambda`$) by a reading $`\{S_r\}`$ on $`R`$. Write $`\Phi_\lambda(m)=(\langle m\rvert\otimes\mathbb 1)\Psi(\lambda)`$, $`p_{(m,r')}`$ for the probability of the joint place $`\lvert m\rangle\lvert r'\rangle`$, and $`p_R(r')=\sum_mp_{(m,r')}`$. By (1.3), for $`p(m)>0`$,
```math
\begin{aligned}
&p(r\,\vert\,m)=\frac{\lVert\Pi^R_r\Phi_\lambda(m)\rVert^2}{\lVert\Phi_\lambda(m)\rVert^2}=\frac{\sum_{r'\in S_r}p_{(m,r')}}{\sum_{r'}p_{(m,r')}} ,\\
&\text{some reading on }R\text{ has }m\text{-dependent }p(\cdot\,\vert\,m)\iff p_{(m,r')}\neq p(m)\,p_R(r')\ \text{ for some }m,r' .
\end{aligned}
\qquad\text{(3.4)}
```
By (3.2) this does not depend on $`\lambda`$. For a *specified* reading $`\{S_r\}`$, $`p(\cdot\vert m)`$ depends on $`m`$ (among the $`m`$ with $`p(m)>0`$) iff at least one class sum in (3.4) does. Coarse-graining can hide the dependence: the one-class reading never shows it. The second line of (3.4) holds for the following reason. If the joint place distribution is not a product, the conditional place distribution $`p_{(m,r')}/p(m)`$ depends on $`m`$, and the finest reading on $`R`$ shows this. If it is a product, every class sum equals $`p(m)\sum_{r'\in S_r}p_R(r')`$, so no reading on $`R`$ depends on $`m`$. Under the orbit restriction of the Setup, the finest admissible reading is the orbit partition. $`\Phi_\lambda(m)\in\mathcal H_{R,\rm adm}`$ has moduli that are constant on orbits, so the orbit distribution carries the same information. The dependence does occur. Take $`C_\partial=0`$, let $`R`$ be one object with places $`0,1`$, set $`\lvert\pm\rangle=(\lvert0\rangle\pm\lvert1\rangle)/\sqrt2`$ and $`C_R=\frac{2\pi}{N\lambda_0}\lvert-\rangle\langle-\rvert`$. Then
```math
\Psi_{\rm ex}=\tfrac1{\sqrt2}\bigl(\lvert f_1\rangle\otimes\lvert+\rangle+\lvert f_0\rangle\otimes\lvert-\rangle\bigr),\qquad
C\Psi_{\rm ex}=\tfrac{2\pi}{N\lambda_0}\Psi_{\rm ex},\qquad
p(0_R\,\vert\,m)=\cos^2\frac{\pi m}{N}.
\qquad\text{(3.5)}
```
Indeed $`\Phi(m)=(2N)^{-1/2}(e^{2\pi im/N}\lvert+\rangle+\lvert-\rangle)`$, so $`\lVert\Phi(m)\rVert^2=1/N`$ and $`\langle0\vert\Phi(m)\rangle=(1+e^{2\pi im/N})/(2\sqrt N)`$. For $`m=0`$ the conditional probability is $`1`$, for $`m=1`$ it is $`\cos^2(\pi/N)<1`$. So **yes**: for such starts the clock outcome can change the statistics of a reading on $`R`$ (here the place reading of $`R`$), although no statistics depend on $`\lambda`$.

### Step 4. Shift relation (item 2a)

For $`C_\partial=0`$ the two terms of $`C`$ commute, so $`e^{-iC\lambda_0}=S\otimes e^{-iC_R\lambda_0}`$. From $`C\Psi=E\Psi`$ follows $`(S\otimes e^{-iC_R\lambda_0})\Psi=e^{-iE\lambda_0}\Psi`$. Applying $`\langle m+1\rvert\otimes\mathbb 1`$ and using $`\langle m+1\rvert S=\langle m\rvert`$ gives
```math
\Phi(m+1)=e^{-i(C_R-E)\lambda_0}\,\Phi(m),\qquad m\in\mathbb Z_N .
\qquad\text{(3.6)}
```

### Step 5. Allowed components and the eigenvector through $`\chi`$ (item 2b)

1. Write $`\Psi=\sum_k\lvert f_k\rangle\otimes\psi_k`$ with $`\psi_k=(\langle f_k\rvert\otimes\mathbb 1)\Psi`$. Then $`C\Psi=\sum_k\lvert f_k\rangle\otimes\bigl(\tfrac{2\pi k}{N\lambda_0}+C_R\bigr)\psi_k`$. So $`C\Psi=E\Psi`$ iff $`Q_s\psi_k=0`$ whenever $`e_s\neq E-\frac{2\pi k}{N\lambda_0}`$. Define
```math
k_s:=\frac{N\lambda_0}{2\pi}(E-e_s),\qquad S_E:=\{s:\ k_s\in\{0,1,\dots,N-1\}\}.
\qquad\text{(3.7)}
```
2. Hence $`Q_s\psi_k=\delta_{k,k_s}Q_s\psi_{k_s}`$ for $`s\in S_E`$, and $`Q_s\psi_k=0`$ for $`s\notin S_E`$. With $`\Phi(m)=N^{-1/2}\sum_ke^{2\pi ikm/N}\psi_k`$ this gives
```math
Q_s\Phi(m)=0\quad(s\notin S_E),\qquad Q_s\Phi(m)=e^{2\pi ik_sm/N}\,Q_s\Phi(0)\quad(s\in S_E).
\qquad\text{(3.8)}
```
So $`Q_s\Phi(m)`$ can be nonzero only if $`E-e_s\in\frac{2\pi}{N\lambda_0}\{0,\dots,N-1\}`$, and then its norm does not depend on $`m`$. This agrees with (3.6), since $`e^{-i(e_s-E)\lambda_0}=e^{2\pi ik_s/N}`$.
3. **Claim.** For a unit vector $`\chi\in\mathcal H_{R,\rm adm}`$, some admissible eigenvector $`\Psi`$ with eigenvalue $`E`$ has $`\Phi(0)\propto\chi`$ iff
```math
Q_s\chi=0\quad\text{for all }s\notin S_E,\qquad\text{i.e.}\qquad \chi\in\bigoplus_{s\in S_E}Q_s\mathcal H_R .
\qquad\text{(3.9)}
```
*Necessity:* $`\Phi(0)=c\chi`$, and $`c\neq0`$, because $`\Phi(0)=0`$ would make every $`\Phi(m)`$ vanish by (3.6). Then (3.8) at $`m=0`$ gives (3.9). *Sufficiency:* set
```math
\Psi=\sum_{s\in S_E}\lvert f_{k_s}\rangle\otimes Q_s\chi=\frac1{\sqrt N}\sum_{m=0}^{N-1}\lvert m\rangle\otimes e^{-i(C_R-E)m\lambda_0}\chi .
\qquad\text{(3.10)}
```
By (3.7), $`C\Psi=\sum_s(\frac{2\pi k_s}{N\lambda_0}+e_s)\lvert f_{k_s}\rangle\otimes Q_s\chi=E\Psi`$. By (3.9), $`\lVert\Psi\rVert^2=\sum_s\lVert Q_s\chi\rVert^2=1`$. The second form of (3.10) follows from $`e^{-i(C_R-E)m\lambda_0}Q_s\chi=e^{2\pi ik_sm/N}Q_s\chi`$, and $`\Psi`$ is admissible because the $`Q_s`$ preserve $`\mathcal H_{R,\rm adm}`$. *Uniqueness:* (3.6) fixes every $`\Phi(m)`$ from $`\Phi(0)=c\chi`$, and normalization fixes $`\lvert c\rvert=N^{-1/2}`$. So $`\Psi`$ is unique up to the common phase. Choosing $`c=N^{-1/2}`$,
```math
\Phi(m)=\frac{1}{\sqrt N}\,e^{iEm\lambda_0}e^{-iC_Rm\lambda_0}\chi,\qquad p(m)=\lVert\Phi(m)\rVert^2=\frac1N .
\qquad\text{(3.11)}
```
This is well defined on $`\mathbb Z_N`$, because $`e^{-i(C_R-E)N\lambda_0}\chi=\sum_se^{2\pi ik_s}Q_s\chi=\chi`$.

### Step 6. Comparison with the evolution of $`R`$ alone (item 2c)

By (3.11), $`\Phi(m)/\lVert\Phi(m)\rVert=e^{iEm\lambda_0}\,e^{-iC_Rm\lambda_0}\chi`$, which by (1.2) is the state $`e^{-iC_R\lambda}\chi`$ at $`\lambda=m\lambda_0`$. Hence, for every reading on $`R`$,
```math
P_r(m):=\frac{\lVert\Pi^R_r\Phi(m)\rVert^2}{\lVert\Phi(m)\rVert^2}=p_r(m\lambda_0),\qquad p_r(\lambda):=\lVert\Pi^R_r\,e^{-iC_R\lambda}\chi\rVert^2 .
\qquad\text{(3.12)}
```
The finest reading on $`R`$ is a reading, so the statistics of every reading coincide iff $`\lambda\in\Lambda_m:=\{\lambda:\ \lvert\langle r\vert e^{-iC_R\lambda}\chi\rangle\rvert=\lvert\langle r\vert e^{-iC_Rm\lambda_0}\chi\rangle\rvert\ \forall r\}`$. Let $`\mathrm{supp}\chi=\{s:Q_s\chi\neq0\}`$. The two states coincide iff $`e^{-ie_s(\lambda-m\lambda_0)}`$ is the same for all $`s\in\mathrm{supp}\chi`$. Since $`e_s-e_{s'}=\frac{2\pi(k_{s'}-k_s)}{N\lambda_0}`$, Bezout's identity turns this into a condition on a gcd, and
```math
\Lambda_m\ \supseteq\ m\lambda_0+\frac{N\lambda_0}{g_\chi}\mathbb Z\ \supseteq\ m\lambda_0+N\lambda_0\mathbb Z,\qquad g_\chi:=\gcd\{k_s-k_{s'}:\ s,s'\in\mathrm{supp}\chi\} .
\qquad\text{(3.13)}
```
The middle set is exactly the set where the states coincide; it is $`\mathbb R`$ if $`\mathrm{supp}\chi`$ has one element. $`\Lambda_m`$ can be larger, because place readings do not see every phase. In (3.5), $`\chi=\lvert0\rangle`$ and $`g_\chi=1`$, and $`p_0(\lambda)=\cos^2\frac{\pi\lambda}{N\lambda_0}`$, so $`\Lambda_m=\pm m\lambda_0+N\lambda_0\mathbb Z`$.

### Step 7. Crossing contracts: a sufficient condition (item 3)

The proof of Step 4 uses only $`e^{-iC\lambda_0}=S\otimes(\cdot)`$. Hence
```math
e^{-iC\lambda_0}=S\otimes W\ \text{ for some unitary }W\text{ on }\mathcal H_R
\ \Longrightarrow\
\Phi(m+1)=U\Phi(m),\quad U=e^{iE\lambda_0}W,
\qquad\text{(3.14)}
```
for every eigenvector. Up to the phase $`e^{iE\lambda_0}`$, $`U`$ is the same for all eigenvectors. Condition (3.14) holds with $`C_\partial\neq0`$ if
```math
C_\partial=\sum_k\lvert f_k\rangle\langle f_k\rvert\otimes B_k,\qquad B_k=B_k^\dagger,\qquad e^{-i(C_R+B_k)\lambda_0}=W\ \ \forall k ,
\qquad\text{(3.15)}
```
because then $`e^{-iC\lambda_0}=\sum_ke^{-2\pi ik/N}\lvert f_k\rangle\langle f_k\rvert\otimes W=S\otimes W`$. The split (3.19) requires $`\mathrm{Tr}_KC_\partial=\sum_kB_k=0`$. This is no restriction: a mean $`\bar B=N^{-1}\sum_kB_k\neq0`$ belongs to $`C_R`$, and moving it there leaves every $`C_R+B_k`$, and hence (3.15), unchanged. One example: $`B_k=\frac{2\pi n_k}{\lambda_0}P`$, with integers $`n_k`$ that are not all equal and satisfy $`\sum_kn_k=0`$ (for instance $`n_0=1`$, $`n_1=-1`$, all others $`0`$). Here $`P`$ is a projector on one object of $`R`$ that commutes with $`C_R`$, and the type of that object occurs only once in $`R`$, so $`C`$ keeps $`\mathcal H_{\rm adm}`$ invariant. This is a pair contract (A5). Since $`e^{-2\pi in_kP}=\mathbb 1`$, it gives $`W=e^{-iC_R\lambda_0}`$, and $`U`$ is the same as in (3.6).

### Step 8. Counterexample (item 3)

A unitary $`U`$ preserves norms, so (3.14) forces $`p(m)=\lVert\Phi(m)\rVert^2`$ to be independent of $`m`$. Take $`N=2`$, let $`R`$ be one object with places $`0,1`$ (not of the clock's type), $`C_R=0`$, and $`C_\partial=g\,Z\otimes\lvert0\rangle\langle0\rvert_R`$ with $`Z=\lvert0\rangle\langle0\rvert-\lvert1\rangle\langle1\rvert`$ on $`K`$ and real $`g\neq0`$. For $`N=2`$, $`C_K=a(\mathbb 1-X)`$ with $`a=\frac{\pi}{2\lambda_0}`$ and $`X=\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert`$. On $`\mathcal H_K\otimes\lvert0\rangle_R`$, $`C`$ acts as $`a(\mathbb 1-X)+gZ`$. With $`\Omega=\sqrt{a^2+g^2}`$ and $`p_\pm=\frac12(1\pm g/\Omega)`$,
```math
\Psi=\bigl(\sqrt{p_+}\,\lvert0\rangle-\sqrt{p_-}\,\lvert1\rangle\bigr)\otimes\lvert0\rangle_R,\qquad C\Psi=(a+\Omega)\Psi,\qquad \lVert\Phi(0)\rVert^2=p_+\neq p_-=\lVert\Phi(1)\rVert^2 .
\qquad\text{(3.16)}
```
*Check.* The first component of $`(a(\mathbb 1-X)+gZ)\Psi`$ is $`(a+g)\sqrt{p_+}+a\sqrt{p_-}`$. It equals $`(a+\Omega)\sqrt{p_+}`$ iff $`a^2p_-=(\Omega-g)^2p_+`$, i.e. iff $`a^2=\Omega^2-g^2`$. The second component equals $`-(a+\Omega)\sqrt{p_-}`$ iff $`a^2p_+=(\Omega+g)^2p_-`$, again iff $`a^2=\Omega^2-g^2`$. So no unitary $`U`$ exists for this eigenvector. **Answer to item 3: no**, not for every crossing contract.

### Step 9. Conversion of rates (item 4)

Assume (i) $`\Psi`$ is an eigenvector of $`C`$, and (ii) (3.14) holds with $`W=e^{-iC_R\lambda_0}`$ up to a constant phase. This includes $`C_\partial=0`$ and the example after (3.15). Here $`C_R`$ is the operator (3.19), so condition (ii) and the reference evolution $`e^{-iC_R\lambda}`$ depend only on the total $`C`$, not on the booking of its terms (M6). Then $`\Phi(m)=U^m\Phi(0)`$ with $`U=e^{-i(C_R-E')\lambda_0}`$ ($`E'`$ absorbs the phase). All $`\lVert\Phi(m)\rVert`$ are equal, hence equal to $`N^{-1/2}`$, and (3.12) holds with $`\chi=\Phi(0)/\lVert\Phi(0)\rVert`$. Define the clock time of the reading $`m`$ from the reading and the tick of $`C_K`$:
```math
\tau_m:=m\lambda_0\pmod{N\lambda_0}.
\qquad\text{(3.17)}
```
Then $`P_r(m)=p_r(\tau_m)`$ holds exactly. It is consistent modulo $`N\lambda_0`$, because $`\Phi(N)=\Phi(0)`$ makes $`p_r`$ periodic with period $`N\lambda_0`$. By Taylor's theorem with remainder,
```math
\frac{P_r(m+1)-P_r(m)}{\lambda_0}=\frac{\mathrm dp_r}{\mathrm d\lambda}\Big\vert_{\lambda=\tau_m}+\delta,\qquad \lvert\delta\rvert\le\frac{\lambda_0}{2}\,w_\chi^2,\qquad w_\chi:=\max_{\mathrm{supp}\chi}e_s-\min_{\mathrm{supp}\chi}e_s .
\qquad\text{(3.18)}
```
*Bound.* $`p_r''=-\langle\psi\vert[\tilde C,[\tilde C,\Pi^R_r]]\vert\psi\rangle`$, with $`\psi=e^{-iC_R\lambda}\chi`$ and $`\tilde C=C_R-c`$, where $`c`$ is the midpoint of $`\{e_s\}_{\mathrm{supp}\chi}`$. On the invariant span of $`\psi`$ one has $`\lVert\tilde C\psi\rVert\le w_\chi/2`$ and $`\lVert\tilde C^2\psi\rVert\le w_\chi^2/4`$. Expanding the double commutator into three terms gives $`\lvert p_r''\rvert\le w_\chi^2`$.
So a rate with respect to $`\lambda`$ under the evolution of $`R`$ alone, evaluated at $`\lambda=\tau_m`$, equals the rate with respect to the clock time $`\tau`$, up to $`\delta`$. The per-step form $`P_r(m+1)-P_r(m)=\int_{\tau_m}^{\tau_m+\lambda_0}\frac{\mathrm dp_r}{\mathrm d\lambda}\mathrm d\lambda`$ is exact. The derivative form requires (iii) $`\lambda_0w_\chi\ll1`$. For the eigenvectors of item 2, $`w_\chi=\frac{2\pi}{N\lambda_0}(\max k_s-\min k_s)`$ by (3.7), so (iii) means $`\max k_s-\min k_s\ll N/2\pi`$. Without (ii), (3.6) can fail (Step 8), and the conditional states then need not follow any unitary evolution of $`R`$.

## Result

- **Split.** $`C_R=N^{-1}\mathrm{Tr}_K(C-C_K\otimes\mathbb 1_R)`$ and $`C_\partial`$ are fixed by (3.19), the unique split with $`\mathrm{Tr}_KC_\partial=0`$. They depend only on the total $`C`$, not on the booking of single-object terms (A5, M6).
- **Item 1.** All reading statistics are $`\lambda`$-independent iff the place-diagonal of every Bohr component $`\rho_\omega`$, $`\omega\neq0`$, vanishes (3.2). Eigenvectors of $`C`$ suffice; they are not necessary (3.3). For such starts, a specified reading on $`R`$ has $`m`$-dependent statistics iff at least one of its class sums in (3.4) depends on $`m`$. *Some* reading on $`R`$ has $`m`$-dependent statistics iff the joint place distribution of $`K`$ and $`R`$ is not a product (3.4). So **yes**, the clock outcome can change the statistics on $`R`$: (3.5) is an eigenvector example.
- **Item 2.** (a) $`\Phi(m+1)=e^{-i(C_R-E)\lambda_0}\Phi(m)`$ (3.6). (b) $`Q_s\Phi(m)\neq0`$ only if $`E-e_s\in\frac{2\pi}{N\lambda_0}\{0,\dots,N-1\}`$ (3.8). An eigenvector through $`\chi`$ exists iff (3.9) holds, and it is then unique: $`\Psi`$ (3.10), with $`\Phi(m)`$ and $`p(m)=1/N`$ (3.11). (c) The conditional statistics equal the statistics of $`e^{-iC_R\lambda}\chi`$ at $`\lambda=m\lambda_0`$ (3.12), and the coincidence set is (3.13).
- **Item 3.** Not for every crossing contract: counterexample (3.16). Sufficient condition (3.14) with $`U=e^{iE\lambda_0}W`$, realized by (3.15).
- **Item 4.** With the clock time (3.17), conditional statistics equal the statistics of $`R`$ alone at $`\lambda=\tau_m`$, and rates convert with factor one, $`\mathrm d/\mathrm d\tau\leftrightarrow\mathrm d/\mathrm d\lambda`$, up to $`\lvert\delta\rvert\le\lambda_0w_\chi^2/2`$ (3.18). Conditions: (i) eigenvector, (ii) (3.14) with $`W\propto e^{-iC_R\lambda_0}`$ and $`C_R`$ from (3.19), (iii) $`\lambda_0w_\chi\ll1`$ for the derivative form.

## Consistency checks

1. **Dimensions and normalization.** $`C\lambda`$ is a phase (1.9), so $`k_s`$, $`(C_R-E)\lambda_0`$ and $`\lambda_0w_\chi`$ are dimensionless, and both sides of (3.18) scale as $`1/\lambda`$. $`\sum_mp(m)=1`$ by (3.11), and $`p_++p_-=1`$ in (3.16). Passed.
2. **$`\chi`$ an eigenvector of $`C_R`$** ($`\mathrm{supp}\chi=\{s\}`$). Then (3.9) requires $`E=e_s+\frac{2\pi k}{N\lambda_0}`$ with $`0\le k\le N-1`$, and (3.10) gives the product $`\lvert f_k\rangle\otimes\chi`$. $`P_r(m)`$ does not depend on $`m`$, $`\Lambda_m=\mathbb R`$, and $`w_\chi=0`$, so $`\delta=0`$: no relational change for a stationary $`R`$. Passed.
3. **$`N=2`$ in (3.5).** Here $`E=\pi/\lambda_0`$, $`k_+=1`$, $`k_-=0`$. Eq. (3.6) gives $`\Phi(1)=e^{-i(C_R-E)\lambda_0}\lvert0\rangle/\sqrt2=-\lvert1\rangle/\sqrt2`$, which agrees with the direct value $`\frac12(-\lvert+\rangle+\lvert-\rangle)`$. Moreover $`P_0(1)=0=p_0(\lambda_0)`$. Passed.

## Open issues

- Readings are place partitions, so $`\lambda`$-independence of all statistics (3.2) is weaker than stationarity. Whether starts that satisfy (3.2) but are not eigenvectors support a relational evolution is not treated.
- $`\Lambda_m`$ in (3.13) is characterized only through place moduli. Beyond the two inclusions, no closed form is given.
- Item 3 gives only a sufficient condition (3.14). A necessary and sufficient condition on $`C_\partial`$ is not determined, and the realization (3.15) needs a fine-tuned spectrum of the $`B_k`$.
- The conversion (3.18) is a statement on clock steps. The $`N`$ samples $`p_r(\tau_m)`$ do not in general determine $`p_r`$ between ticks; the clock's resolution belongs to criterion 1.
- Superpositions of eigenvectors with different $`E`$ are not treated.

## Methods used

- spectral decomposition, Bohr-frequency expansion
- linear independence of exponentials
- discrete Fourier basis of a ring
- partial trace (booking-independent split of the generator)
- conditional states with respect to a clock reading
- Bezout identity
- Taylor remainder and commutator norm bounds
