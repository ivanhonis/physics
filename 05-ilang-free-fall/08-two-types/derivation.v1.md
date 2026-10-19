# Two types of bodies in one background: equal fall and equal clock response

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-11

## Setup and assumptions

**Setting (assumptions of this package, M8).** Objects $`b_1`$, $`b_2`$, $`c`$ (and $`f`$ in Step 5) of pairwise different types, one instance each; no swap condition applies and every unit vector is an admissible start. The contract is $`C=F_1+F_2`$ with $`F_i:=C_i+\kappa_i\,\hat x_i\otimes X`$, $`\kappa_i>0`$, and $`C_i`$ of the class $`\mathcal C`$ of 03-clock-and-fall: data $`\tau_i>0`$, $`m_i>0`$, $`N_i\ge2`$, $`\lambda_{0,i}>0`$, linear profiles with the gradients $`g_{m,i}`$, $`g_{\eta,i}`$, $`g_{\zeta,i}`$, $`\mathcal F_i`$ on a chain $`\lvert x\rvert\le L`$, $`L\ge1`$. The start is a product with the medium in $`\chi`$, $`\sigma_X>0`$. All profiles are those of $`C^{\rm eff}_i=C_i+\kappa_i\langle X\rangle\hat x_i`$, (8.19) of 04-ilang-time/08-maximal-speed; so $`\mathcal F_i=\mathcal F^{\rm own}_i-\kappa_i\langle X\rangle`$, with $`\mathcal F^{\rm own}_i`$ the gradient written in $`C_i`$.

**Quoted inputs and the quantities built from them.**
- (17.15) of 03-ilang-space/17-motion: $`u^{(i)}_x=\kappa_i\,x\,e`$, $`d_{0,i}=\kappa_i\sigma_X`$, $`\hat e=e/\sigma_X`$. (5.11) of 04-ilang-time/05-moving-clock at zero gradients: $`v_i=\tau_i\,d_{0,i}`$.
- (3.23): $`r_i(x)=\eta^{(i)}_x/\lambda_{0,i}`$ with $`\eta^{(i)}_x=1+g_{\eta,i}x`$ (wide start $`S_{\rm clock}(x)`$).
- (4.16): $`a^{(i)}_{k,\sigma}(0)=\frac{\tau_i^2}{M^{(i)}_k}\bigl(\sigma\mathcal F_i-G^{(i)}_k\bigr)`$, $`M^{(i)}_k=m_i+d^{(i)}_k`$, $`G^{(i)}_k=m_ig_{m,i}+d^{(i)}_kg_{\eta,i}`$, $`d^{(i)}_k=\frac{2\pi k}{N_i\lambda_{0,i}}`$; $`A^{(i)}_{k,\sigma}:=d_{0,i}\,a^{(i)}_{k,\sigma}(0)`$. Also (4.22), (4.24).
- (5.19), (5.20), (5.25) of 05-rate-comparison; (2.3), (2.20) of 02-field-object; (8.1), (8.20) of 04-ilang-time/08-maximal-speed.

**Regime and orders (A13).** Branch starts at rest; first order in the gradients ($`\lvert g\rvert L\ll1`$); the drift acceleration of (4.16) (window average, then a sharp label); records at leading order in $`\kappa_i`$; rates in the wide-start form; $`\lambda\ge0`$.

**Names.** $`(\mathrm L_i)`$: $`\mathcal F_i=m_i(g_{m,i}-g_{\eta,i})`$. FA: the two types fall alike from rest. RL, RD: the clocks respond alike per label, per distance. A tag $`(8.k)`$ without a package name is a tag of this package; the three quoted tags of 04-ilang-time/08-maximal-speed always carry that name.

## Derivation

### Step 1. One type in the background (item 1)

**(a)** By (3.23), $`\bigl(r_i(x+1)-r_i(x)\bigr)/r_i(x)=g_{\eta,i}/(1+g_{\eta,i}x)`$, whose first order in the gradients does not depend on $`x`$. With (4.16):

```math
\varrho_i=g_{\eta,i},\qquad A^{(i)}_{k,\sigma}=\frac{d_{0,i}\,\tau_i^2}{M^{(i)}_k}\Bigl(\sigma\,\mathcal F_i-m_ig_{m,i}-d^{(i)}_kg_{\eta,i}\Bigr).
\qquad\text{(8.1)}
```

Since $`d_{0,i}>0`$, $`A^{(i)}_{k,+}`$ is level-independent exactly when $`a^{(i)}_{k,+}(0)`$ is. By (4.22) and $`v_i=\tau_id_{0,i}`$:

```math
A^{(i)}_{k,+}\ \text{the same for all }k\iff(\mathrm L_i):\ \mathcal F_i=m_i\,(g_{m,i}-g_{\eta,i});\qquad\text{value}\quad A^{(i)}=-d_{0,i}\,\tau_i^2\,g_{\eta,i}=-\frac{v_i^2}{d_{0,i}}\,\varrho_i .
\qquad\text{(8.2)}
```

