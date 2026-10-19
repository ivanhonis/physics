# Two clocks of one body: gap responses, common response and fall

- **Subproject:** 05-ilang-free-fall
- **Package:** 06-two-clocks
- **Version:** v2
- **Mode:** internal regeneration
- **Date:** 2026-10-11

## Changes from previous version

Local regeneration after `review.v1.md` (I1 major, I2 minor). All tags (6.1)–(6.28) are kept, and no tag is reused. The passages listed below are the only ones that differ from v1.

- **Header.** Version and mode; this section is new.
- **Step 12, (6.21): the tagged statement is changed and keeps its tag (I1).** The left side of v1 read "(6.11), $`V_k`$ level-independent, $`\tau_k=\tau`$". It now reads "(6.11), $`V_k=V_\circ`$, $`\tau_k=\tau`$", the condition that the third line of (6.17) proves. The v1 form was false: the first control of Step 9 satisfies the v1 left side and violates the right side. Under (6.11), equal level offsets only make $`\mathcal F_k`$ level-independent, not zero.
- **Step 12, text (I1).** Changed: the line before (6.21) (it now names $`V_\circ`$); the sentence under (6.21) (it now ends with a colon and is followed by two new bullets, one per direction); the two answer bullets of v1 (each now says for which branches it is made, and each carries the one-branch statement). New: one bullet on the three forms of the condition on the level offsets, and one bullet that checks (6.21) against the controls of Steps 9 and 10.
- **Step 10 (I2).** New: one sentence between (6.19) and its bullets. Changed: the bullet "What follows from the hypothesis alone" (the clause "with $`\mathcal F_k=0`$ from (6.18)") and the bullet "What need not" (the final parenthesis). The display (6.19) is unchanged.
- **Step 14 (I2).** New: the bullet "Form of the conditions on the level offsets", after the bullet "In [C] the row ...". Changed: the second bullet under (6.25) (in v1 it began "For $`g_*\neq0`$ the level offsets are equal"), which now begins "In (6.25) ...". The displays (6.23)–(6.25) are unchanged.
- **Step 16 (I2).** New: two sentences after "... for all levels ($`M_0\neq M_1`$)." The table (6.28) is unchanged.
- **Result.** The line of item 3: the answer to criterion 4 is restated as (6.21) now proves it.
- **Results.** No result other than (6.21) changed. With the condition on $`\mathcal F_k`$ stated at each place, (6.19), (6.24), (6.25) and (6.28) are correct as displayed in v1.
- **JSON twin.** Changed statements of key results: 6.21 (restated as above); 6.20 (the v1 twin said "equal level offsets", it now says "$`V_k=V_\circ`$", as Step 11 has it in both versions); 6.19, 6.24, 6.25 and 6.28 (each now names the condition on $`\mathcal F_k`$; 6.25 no longer presents the operator identity as equivalent to its conditions). All other entries of the twin are those of v1, apart from version and mode.

## Setup and assumptions

