# Field with its own contract: seen factor, second-order terms, fall and clock

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-11

## Setup and assumptions

- **Setting.** The class $`\mathcal D`$, the start $`\Psi_0=\phi\otimes\varphi_0\otimes\chi`$ with $`C_f\varphi_0=e_0\varphi_0`$ ($`e_0`$ simple, gap $`\Delta_f`$), and $`N(x)`$, $`\tilde\Phi_x`$, $`\varepsilon_x`$, $`\varepsilon`$, $`d_k`$, $`M_k`$, $`M_{\max}`$, $`N_{\max}`$, $`\epsilon_1`$, $`\epsilon_2`$, $`\mathcal C`$, $`\mathcal C_{\rm lev}`$ are those of question.md; $`\lambda\ge0`$. Class, field start, linear profiles and cells are assumptions of this package (M8, M9, A11). Inputs, as quoted in question.md: (2.1), (2.3), (2.20), (2.22) of 02-field-object; (3.23), (3.36) of 03-clock-and-fall; (4.7), (4.16), (4.19), (4.22), (4.24) of 04-branch-fall; (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion.
- **Notation.** $`P_x:=\lvert x\rangle\langle x\rvert`$, $`h_x:=\lvert x+1\rangle\langle x\rvert`$, $`\mathcal M:=m\mathbb 1_N+D`$ (so $`\mathcal M\lvert f_k\rangle=M_k\lvert f_k\rangle`$, $`G=\sigma_3\otimes\mathcal M`$, $`\lVert G\rVert=M_{\max}`$), $`B_x:=P_x\otimes G`$, $`\langle O\rangle:=\langle\varphi_0\vert O\vert\varphi_0\rangle`$, $`Q:=\mathbb 1_f-\lvert\varphi_0\rangle\langle\varphi_0\rvert`$, $`Q_0:=\mathbb 1-\Pi_0`$, and the reduced resolvent $`S:=Q\,(C_f-e_0)^{-1}Q`$, $`\lVert S\rVert=1/\Delta_f`$. Tensor factors are written in the order $`(b,c),f`$ where convenient. The $`M_k`$ are positive and pairwise different.
- **A third number of the class.** $`\nu:=\max_x\lVert Q\tilde\Phi_xQ\rVert`$ and $`\epsilon_3:=\nu M_{\max}/\Delta_f`$ (the pair term inside the excited states of the field against the gap). In $`\mathcal D`$ it is bounded neither by $`\epsilon_1`$ nor by $`\epsilon_2`$; for the cells of item 4, $`\epsilon_3=\epsilon_1`$. Every order estimate below needs $`\epsilon_3\ll1`$ besides $`\epsilon_1,\epsilon_2\ll1`$; this is stated with each result.
- **Regimes.** *R0:* no condition, every member of $`\mathcal D`$, every start $`\phi`$, all $`\lambda\ge0`$ (exact statements and bounds). *R1:* $`2\epsilon_1+2\epsilon_2+\epsilon_3<1`$, in the weak-record regime ($`\kappa\to0`$ at fixed $`\lambda`$, chain and start, so that $`\lVert\hat C-e_0\rVert\to\tau+N_{\max}M_{\max}=\epsilon_2\Delta_f`$); order estimates are expansions in $`\epsilon_1`$ whose coefficients are expanded in $`\epsilon_2`$ and $`\epsilon_3`$.
- **Perturbation theory used (standard).** In R1 the diagonal blocks $`\Pi_0C\Pi_0`$ and $`Q_0CQ_0`$ have spectra separated by at least $`\Delta_f(1-2\epsilon_2-\epsilon_3)`$, more than twice the norm $`\le\varepsilon M_{\max}`$ of the off-diagonal block. Then a unitary $`e^{\mathcal S}`$ with $`\mathcal S`$ anti-self-adjoint and block-off-diagonal with respect to $`\Pi_0`$ block-diagonalises $`C`$ exactly (Schrieffer–Wolff form of nondegenerate perturbation theory), and $`\mathcal S`$ is given by its series in the off-diagonal block.
- **Status words.** *Exact*: an identity. *Bound*: a proven inequality. *Order estimate*: leading term computed, remainder given by its order under the stated conditions.

## Derivation

### Step 1. First order (item 1)

**(a)** Because $`\langle\Phi_x\rangle=N(x)`$ and $`\langle C_f\rangle=e_0`$, the compression of $`C`$ is

```math
\hat C=\hat C_b\otimes\mathbb 1_c+\sum_xP_x\otimes\kappa\,x\,X,\qquad
\hat C_b=A+\sum_xP_x\otimes\Bigl[N(x)\,\sigma_3\otimes(m\mathbb 1_N+D)+e_0\,\mathbb 1_2\otimes\mathbb 1_N\Bigr].
\qquad\text{(10.1)}
```

*Class and status:* every member of $`\mathcal D`$ and every $`\varphi_0`$ as stated, $`\varepsilon=0`$ or $`\varepsilon>0`$; exact. For $`\varepsilon=0`$ it is (2.22) with $`n_x=N(x)`$, $`e_f=e_0`$. The body part $`\hat C_b`$ is the member of $`\mathcal C`$ with $`\tau`$, $`\zeta_x=1`$, $`m_x=m\,N(x)`$, $`\eta_x=N(x)`$, $`V_x=e_0`$ (it is a member because $`N(x)>0`$); for $`N(x)=1+gx`$ it is the variant (a), $`g_m=g_\eta=g`$, $`g_\zeta=0`$, $`\mathcal F=0`$, plus the constant $`e_0`$. $`\hat C`$ is self-adjoint, independent of $`\lambda`$ and of the state of $`b`$ and $`c`$, and is one pair term between $`b`$ and $`c`$ (A5): **yes**, it is the contract of an admissible description of $`b`$ and $`c`$. That this description reproduces the one with $`C`$ is a separate statement, (10.7).

Under (2.20) with $`j=x`$, $`B_j=B_x`$ (the $`B_x`$ and $`\mathbb 1_b`$ are linearly independent, so these are all replacements):

```math
N(x)\to N(x)+a_x,\qquad e_0\to e_0+c,\qquad \varphi_0,\ \tilde\Phi_x,\ S,\ \varepsilon_x,\ \Delta_f,\ \nu\ \text{unchanged},\qquad \hat C\to\hat C .
\qquad\text{(10.2)}
```

$`\hat C`$ is invariant because it is built from $`C`$ and $`\varphi_0`$ only. $`N(x)`$ alone is not well defined (M6): after the replacement $`C_{br}`$ contains $`-a_xB_x`$, and only the sum of $`N(x)`$ and the coefficient of $`B_x`$ in $`C_{br}`$ is invariant. In the form of $`\mathcal D`$ that coefficient is zero, which fixes $`a_x=0`$; $`\epsilon_1`$, $`\epsilon_3`$ are invariant, $`\epsilon_2`$ is defined in this form.

**(b)** Split the contract:

```math
C=H_0+W,\qquad H_0:=(\hat C-e_0)\otimes\mathbb 1_f+\mathbb 1\otimes C_f,\qquad W:=\sum_xB_x\otimes\tilde\Phi_x,\qquad [H_0,\Pi_0]=0,\quad \Pi_0W\Pi_0=0,\quad \lVert W\Pi_0\rVert\le\varepsilon M_{\max}.
\qquad\text{(10.3)}
```

The last relation: $`W(\Psi\otimes\varphi_0)=\sum_xP_xG\Psi\otimes\tilde\Phi_x\varphi_0`$ has orthogonal summands, so its squared norm is $`\sum_x\lVert P_xG\Psi\rVert^2\varepsilon_x^2\le\varepsilon^2M_{\max}^2\lVert\Psi\rVert^2`$. Since $`e^{-iH_0\lambda}\Psi_0=\bigl(e^{-i\hat C\lambda}(\phi\otimes\chi)\bigr)\otimes\varphi_0`$ stays in $`\Pi_0\mathcal H`$, Duhamel's formula gives, in R0,

```math
\lVert Q_0\Psi(\lambda)\rVert\le\bigl\lVert\Psi(\lambda)-e^{-iH_0\lambda}\Psi_0\bigr\rVert\le\int_0^\lambda\lVert W\Pi_0\rVert\,\mathrm ds\le\varepsilon\,M_{\max}\,\lambda\qquad(\text{bound, all }\lambda\ge0).
\qquad\text{(10.4)}
```

In R1, with the block-diagonalising unitary of "Setup",

```math
e^{\mathcal S}Ce^{-\mathcal S}=H_{\rm eff}\otimes\lvert\varphi_0\rangle\langle\varphi_0\rvert+Q_0\,e^{\mathcal S}Ce^{-\mathcal S}Q_0,\qquad \lVert\mathcal S\rVert\le\epsilon_1\bigl[1+O(\epsilon_1^2+\epsilon_2+\epsilon_3)\bigr],
\qquad\text{(10.5)}
```

where the leading term of $`Q_0\mathcal S\Pi_0`$ is $`(\mathbb 1\otimes S)W\Pi_0`$, of norm $`\le\varepsilon M_{\max}/\Delta_f`$ by the argument of (10.3). For an off-diagonal anti-self-adjoint $`\mathcal S`$, $`\lVert Q_0e^{\pm\mathcal S}\Pi_0\rVert\le\sin\lVert\mathcal S\rVert`$ and $`\lVert\Pi_0e^{\pm\mathcal S}\Pi_0-\Pi_0\rVert\le1-\cos\lVert\mathcal S\rVert`$. Writing $`\Psi(\lambda)=e^{-\mathcal S}e^{-i(e^{\mathcal S}Ce^{-\mathcal S})\lambda}e^{\mathcal S}\Psi_0`$ and using that the middle factor commutes with $`\Pi_0`$:

```math
\lVert Q_0\Psi(\lambda)\rVert\le2\lVert\mathcal S\rVert\le2\,\epsilon_1\bigl[1+O(\epsilon_1^2+\epsilon_2+\epsilon_3)\bigr]\qquad(\text{R1, order estimate of the constant, all }\lambda\ge0).
\qquad\text{(10.6)}
```

For $`\varepsilon=0`$ both (10.4) and (10.6) give $`Q_0\Psi(\lambda)=0`$.

**(c)** Let $`p`$ be the outcome distribution of a schedule (readings $`\Pi_i\otimes\mathbb 1_f`$ at $`\lambda_1\le\dots\le\lambda_k`$) in the description with $`C`$, and $`\hat p`$ that in the description of $`b`$, $`c`$ with $`\hat C`$ and the start $`\phi\otimes\chi`$. The readings commute with $`\Pi_0`$, so the vectors of the $`\hat C`$-description stay in $`\Pi_0\mathcal H`$ and (10.4) applies on every interval; the outcome-labelled vectors of the two descriptions then differ by at most $`\varepsilon M_{\max}\lambda_k`$ in norm (telescoping). In R1, $`\Pi_0\Psi`$ follows $`H_{\rm eff}`$ up to $`O(\epsilon_1^2)`$ by (10.8), the $`Q_0`$ components have squared norm $`O(\epsilon_1^2)`$ by (10.6) and are orthogonal to the $`\Pi_0`$ components, and $`\lVert H_{\rm eff}-\hat C\rVert\le\epsilon_1^2\Delta_f[1+O(\epsilon_1^2+\epsilon_2+\epsilon_3)]`$ by (10.9). Hence

```math
\sum_{r_1,\dots,r_k}\lvert p-\hat p\rvert\le2\,\varepsilon M_{\max}\lambda_k\ \ (\text{R0, bound}),\qquad
\sum_{r_1,\dots,r_k}\lvert p-\hat p\rvert=O(\epsilon_1^2)+O\bigl(\epsilon_1^2\Delta_f\lambda_k\bigr)\ \ (\text{R1, order estimate, fixed schedule}).
\qquad\text{(10.7)}
```

*Answer:* in R1 the statistics of every schedule on $`b`$ and $`c`$ are those of the body in a sharp field with the profile $`N(x)`$ through first order in $`\epsilon_1`$ (there is no term linear in $`\epsilon_1`$), on the range $`\lambda\ll1/(\epsilon_1^2\Delta_f)=\Delta_f/(\varepsilon M_{\max})^2`$; the deviation starts at $`\epsilon_1^2`$, with a part that does not grow with $`\lambda`$ and a part that grows linearly. Without any condition on $`\epsilon_2`$, $`\epsilon_3`$ they agree at zeroth order on $`\lambda\ll1/(\varepsilon M_{\max})`$. Control: for $`\varepsilon=0`$, $`p=\hat p`$ for all $`\lambda`$.

### Step 2. Second order (item 2)

**(a)** Write $`W_1:=Q_0W\Pi_0`$, $`W_{\rm d}:=Q_0WQ_0`$, $`\mathcal S_1:=Q_0\mathcal S\Pi_0`$. Expanding $`e^{\mathcal S}Ce^{-\mathcal S}`$ and requiring the terms of first order in $`W_1`$ to be block-diagonal gives the Sylvester equation for the leading part of $`\mathcal S_1`$ and the effective operator:

```math
(\mathbb 1\otimes(C_f-e_0))\,\mathcal S_1+[\hat C\otimes\mathbb 1_f,\mathcal S_1]+W_{\rm d}\,\mathcal S_1=W_1,\qquad
H_{\rm eff}=\hat C-\tfrac12\bigl(\mathcal S_1^{\dagger}W_1+W_1^{\dagger}\mathcal S_1\bigr)+O(\epsilon_1^4\Delta_f),
\qquad\text{(10.8)}
```

read on $`\mathcal H_b\otimes\mathcal H_c`$ (sandwiched with $`\varphi_0`$). $`H_{\rm eff}`$ is self-adjoint. By the two norm relations after (10.5), for the exact $`H_{\rm eff}`$ of (10.5): $`\bigl\lVert\Pi_0\Psi(\lambda)-\bigl(e^{-iH_{\rm eff}\lambda}(\phi\otimes\chi)\bigr)\otimes\varphi_0\bigr\rVert\le2\lVert\mathcal S\rVert^2\le2\epsilon_1^2[1+\dots]`$ for all $`\lambda\ge0`$; a truncation $`H'`$ of $`H_{\rm eff}`$ adds at most $`\lambda\,\lVert H_{\rm eff}-H'\rVert`$.

Solve the Sylvester equation by iteration in $`[\hat C,\cdot\,]`$ and $`W_{\rm d}`$ against $`C_f-e_0`$: $`\mathcal S_1=(\mathbb 1\otimes S)W_1-(\mathbb 1\otimes S)[\hat C,(\mathbb 1\otimes S)W_1]-(\mathbb 1\otimes S)W_{\rm d}(\mathbb 1\otimes S)W_1+\dots`$. With $`B_xB_y=\delta_{xy}P_x\otimes\mathbb 1_2\otimes\mathcal M^2`$, the leading term is

```math
\boxed{\;H^{(2)}=-\sum_x\gamma_x\,P_x\otimes\mathbb 1_2\otimes(m\mathbb 1_N+D)^2\otimes\mathbb 1_c,\qquad \gamma_x:=\langle\tilde\Phi_x\,S\,\tilde\Phi_x\rangle=\sum_{e\neq e_0}\frac{\lVert\Pi_e\tilde\Phi_x\varphi_0\rVert^2}{e-e_0},\qquad\lvert\gamma_x\rvert\le\frac{\varepsilon_x^2}{\Delta_f}\;}
\qquad\text{(10.9)}
```

($`\Pi_e`$ the eigenprojectors of $`C_f`$), so $`\lVert H^{(2)}\rVert\le\epsilon_1^2\Delta_f`$. *Class:* all of $`\mathcal D`$; *regime:* R1; *status:* exact coefficient of the second order in $`\epsilon_1`$ at leading order in $`\epsilon_2`$, $`\epsilon_3`$. $`\gamma_x>0`$ ($`<0`$) whenever $`\varepsilon_x>0`$ and $`e_0`$ is the lowest (highest) eigenvalue; for an inner $`e_0`$, $`\gamma_x=0`$ with $`\varepsilon_x>0`$ is possible (exceptional).

First correction. Only the motion term fails to commute with $`B_x`$ (the on-site terms and the record term commute with $`P_x\otimes G`$): $`[\hat C,B_x]=[A,B_x]=\tfrac\tau2\,\sigma_2\otimes\mathcal M\,\bigl[(h_x^{\dagger}-h_x)+(h_{x-1}^{\dagger}-h_{x-1})\bigr]`$. Inserting the second and third terms of $`\mathcal S_1`$ into (10.8), with $`\rho_{xy}:=\langle\tilde\Phi_xS^2\tilde\Phi_y\rangle`$ ($`\lvert\rho_{xy}\rvert\le\varepsilon_x\varepsilon_y/\Delta_f^2`$):

```math
\begin{aligned}
H^{(2,1)}&=-\frac\tau2\sum_x\Bigl(c_x\,h_x\otimes(-i\sigma_1)+c_x^{*}\,h_x^{\dagger}\otimes(i\sigma_1)\Bigr)\otimes\mathcal M^2,\qquad c_x:=\tfrac12(\rho_{xx}+\rho_{x+1,x+1})+\rho_{x+1,x},\\
H^{(3)}&=\sum_x\gamma^{(3)}_x\,P_x\otimes\sigma_3\otimes\mathcal M^3,\qquad \gamma^{(3)}_x:=\langle\tilde\Phi_xS\tilde\Phi_xS\tilde\Phi_x\rangle,\qquad \lVert H^{(2,1)}\rVert\le2\tau\epsilon_1^2,\quad\lVert H^{(3)}\rVert\le\epsilon_1^2\epsilon_3\Delta_f .
\end{aligned}
\qquad\text{(10.10)}
```

So $`H_{\rm eff}=\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}+O\bigl(\epsilon_1^2(\epsilon_2+\epsilon_3)^2\Delta_f\bigr)+O(\epsilon_1^4\Delta_f)`$ (R1, order estimate of the remainder): the first correction has relative order $`\epsilon_2`$ in the motion term (form: a factor on the hopping) and relative order $`\epsilon_3`$ on site (form: a term in $`\sigma_3\otimes\mathcal M^3`$). Through this order $`H_{\rm eff}-\hat C`$ acts as the identity on $`c`$ and does not contain $`\kappa`$. *Range:* by (10.8) and the argument of (10.7), the description of $`b`$, $`c`$ with $`\hat C+H^{(2)}`$ reproduces the statistics of a fixed schedule to an accuracy $`\eta\gg\epsilon_1^2`$ for $`\lambda\lesssim\eta/[\epsilon_1^2\Delta_f(\epsilon_2+\epsilon_3+\epsilon_1^2)]`$, and with $`H^{(2,1)}+H^{(3)}`$ added for $`\lambda\lesssim\eta/[\epsilon_1^2\Delta_f((\epsilon_2+\epsilon_3)^2+\epsilon_1^2)]`$; the part $`O(\epsilon_1^2)`$ of the error that does not grow with $`\lambda`$ is not removed by these terms.

**(b)** Every term is a function of $`D`$ on the clock label, so the level is conserved. On the level $`k`$ the on-site block at $`x`$ and the hopping block from $`x`$ to $`x+1`$ of the body part are

```math
\bigl(N(x)M_k+\gamma^{(3)}_xM_k^3\bigr)\sigma_3+\bigl(e_0-\gamma_xM_k^2\bigr)\mathbb 1_2,\qquad T_{x,k}=-\frac{i\tau}2\bigl(1-M_k^2c_x\bigr)\sigma_1 .
\qquad\text{(10.11)}
```

At second order and leading order in $`\epsilon_2`$, $`\epsilon_3`$ the body part is a member of $`\mathcal C_{\rm lev}`$: **yes**, with $`\tau_k=\tau`$, $`\zeta_{x,k}=1`$, $`M_{x,k}=N(x)M_k`$, $`V_{x,k}=e_0-\gamma_xM_k^2`$; it is a member of $`\mathcal C`$ if and only if $`\gamma_x=0`$ for all $`x`$ (the $`M_k^2`$ are pairwise different). With the first corrections, $`M_{x,k}=N(x)M_k+\gamma_x^{(3)}M_k^3`$ and $`\tau_k\zeta_{x,k}=\tau\lvert1-M_k^2c_x\rvert`$ are of the form of $`\mathcal C_{\rm lev}`$. The one term not of that form is the phase $`\arg(1-M_k^2c_x)=-M_k^2\mathrm{Im}\rho_{x+1,x}+O(\epsilon_1^4)`$ of the hopping, present iff $`\mathrm{Im}\rho_{x+1,x}\neq0`$. On the open chain the unitary $`\sum_{x,k}e^{i\vartheta_{x,k}}P_x\otimes\mathbb 1_2\otimes\lvert f_k\rangle\langle f_k\rvert`$ with $`\vartheta_{x+1,k}-\vartheta_{x,k}=\arg(1-M_k^2c_x)`$ removes it; this unitary is diagonal in $`(x,s,k)`$, so it changes no position or branch statistics and nothing for a start in one level. (Beyond the order kept, at relative order $`\epsilon_2^2`$, hops over two sites and record-dependent terms appear.)

**(c)** By (10.2), $`\tilde\Phi_x`$, $`S`$ and $`\varphi_0`$ are unchanged under (2.20), and all coefficients are sesquilinear in $`\varphi_0`$. Hence $`\gamma_x`$, $`\rho_{xy}`$, $`c_x`$, $`\gamma^{(3)}_x`$, and with them $`H^{(2)}`$, $`H^{(2,1)}`$, $`H^{(3)}`$, each separately, are well defined: **yes**. In (10.11) the differences $`V_{x,k}-V_{x',k'}`$ are well defined, the common constant $`e_0`$ is not (it shifts by $`c`$), and $`N(x)`$ only in the sense of (10.2). $`H_{\rm eff}`$ is fixed by the off-diagonal choice of $`\mathcal S`$; a conjugation by a unitary $`\mathbb 1+O(\epsilon_1^2)`$ on $`\mathcal H_b\otimes\mathcal H_c`$ satisfies (10.8) equally and leaves the spectrum unchanged.

### Step 3. Fall, clock and relation (item 3)

*Class:* $`\Phi_x=N_0+xY`$, every $`N_0`$, $`Y`$, $`C_f`$, $`\varphi_0`$ as stated. *Regime:* R1, second order in $`\epsilon_1`$ with the first corrections in $`\epsilon_2`$, $`\epsilon_3`$, first order in $`Y`$, leading order in $`\kappa`$. *Status:* closed forms of the body part of $`\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}`$; remainders as in (10.10).

**(a)** Put $`\tilde N_0:=N_0-\mathbb 1_f`$, $`\tilde Y:=Y-g\,\mathbb 1_f`$, so $`\tilde\Phi_x=\tilde N_0+x\tilde Y`$, and $`\varepsilon_0:=\lVert\tilde N_0\varphi_0\rVert`$, $`\varepsilon_Y:=\lVert\tilde Y\varphi_0\rVert`$. To first order in $`Y`$: $`\gamma_x=\gamma_0+\gamma_1x`$, $`\rho_{xy}=\rho_0+x\rho_Y^{*}+y\rho_Y`$, $`\gamma^{(3)}_x=\gamma^{(3)}_0+\gamma^{(3)}_1x`$, $`c_x=2\rho_0+4\mathrm{Re}\rho_Y\,(x+\tfrac12)-i\mathrm{Im}\rho_Y`$, with

```math
\begin{aligned}
&\gamma_0:=\langle\tilde N_0S\tilde N_0\rangle,\quad \gamma_1:=2\mathrm{Re}\langle\tilde N_0S\tilde Y\rangle,\quad \rho_0:=\langle\tilde N_0S^2\tilde N_0\rangle\ge0,\quad \rho_Y:=\langle\tilde N_0S^2\tilde Y\rangle,\\
&\gamma^{(3)}_0:=\langle\tilde N_0S\tilde N_0S\tilde N_0\rangle,\quad \gamma^{(3)}_1:=\langle\tilde N_0S\tilde YS\tilde N_0\rangle+2\mathrm{Re}\langle\tilde N_0S\tilde N_0S\tilde Y\rangle;\\
&\tau_k=\tau\,(1-2\rho_0M_k^2),\quad \hat M_k=M_k\,(1+\gamma^{(3)}_0M_k^2),\quad G_k=g\,M_k+\gamma^{(3)}_1M_k^3,\quad \mathcal F_k=\gamma_1M_k^2,\quad g_{\zeta,k}=-4M_k^2\mathrm{Re}\rho_Y,\quad V_k=e_0-\gamma_0M_k^2 .
\end{aligned}
\qquad\text{(10.12)}
```

These follow from (10.11) by matching $`M_{x,k}=\hat M_k+G_kx`$, $`V_{x,k}=V_k-\mathcal F_kx`$, $`\tau_k\zeta_{x,k}=\tau(1-M_k^2\mathrm{Re}c_x)`$; $`\hat M_k`$ is the rest term of the level $`k`$ (the "$`M_k`$" of the level data). At leading order in $`\epsilon_2`$, $`\epsilon_3`$: $`\tau_k=\tau`$, $`\hat M_k=M_k`$, $`G_k=gM_k`$, $`g_{\zeta,k}=0`$, and $`\mathcal F_k`$, $`V_k`$ as above. The phase of (10.11) is uniform, $`\theta_k=M_k^2\mathrm{Im}\rho_Y`$; it shifts the plane-wave label of the level block, $`p\to p-\theta_k`$, is of first order in $`Y`$ and independent of $`\lambda`$, and therefore changes $`a_{k,\sigma}`$ only at second order in $`Y`$. The mean record $`\kappa\langle X\rangle x`$ of (8.19) adds $`-\kappa\langle X\rangle`$ to every $`\mathcal F_k`$ and vanishes at leading order in $`\kappa`$.

*Level offset.* The level is conserved, and on the level $`k`$ the offset is $`V_k`$ times the identity. For a start in one level it multiplies the state by the common phase $`e^{-iV_k\lambda}`$ (1.2), so no view and no reading changes: (4.7) and (4.16), derived with $`V_k=0`$, hold unchanged.

**(b)** Inserting (10.12) into (4.16), $`a_{k,\sigma}(0)=\frac{\tau_k^2}{\hat M_k}(\sigma\mathcal F_k-G_k)`$, and keeping the second order in $`\varepsilon`$:

```math
\boxed{\;a_{k,\sigma}(0)=\tau^2\Bigl[-g+\sigma\,\gamma_1M_k+\beta\,M_k^2\Bigr],\qquad \beta:=g\,\bigl(4\rho_0+\gamma^{(3)}_0\bigr)-\gamma^{(3)}_1,\qquad \lvert\gamma_1\rvert M_k\le\frac{2\varepsilon_0\varepsilon_YM_{\max}}{\Delta_f},\quad \rho_0M_k^2\le\epsilon_1^2\;}
\qquad\text{(10.13)}
```

The term in $`\gamma_1`$ is the leading order in $`\epsilon_2`$, $`\epsilon_3`$; the term in $`\beta`$ is their first correction (relative to the $`\gamma_1`$ term it carries $`M_{\max}/\Delta_f\le\epsilon_2`$, respectively $`\epsilon_3`$). These are drift accelerations of the description of $`b`$, $`c`$ with the contract $`H_{\rm eff}`$; the description with $`C`$ has the same position statistics within (10.10) on its range, and no rate in the description with $`C`$ is inferred beyond that. Since the $`M_k`$ are pairwise different:

```math
\begin{aligned}
&\text{leading order in }\epsilon_2,\epsilon_3\ (\text{every }N\ge2):\quad a_{k,+}(0)\ \text{level-independent}\iff\gamma_1=0\iff a_{k,-}(0)\ \text{level-independent}\iff\text{both, with the one value }-\tau^2g;\\
&\text{with the first corrections},\ N\ge3:\quad \text{each of the three}\iff\gamma_1=0\ \text{and}\ \beta=0;\\
&\text{with the first corrections},\ N=2:\quad \text{upper}\iff\gamma_1+\beta(M_0+M_1)=0,\quad \text{lower}\iff\gamma_1-\beta(M_0+M_1)=0,\quad \text{both (then one value)}\iff\gamma_1=\beta=0 .
\end{aligned}
\qquad\text{(10.14)}
```

(For $`N\ge3`$ a polynomial $`\sigma\gamma_1M+\beta M^2`$ with equal values at three points is constant.) Sufficient for $`\gamma_1=0`$: $`\varepsilon_0=0`$ or $`\varepsilon_Y=0`$; it also holds when $`\mathrm{Re}\langle\tilde N_0S\tilde Y\rangle`$ vanishes otherwise. *Order:* at first order in $`\epsilon_1`$ the fall from rest is level-independent in both branches, with the value $`-\tau^2g`$ ((10.1) and (4.22) with $`\mathcal F=m(g_m-g_\eta)=0`$). The independence is lost at second order in $`\epsilon_1`$, already at the leading order of the coefficient in $`\epsilon_2`$, by the branch-odd term $`\sigma\tau^2\gamma_1M_k`$, bilinear in $`\varepsilon_0`$ and $`\varepsilon_Y`$; if $`\gamma_1=0`$, it is lost at second order in $`\epsilon_1`$ and first order in $`\epsilon_2`$, $`\epsilon_3`$ by $`\tau^2\beta M_k^2`$ unless $`\beta=0`$.

**(c)** With $`E^+_{x,k}=e_0+N(x)M_k-\gamma_xM_k^2+\gamma^{(3)}_xM_k^3`$:

```math
E^+_{x,k+1}-E^+_{x,k}=\frac{2\pi}{N\lambda_0}\Bigl[N(x)-\gamma_x\,(M_k+M_{k+1})+\gamma^{(3)}_x\bigl(M_k^2+M_kM_{k+1}+M_{k+1}^2\bigr)\Bigr].
\qquad\text{(10.15)}
```

At leading order in $`\epsilon_2`$, $`\epsilon_3`$ the differences are independent of $`k`$ if and only if $`\gamma_x=0`$ or $`N=2`$ (one difference only): for $`N\ge3`$ and $`\gamma_x\neq0`$, **no**; the second difference is $`-2\gamma_x(2\pi/N\lambda_0)^2`$. Clock of $`S_{\rm clock}(x_0)`$, at the orders of (3.36) (zeroth order in the gradients): the body part is then $`\hat C_b-\gamma_{x_0}\mathcal M^2`$, the two terms commute, and $`\mathcal M^2=m^2+\Sigma\,D-D(d_{N-1}-D)`$ with $`\Sigma:=M_0+M_{N-1}`$. The factor $`e^{i\gamma_{x_0}\Sigma D\lambda}`$ shifts every advance of the mixture (3.36) (taken with $`\eta^0=N(x_0)`$, $`m^0=mN(x_0)`$, $`\tau^0=\tau`$) by $`-\gamma_{x_0}\Sigma\lambda/\lambda_0`$, in both branch components alike; the factor $`e^{-i\gamma_{x_0}D(d_{N-1}-D)\lambda}`$ has phases in $`[0,\tfrac14\lvert\gamma_{x_0}\rvert d_{N-1}^2\lambda]`$ and is the identity for $`N=2`$. Hence

```math
\text{clock statistics}=\text{ring-clock mixture (3.36) with rate }\bar r(x_0)\text{ in the wide-start limit, up to total variation }\le\tfrac12\lvert\gamma_{x_0}\rvert\,d_{N-1}^2\,\lambda;\qquad \text{accuracy }\eta\ \text{for}\ \lambda\le\frac{2\eta}{\lvert\gamma_{x_0}\rvert\,d_{N-1}^2}\ (N\ge3),\ \ \text{all }\lambda\ (N=2\text{ or }\gamma_{x_0}=0).
\qquad\text{(10.16)}
```

*Status:* order estimate; $`\lvert\gamma_{x_0}\rvert d_{N-1}^2\le\epsilon_1^2\Delta_f\,(d_{N-1}/M_{\max})^2`$. The level dependence of $`\tau_k`$ changes $`\varsigma_W`$ of (3.23) only at relative order $`\epsilon_1^2`$.

**(d)** From (10.15), at leading order in $`\epsilon_2`$, $`\epsilon_3`$, $`\bar r(x)=\lambda_0^{-1}\bigl[N(x)-\gamma_x\Sigma\bigr]`$, so $`\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\big\vert_{x=0}=g\,(1+\gamma_0\Sigma)-\gamma_1\Sigma`$ at first order in $`Y`$ and second order in $`\varepsilon`$. With $`v_{\max}^2/d_0^2=\tau^2`$, (4.24) for the body part of $`H_{\rm eff}`$ would read $`a_{k,+}(0)=-\tau^2\,(\bar r(x+1)-\bar r(x))/\bar r(x)`$. Its defect is

```math
\boxed{\;\mathcal R_k:=a_{k,+}(0)+\tau^2\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\Big\vert_{x=0}=\tau^2\Bigl[\gamma_1\,(M_k-\Sigma)+g\,\gamma_0\,\Sigma\Bigr],\qquad \Sigma=M_0+M_{N-1}=2m+d_{N-1}\;}
\qquad\text{(10.17)}
```

up to the first corrections in $`\epsilon_2`$, $`\epsilon_3`$ and $`O(\varepsilon^4)`$. **No**: (4.24) holds for all levels if and only if $`\gamma_1=0`$ and $`g\gamma_0=0`$. Under the hypothesis of (4.24) (a level-independent $`a\neq0`$, which needs $`\gamma_1=0`$ and $`g\neq0`$) it holds iff $`\gamma_0=0`$; otherwise $`a=-\tau^2\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\,(1-\gamma_0\Sigma)`$, and the leading deviation $`d_0\mathcal R_k\hat e=d_0\tau^2g\gamma_0\Sigma\,\hat e`$ contains the data $`m`$, $`d_{N-1}`$ of the body. At first order in $`\epsilon_1`$, (4.24) holds with $`r(x)=N(x)/\lambda_0`$.

### Step 4. Example and control: independent cells (item 4)

*Class:* the cells, every $`\Delta_x>0`$, $`n_x>0`$, $`\varepsilon_x\ge0`$. *Regime:* R1 for (a), (c); (b) is exact on site.

**(a)** $`\varphi_0=\bigotimes_x\lvert0\rangle`$ has $`e_0=-\tfrac12\sum_x\Delta_x`$, the lowest and simple eigenvalue of $`C_f`$; an excited eigenvector has a set of flipped cells. With $`\sigma^{(x)}_1:=\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert`$ on the cell $`x`$, $`\tilde\Phi_x=\varepsilon_x\sigma_1^{(x)}`$ and $`\tilde\Phi_x\varphi_0`$ is the eigenvector with the cell $`x`$ flipped, at $`e_0+\Delta_x`$:

```math
N(x)=n_x,\quad \lVert\tilde\Phi_x\varphi_0\rVert=\varepsilon_x,\quad \varepsilon=\max_x\varepsilon_x,\quad \Delta_f=\min_x\Delta_x,\quad \nu=\varepsilon,\quad
\gamma_x=\frac{\varepsilon_x^2}{\Delta_x},\quad \rho_{xy}=\delta_{xy}\frac{\varepsilon_x^2}{\Delta_x^2},\quad c_x=\frac12\Bigl(\frac{\varepsilon_x^2}{\Delta_x^2}+\frac{\varepsilon_{x+1}^2}{\Delta_{x+1}^2}\Bigr),\quad \gamma^{(3)}_x=0 .
\qquad\text{(10.18)}
```

So $`H^{(2)}=-\sum_x\frac{\varepsilon_x^2}{\Delta_x}P_x\otimes\mathbb 1_2\otimes\mathcal M^2`$, $`H^{(3)}=0`$, the hopping has the real factor $`1-M_k^2c_x`$, and the body part is a member of $`\mathcal C_{\rm lev}`$ with $`M_{x,k}=n_xM_k`$, $`V_{x,k}=e_0-\varepsilon_x^2M_k^2/\Delta_x`$, $`\tau_k\zeta_{x,k}=\tau(1-M_k^2c_x)`$; no term is outside the form.

**(b)** In the basis $`(\lvert0\rangle,\lvert1\rangle)`$, $`C_{f_x}\pm M_k\Phi_x=\pm M_kn_x\mathbb 1-\Omega_{x,k}\bigl(\cos\alpha_{x,k}\,\sigma_3\mp\sin\alpha_{x,k}\,\sigma_1\bigr)`$ with $`\Omega_{x,k}\cos\alpha_{x,k}=\Delta_x/2`$, $`\Omega_{x,k}\sin\alpha_{x,k}=M_k\varepsilon_x`$. Exactly:

```math
\text{eigenvalues }\pm M_kn_x-\Omega_{x,k}\ (\text{lower}),\ \ \pm M_kn_x+\Omega_{x,k}\ (\text{upper}),\quad \Omega_{x,k}=\sqrt{\tfrac14\Delta_x^2+M_k^2\varepsilon_x^2};\qquad \text{lower eigenvector }\cos\tfrac{\alpha_{x,k}}2\lvert0\rangle\mp\sin\tfrac{\alpha_{x,k}}2\lvert1\rangle;\qquad \cos\tfrac{\alpha_{x,k}}2=\Bigl[\tfrac12\Bigl(1+\tfrac{\Delta_x}{2\Omega_{x,k}}\Bigr)\Bigr]^{1/2}.
\qquad\text{(10.19)}
```

*Comparison.* With the other cells in $`\lvert0\rangle`$ the field costs $`e_0+\tfrac12\Delta_x\pm M_kn_x-\Omega_{x,k}=e_0\pm M_kn_x-\frac{\varepsilon_x^2M_k^2}{\Delta_x}+\frac{\varepsilon_x^4M_k^4}{\Delta_x^3}-\dots`$: the part odd in the branch is $`n_xM_k`$ exactly (so $`\gamma_x^{(3)}=0`$), the even part reproduces $`-\gamma_xM_k^2`$ of (10.11), and the remainder has the relative size $`(M_k\varepsilon_x/\Delta_x)^2\le\epsilon_1^2`$. *Overlap:* $`\langle0\vert\text{lower}\rangle=\cos\tfrac{\alpha_{x,k}}2=1-\frac{M_k^2\varepsilon_x^2}{2\Delta_x^2}+O(\epsilon_1^4)`$, the same for both signs. *What it multiplies:* at leading order in $`\tau/\Delta_x`$ the cells follow the body; a hop from $`x`$ to $`x+1`$ returns the cell $`x`$ to $`\lvert0\rangle`$ and takes the cell $`x+1`$ to its lower eigenvector, so the hopping block of the level $`k`$, that is the motion term $`\tau`$, is multiplied by $`\cos\tfrac{\alpha_{x,k}}2\cos\tfrac{\alpha_{x+1,k}}2=1-M_k^2c_x+O(\epsilon_1^4)`$, in agreement with (10.18).

**(c)** The cells are not of the form $`N_0+xY`$ (the $`\sigma_1^{(x)}`$ of more than two cells are linearly independent), so (10.11) is used directly, with $`n_x=1+gx`$ and, to first order in the gradients of the cell data, $`\gamma_x=\gamma_0+\gamma_1x`$, $`\rho_{xx}=\rho_0+\rho_1x`$. Then $`\tau_k=\tau(1-\rho_0M_k^2)`$, $`g_{\zeta,k}=-\rho_1M_k^2`$, $`\hat M_k=M_k`$, $`G_k=gM_k`$, $`\mathcal F_k=\gamma_1M_k^2`$, $`V_k=e_0-\gamma_0M_k^2`$, and by (4.16)

```math
a_{k,\sigma}(0)=\tau^2\Bigl[-g+\sigma\,\gamma_1M_k+2g\,\rho_0M_k^2\Bigr],\qquad \gamma_1=\frac{\varepsilon_{x+1}^2}{\Delta_{x+1}}-\frac{\varepsilon_x^2}{\Delta_x},\quad \rho_0=\frac{\varepsilon_x^2}{\Delta_x^2}\Big\vert_{x=0}\ (\text{the cell at }x=0),
\qquad\text{(10.20)}
```

that is (10.13), (10.14) with $`\beta=2g\rho_0`$ (here $`\rho_{x+1,x}=0`$, whence $`\rho_0`$ in place of the $`2\rho_0`$ of (10.12)). *Control,* $`\varepsilon_x^2/\Delta_x=\gamma`$ for all $`x`$ against cells in which it depends on $`x`$: for constant $`\gamma`$, $`\gamma_1=0`$, so $`\mathcal F_k`$, the branch-odd term $`\sigma\tau^2\gamma_1M_k`$ and the $`\gamma_1`$ part of $`\mathcal R_k`$ vanish. What remains: the level offsets $`V_k=e_0-\gamma M_k^2`$, hence the unequal spacings (10.15) and the range (10.16); the defect $`\mathcal R_k=\tau^2g\gamma\Sigma`$ of (4.24); and the level-dependent hopping, $`a_{k,\sigma}(0)=-\tau^2g\,(1-2\rho_0M_k^2)`$ with $`\rho_0=\gamma/\Delta_0>0`$, level-dependent iff $`g\neq0`$. If $`\gamma_x`$ depends on $`x`$, $`\gamma_1\neq0`$ and the fall is level-dependent at the leading order, with opposite sign in the two branches. For $`\varepsilon_x=0`$ for all $`x`$ every new term vanishes.

### Step 5. Orders (item 5)

All rows: class $`\mathcal D`$ (rows 2–4: linear profiles of the field), regime R1, the ranges of $`\lambda`$ of (10.7), (10.10), (10.16).

| Quantity | Order $`\epsilon_1`$ | First change: order $`\epsilon_1^2`$, leading order in $`\epsilon_2`$, $`\epsilon_3`$ | Order $`\epsilon_1^2`$, first order in $`\epsilon_2`$, $`\epsilon_3`$ | Tags |
| --- | --- | --- | --- | --- |
| Factor that the body sees | $`N(x)`$ on $`G`$; no term linear in $`\epsilon_1`$ | factor unchanged; new on-site term $`-\gamma_xM_k^2\,\mathbb 1_2`$ | factor $`N(x)+\gamma^{(3)}_xM_k^2`$ ($`\epsilon_3`$); motion term times $`1-M_k^2c_x`$ ($`\epsilon_2`$) | (10.1), (10.7), (10.9), (10.10), (10.11) |
| Fall from rest independent of the level | holds, both branches, $`-\tau^2g`$ | lost iff $`\gamma_1\neq0`$: $`\sigma\tau^2\gamma_1M_k`$ | lost iff $`\beta\neq0`$ ($`N\ge3`$): $`\tau^2\beta M_k^2`$ | (10.13), (10.14), (4.22) |
| Clock a ring clock with one rate | holds, rate $`N(x)/\lambda_0`$ | lost iff $`\gamma_{x_0}\neq0`$ and $`N\ge3`$; range (10.16); rate $`\bar r`$ shifted by $`-\gamma_x\Sigma/\lambda_0`$ | cubic term $`\gamma^{(3)}_xM_k^3`$ in $`E^+_{x,k}`$ | (10.15), (10.16), (3.23), (3.36) |
| Relation (4.24) | holds | defect $`\mathcal R_k=\tau^2[\gamma_1(M_k-\Sigma)+g\gamma_0\Sigma]`$; holds iff $`\gamma_1=0`$ and $`g\gamma_0=0`$ | further defect from $`\beta`$ and $`\gamma^{(3)}_x`$ | (10.17), (4.24) |

```math
\text{every row: unchanged at order }\epsilon_1;\quad\text{first change at order }\epsilon_1^2\text{ with the coefficient at its leading order in }\epsilon_2,\ \epsilon_3,\ \text{of relative size }\lvert\gamma_x\rvert M_{\max}\le\epsilon_1\varepsilon=\epsilon_1^2\,\Delta_f/M_{\max}.
\qquad\text{(10.21)}
```

## Result

- **Item 1.** (10.1): $`\hat C`$, exact, whole class; body part in $`\mathcal C`$ with $`m_x=mN(x)`$, $`\eta_x=N(x)`$, $`\zeta_x=1`$, $`V_x=e_0`$; admissible. (10.2): rules under (2.20). (10.4): bound $`\varepsilon M_{\max}\lambda`$, R0, all $`\lambda`$; (10.6): $`2\epsilon_1`$, R1, all $`\lambda`$, order estimate. (10.7): statistics as in a sharp field with $`N(x)`$ through first order in $`\epsilon_1`$ for $`\lambda\ll1/(\epsilon_1^2\Delta_f)`$.
- **Item 2.** (10.8)–(10.10): $`H_{\rm eff}=\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}`$ with remainder and range, R1. (10.11): blocks; member of $`\mathcal C_{\rm lev}`$ up to the hopping phase; all new terms well defined under (2.20).
- **Item 3.** (10.12): level data. (10.13), (10.14): fall from rest and its level-independence. (10.15), (10.16): spacings and clock range. (10.17): defect of (4.24).
- **Item 4.** (10.18)–(10.20): cells, exact on-site solution, fall and control.
- **Item 5.** The table of Step 5 and (10.21).

## Consistency checks

1. **Dimensions.** $`\Phi_x`$, $`N`$, $`\varepsilon`$, $`g`$ are pure numbers; $`\tau`$, $`M_k`$, $`\Delta_f`$, $`e_0`$ are costs. Then $`\gamma_x`$ is an inverse cost and $`\gamma_xM_k^2`$ a cost; $`\rho_{xy}M_k^2`$, $`\gamma^{(3)}_xM_k^2`$, $`\gamma_1M_k`$, $`\beta M_k^2`$ are pure numbers like $`g`$; $`a_{k,\sigma}(0)`$ and $`\mathcal R_k`$ are $`\tau^2`$ times a number, as in (4.16). Passed.
2. **Sharp field and commuting operators.** For $`\varepsilon=0`$: $`W\Pi_0=0`$, so $`\gamma_x=\rho_{xy}=\gamma^{(3)}_x=0`$, $`H_{\rm eff}=\hat C`$, $`Q_0\Psi=0`$ and $`p=\hat p`$ exactly, which is (2.3) with $`n_x=N(x)`$, $`e_f=e_0`$. If every $`\Phi_x`$ commutes with $`C_f`$, the simple eigenvector $`\varphi_0`$ is an eigenvector of every $`\Phi_x`$, so $`\varepsilon=0`$: all new terms need $`[\Phi_x,C_f]\neq0`$. Passed.
3. **Cell, exact against second order.** The exact lower eigenvalue and overlap (10.19) reproduce $`-\gamma_xM_k^2`$, $`\gamma^{(3)}_x=0`$ and the hopping factor $`1-M_k^2c_x`$ of (10.18), derived independently from (10.9), (10.10). Passed.

## Open issues

- The two small numbers of the question do not control the class $`\mathcal D`$: a third one, $`\epsilon_3=\nu M_{\max}/\Delta_f`$, enters the conditions and the first corrections. It is stated with every result; whether it should be part of the regime of the question is for the main model.
- (10.6), the R1 part of (10.7) and the remainders of (10.10) are order estimates: their constants, and the dependence of (10.7) on the number of readings, are not bounded explicitly.
- The accelerations (10.13), (10.20) are those of the description with $`H_{\rm eff}`$; for the description with $`C`$ only the agreement of the statistics within (10.10) is derived, not a statement about its acceleration.
- (10.16) has the orders of (3.36) (zeroth order in the gradients). The loss of clock coherence by the level-dependent force $`\mathcal F_k`$, which separates the levels in position at first order in the gradients, is not treated.
- Where $`2\epsilon_1+2\epsilon_2+\epsilon_3\ge1`$ (a slow field) the expansion fails and only the R0 statements (10.1), (10.2), (10.4) and the first part of (10.7) remain.

## Methods used

- Compression of the contract onto an eigenvector of the field
- Duhamel formula and norm bounds
- Schrieffer–Wolff block diagonalisation (nondegenerate perturbation theory with a gap)
- Sylvester equation, expansion in commutators with the body contract
- Rayleigh–Schrödinger second and third order with the reduced resolvent
- Exact diagonalisation of a two-place cell
- Level blocks and linear level profiles of the class $`\mathcal C_{\rm lev}`$