**(b)** The three operations act as follows.
- *(8.1) of 04-ilang-time/08-maximal-speed.* By (8.20) of 04-ilang-time/08-maximal-speed, $`C^{\rm eff}_i\to C^{\rm eff}_i\pm\langle Z\rangle\mathbb 1`$: $`V^{(i)}_x`$ gets a constant, and no gradient and no off-diagonal entry changes. The record vectors become $`u^{(i)}_x\pm(Z-\langle Z\rangle)\chi`$, the same shift for all positions of a type, so all differences $`u^{(i)}_x-u^{(i)}_{x'}`$ and $`d_{0,i}`$ are unchanged. Hence none of the eight quantities changes; $`\kappa_i`$ is defined only together with $`X`$.
- *Unit of $`\lambda`$.* Every entry of $`C`$ is divided by $`s`$: $`\tau_i`$, $`m_i`$, $`d^{(i)}_k`$, $`\mathcal F_i`$, $`\kappa_iX`$ are divided by $`s`$ ($`\lambda_{0,i}\to s\lambda_{0,i}`$), while $`g_{m,i}`$, $`g_{\eta,i}`$, $`g_{\zeta,i}`$ are unchanged, because the profiles are normalised.
- *$`X\to tX`$, $`\kappa_i\to\kappa_i/t`$.* $`\sigma_X\to t\sigma_X`$, so $`d_{0,i}`$ and the effective contracts are unchanged.

With the factor $`1/s`$ of $`\kappa_iX`$ put into $`\kappa_i`$, and with (8.1):

```math
\Bigl(\tau_i,\ \kappa_i,\ d_{0,i},\ v_i,\ \varrho_i,\ \tfrac{\varrho_i}{d_{0,i}},\ A^{(i)}_{k,+},\ \tfrac{A^{(i)}_{k,+}}{v_i^2}\Bigr)\longmapsto\Bigl(\tfrac{\tau_i}{s},\ \tfrac{\kappa_i}{st},\ \tfrac{d_{0,i}}{s},\ \tfrac{v_i}{s^2},\ \varrho_i,\ s\,\tfrac{\varrho_i}{d_{0,i}},\ \tfrac{A^{(i)}_{k,+}}{s^3},\ s\,\tfrac{A^{(i)}_{k,+}}{v_i^2}\Bigr).
\qquad\text{(8.3)}
```

| | $`\tau_i`$ | $`\kappa_i`$ | $`d_{0,i}`$ | $`v_i`$ | $`\varrho_i`$ | $`\varrho_i/d_{0,i}`$ | $`A^{(i)}_{k,+}`$ | $`A^{(i)}_{k,+}/v_i^2`$ |
|---|---|---|---|---|---|---|---|---|
| well defined | no | no | no | no | yes | no | no | no |
| ratio of the two types well defined | yes | yes | yes | yes | yes | yes | yes | yes |

All ratios are well defined because $`s`$ and $`t`$ are common to the two types: there is one $`\lambda`$ and one $`X`$. The product $`A^{(i)}_{k,+}\,d_{0,i}/v_i^2`$ is well defined as well. Step 7 tests the ratios against a wider class of changes of description.

### Step 2. Fall alike (item 2)

**(a)** *Necessity.* If $`A^{(i)}_{k,+}=A\neq0`$ for all $`k`$ and $`i`$, then for each $`i`$ the acceleration is level-independent, so $`(\mathrm L_i)`$ holds and $`A=-d_{0,i}\tau_i^2g_{\eta,i}`$ by (8.2), for both $`i`$. *Sufficiency.* $`(\mathrm L_1)`$, $`(\mathrm L_2)`$ give the values (8.2), which are then equal and non-zero. With $`d_{0,i}=\kappa_i\sigma_X`$ and one $`\sigma_X>0`$:

```math
\text{FA}\iff(\mathrm L_1),\ (\mathrm L_2),\ \ \kappa_1\tau_1^2\,g_{\eta,1}=\kappa_2\tau_2^2\,g_{\eta,2}\neq0\iff(\mathrm L_1),\ (\mathrm L_2),\ \ v_1^2\,\frac{\varrho_1}{d_{0,1}}=v_2^2\,\frac{\varrho_2}{d_{0,2}}\neq0;\qquad A=-v_i^2\,\frac{\varrho_i}{d_{0,i}} .
\qquad\text{(8.4)}
```

**(b)** By (4.22), $`a^{(i)}_{k,-}(0)`$ is level-independent iff $`\mathcal F_i=-m_i(g_{m,i}-g_{\eta,i})`$. Together with $`(\mathrm L_i)`$ and $`m_i>0`$ this is $`\mathcal F_i=0`$, $`g_{m,i}=g_{\eta,i}`$, and the value is $`-\tau_i^2g_{\eta,i}`$ in both branches. Hence, by the argument of (a):

```math
A^{(i)}_{k,\sigma}=A\neq0\ \ \text{for all }k,\ \sigma=\pm,\ i=1,2\iff\mathcal F_i=0,\ \ g_{m,i}=g_{\eta,i}\ \ (i=1,2)\ \ \text{and}\ \ v_1^2\,\frac{\varrho_1}{d_{0,1}}=v_2^2\,\frac{\varrho_2}{d_{0,2}}\neq0 .
\qquad\text{(8.5)}
```