- **Setting.** One body $`b`$ and a medium $`c`$ with the records $`K_x=\kappa\,x\,X`$; no field object: the position dependence sits in the body contract (A10; an assumption, M8). Local member, gaps, labels, responses, named gaps, branch starts and drift acceleration are those of `question.md`. All profiles are those of $`C_{\rm eff}`$, (8.19) of 04-ilang-time/08-maximal-speed. Nothing below says that the language selects such descriptions (M10).
- **Classes.** **[L]**: every member of $`\mathcal C_{\rm lev}`$ with linear level profiles and $`N\ge2`$ levels, all level offsets, both branches, all labels. **[C]**: the class $`\mathcal C`$ with the linear profiles of 03-clock-and-fall ($`\tau_k=\tau`$, $`M_k=m+d_k`$, $`G_k=m\,g_m+d_kg_\eta`$, $`\mathcal F_k=\mathcal F`$, $`g_{\zeta,k}=g_\zeta`$, $`V_k=0`$), every $`N\ge2`$.
- **Inputs, as quoted in the question.** (2.5) of 04-ilang-time/02-clock; (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion; (3.2), (3.23), (3.36) of 03-clock-and-fall; (4.7), (4.10), (4.11), (4.16)–(4.19), (4.22), (4.24), (4.25) of 04-branch-fall.
- **Approximations.** Responses: first order in the gradients; the second order is not estimated. Fall: the drift acceleration of 04-branch-fall (first order in the gradients, long window, sharp label), at leading order in $`\kappa`$ (weak-record regime).
- **Notation.**

```math
e_{k,\sigma}(p):=V_k+\sigma\,\omega_k(p),\qquad \Omega^0_\gamma:=e_{k,\sigma}(p)-e_{k',\sigma'}(p'),\qquad u_k:=\frac{G_k}{M_k},\qquad W_k:=\sqrt{M_k^2+\tau_k^2}=\omega_k(\tfrac\pi2).
\qquad\text{(6.1)}
```

  A label $`\gamma`$ is *admissible* if $`\Omega^0_\gamma\neq0`$; it is a *rest label* if $`\sin p=\sin p'=0`$, and otherwise it *has a moving label*. The *plain part* of the level $`k`$ is $`V_{x,k}\mathbb 1_2`$. Statements about level gaps assume $`\Omega^0_{\gamma_{\rm lev}(j)}=M_{j+1}-M_j+V_{j+1}-V_j\neq0`$ for all $`j\le N-2`$ (true in [C]).
- **Level offsets and the quoted results of 04-branch-fall.** The level is conserved, so a start in the level $`k`$ stays in (level $`k`$)$`\,\otimes\,\mathcal H_c`$. On this subspace the total contract with the offset is the total contract without it plus $`V_k\mathbb 1`$. The state changes by the common phase $`e^{-iV_k\lambda}`$, which is not data (1.2): no view, no weight $`p_x`$ and no $`\bar x_{\rm lab}`$ changes, and the vectors $`\beta_{k,\sigma}`$ are the same. Hence (4.7)–(4.19) hold as quoted for every $`V_k`$.

## Derivation

### Step 1. Response of a general gap (item 1(a))

At $`x_0=0`$ the local member has $`M_{0,k}=M_k`$, $`V_{0,k}=V_k`$, $`\zeta^0_k(0)=1`$, so $`\varepsilon_{k,\sigma}(p;0)=e_{k,\sigma}(p)`$ and $`\Omega_\gamma(0)=\Omega^0_\gamma`$ exactly. At $`x_0=1`$: $`M_{1,k}=M_k+G_k`$, $`V_{1,k}=V_k-\mathcal F_k`$, $`\zeta^0_k(1)=1+g_{\zeta,k}`$. The Taylor expansion of the square root ($`\omega_k\ge M_k>0`$) gives

```math
\varepsilon_{k,\sigma}(p;1)-\varepsilon_{k,\sigma}(p;0)=-\mathcal F_k+\sigma\,\delta\omega_k(p)+O(\text{gradients}^2),\qquad
\delta\omega_k(p):=\frac{M_kG_k+\tau_k^2g_{\zeta,k}\sin^2p}{\omega_k(p)}=g_{\zeta,k}\,\omega_k(p)+(u_k-g_{\zeta,k})\frac{M_k^2}{\omega_k(p)} .
\qquad\text{(6.2)}
```

The difference of two such shifts, divided by $`\Omega^0_\gamma`$, is the response. **[L]**, every admissible label $`\gamma=(k,\sigma,p;k',\sigma',p')`$:

```math
\boxed{\;\rho_\gamma=\frac{\sigma\,\delta\omega_k(p)-\sigma'\,\delta\omega_{k'}(p')-(\mathcal F_k-\mathcal F_{k'})}{V_k-V_{k'}+\sigma\,\omega_k(p)-\sigma'\,\omega_{k'}(p')}\;}
\qquad\text{(6.3)}
```

It is a linear form in the gradients: the coefficient of $`G_k`$ is $`\sigma M_k/(\omega_k(p)\,\Omega^0_\gamma)`$, of $`g_{\zeta,k}`$ it is $`\sigma\tau_k^2\sin^2p/(\omega_k(p)\,\Omega^0_\gamma)`$, of $`\mathcal F_k`$ it is $`-1/\Omega^0_\gamma`$; the gradients of the second level enter with $`(k,\sigma,p)\to(k',\sigma',p')`$ and the opposite sign. Inside one level ($`k=k'`$) the terms $`\mathcal F_k`$ and $`V_k`$ cancel. With $`\sigma/\omega-\sigma'/\omega'=-\sigma\sigma'(\sigma\omega-\sigma'\omega')/(\omega\omega')`$ and the second form of (6.2):

```math
\rho_\gamma=g_{\zeta,k}-\sigma\sigma'\,(u_k-g_{\zeta,k})\,\frac{M_k^2}{\omega_k(p)\,\omega_k(p')}\qquad(k=k').
\qquad\text{(6.4)}
```

So the gaps inside one level contain only $`G_k`$ and $`g_{\zeta,k}`$. The gradient $`\mathcal F_k`$ of the plain part enters only the gaps between two levels, and only as $`\mathcal F_k-\mathcal F_{k'}`$, together with the difference $`V_k-V_{k'}`$ of the level offsets in the denominator.

### Step 2. The named gaps (item 1(b))

**[L]**. From (6.3) with $`\omega_k(0)=M_k`$, $`\delta\omega_k(0)=G_k`$; from (6.4) with $`\sigma\sigma'=-1`$, $`p=p'=0`$; and from (6.4) with $`\sigma\sigma'=+1`$, $`\omega_k(\tfrac\pi2)=W_k`$, $`\omega_k(0)=M_k`$:

```math
\rho_{\rm lev}(k)=\frac{(G_{k+1}-\mathcal F_{k+1})-(G_k-\mathcal F_k)}{(M_{k+1}+V_{k+1})-(M_k+V_k)},\qquad
\rho_{\rm br}(k)=\frac{G_k}{M_k}=u_k,\qquad
\rho_{\rm band}(k)=g_{\zeta,k}-\frac{M_k}{W_k}\,(u_k-g_{\zeta,k}) .
\qquad\text{(6.5)}
```

**[C]**. Here $`\varepsilon_{k,+}(0;x_0)=E^+_{x_0,k}`$, so by (3.23), exactly in the gradients and for every $`k\le N-2`$,

```math
\Omega_{\gamma_{\rm lev}(k)}(x_0)=E^+_{x_0,k+1}-E^+_{x_0,k}=\frac{2\pi}{N}\,r(x_0),\qquad \rho_{\rm lev}(k)=g_\eta=\frac{r(1)-r(0)}{r(0)} .
\qquad\text{(6.6)}
```

The level gap is $`2\pi/N`$ times the rate in its wide-start form. The rate $`r_W`$ at finite $`W`$ carries the further factor $`1-\varsigma_W`$, which depends on the place only through $`\tau^0/\bar\mu`$.

### Step 3. Starts and readings (item 1(c))

The body evolves by $`C_{\rm loc}(x_0)`$ alone ($`\kappa=0`$), so (2.5) of 04-ilang-time/02-clock applies; $`\beta_{k,\sigma}`$, $`\theta_k`$ are those of the local member. $`g_0`$ is a label weight concentrated at $`0`$ with the spread $`\delta p`$, and the limit $`\delta p\to0`$ is taken at fixed $`\lambda`$. Each eigenvector evolves by its phase, and (1.3) gives, with $`\langle a\vert f_k\rangle=N^{-1/2}e^{2\pi ika/N}`$, $`\langle\beta_{k,+}(0)\vert\beta_{k+1,+}(0)\rangle=1`$ and $`\langle\beta_{k,+}(0)\vert\beta_{k,+}(\tfrac\pi2)\rangle=\cos\tfrac{\theta_k(\pi/2)}2\neq0`$:

```math
\begin{array}{l|l|l|l}
\text{gap}&\text{start: label weight, internal factor at }p&\text{reading}&\text{statistics for }\delta p\to0\\\hline
\gamma_{\rm lev}(k)&g_0(p),\ \ \tfrac1{\sqrt2}\bigl[\beta_{k,+}(p)\otimes\lvert f_k\rangle+\beta_{k+1,+}(p)\otimes\lvert f_{k+1}\rangle\bigr]&\text{clock label }a&\tfrac1N\bigl[1+\cos\bigl(\Omega_{\gamma_{\rm lev}(k)}(x_0)\,\lambda-\tfrac{2\pi a}N\bigr)\bigr]\\
\gamma_{\rm band}(k)&\tfrac1{\sqrt2}\bigl[g_0(p)+g_0(p-\tfrac\pi2)\bigr],\ \ \beta_{k,+}(p)\otimes\lvert f_k\rangle&r=x\bmod4&\tfrac14\bigl[1+\cos\tfrac{\theta_k(\pi/2)}2\,\cos\bigl(\Omega_{\gamma_{\rm band}(k)}(x_0)\,\lambda-\tfrac{\pi r}2\bigr)\bigr]
\end{array}
\qquad\text{(6.7)}
```

Both limits are periodic in $`\lambda`$, with the period $`2\pi/\lvert\Omega_\gamma(x_0)\rvert`$. At a finite spread neither is: for the first row the exact statistics is $`\tfrac1N\bigl[1+\bigl\langle\cos\tfrac{\theta_{k+1}-\theta_k}2\cos\bigl((\varepsilon_{k+1,+}(p;x_0)-\varepsilon_{k,+}(p;x_0))\lambda-\tfrac{2\pi a}N\bigr)\bigr\rangle_{g_0}\bigr]`$, a continuous superposition of gaps.

**The branch gap has no such example.** Since $`\theta_k(0)=\theta_k(\pi)=0`$, the eigenvectors with the labels $`(k,+,0)`$ and $`(k,-,0)`$ are $`\lvert p\rangle\otimes\lvert s{=}1\rangle\otimes\lvert f_k\rangle`$ and $`\lvert p\rangle\otimes\lvert s{=}2\rangle\otimes\lvert f_k\rangle`$ with $`p\in\{0,\pi\}`$. Every reading projector $`\Pi_r`$ is diagonal in the places (A4), hence in the branch label $`s`$, so the coefficient of this term of (2.5) vanishes:

```math
\bigl(\langle p\rvert\otimes\langle s{=}2\rvert\otimes\langle f_k\rvert\bigr)\,\Pi_r\,\bigl(\lvert p'\rangle\otimes\lvert s{=}1\rangle\otimes\lvert f_k\rangle\bigr)=0\quad\text{for every reading and }p,p'\in\{0,\pi\}:\qquad\gamma_{\rm br}(k)\ \text{is in no statistics of the body}.
\qquad\text{(6.8)}
```

The nearest term: start with the weight $`g_0(p-p_0)`$, $`\sin p_0\neq0`$, and the internal factor $`\lvert s{=}1\rangle\otimes\lvert f_k\rangle=\cos\tfrac{\theta_k}2\beta_{k,+}-\sin\tfrac{\theta_k}2\beta_{k,-}`$; reading of the branch label. Then $`p(s{=}1;\lambda)\to1-\tfrac12\sin^2\theta_k(p_0)\,\bigl[1-\cos\bigl(2\omega_k(p_0;x_0)\lambda\bigr)\bigr]`$, periodic, with the gap $`(k,+,p_0;k,-,p_0)`$. By (6.4) its response is $`g_{\zeta,k}+(u_k-g_{\zeta,k})M_k^2/\omega_k(p_0)^2`$. For $`p_0\to0`$ the response tends to $`\rho_{\rm br}(k)`$ and the coefficient $`\tfrac12\sin^2\theta_k(p_0)`$ tends to zero: the branch gap is the lower edge of the band $`[2M_k,2W_k]`$ of these frequencies.

### Step 4. Well-definedness (item 1(d))

With one body, (8.1) of 04-ilang-time/08-maximal-speed changes $`C_{\rm eff}`$ by $`\langle Z\rangle\mathbb 1`$ at most, (8.20) there. So $`V_{x,k}\mapsto V_{x,k}+z`$ for all $`x`$, $`k`$ with one $`z`$ (only the offsets change, $`V_k\mapsto V_k+z`$), and $`C_{\rm loc}(x_0)\mapsto C_{\rm loc}(x_0)+z\mathbb 1`$. A change of the unit, $`\lambda'=\lambda/s`$ with $`s>0`$, replaces $`C`$ by $`sC`$ in (1.9). **[L]**:

```math
\text{(8.1)}:\ \ \Omega_\gamma\mapsto\Omega_\gamma,\ \ \rho_\gamma\mapsto\rho_\gamma;\qquad\qquad \lambda\mapsto\lambda/s:\ \ \Omega_\gamma\mapsto s\,\Omega_\gamma,\ \ \rho_\gamma\mapsto\rho_\gamma .
\qquad\text{(6.9)}
```

Gaps are well defined under (8.1), and under a change of the unit only up to one common positive factor (their ratios are well defined). Responses are well defined under both: (6.3) is homogeneous of degree zero in $`C`$.

### Step 5. Common response inside one level (item 2(a))

**[L]**, one level $`k`$:

```math
\boxed{\;\text{all admissible gaps inside the level }k\text{ have a common response}\iff G_k=M_k\,g_{\zeta,k};\qquad\text{its value is }g_{\zeta,k}=u_k\;}
\qquad\text{(6.10)}
```

- ($`\Leftarrow`$) If $`u_k=g_{\zeta,k}`$, (6.4) gives $`\rho_\gamma=g_{\zeta,k}`$ for both branches and all $`p`$, $`p'`$.
- ($`\Rightarrow`$) The branch gap and the band gap are admissible ($`2M_k>0`$, $`W_k-M_k>0`$ since $`\tau_k>0`$). By (6.5), $`\rho_{\rm br}(k)-\rho_{\rm band}(k)=(u_k-g_{\zeta,k})(1+M_k/W_k)`$, which vanishes only if $`u_k=g_{\zeta,k}`$.

The condition does not contain $`\tau_k`$ (beyond $`\tau_k>0`$). Control: the variant (a), where $`u_k=g\neq0=g_\zeta`$.

### Step 6. Common response of all gaps (item 2(b))

**[L]**, with one real number $`c`$:

```math
\boxed{\;\text{all admissible gaps have the common response }g_*\iff G_k=g_*M_k,\quad g_{\zeta,k}=g_*,\quad \mathcal F_k+g_*V_k=c\qquad\forall k\;}
\qquad\text{(6.11)}
```

- ($`\Leftarrow`$) Then $`\delta\omega_k=g_*\omega_k`$ by (6.2), and the numerator of (6.3) is $`g_*(\sigma\omega_k-\sigma'\omega_{k'})+g_*(V_k-V_{k'})=g_*\Omega^0_\gamma`$.
- ($`\Rightarrow`$) The gaps inside each level have the common response $`g_*`$, so by (6.10) $`u_k=g_{\zeta,k}=g_*`$. For $`k\neq k'`$ the label $`(k,+,p;k',-,p')`$ has $`\Omega^0_\gamma=V_k-V_{k'}+\omega_k(p)+\omega_{k'}(p')`$, which is not constant in $`p`$ ($`\tau_k>0`$), so it is admissible for some $`p`$. For it, (6.3) equals $`g_*`$ only if $`-(\mathcal F_k-\mathcal F_{k'})=g_*(V_k-V_{k'})`$.

The general form of the profiles follows by inserting (6.11) into the linear profiles; the anticommutator reproduces $`\zeta_{x,k}=1+g_*(x+\tfrac12)`$ on the bond $`(x,x+1)`$. With $`C_b^0`$ the member with all gradients zero (level offsets included):

```math
M_{x,k}=(1+g_*x)\,M_k,\qquad \zeta_{x,k}=1+g_*(x+\tfrac12),\qquad V_{x,k}=(1+g_*x)\,V_k-c\,x;\qquad C_b=\tfrac12\bigl\{\mathbb 1+g_*\hat x,\ C_b^0\bigr\}-c\,\hat x .
\qquad\text{(6.12)}
```

One position factor multiplies the whole body contract, level offsets included, up to a term $`-c\,\hat x`$ common to all levels. For $`g_*\neq0`$ put $`V_\circ:=c/g_*`$; then $`\mathcal F_k=-g_*(V_k-V_\circ)`$. Under $`V_k\mapsto V_k+z`$ of Step 4, $`c\mapsto c+g_*z`$ and $`V_\circ\mapsto V_\circ+z`$: the condition and $`V_k-V_\circ`$ are well defined. Controls: the variant (a) (fails $`g_{\zeta,k}=g_*`$); a member with the first two conditions and $`\mathcal F_0+g_*V_0\neq\mathcal F_1+g_*V_1`$ (fails for the gaps between the levels $`0`$ and $`1`$).

### Step 7. The class $`\mathcal C`$ (item 2(c))

**[C]**. Insert $`G_k=m\,g_m+d_kg_\eta`$, $`M_k=m+d_k`$ into (6.10), (6.11) and use $`d_0=0`$, $`d_1\neq0`$, $`m>0`$; the third condition of (6.11) holds identically, since $`\mathcal F_k=\mathcal F`$ and $`V_k=0`$:

```math
\begin{aligned}
\text{level }k\text{ alone has a common response}&\iff m\,(g_m-g_\zeta)+d_k\,(g_\eta-g_\zeta)=0;\\
\text{every level has one}\iff\text{all admissible gaps have a common response}&\iff g_m=g_\eta=g_\zeta\ (=g_*),\quad\mathcal F\ \text{arbitrary}.
\end{aligned}
\qquad\text{(6.13)}
```

By (6.5), $`\rho_{\rm lev}=g_\eta`$, $`\rho_{\rm br}(k)=(m\,g_m+d_kg_\eta)/M_k`$, $`\rho_{\rm band}(k)=g_\zeta-\tfrac{M_k}{W_k}(\rho_{\rm br}(k)-g_\zeta)`$, with $`W_k=\sqrt{M_k^2+\tau^2}`$. For $`g\neq0`$ (in (d): $`\mathcal F\neq0`$):

```math
\begin{array}{l|c|c|c|l}
\text{variant}&\rho_{\rm lev}&\rho_{\rm br}(k)&\rho_{\rm band}(k)&\text{equal responses}\\\hline
\text{(a)}&g&g&-\frac{M_k}{W_k}g&\text{level}=\text{branch}\neq\text{band}\\
\text{(b1)}&0&\frac{m\,g}{M_k}&-\frac{m\,g}{W_k}&\text{none}\\
\text{(b2)}&g&\frac{d_kg}{M_k}&-\frac{d_kg}{W_k}&\text{none for }k\ge1;\ \ k=0:\ \text{branch}=\text{band}=0\neq\text{level}\\
\text{(c)}&g&g&g&\text{all three}\\
\text{(d)}&0&0&0&\text{all three (zero)}\\
\text{(f)}&g&g&-\frac{M_k}{W_k}g&\text{level}=\text{branch}\neq\text{band}
\end{array}
\qquad\text{(6.14)}
```

### Step 8. The exact form (item 2(d))

**[L]** (only the values of the profiles at $`x_0`$ and $`x_1`$ enter; no expansion):

```math
\exists\,\nu:\ \Omega_\gamma(x_1)=\nu\,\Omega_\gamma(x_0)\ \ \forall\gamma\iff\exists\,\nu>0,\ c'\in\mathbb R:\ \ M_{x_1,k}=\nu M_{x_0,k},\ \ \zeta^0_k(x_1)=\nu\,\zeta^0_k(x_0),\ \ V_{x_1,k}=\nu V_{x_0,k}+c'\ \ \forall k\iff C_{\rm loc}(x_1)=\nu\,C_{\rm loc}(x_0)+c'\,\mathbb 1 .
\qquad\text{(6.15)}
```

- ($`\Leftarrow`$) Then $`\omega_k(p;x_1)=\nu\,\omega_k(p;x_0)`$ and $`\varepsilon_{k,\sigma}(p;x_1)=\nu\,\varepsilon_{k,\sigma}(p;x_0)+c'`$; every gap is multiplied by $`\nu`$.
- ($`\Rightarrow`$) The labels $`(k,+,p;k,-,p)`$ give $`\omega_k(p;x_1)=\nu\,\omega_k(p;x_0)`$ for all $`p`$, so $`\nu>0`$; at $`p=0`$ and $`p=\tfrac\pi2`$ this gives the first two conditions (all quantities are positive). A label between the levels $`k\neq k'`$ then gives $`V_{x_1,k}-V_{x_1,k'}=\nu(V_{x_0,k}-V_{x_0,k'})`$.
- The last equivalence holds because the on-site block of the level $`k`$ of $`C_{\rm loc}(x_0)`$ is $`M_{x_0,k}\sigma_3+V_{x_0,k}\mathbb 1_2`$ and its hopping factor is $`\tau_k\zeta^0_k(x_0)`$.

The linear profiles (6.12) satisfy (6.15) exactly for every pair, with $`\nu=(1+g_*x_1)/(1+g_*x_0)`$.

### Step 9. Common response and fall (item 3(a))

**[L]** with (6.11) and $`g_*\neq0`$. Inserting $`G_k=g_*M_k`$ and $`\mathcal F_k=-g_*(V_k-V_\circ)`$ into (4.16):

```math
\boxed{\;a_{k,\sigma}(0)=-\tau_k^2\Bigl(g_*-\sigma\frac{\mathcal F_k}{M_k}\Bigr)=-g_*\,\tau_k^2\,\frac{M_k+\sigma\,(V_k-V_\circ)}{M_k}\;}
\qquad\text{(6.16)}
```

```math
\begin{aligned}
a_{k,+}(0)=a_+\ \forall k&\iff\tau_k^2\,\frac{M_k+V_k-V_\circ}{M_k}=-\frac{a_+}{g_*}\ \ \forall k,\qquad
a_{k,-}(0)=a_-\ \forall k\iff\tau_k^2\,\frac{M_k-V_k+V_\circ}{M_k}=-\frac{a_-}{g_*}\ \ \forall k,\\
\text{both, with }a_+=a_-=a&\iff V_k=V_\circ\ \text{ and }\ \tau_k=\tau\quad\forall k;\qquad\text{then }a=-g_*\tau^2 .
\end{aligned}
\qquad\text{(6.17)}
```

- The first two lines are (6.16) read in both directions (they are the first line of (4.19) with (6.11) inserted).
- Third line: by (4.19), both with one value $`\iff\mathcal F_k=0`$ and $`\tau_k^2u_k=-a`$ for all $`k`$. With $`u_k=g_*\neq0`$: $`\mathcal F_k=0\iff V_k=V_\circ`$, and $`\tau_k^2=-a/g_*`$ for all $`k`$ $`\iff`$ the positive numbers $`\tau_k`$ are equal. Conversely (6.16) gives $`-g_*\tau^2`$.
- The condition $`V_k=V_\circ`$ concerns the plain parts: every plain part is $`V_\circ\mathbb 1_2`$ at every position, a multiple of $`\mathbb 1`$. The condition $`\tau_k=\tau`$ concerns the numbers $`\tau_k`$. For one branch alone the two do not separate: one equation per level ties $`V_k-V_\circ`$ to $`\tau_k`$.
- Controls. [C] with $`g_m=g_\eta=g_\zeta=g\neq0`$ and $`\mathcal F\neq0`$ (the variant (c) with a constant under the factor, $`V_\circ=\mathcal F/g`$): common response $`g`$ by (6.13), but $`a_{k,\sigma}(0)=-\tau^2g+\sigma\tau^2\mathcal F/M_k`$ depends on the level. A member with $`V_k=V_\circ`$ and $`\tau_0\neq\tau_1`$: $`a_{k,\sigma}(0)=-g_*\tau_k^2`$. The variant (d) (common response $`0`$): $`a_{k,\sigma}(0)=\sigma\tau^2\mathcal F/M_k\neq0`$, a fall without any response.

### Step 10. The converse (item 3(b))

**[L]**. By (4.19) and (6.5), for $`a\neq0`$:

```math
a_{k,+}(0)=a_{k,-}(0)=a\ \ \forall k\iff\mathcal F_k=0\ \text{ and }\ \rho_{\rm br}(k)=-\frac{a}{\tau_k^2}\quad\forall k .
\qquad\text{(6.18)}
```

Under this hypothesis, (6.3) with $`\delta\omega_k(0)=\delta\omega_k(\pi)=G_k=-aM_k/\tau_k^2`$ gives for the rest labels

```math
\rho_\gamma=-a\,\frac{\sigma M_k/\tau_k^2-\sigma'M_{k'}/\tau_{k'}^2}{V_k-V_{k'}+\sigma M_k-\sigma'M_{k'}};\qquad\text{all admissible rest gaps have a common response}\iff\tau_k=\tau\ \text{and}\ V_k\ \text{level-independent};\quad\text{value }-\frac a{\tau^2}.
\qquad\text{(6.19)}
```

In (6.19) the condition $`\mathcal F_k=0`$ is in force, by the hypothesis (6.18). This is why the condition on the level offsets has the form "$`V_k`$ level-independent": with $`\mathcal F_k=0`$ it says that every plain part is the same multiple of $`\mathbb 1_2`$ at all positions and in all levels. No $`V_\circ`$ is defined here, since (6.11) is not assumed.

- ($`\Leftarrow`$) is read off. ($`\Rightarrow`$) The branch gaps give $`-a/\tau_k^2`$, so $`\tau_k=\tau`$. For $`k\neq k'`$ one of the labels $`(k,+,0;k',-,0)`$, $`(k',+,0;k,-,0)`$ is admissible ($`\Omega^0=\pm(V_k-V_{k'})+M_k+M_{k'}`$), and its response is $`-a/\tau^2`$ only if $`V_k=V_{k'}`$.
- What follows from the hypothesis alone: the branch gap of each level responds with $`-a/\tau_k^2`$. In the subclass $`\tau_k=\tau`$ with equal level offsets, which contains [C], all rest gaps (branch gaps and level gaps) have the common response $`-a/\tau^2`$, with $`\mathcal F_k=0`$ from (6.18).
- What need not: every gap with a moving label, since by (6.4) it needs $`g_{\zeta,k}=u_k`$ and $`g_{\zeta,k}`$ does not enter (4.16); the branch gaps of different levels when the $`\tau_k`$ differ; the gaps between levels when the $`V_k`$ differ (here $`\mathcal F_k=0`$, so nothing in the numerator of (6.3) matches $`V_k-V_{k'}`$ in its denominator).
- Control: the variant (a). $`a_{k,\pm}(0)=-\tau^2g`$ for all $`k`$ by (4.25), and $`\rho_{\rm band}(k)=-\tfrac{M_k}{W_k}g\neq g=\rho_{\rm br}(k)`$ by (6.14). Further controls: $`\mathcal F_k=0`$, $`G_k=-aM_k/\tau_k^2`$ with $`\tau_0\neq\tau_1`$, or with $`V_0\neq V_1`$.

### Step 11. The order $`v^2`$ (item 3(c))

**[L]** with (6.11), $`g_*\neq0`$. (4.17) gives $`c_{2,k,\sigma}=2g_*\bigl(1+\tfrac{M_k^2}{\tau_k^2}\bigr)-\sigma\tfrac{\mathcal F_k}{M_k}\bigl(\tfrac32+\tfrac{2M_k^2}{\tau_k^2}\bigr)`$. With the further conditions of the third line of (6.17):

```math
c_{2,k,\sigma}=2g_*\Bigl(1+\frac{M_k^2}{\tau^2}\Bigr),\qquad a_{k,\sigma}=-g_*\tau^2+2g_*\Bigl(1+\frac{M_k^2}{\tau^2}\Bigr)v^2+O(v^4)\qquad\text{(both branches)} .
\qquad\text{(6.20)}
```

Through the order $`v^2`$ the fall is the same for all levels exactly $`\iff`$ the numbers $`M_k`$ are equal; so exactly no as soon as two levels differ in $`M_k`$ (always in [C]). To leading order in $`M_k/\tau`$ yes: $`c_{2,k,\sigma}=2g_*\,[1+O(M_k^2/\tau^2)]`$.

### Step 12. Answer to criterion 4 (item 3(d))

**[L]**. From (6.11), (6.17), (6.18): for $`g_*\neq0`$, $`a\neq0`$ and $`a=-g_*\tau^2`$, with $`V_\circ=c/g_*`$ of Step 6 on the left side,

```math
\Bigl[\text{(6.11)}\Bigr]\wedge\Bigl[V_k=V_\circ,\ \ \tau_k=\tau\ \ \forall k\Bigr]\iff\Bigl[a_{k,\pm}(0)=a\ \forall k\Bigr]\wedge\Bigl[\tau_k=\tau,\ \ g_{\zeta,k}=-\tfrac a{\tau^2}\ \forall k,\ \ V_k\ \text{level-independent}\Bigr].
\qquad\text{(6.21)}
```

Both sides are the members with $`\tau_k=\tau`$, $`G_k=g_*M_k`$, $`g_{\zeta,k}=g_*`$, $`\mathcal F_k=0`$ and equal level offsets:
- Left $`\Rightarrow`$ right. Under (6.11), $`\mathcal F_k=-g_*(V_k-V_\circ)`$, so $`V_k=V_\circ\iff\mathcal F_k=0`$, and the level offsets are then equal. The third line of (6.17) gives $`a_{k,\pm}(0)=-g_*\tau^2=a`$, and $`g_{\zeta,k}=g_*=-a/\tau^2`$.
- Right $`\Rightarrow`$ left. (6.18) gives $`\mathcal F_k=0`$ and $`u_k=-a/\tau^2=g_*`$, and $`g_{\zeta,k}=g_*`$ is assumed. With $`\mathcal F_k=0`$ the third condition of (6.11) reads $`g_*V_k=c`$, which holds because the level offsets are equal. Then $`V_\circ=c/g_*=V_k`$.
- The three forms of the condition on the level offsets. Under (6.11) alone, with $`g_*\neq0`$: "$`V_k=V_\circ`$" is $`\mathcal F_k=0`$, while "$`V_k`$ level-independent" is only "$`\mathcal F_k`$ level-independent"; it leaves a common $`\mathcal F_k=c-g_*V_k`$, which need not vanish. Where $`\mathcal F_k=0`$ is in force (by (6.18) on the right side of (6.21) and in (6.19); as a listed condition in (6.25)), the level offsets enter as "$`g_*V_k`$ level-independent", the third condition of (6.11) with $`\mathcal F_k=0`$. For $`g_*\neq0`$ this is "$`V_k`$ level-independent", and it is then the same as $`V_k=V_\circ`$.
- Check against the controls. First control of Step 9 ([C], $`g_m=g_\eta=g_\zeta=g\neq0`$, $`\mathcal F\neq0`$): (6.11) and $`\tau_k=\tau`$ hold and the level offsets are equal ($`V_k=0`$), but $`V_\circ=\mathcal F/g\neq V_k`$. The left side fails, and so does the right, since $`a_{k,\sigma}(0)=-\tau^2g+\sigma\tau^2\mathcal F/M_k`$. Second control of Step 9 ($`V_k=V_\circ`$, $`\tau_0\neq\tau_1`$): both sides fail in $`\tau_k=\tau`$. Controls of Step 10: the variant (a) fails $`g_{\zeta,k}=-a/\tau^2`$ on the right and (6.11) on the left; the member with $`\tau_0\neq\tau_1`$ fails $`\tau_k=\tau`$ on both sides; the member with $`V_0\neq V_1`$ and $`\mathcal F_k=0`$ fails the right side and the third condition of (6.11).

The answer, in each direction:
- **From a common response to the fall.** A common response $`g_*\neq0`$ of all periodic processes does not imply a fall that is the same for all levels, neither in one branch nor in both (first control of Step 9). For both branches with one value it does exactly when, in addition, $`V_k=V_\circ`$ for all $`k`$ and the $`\tau_k`$ are equal (third line of (6.17)); $`V_k=V_\circ`$ is $`\mathcal F_k=0`$, that is, the plain part of every level is $`V_\circ\mathbb 1_2`$ at every position. For one branch $`\sigma`$ alone it does exactly when $`\tau_k^2\,\bigl(M_k+\sigma(V_k-V_\circ)\bigr)/M_k`$ is the same for all $`k`$ (first two lines of (6.17)). This is weaker: with $`\tau_k=\tau`$ and $`V_k-V_\circ=\delta M_k`$ for one number $`\delta\neq0`$, each branch falls alike in all levels, with the two different values $`-g_*\tau^2(1\pm\delta)`$.
- **From the fall to a common response.** A fall that is the same for all levels in both branches with one value $`a\neq0`$ does not imply a common response (controls of Step 10). It does exactly when, in addition, the $`\tau_k`$ are equal, $`g_{\zeta,k}=-a/\tau^2`$ in every level and the level offsets are equal. Here $`\mathcal F_k=0`$ holds by (6.18), which is why equal level offsets are the correct form. Each further condition is necessary, by (6.11). For one branch $`\sigma`$ alone the hypothesis $`a_{k,\sigma}(0)=a_\sigma`$ for all $`k`$ is $`G_k-\sigma\mathcal F_k=-a_\sigma M_k/\tau_k^2`$ by (4.16); it does not give $`\mathcal F_k=0`$, and the further condition is (6.11) itself. The members with a common response $`g_*\neq0`$ and a level-independent fall in the branch $`\sigma`$ are those of (6.11) with the line $`\sigma`$ of (6.17).

### Step 13. The relation behind (4.24) (item 4(a))

**[L]**. In (4.18) write $`\delta E^\sigma_k=\tfrac\sigma2\delta\Delta_k+\tfrac12(\delta E^+_k+\delta E^-_k)`$, and use $`\delta\Delta_k/\Delta_k=G_k/M_k=\rho_{\rm br}(k)`$, $`\delta E^+_k+\delta E^-_k=-2\mathcal F_k`$, $`2\bar t_k=\tau_k`$:

```math
\boxed{\;a_{k,\sigma}(0)=-(2\bar t_k)^2\Bigl[\frac{\delta\Delta_k}{\Delta_k}+\sigma\,\frac{\delta E^+_k+\delta E^-_k}{\Delta_k}\Bigr]=-\tau_k^2\Bigl[\rho_{\rm br}(k)-\sigma\,\frac{\mathcal F_k}{M_k}\Bigr],\qquad\tfrac12\bigl[a_{k,+}(0)+a_{k,-}(0)\bigr]=-\tau_k^2\,\rho_{\rm br}(k)\;}
\qquad\text{(6.22)}
```

Both equations are identities for every member of [L]: no condition on the gradients, the offsets or the $`\tau_k`$. The mean of the falls of the two branches is $`-\tau_k^2`$ times the response of the branch gap of the same level. The term that is odd in the branch vanishes if and only if $`\delta E^+_k+\delta E^-_k=0`$, that is $`\mathcal F_k=0`$: no gradient of the plain part.

### Step 14. The relation with a given gap (item 4(b))

**[L]**. For a branch $`\sigma`$ and a named gap, the relation (4.24) with the response of that gap in the place of $`\bigl(r(x+1)-r(x)\bigr)/r(x)`$ is

```math
R^\sigma_\gamma:\qquad a_{k,\sigma}(0)=-\tau_k^2\,\rho_\gamma\ \ \text{for all levels }k,\qquad\text{in space:}\ \ \frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=-\frac{v_k^2}{d_0}\,\rho_\gamma\,\hat e,\quad v_k:=\tau_kd_0 ,
\qquad\text{(6.23)}
```

with $`\gamma=\gamma_{\rm br}(k)`$ or $`\gamma_{\rm band}(k)`$ of the same level, or with every level gap $`\gamma_{\rm lev}(j)`$, $`j\le N-2`$. The necessary and sufficient conditions:

```math
\begin{array}{l|l|l}
\text{gap}&\text{one branch }\sigma&\text{both branches}\\\hline
\gamma_{\rm br}(k)&\mathcal F_k=0\ \ \forall k&\mathcal F_k=0\ \ \forall k\\
\gamma_{\rm band}(k)&\sigma\,\mathcal F_k=(G_k-M_kg_{\zeta,k})\bigl(1+\tfrac{M_k}{W_k}\bigr)\ \ \forall k&\mathcal F_k=0,\ \ G_k=M_kg_{\zeta,k}\ \ \forall k\\
\gamma_{\rm lev}(j)&\exists\,g_\ell:\ G_k-\sigma\mathcal F_k=g_\ell M_k\ \forall k,\ \ (1-\sigma)\mathcal F_k+g_\ell V_k\ \text{level-independent}&\exists\,g_\ell:\ \mathcal F_k=0,\ G_k=g_\ell M_k\ \forall k,\ \ g_\ell V_k\ \text{level-independent}
\end{array}
\qquad\text{(6.24)}
```

- Branch gap: by (6.22), $`a_{k,\sigma}(0)+\tau_k^2\rho_{\rm br}(k)=\sigma\tau_k^2\mathcal F_k/M_k`$, zero if and only if $`\mathcal F_k=0`$.
- Band gap: by (6.22), $`R^\sigma_{\rm band}\iff\rho_{\rm br}(k)-\rho_{\rm band}(k)=\sigma\mathcal F_k/M_k`$, and $`\rho_{\rm br}(k)-\rho_{\rm band}(k)=(u_k-g_{\zeta,k})(1+M_k/W_k)`$ by (6.5). For both signs: $`\mathcal F_k=0`$, and then $`u_k=g_{\zeta,k}`$ since $`1+M_k/W_k>0`$.
- Level gap, ($`\Rightarrow`$): put $`g_\ell:=\rho_{\rm lev}(0)`$; then $`a_{k,\sigma}(0)=-\tau_k^2g_\ell`$ is $`G_k-\sigma\mathcal F_k=g_\ell M_k`$ by (4.16). Inserting $`G_k=g_\ell M_k+\sigma\mathcal F_k`$ into (6.5), $`\rho_{\rm lev}(j)=g_\ell`$ becomes $`(\sigma-1)(\mathcal F_{j+1}-\mathcal F_j)=g_\ell(V_{j+1}-V_j)`$ for all $`j`$. ($`\Leftarrow`$): the same two steps backwards. Both branches: add and subtract the conditions of $`\sigma=\pm`$.
- In [C] the row $`\gamma_{\rm lev}`$, $`\sigma=+`$ reads $`g_\ell=g_\eta`$, $`\mathcal F=m(g_m-g_\eta)`$: the hypothesis of (4.24), by (4.22).
- Form of the conditions on the level offsets. In the column of both branches, $`\mathcal F_k=0`$ is part of every condition, and the level offsets enter only the row $`\gamma_{\rm lev}`$, as "$`g_\ell V_k`$ level-independent": equal level offsets for $`g_\ell\neq0`$, no condition for $`g_\ell=0`$. In the column of one branch, $`\mathcal F_k`$ is not zero in general, and the level offsets enter only together with it, as $`(1-\sigma)\mathcal F_k+g_\ell V_k`$: for $`\sigma=+`$ this is "$`g_\ell V_k`$ level-independent" with $`\mathcal F_k=G_k-g_\ell M_k`$ not restricted further, for $`\sigma=-`$ it is "$`2\mathcal F_k+g_\ell V_k`$ level-independent". No $`V_\circ`$ occurs in (6.24), since (6.11) is not assumed there.

With the response of every admissible gap, for one branch or both:

```math
\boxed{\;R^\sigma_\gamma\ \text{for every admissible }\gamma\iff G_k=g_*M_k,\ \ g_{\zeta,k}=g_*,\ \ \mathcal F_k=0\ \ \forall k,\ \ g_*V_k\ \text{level-independent}\;}\qquad(g_*\neq0:)\quad C_b-V_\circ\mathbb 1=\tfrac12\bigl\{\mathbb 1+g_*\hat x,\ C_b^0-V_\circ\mathbb 1\bigr\} .
\qquad\text{(6.25)}
```

- ($`\Rightarrow`$) The left side of $`R^\sigma_\gamma`$ does not depend on $`\gamma`$, so all admissible gaps have one response $`g_*`$: (6.11). Then (6.22) with $`\rho_{\rm br}(k)=g_*`$ gives $`\mathcal F_k=0`$, and the third condition of (6.11) becomes $`g_*V_k=c`$. ($`\Leftarrow`$) (6.11) holds with $`c=g_*V_k`$, and (6.16) gives $`a_{k,\sigma}(0)=-\tau_k^2g_*`$.
- In (6.25) $`\mathcal F_k=0`$ is one of the conditions; with it the third condition of (6.11) has the form "$`g_*V_k`$ level-independent". For $`g_*\neq0`$ the level offsets are therefore equal, and equal to $`V_\circ=c/g_*`$: this is $`V_k=V_\circ`$, the condition of the third line of (6.17) without $`\tau_k=\tau`$. The operator identity displayed in (6.25) is (6.12) with $`c=g_*V_\circ`$, and it holds for every member of (6.11) with $`g_*\neq0`$. What $`\mathcal F_k=0`$ adds is that the level blocks of $`C_b^0-V_\circ\mathbb 1`$ have the spectrum $`\pm\omega_k(p)`$: the factor multiplies the body contract measured from the common symmetry point of the spectra of its level blocks. The numbers $`\tau_k`$ may differ.
- So (4.24) rests on two facts for both branches: the identity (6.22), which ties the fall to the branch gap of the same level when $`\mathcal F_k=0`$; and the equality of the response of the level gap with that of the branch gap, which is a condition on the contract (the row $`\gamma_{\rm lev}`$).

### Step 15. Speeds and orders (items 4(c), 4(d))

**Speeds.** [L], at zero gradients (the order needed in a first-order relation). The hopping part of $`C_b`$ has the matrix elements $`\mp\tfrac i2(\sigma_1)_{s's}T_{a'a}`$ between $`(x,s,a)`$ and $`(x\pm1,s',a')`$, with $`T:=\sum_k\tau_k\lvert f_k\rangle\langle f_k\rvert`$ and $`T_{a'a}=\tfrac1N\sum_k\tau_ke^{2\pi ik(a'-a)/N}`$. Places with equal $`x`$ have the distance $`0`$, neighbours $`d_0=\kappa\sigma_X`$ by (17.15) of 03-ilang-space/17-motion. The formula (5.11) of 04-ilang-time/05-moving-clock gives

```math
v_{\max}=d_0\,\tau_{*},\qquad\tau_{*}:=\sum_{n=0}^{N-1}\Bigl\lvert\frac1N\sum_{k=0}^{N-1}\tau_k\,e^{2\pi ikn/N}\Bigr\rvert\ \ge\ \max_k\tau_k,\qquad v_k=\tau_kd_0\le v_{\max} .
\qquad\text{(6.26)}
```

The inequality follows from $`\tau_k=\sum_nT_{n0}\,e^{-2\pi ikn/N}`$. The relation of the level $`k`$ contains the level speed $`v_k`$ (the value of the same formula for the level block $`C^{(k)}_0`$ on the places $`(x,s)`$), not the bound $`v_{\max}`$ of the body. All levels contain $`v_{\max}`$ if and only if $`\tau_k=\tau`$ for all $`k`$; then $`\tau_{*}=\tau`$.

**Orders.** For each relation of (6.24), (6.25):
- Gradients: first order. $`a_{k,\sigma}(0)`$ and $`\rho_\gamma`$ are first-order coefficients and the relation between them is exact; the second order is not determined here.
- Drift velocity: zeroth order in $`v`$. By (4.17) the correction is $`c_{2,k,\sigma}v^2+O(v^4)`$; under (6.25)

```math
a_{k,\sigma}=-\tau_k^2\,g_*\Bigl[1-\frac{2v^2}{\tau_k^2}\Bigl(1+\frac{M_k^2}{\tau_k^2}\Bigr)\Bigr]+O(v^4),
\qquad\text{(6.27)}
```

  with a level-dependent part of relative order $`v^2M_k^2/\tau_k^4`$. The window and the spread add the errors of (4.10), (4.11).
- $`M_k/\tau_k`$: no expansion; at rest the relations are exact in the level data. Only the level-independence of the $`v^2`$ term holds to leading order in $`M_k/\tau_k`$.
- $`\kappa`$: leading order (weak-record regime). In the space form both sides are of the order $`\kappa^1`$ through $`d_0`$; the next order is not determined here.

### Step 16. Control: where the factor sits (item 5)

**[C]**, $`g\neq0`$, in (f) $`c_{\rm f}\neq0`$; $`R^\pm`$ means the relation (6.23) for both branches and all levels. From (6.14), (4.25), (6.24):

```math
\begin{array}{l|c|c|c|c|c|c|c|c}
\text{variant}&\rho_{\rm lev}&\rho_{\rm br}(k)&\rho_{\rm band}(k)&a_{k,+}(0)&a_{k,-}(0)&R^\pm_{\rm lev}&R^\pm_{\rm br}&R^\pm_{\rm band}\\\hline
\text{(a)}&g&g&-\frac{M_k}{W_k}g&-\tau^2g&-\tau^2g&\text{yes}&\text{yes}&\text{no}\\
\text{(c)}&g&g&g&-\tau^2g&-\tau^2g&\text{yes}&\text{yes}&\text{yes}\\
\text{(f)}&g&g&-\frac{M_k}{W_k}g&-\tau^2g\bigl(1+\frac{c_{\rm f}}{M_k}\bigr)&-\tau^2g\bigl(1-\frac{c_{\rm f}}{M_k}\bigr)&\text{no}&\text{no}&\text{no}
\end{array}
\qquad\text{(6.28)}
```

In (f) each relation fails for a single branch as well: $`\mathcal F=-c_{\rm f}g\neq0`$ violates the rows of (6.24) for all levels ($`M_0\neq M_1`$). In all three variants the level offsets are equal ($`V_k=0`$ in [C]), so every condition of (6.24) on the level offsets holds in each of them; (f) differs from (a) only in $`\mathcal F`$, which is zero in (a) and (c) and not zero in (f). Equal level offsets together with $`\mathcal F\neq0`$ are not the condition $`\mathcal F_k=0`$ of (6.24), (6.25). The variants (a) and (c) agree in the level gap, the branch gap and the fall from rest of both branches. They differ in every gap with a moving label. In one body the ratio of the band gap to the level gap changes from place to place at the relative rate $`\rho_{\rm band}-\rho_{\rm lev}=-g\,(1+M_k/W_k)`$ in (a) and $`0`$ in (c); the two readings of (6.7) show it. They also differ in the $`v^2`$ coefficient of the fall, $`g\,\ell_k`$ against $`g\,(1+\ell_k)`$ in (4.25).

## Result

All results are for the class [L], except (6.6), (6.13), (6.14), (6.28), which are for [C].
- **Item 1.** Response of a general gap (6.3), inside one level (6.4); named gaps (6.5); in [C] the level gap is $`2\pi/N`$ times the rate (6.6). Readings that contain the level gap and the band gap (6.7); none contains the branch gap (6.8). Gaps are defined up to the unit of $`\lambda`$, responses are well defined (6.9).
- **Item 2.** One level: $`G_k=M_kg_{\zeta,k}`$ (6.10). All gaps: (6.11), with the profiles (6.12). Class $`\mathcal C`$: $`g_m=g_\eta=g_\zeta`$, $`\mathcal F`$ arbitrary (6.13), variants (6.14). Exact form: $`C_{\rm loc}(x_1)=\nu\,C_{\rm loc}(x_0)+c'\mathbb 1`$ (6.15).
- **Item 3.** Fall under a common response (6.16), three equivalences (6.17). Converse (6.18), (6.19), with the variant (a) as control. Order $`v^2`$ (6.20). Criterion 4: neither property implies the other, in one branch or in both. For both branches with one value, a common response $`g_*\neq0`$ gives the fall exactly with $`V_k=V_\circ`$ (that is $`\mathcal F_k=0`$) and $`\tau_k=\tau`$, and the fall gives a common response exactly with $`\tau_k=\tau`$, $`g_{\zeta,k}=-a/\tau^2`$ and equal level offsets; the two sets of members are the same, (6.21). For one branch $`\sigma`$ the further condition under a common response is the line $`\sigma`$ of (6.17).
- **Item 4.** Identity (6.22). The relation (6.23) holds with a named gap under (6.24), and with every gap under (6.25). Bound and level speed (6.26); orders, with (6.27).
- **Item 5.** Table (6.28).

## Consistency checks

1. **Units and zero gradients.** Under $`C\mapsto sC`$: $`\rho_\gamma`$ has degree $`0`$, $`a_{k,\sigma}(0)=\tfrac{\tau_k^2}{M_k}(\sigma\mathcal F_k-G_k)`$ and $`\tau_k^2\rho_\gamma`$ have degree $`2`$ (position labels per $`\lambda^2`$), so (6.22), (6.23) are homogeneous. With all gradients zero, (6.3) and (4.16) give $`\rho_\gamma=0`$ and $`a_{k,\sigma}(0)=0`$. Passed.
2. **Variant (c) against an exact rescaling.** There $`C_{\rm loc}(x_0)=(1+gx_0)\,C_{\rm loc}(0)`$ exactly, so every gap at $`x_0=1`$ is $`(1+g)`$ times the gap at $`0`$ and $`\rho_\gamma=g`$ for every label. (6.3) with $`\delta\omega_k=g\,\omega_k`$, $`\mathcal F=0`$, $`V_k=0`$ gives the same, and (6.15) holds with $`\nu=1+gx_0`$. Passed.
3. **$`\tau_k\to0`$.** The band gap tends to $`\tau_k^2\zeta^0_k(x_0)^2/(2M_{x_0,k})`$, whose relative first-order change between $`x_0=0`$ and $`1`$ is $`2g_{\zeta,k}-u_k`$; (6.5) with $`W_k\to M_k`$ gives $`g_{\zeta,k}-(u_k-g_{\zeta,k})`$, the same. A body that cannot hop does not fall, $`a_{k,\sigma}(0)\to0`$ in (6.22), while $`\rho_{\rm br}(k)`$ stays finite, in agreement with $`v_k\to0`$ in (6.23). Passed.

## Open issues

- Item 1(c) asked for a start and a reading for each named gap. For the branch gap none exists, (6.8): the term with the label $`\gamma_{\rm br}(k)`$ has the coefficient zero in every reading of a body that evolves by the local member. The gap is reached only as the limit $`p_0\to0`$ of the frequencies $`2\omega_k(p_0)`$, with a vanishing coefficient. The identity (6.22) therefore ties the fall to a gap that is not a process in the sense of the definition of this package. Whether a reading in a larger description (a record object, A8) shows it is not examined.
- The statistics (6.7) are limits of a sharp label at fixed $`\lambda`$; the rate of convergence is not estimated.
- Readings of the question fixed here: "the relation holds for all levels with the level gap" is taken for every pair of a level $`k`$ and a level gap $`\gamma_{\rm lev}(j)`$; the relation of the level $`k`$ is written with $`v_k=\tau_kd_0`$; $`v_{\max}`$ in (6.26) is evaluated at zero gradients.
- Statements about level gaps assume that the level gaps are not zero at zero gradients.
- Not treated (out of scope): the second order in the gradients, starts in a superposition of levels, records beyond the leading order in $`\kappa`$, a field object.
- M10: the results state what members of $`\mathcal C_{\rm lev}`$ give; they do not show that the language selects the members of (6.25).

## Methods used

- First-order perturbation of the eigenvalues of a $`2\times2`$ block family
- Spectral decomposition of reading statistics (gaps of a self-driven part)
- Linear algebra of the conditions (both directions of each equivalence)
- Invariance analysis under contract replacements and rescaling of $`\lambda`$
- Discrete Fourier transform on $`\mathbb Z_N`$ (circulant hopping matrix)
- Limiting cases and homogeneity checks