Here $`\mathcal F_i=0`$ is a condition on the effective profile: $`\mathcal F^{\rm own}_i=\kappa_i\langle X\rangle`$. $`g_{\zeta,i}`$ is free in (8.4) and (8.5).

**(c)** The same argument without the factors $`d_{0,i}`$:

```math
a^{(1)}_{k,+}(0)=a^{(2)}_{k',+}(0)\ \ \text{for all }k,k'\iff(\mathrm L_1),\ (\mathrm L_2)\ \ \text{and}\ \ \tau_1^2\,g_{\eta,1}=\tau_2^2\,g_{\eta,2} .
\qquad\text{(8.6)}
```

This statement is well defined: both sides scale by $`1/s^2`$ under (8.3), the labels belong to the types (A2), and their orientation is fixed by $`\kappa_i>0`$. It is not a statement about the space of 03-ilang-space (M2): it counts the own positions of each type. By (8.4) it coincides with FA iff $`d_{0,1}=d_{0,2}`$, that is $`\kappa_1=\kappa_2`$.

### Step 3. Clocks respond alike (item 3)

From (8.1) and $`d_{0,i}=\kappa_i\sigma_X`$:

```math
\text{RL}:\ \ \varrho_1=\varrho_2\iff g_{\eta,1}=g_{\eta,2};\qquad\text{RD}:\ \ \frac{\varrho_1}{d_{0,1}}=\frac{\varrho_2}{d_{0,2}}\iff\frac{g_{\eta,1}}{\kappa_1}=\frac{g_{\eta,2}}{\kappa_2} .
\qquad\text{(8.7)}
```

- *Same distance.* Positions $`x`$ and $`x+n`$ of the type $`i`$ are the distance $`\ell=n\,d_{0,i}`$ apart by (17.15) of 03-ilang-space/17-motion, and at first order $`\bigl(r_i(x+n)-r_i(x)\bigr)/r_i(x)=n\varrho_i=\ell\,\varrho_i/d_{0,i}`$. For two intervals of the same length $`\ell`$, one in the positions of each type, the relative rate differences agree iff RD. RL compares the clocks over $`d_{0,1}`$ for one type and over $`d_{0,2}`$ for the other.
- *What they rely on (A8).* Each $`\varrho_i`$ compares the rates of one type for two starts at equal $`\lambda`$: it uses the order of $`\lambda`$ within the type, and the unit of $`\lambda`$ cancels. RL then compares two numbers and uses no equal $`\lambda`$ between the types. RD uses in addition $`d_{0,1}/d_{0,2}=\kappa_1/\kappa_2`$, a ratio of entries of one contract $`C`$ that belong to different types; this ratio presupposes one $`\lambda`$ for both types (Step 7).

### Step 4. Relation (item 4)

**(a)** Assume FA. By (8.4) both $`\varrho_i/d_{0,i}`$ are non-zero and $`v_1^2\varrho_1/d_{0,1}=v_2^2\varrho_2/d_{0,2}`$, so RD holds iff $`v_1^2=v_2^2`$, that is iff $`v_1=v_2`$ ($`v_i>0`$). Assume RD. If $`(\mathrm L_1)`$, $`(\mathrm L_2)`$, $`\varrho_1\neq0`$ and $`v_1=v_2`$, then (8.2) gives $`A^{(1)}=A^{(2)}\neq0`$, which is FA; conversely FA gives $`(\mathrm L_i)`$ and $`\varrho_i\neq0`$ by (8.4) and $`v_1=v_2`$ by the first part. Hence neither statement implies the other, and

```math
\text{FA}\ \Longrightarrow\ \bigl(\text{RD}\iff v_1=v_2\bigr);\qquad\text{RD}\ \Longrightarrow\ \bigl(\text{FA}\iff(\mathrm L_1),\ (\mathrm L_2),\ \varrho_1\neq0,\ v_1=v_2\bigr).
\qquad\text{(8.8)}
```

**(b)** Controls, both of the variant (a) of 03-clock-and-fall for each type ($`g_{m,i}=g_{\eta,i}=g_i`$, $`g_{\zeta,i}=0`$, $`\mathcal F_i=0`$, so $`(\mathrm L_i)`$ holds), with $`\kappa_1=\kappa_2`$, $`\tau_2=2\tau_1`$ and $`m_i`$, $`N_i`$, $`\lambda_{0,i}`$ arbitrary:

```math
\text{K1}:\ g_1=4g_2\neq0\ \Rightarrow\ A^{(1)}=A^{(2)}=-4d_0\tau_1^2g_2,\ \ \frac{\varrho_1}{d_{0,1}}=4\,\frac{\varrho_2}{d_{0,2}};\qquad\text{K2}:\ g_1=g_2\neq0\ \Rightarrow\ \varrho_1=\varrho_2,\ \ \frac{\varrho_1}{d_{0,1}}=\frac{\varrho_2}{d_{0,2}},\ \ A^{(2)}=4A^{(1)} .
\qquad\text{(8.9)}
```

K1 falls alike while the clocks respond differently; in K2 the clocks respond alike while the types fall differently. In both $`v_2=2v_1`$, as (8.8) requires.

**(c)** With $`v_1=v_2=:v`$, FA implies RD with no further condition. RD implies FA only together with $`(\mathrm L_1)`$, $`(\mathrm L_2)`$ and $`\varrho_1\neq0`$, which are conditions inside each type. For two types that satisfy these, any two of FA, RD, $`v_1=v_2`$ imply the third, and (8.2) reads $`A=-v^2\varrho_i/d_{0,i}`$ with one $`v`$. The condition $`v_1=v_2`$ is $`\tau_1\kappa_1=\tau_2\kappa_2`$, not $`\tau_1=\tau_2`$.

### Step 5. A common field (item 5)

**(a)** (2.1) of 02-field-object couples the field to one body, so the argument of (2.3) is repeated for two. For $`\Psi\in\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_c`$: $`(B_i\otimes\Phi)(\Psi\otimes\varphi)=\gamma\,(B_i\Psi)\otimes\varphi`$ and $`C_f\varphi=e_f\varphi`$, hence

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}=\sum_{i=1,2}\Bigl[A_i+\sum_xP^{(i)}_x\otimes(1+\gamma\theta_ix)\,\sigma_3\otimes\bigl(m_i\mathbb 1_{N_i}+D_i\bigr)+\kappa_i\,\hat x_i\otimes X\Bigr],
\qquad\text{(8.10)}
```

with $`A_i`$ the motion term of $`C^{\rm D}_i`$. So $`e^{-iC\lambda}(\Psi_0\otimes\varphi)=e^{-ie_f\lambda}\bigl(e^{-iC_{\rm red}\lambda}\Psi_0\bigr)\otimes\varphi`$: the field stays a factor, $`e_f`$ is a common phase (1.2), and the bodies and the medium evolve by $`C_{\rm red}`$, which has the form of the setting. Reading off the effective profiles ($`V^{(i)}_x=\kappa_i\langle X\rangle x`$):

```math
g_{m,i}=g_{\eta,i}=\gamma\theta_i,\qquad g_{\zeta,i}=0,\qquad\mathcal F_i=-\kappa_i\langle X\rangle;\qquad\text{class }\mathcal C\iff\lvert\gamma\rvert\,L\,\max(\lvert\theta_1\rvert,\lvert\theta_2\rvert)<1 .
\qquad\text{(8.11)}
```

The range is the positivity of $`1+\gamma\theta_ix`$ on $`\lvert x\rvert\le L`$; the first-order results need $`\lvert\gamma\theta_i\rvert L\ll1`$.

**(b)** Insert (8.11) into (8.1)–(8.8); $`\varrho_i=\gamma\theta_i`$.
- *$`(\mathrm L_i)`$.* It reads $`\kappa_i\langle X\rangle=0`$, that is $`\langle X\rangle=0`$, and contains neither $`\theta_i`$ nor $`\gamma`$. For $`\langle X\rangle\neq0`$, (8.1) gives $`A^{(i)}_{k,+}=-d_{0,i}\tau_i^2\bigl(\gamma\theta_i+\kappa_i\langle X\rangle/M^{(i)}_k\bigr)`$: the level-dependent part is of the order $`\kappa_i^2`$ and the level-independent part of the order $`\kappa_i`$, so at the leading order in $`\kappa_i`$ of (4.24) $`(\mathrm L_i)`$ holds for every $`\langle X\rangle`$.
- *The other conditions*, with $`(\mathrm L_i)`$ in this sense and $`\gamma\neq0`$:

```math
\begin{aligned}
&A^{(i)}=-\sigma_X\,\kappa_i\tau_i^2\,\theta_i\,\gamma;\qquad\text{FA and (8.5)}\iff\kappa_1\tau_1^2\theta_1=\kappa_2\tau_2^2\theta_2\neq0;\qquad(8.6)\iff\tau_1^2\theta_1=\tau_2^2\theta_2;\\
&\text{RL}\iff\theta_1=\theta_2;\qquad\text{RD}\iff\frac{\theta_1}{\kappa_1}=\frac{\theta_2}{\kappa_2};\qquad\text{FA and RD}\iff\frac{\theta_1}{\kappa_1}=\frac{\theta_2}{\kappa_2}\neq0,\ \ \tau_1\kappa_1=\tau_2\kappa_2 .
\end{aligned}
\qquad\text{(8.12)}
```

(8.5) adds nothing to FA because $`\mathcal F_i=0`$ and $`g_{m,i}=g_{\eta,i}`$ hold already. No condition of (8.12) contains $`\gamma`$: each holds for every sharp value $`\gamma\neq0`$ of the range (8.11) once it holds for one. Only the common value $`A`$ is proportional to $`\gamma`$. At $`\gamma=0`$, RL and RD hold trivially and FA fails ($`A=0`$).

**(c)** The replacements are: (2.20) for two bodies, $`\Phi\to\Phi+a\mathbb 1_f`$, $`C_f\to C_f+c\,\mathbb 1_f`$, $`C^{\rm D}_i\to C^{\rm D}_i-aB_i`$ (and $`-c`$), which leaves $`C`$ unchanged by direct substitution, keeps $`\theta_i`$ and gives $`\gamma\to\gamma+a`$; $`\Phi\to t\Phi`$, $`\theta_i\to\theta_i/t`$, $`\gamma\to t\gamma`$; and those of (8.3), which leave $`\theta_i`$ unchanged. There is one $`\Phi`$, so $`a`$ and $`t`$ are common to the two types.

```math
\text{well defined: }\ \theta_1=\theta_2,\quad\text{the value of }\theta_1/\theta_2,\quad\frac{\theta_1}{d_{0,1}}=\frac{\theta_2}{d_{0,2}};\qquad\text{not well defined: the value of }\theta_i\gamma\ \ (\theta_i\gamma\to\theta_i\gamma+a\theta_i).
\qquad\text{(8.13)}
```

After (2.20) the own contracts are of the class $`\mathcal C`$ with the own gradients $`-a\theta_i`$, and the well-defined number is the gradient of $`C_{\rm red}`$, $`g_{\eta,i}=-a\theta_i+\theta_i(\gamma+a)=\varrho_i`$. It equals $`\theta_i\gamma`$ only in the descriptions whose body contracts are Model D contracts, a convention that fixes the zero of $`\Phi`$. Differences $`\theta_i(\gamma-\gamma')`$ of two sharp values are well defined.

**(d)** By (8.12), with $`\Theta_i:=v_i^2\theta_i/d_{0,i}=\sigma_X\kappa_i\tau_i^2\theta_i`$:

```math
\text{common coupling for the fall:}\ \ \Theta_1=\Theta_2\ \ (\text{then }A=-\Theta\gamma);\qquad\text{common coupling for the clocks:}\ \ \frac{\theta_1}{d_{0,1}}=\frac{\theta_2}{d_{0,2}} .
\qquad\text{(8.14)}
```

Both are well defined by (8.13) and (8.3). They coincide iff $`v_1=v_2`$. Equal couplings per label, $`\theta_1=\theta_2`$, are RL only: they give RD iff $`\kappa_1=\kappa_2`$ and FA iff $`\kappa_1\tau_1^2=\kappa_2\tau_2^2`$.

### Step 6. Equivalences of the setting (items 6a, 6b)

**(a)** For the class $`\mathcal C`$ with $`\tau_i>0`$, $`C_i`$ has the entries $`\mp\tfrac{i}{2}\tau_i\zeta_x\neq0`$ between $`x`$ and $`x+1`$, so $`J_1\neq0`$ and $`J_2\neq0`$. With the medium read, (5.19) leaves two rows: $`X`$ diagonal, with $`a_1`$, $`a_2`$ free; $`X`$ not diagonal, with $`a_1=a_2=a_c`$. With the medium not read, (5.20) has all $`a_1,a_2>0`$ for every $`X`$. Hence

```math
\text{the relative factor of }b_1,b_2\text{ is detectable}\iff\text{the medium is read and }X\text{ is not diagonal in the places of the medium}.
\qquad\text{(8.15)}
```

**(b)** In (5.20), $`C_i/a_i`$ is of the class $`\mathcal C`$ with every entry divided by $`a_i`$, and $`X`$, $`\chi`$ are unchanged. With (8.1), (4.16) and $`v_i=\tau_id_{0,i}`$:

```math
\begin{aligned}
&\tau_i,\ m_i,\ d^{(i)}_k,\ \mathcal F_i,\ \kappa_i,\ d_{0,i}\ \to\ \tfrac1{a_i}\,(\,\cdot\,);\qquad\lambda_{0,i}\to a_i\lambda_{0,i};\qquad g_{m,i},\ g_{\eta,i},\ g_{\zeta,i},\ \varrho_i\ \ \text{unchanged};\\
&v_i\to\frac{v_i}{a_i^2},\qquad\frac{\varrho_i}{d_{0,i}}\to a_i\,\frac{\varrho_i}{d_{0,i}},\qquad a^{(i)}_{k,\sigma}(0)\to\frac{a^{(i)}_{k,\sigma}(0)}{a_i^2},\qquad A^{(i)}_{k,\sigma}\to\frac{A^{(i)}_{k,\sigma}}{a_i^3},\qquad\frac{A^{(i)}_{k,+}}{v_i^2}\to a_i\,\frac{A^{(i)}_{k,+}}{v_i^2} .
\end{aligned}
\qquad\text{(8.16)}
```

$`C^{\rm eff}_i/a_i`$ has the eigenvectors of $`C^{\rm eff}_i`$, so the levels, the branches, the branch starts and $`S_{\rm clock}`$ are the same, and $`(\mathrm L_i)`$ is unchanged. The rates obey $`r'_i=r_i/a_i`$, as in (5.25).

### Step 7. All equivalent descriptions of the setting

The statements of item 6(c) are defined for descriptions of the form of the setting. The following lemma lists all of them.

**Lemma.** Let $`(a_1,a_2;C')`$ be an equivalence of $`C`$, the medium read or not, with $`C'=F'_1+F'_2`$ again of the form of the setting: $`F'_i=C'_i+\kappa'_i\hat x_i\otimes X'`$, $`C'_i`$ of the class $`\mathcal C`$ on the same places with linear profiles, $`\kappa'_i>0`$. Then

```math
F'_i=\frac{F_i}{a_i}+c_i\,\mathbb 1,\qquad\text{hence}\qquad C'^{\rm eff}_i=\frac{C^{\rm eff}_i}{a_i}+c_i\,\mathbb 1,\qquad\kappa'_i\,(X'-\langle X'\rangle)=\frac{\kappa_i}{a_i}\,(X-\langle X\rangle),
\qquad\text{(8.17)}
```

and the rules (8.16) hold for it. Conversely $`F_1/a_1+F_2/a_2+c\,\mathbb 1`$ is an equivalence for all $`a_1,a_2>0`$ if the medium is not read (5.20), and if it is read and $`X`$ is diagonal (5.19); for $`X`$ not diagonal and the medium read, only for $`a_1=a_2`$ (5.19).

*Proof.*
1. Take the schedule with one event: $`b_1`$, the reading into single places $`h`$ (projectors $`P_h`$), at $`\lambda`$. With $`U=e^{-iC\lambda}`$ and $`U'=e^{-iC'a_1\lambda}`$, the equality of the statistics for every start gives $`U'^{\dagger}P_hU'=U^{\dagger}P_hU`$ (a self-adjoint operator is fixed by its expectation values). So $`W(\lambda):=U'U^{\dagger}`$ commutes with every $`P_h`$, for all $`\lambda\ge0`$.
2. The derivatives of $`W`$ at $`\lambda=0`$ commute with every $`P_h`$ as well: $`i\dot W(0)=a_1C'-C=:R`$ and $`-\ddot W(0)=R^2+[C,R]`$. Hence $`R=\sum_hP_h\otimes R_h`$, with $`R_h`$ on $`\mathcal H_{b_2}\otimes\mathcal H_c`$, and $`[C,R]`$ is block diagonal in the places of $`b_1`$. Only the off-diagonal part of $`C_1`$ is not block diagonal, so $`(C_1)_{hh'}(R_{h'}-R_h)=0`$ for $`h\neq h'`$.
3. $`R`$ block diagonal means that $`a_1C'_1-C_1`$ is diagonal in the places of $`b_1`$. The hopping entries give $`a_1\tau'_1\zeta'_x=\tau_1\zeta_x`$ on all bonds. The clock entries give $`a_1\eta'_x/\lambda'_{0,1}=\eta_x/\lambda_{0,1}`$, because $`D'_1=(\lambda_{0,1}/\lambda'_{0,1})D_1`$ and $`D_1`$ is not diagonal in the clock label ($`\langle a\vert D\vert a'\rangle=\frac{2\pi}{N\lambda_0}\bigl(e^{2\pi i(a-a')/N}-1\bigr)^{-1}\neq0`$ for $`a\neq a'`$). With the normalised linear profiles: $`\tau'_1=\tau_1/a_1`$, $`\lambda'_{0,1}=a_1\lambda_{0,1}`$, $`g'_{\zeta,1}=g_{\zeta,1}`$, $`g'_{\eta,1}=g_{\eta,1}`$. What remains is $`R_h=s\,\mu(x)+\nu(x)+x\,Y+R_0`$ for $`h=(x,s,a)`$, $`s=\pm1`$, with $`\mu(x):=a_1m'_x-m_x`$, $`\nu(x):=a_1V'_x-V_x`$ (the own profiles), $`Y:=a_1\kappa'_1X'-\kappa_1X`$ and $`R_0`$ independent of $`h`$.
4. The hopping connects $`(x,s,a)`$ and $`(x+1,-s,a)`$, so by item 2 $`s\,[\mu(x)+\mu(x+1)]\,\mathbb 1=\nu(x+1)-\nu(x)+Y`$ for $`s=\pm1`$. Hence $`\mu(x)+\mu(x+1)=0`$ on at least two bonds, so the linear $`\mu`$ vanishes ($`m'_1=m_1/a_1`$, $`g'_{m,1}=g_{m,1}`$), and $`Y=-\nu'\mathbb 1_c`$ with $`\nu(x)=\nu_0+\nu'x`$. Then $`a_1F'_1=C_1+\nu_0+\nu'\hat x_1+\hat x_1\otimes(\kappa_1X-\nu')=F_1+\nu_0`$. The same holds for $`b_2`$ with $`a_2`$.
5. Taking $`\langle\chi\vert\cdot\vert\chi\rangle`$ of $`F'_i`$ gives $`C'^{\rm eff}_i`$, and $`F'_i-C'^{\rm eff}_i`$ gives the record part. The split of $`F'_i`$ into $`C'_i`$ and the record is free up to the replacements of Step 1(b), which change none of the quantities in (8.16). $`\blacksquare`$

### Step 8. What is the same in every equivalent description (items 6c, 6d, 6e)

**(c)** By (8.17) every equivalent description of the setting acts by (8.16) with its factors. So in it: $`(\mathrm L_i)`$ is unchanged; FA reads $`(\mathrm L_i)`$ and $`A^{(1)}/a_1^3=A^{(2)}/a_2^3\neq0`$; $`v'_1=v'_2`$ reads $`v_1/a_1^2=v_2/a_2^2`$; RL is unchanged; RD reads $`a_1\varrho_1/d_{0,1}=a_2\varrho_2/d_{0,2}`$; and for (4.24) the hypothesis is unchanged ($`a'^{(i)}_{k,+}=a^{(i)}_{k,+}/a_i^2`$) and $`A'^{(i)}=A^{(i)}/a_i^3=-v_i^2\varrho_i/(a_i^3d_{0,i})=-v'^2_i\varrho'_i/d'_{0,i}`$. In the first column below $`a_1=a_2`$ by (8.15). In the other two all $`a_1,a_2>0`$ occur, and the equivalence $`a_1=2`$, $`a_2=1`$ makes a true FA, a true $`v_1=v_2`$ and a true RD with $`\varrho_i\neq0`$ false ($`A'^{(1)}=A/8`$, $`v'_1=v/4`$, $`\varrho'_1/d'_{0,1}=2\varrho_1/d_{0,1}`$).

```math
\begin{array}{l|c|c|c}
\text{statement} & \text{read, }X\text{ not diagonal} & \text{read, }X\text{ diagonal} & \text{not read}\\\hline
\text{FA} & \text{same} & \text{not the same} & \text{not the same}\\
v_1=v_2 & \text{same} & \text{not the same} & \text{not the same}\\
\text{RL} & \text{same} & \text{same} & \text{same}\\
\text{RD} & \text{same} & \text{not the same} & \text{not the same}\\
\text{(4.24) for each type} & \text{same} & \text{same} & \text{same}
\end{array}
\qquad\text{(8.18)}
```

**(d)** Medium not read. By (8.16), $`v'_1=v'_2`$ iff $`a_1/a_2=\sqrt{v_1/v_2}`$, which has a solution for every pair; the common factor left free is the unit of $`\lambda`$. In this description, with $`v'`$ the common speed,

```math
\frac{A'^{(1)}_{k,+}}{A'^{(2)}_{k',+}}=\Bigl(\frac{v_2}{v_1}\Bigr)^{3/2}\frac{A^{(1)}_{k,+}}{A^{(2)}_{k',+}},\qquad\varrho'_i=\varrho_i,\qquad\frac{\varrho'_1/d'_{0,1}}{\varrho'_2/d'_{0,2}}=\sqrt{\frac{v_1}{v_2}}\;\frac{\varrho_1/d_{0,1}}{\varrho_2/d_{0,2}},\qquad A'^{(i)}=-v'^2\,\frac{\varrho_i}{d'_{0,i}}\ \ \text{under }(\mathrm L_i).
\qquad\text{(8.19)}
```

A description in which the types fall alike needs $`(\mathrm L_i)`$ and $`(a_1/a_2)^3=A^{(1)}/A^{(2)}>0`$. By (8.17) there are no other equivalent descriptions of the setting, and $`\mathrm{sign}A^{(i)}=-\mathrm{sign}g_{\eta,i}`$ by (8.2), so

```math
\text{an equivalent description with FA exists}\iff(\mathrm L_1),\ (\mathrm L_2)\ \ \text{and}\ \ g_{\eta,1}\,g_{\eta,2}>0 ;\qquad\text{in it}\quad\frac{v'_1}{v'_2}=\frac{v_1}{v_2}\Bigl(\frac{A^{(2)}}{A^{(1)}}\Bigr)^{2/3} .
\qquad\text{(8.20)}
```

**(e)** *Relative factor detectable.* All equivalent descriptions of the setting are $`C/\alpha+c`$: a change of the unit of $`\lambda`$, (8.3) with $`s=\alpha`$. FA, $`v_1=v_2`$, RL, RD and every ratio of (8.3) mean the same in all of them, as in Steps 2–4.

*Relative factor not detectable.* By (8.16) the following are the same in all equivalent descriptions: $`(\mathrm L_i)`$, $`\mathrm{sign}A^{(i)}`$ (the direction of the fall along $`\hat e`$), $`\varrho_i`$, the relation (4.24) of each type, RL, and the numbers $`A^{(i)}/v_i^{3/2}`$. An equality of the magnitudes of the falls, or of the responses per distance, has a meaning only relative to a convention that fixes $`a_1/a_2`$. With the convention of equal maximal speeds, $`v'_1=v'_2`$, FA and RD become by (8.8) one statement that no equivalence changes:

```math
(\mathrm L_1),\ (\mathrm L_2)\quad\text{and}\quad\frac{A^{(1)}}{v_1^{3/2}}=\frac{A^{(2)}}{v_2^{3/2}}\neq0\iff(\mathrm L_1),\ (\mathrm L_2)\quad\text{and}\quad\varrho_1\sqrt{\frac{\tau_1}{\kappa_1}}=\varrho_2\sqrt{\frac{\tau_2}{\kappa_2}}\neq0 .
\qquad\text{(8.21)}
```

The second form uses $`A^{(i)}/v_i^{3/2}=-\varrho_i\sqrt{\tau_i/d_{0,i}}`$ from (8.2). Without a convention, "fall alike" can only mean (8.20): each type falls level-independently, and both in the same direction. The equal maximal speed is then a convention, not a condition (M7).

## Result

Class: all pairs of bodies of the class $`\mathcal C`$ with linear profiles, all $`\kappa_i>0`$, every $`X`$, $`\chi`$ with $`\sigma_X>0`$; branch starts at rest, first order in the gradients, leading order in $`\kappa_i`$. Item 5: all pairs of Model D bodies, all $`\theta_i`$, every sharp stationary field state in the range (8.11).

1. **One type.** (8.1): $`\varrho_i=g_{\eta,i}`$. (8.2): level-independent fall iff $`(\mathrm L_i)`$, value $`-v_i^2\varrho_i/d_{0,i}`$. (8.3) with its table: of the eight quantities only $`\varrho_i`$ is well defined; all ratios between the types are.
2. **Fall alike.** (8.4) in the data and through $`v_i`$ and the responses; (8.5) for both branches; (8.6) for the labels, well defined but not a statement about distances.
3. **Clocks.** (8.7); RD compares over the same distance; RL uses no common $`\lambda`$ of the two types, RD does.
4. **Relation.** (8.8): neither implies the other; controls (8.9); with $`(\mathrm L_i)`$ and $`\varrho_i\neq0`$, any two of FA, RD, $`v_1=v_2`$ imply the third.
5. **Common field.** Generator (8.10), gradients and range (8.11), conditions (8.12), all independent of $`\gamma`$; (8.13); common couplings (8.14).
6. **Equivalent descriptions.** Detectability (8.15); rules (8.16); all equivalent descriptions of the setting (8.17); table (8.18); the description of equal maximal speeds (8.19) and the existence condition (8.20); the convention-free and the convention-relative meaning (8.21).

Controls (M9): K1, K2 of (8.9); the columns of (8.18) (medium read against not read, $`X`$ diagonal against not diagonal).

## Consistency checks

1. **Dimensions and $`a_1=a_2`$.** With costs in units of $`1/\lambda`$: $`d_{0,i}\sim\lambda^{-1}`$, $`v_i\sim\lambda^{-2}`$, $`A\sim\lambda^{-3}`$, and (8.2) gives $`\lambda^{-4}/\lambda^{-1}`$. The rules (8.16) with $`a_1=a_2=s`$ are (8.3) with $`t=1`$, and then every row of (8.18) is "same", as in its first column. Passed.
2. **Identical data.** For $`\tau_1=\tau_2`$, $`\kappa_1=\kappa_2`$ and equal gradients: $`v_1=v_2`$, RL and RD hold, and (8.4) reduces to $`(\mathrm L)`$ and $`g_\eta\neq0`$, as (8.8) states. With the medium not read, (5.20) with $`a_1\neq a_2`$ still gives a description without FA, as (8.18) states. Passed.
3. **One gradient zero.** For $`g_{\eta,2}=0`$ and $`(\mathrm L_2)`$: $`A^{(2)}=0`$, so FA fails by (8.4), RD holds iff $`g_{\eta,1}=0`$ by (8.7), and no equivalent description with FA exists by (8.20), in agreement with $`A'^{(2)}=A^{(2)}/a_2^3=0`$. Passed.

## Open issues

- Item 5: with Model D body contracts the effective gradient is $`\mathcal F_i=-\kappa_i\langle X\rangle`$, so the level-independence is exact only for $`\langle X\rangle=0`$; for $`\langle X\rangle\neq0`$ it holds at the leading order in $`\kappa_i`$. The conditions on the six numbers in (8.12) are stated with this qualification.
- (8.17) lists the equivalent descriptions that are again of the form of the setting (class $`\mathcal C`$, linear profiles, one operator of the medium, at least three positions). For an equivalent contract outside this form, for example with a term $`\Delta`$ of (5.19) that is not a constant, the statements of (8.18) are not defined here.
- All results are of first order in the gradients, from rest and at leading order in the records; the fall in motion, the lattice terms and a field that is not sharp are out of scope.
- The convention $`v'_1=v'_2`$ in (8.21) is a choice. Whether anything in the language selects it belongs to criterion 10.

## Methods used

- Level-independence conditions of the drift acceleration (linear algebra in the level index)
- Scaling analysis under changes of the unit of the evolution parameter and of operator normalisations
- Invariance under replacements of contract terms at fixed total contract
- Reduction of a contract on an eigenstate of the field operators
- Operator identities from equal reading statistics (polarisation), expansion of unitary groups to second order
- Connectivity argument for operators commuting with a hopping contract
