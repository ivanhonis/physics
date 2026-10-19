# Field with its own contract: seen factor, second-order terms, fall and clock

- **Subproject:** 05-ilang-free-fall
- **Package:** 10-field-own-contract
- **Version:** v4
- **Mode:** external regeneration
- **Date:** 2026-10-11

## Changes from previous version

Only the two issues of verification.r2.md (external round 2) are answered; every sentence and display of v3 that they do not touch is unchanged.

- **I1 (reciprocal of the clock rate).**
  - Setup: new bullet "Not small in R1" ($`\varepsilon`$, $`\gamma_xM_{\max}`$ and $`\gamma^{(3)}_xM_{\max}^2`$ are not small numbers of R1).
  - Step 3(b): new (10.32), the acceleration before the expansion, with the paragraph "Control of the expansion"; one sentence after (10.14) and one after (10.22) on the range of the lines with the first corrections.
  - Step 3(c): one sentence after (10.15) on the sign of the spacings; new paragraph and new (10.33) on the sign and the vanishing of the mean rate and on the ring clock with a rate that is zero or negative.
  - Step 3(d): rewritten. New (10.34): relative gradient of the mean rate and defect of (4.24) with the denominator kept. New (10.35): the condition under which the comparison is defined, its margin, and the hierarchy (H). New (10.36): the members with a vanishing mean rate. Paragraph on a negative mean rate. (10.17), (10.26) and their "if and only if" statements are restated for the range in which they are derived; the condition of (10.26) for $`N=2`$ is corrected to its form with the denominator kept.
  - Step 4(c): the defect in the control is given with the denominator. Step 5: rows 1–4 and (10.21). Result, check 3, Open issues.
- **I2 (cells).** The question was amended (item 4(c), Scope). Step 4 (header and (c)): $`\mathcal L`$ of (10.31) is the class of item 4(c) of the question and no longer an added assumption; the constant-$`\gamma`$ control is stated with its condition on $`c_x`$; "Cells outside $`\mathcal L`$" states which results of items 4(a), 4(b) hold. Result and Open issues accordingly.
- **Tags.** (10.1)–(10.31) are kept; none is withdrawn or renumbered. Restated: (10.17), (10.26) (same formulas, now under (H) of (10.35)), (10.21) (same formula, one clause added), (10.31) (same conditions, new status). New: (10.32)–(10.36).

## Response to verification

- **I1: Accepted and fixed in Step 3(d)** ((10.34)–(10.36), restated (10.17), (10.26)), with the additions listed above in "Setup", Step 3(b), Step 3(c), Step 4(c), Step 5 and the Result. The reciprocal of the mean rate is no longer expanded: the defect is given with the denominator $`D_0=1-\gamma_0\Sigma`$; the comparison is defined if and only if $`D_0\neq0`$; the expanded forms (10.17), (10.26) hold under the hierarchy (H), $`\lvert\gamma_0\rvert\Sigma\ll1`$; the verifier's two-level member is the control of (10.36). Places checked, and what was found:
  1. Steps 1, 2: the new terms are compared with $`\Delta_f`$ only; the one comparison with the rest term is (P) of (10.27), already a condition. No change.
  2. (10.12): $`\tau_k`$ and $`g_{\zeta,k}`$ are controlled by $`\epsilon_1^2`$, $`\hat M_k`$ by the first margin of (10.28); $`G_k`$, $`\mathcal F_k`$, $`V_k`$ are exact in $`\gamma_1`$, $`\gamma_0`$. No change.
  3. (10.13), (10.14), (10.22), (10.23): at leading order exact in $`\gamma_1M_k`$ (added to $`-g`$, never treated as small against it); with the first corrections the expansion of $`\tau_k^2/\hat M_k`$ is controlled by $`\epsilon_1^2`$ and (10.28), but the terms dropped can exceed the term in $`\beta`$ when $`\gamma_1\neq0`$. New (10.32) and the range of the lines with the first corrections.
  4. (10.24), (10.25): $`\tau_k\to\tau`$, $`\hat M_k\to M_k`$ are controlled by $`\epsilon_1^2`$ and (10.28). No change.
  5. (10.15), (10.29): polynomial identities, nothing expanded; the sign of a spacing is not fixed by R1. One sentence added.
  6. (10.16), (10.30): exact in $`\gamma_{x_0}\Sigma`$, no division by the rate; they hold for every sign of $`\bar r(x_0)`$. New (10.33) states what the ring clock is for a rate that is zero or negative.
  7. (10.17), (10.26): the uncontrolled reciprocal. Fixed as above.
  8. Step 4: (10.18), (10.19) are controlled by $`\epsilon_1^2`$; (10.20) drops a term of relative order $`\epsilon_1^2`$; the defect of the control divided by the rate. Restated.
  9. Step 5, (10.21), Result, twin: brought into agreement.
- **I2: Accepted.** The main model amended the question after this verification: item 4(c) now asks the evaluation for the cells with $`n_x=1+gx`$ whose level profiles are linear, with the control inside that subclass, and, for the cells outside it, only which results of items 4(a), 4(b) hold; the fall in level profiles that are not linear is out of scope (a later package). The package now states: $`\mathcal L`$ of (10.31) is that subclass, named by conditions on the cell data; (10.20) and its control are the answer to item 4(c); cells with $`\varepsilon_x^2/\Delta_x`$ independent of $`x`$ are in $`\mathcal L`$ only if their $`c_x`$ is linear in $`x`$ as well; for the cells outside $`\mathcal L`$ every result of items 4(a), 4(b) holds, and their fall is not stated. Fixed in Step 4 (header, (c)), the Result and the Open issues.

## Setup and assumptions

- **Setting.** The class $`\mathcal D`$, the start $`\Psi_0=\phi\otimes\varphi_0\otimes\chi`$ with $`C_f\varphi_0=e_0\varphi_0`$ ($`e_0`$ simple, gap $`\Delta_f`$), and $`N(x)`$, $`\tilde\Phi_x`$, $`\varepsilon_x`$, $`\varepsilon`$, $`d_k`$, $`M_k`$, $`M_{\max}`$, $`N_{\max}`$, $`\epsilon_1`$, $`\epsilon_2`$, $`\mathcal C`$, $`\mathcal C_{\rm lev}`$ are those of question.md; $`\lambda\ge0`$. Class, field start, linear profiles and cells are assumptions of this package (M8, M9, A11). Inputs, as quoted in question.md: (2.1), (2.3), (2.20), (2.22) of 02-field-object; (3.23), (3.36) of 03-clock-and-fall; (4.7), (4.16), (4.19), (4.22), (4.24) of 04-branch-fall; (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (8.1), (8.19), (8.20) of 04-ilang-time/08-maximal-speed; (17.15) of 03-ilang-space/17-motion.
- **Notation.** $`P_x:=\lvert x\rangle\langle x\rvert`$, $`h_x:=\lvert x+1\rangle\langle x\rvert`$, $`\mathcal M:=m\mathbb 1_N+D`$ (so $`\mathcal M\lvert f_k\rangle=M_k\lvert f_k\rangle`$, $`G=\sigma_3\otimes\mathcal M`$, $`\lVert G\rVert=M_{\max}`$), $`B_x:=P_x\otimes G`$, $`\langle O\rangle:=\langle\varphi_0\vert O\vert\varphi_0\rangle`$, $`Q:=\mathbb 1_f-\lvert\varphi_0\rangle\langle\varphi_0\rvert`$, $`Q_0:=\mathbb 1-\Pi_0`$, and the reduced resolvent $`S:=Q\,(C_f-e_0)^{-1}Q`$, $`\lVert S\rVert=1/\Delta_f`$. Tensor factors are written in the order $`(b,c),f`$ where convenient. The $`M_k`$ are positive and pairwise different.
- **A third number of the class.** $`\nu:=\max_x\lVert Q\tilde\Phi_xQ\rVert`$ and $`\epsilon_3:=\nu M_{\max}/\Delta_f`$ (the pair term inside the excited states of the field against the gap). In $`\mathcal D`$ it is bounded neither by $`\epsilon_1`$ nor by $`\epsilon_2`$; for the cells of item 4, $`\epsilon_3=\epsilon_1`$. $`\epsilon_3\ll1`$ is a condition of this package, in addition to the two small numbers of the question. It is a sufficient condition: it enters the norm estimate by which the two diagonal blocks of the contract are shown to be separated ("Perturbation theory used"), and it is not shown to be necessary for the separation or for an effective description. A member that needs no such condition: the sharp field ($`\varepsilon=0`$) is exactly reducible for every $`\nu`$ and every $`\epsilon_2`$, by (2.3) ($`H_{\rm eff}=\hat C`$, $`Q_0\Psi(\lambda)=0`$). Every order estimate below is derived in the regime R1, which contains this condition, and this is stated with each result; for the members of $`\mathcal D`$ in which $`\epsilon_3`$ is not small this package derives the statements of R0 only: (10.1), (10.2), (10.4) and the first part of (10.7).
- **Regimes.** *R0:* no condition, every member of $`\mathcal D`$, every start $`\phi`$, all $`\lambda\ge0`$ (exact statements and bounds). *R1:* $`2\epsilon_1+2\epsilon_2+\epsilon_3<1`$, in the weak-record regime ($`\kappa\to0`$ at fixed $`\lambda`$, chain and start; $`\lVert\hat C-e_0\rVert\le\tau+N_{\max}M_{\max}+\kappa L\lVert X\rVert`$, and this bound tends to $`\tau+N_{\max}M_{\max}=\epsilon_2\Delta_f`$); order estimates are expansions in $`\epsilon_1`$ whose coefficients are expanded in $`\epsilon_2`$ and $`\epsilon_3`$. R1 is a sufficient condition for the construction used here, not a necessary one.
- **Not small in R1.** The small numbers of R1 are $`\epsilon_1`$, $`\epsilon_2`$, $`\epsilon_3`$. The pure number $`\varepsilon=\epsilon_1\Delta_f/M_{\max}`$ is not one of them: $`\Delta_f/M_{\max}\ge N_{\max}/\epsilon_2`$, and R1 does not bound it from above, so $`\varepsilon`$ can be small, of order one or large. With it the pure numbers $`\lvert\gamma_x\rvert M_{\max}\le\varepsilon_x^2M_{\max}/\Delta_f\le\epsilon_1\varepsilon`$ and $`\lvert\gamma^{(3)}_x\rvert M_{\max}^2\le\varepsilon\,\epsilon_1\epsilon_3`$ (see (10.9), (10.27)) are not bounded by the small numbers of R1. The terms of second order in $`\epsilon_1`$ of $`H_{\rm eff}`$ are small against $`\Delta_f`$; they are small against the rest term $`N(x)M_k`$ and against the level spacing of the body only under a further hierarchy. Each such hierarchy is named where it is used: (P), (P′) of (10.27) and the margins of (10.28) for $`\gamma^{(3)}_x`$, and (H) of (10.35) for $`\gamma_x`$. Outside these places no statement of this package treats $`\gamma_xM_k`$ as small against $`N(x)`$, and no rate is divided by except under the condition of (10.35).
- **Records at leading order in $`\kappa`$.** The convention is that of 04-branch-fall, whose (4.7), (4.16) and (4.24) are used: at leading order in $`\kappa`$ the body evolves by the effective body contract (8.19) of 04-ilang-time/08-maximal-speed, which is its own contract plus $`\kappa\langle X\rangle\hat x`$, $`\hat x:=\sum_xx\,P_x`$, $`\langle X\rangle=\langle\chi\vert X\vert\chi\rangle`$. The plain gradient $`-\kappa\langle X\rangle`$ of this contract is one of the first-order gradients and is kept. $`\langle X\rangle=0`$ is a condition, named with every statement that needs it.
- **Perturbation theory used (standard).** In R1 the diagonal blocks $`\Pi_0C\Pi_0`$ and $`Q_0CQ_0`$ have spectra separated by at least $`\Delta_f(1-2\epsilon_2-\epsilon_3)`$, more than twice the norm $`\le\varepsilon M_{\max}`$ of the off-diagonal block. Then a unitary $`e^{\mathcal S}`$ with $`\mathcal S`$ anti-self-adjoint and block-off-diagonal with respect to $`\Pi_0`$ block-diagonalises $`C`$ exactly (Schrieffer–Wolff form of nondegenerate perturbation theory), and $`\mathcal S`$ is given by its series in the off-diagonal block. The separation is shown by norm estimates ($`\lVert\hat C-e_0\rVert\le\epsilon_2\Delta_f`$, $`\lVert Q_0WQ_0\rVert\le\nu M_{\max}`$ with $`W`$ of (10.3)): R1 guarantees it; where R1 fails the separation is not guaranteed by this argument, and it is not excluded.
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

*Leading order.* At second order and leading order in $`\epsilon_2`$, $`\epsilon_3`$ the body part is a member of $`\mathcal C_{\rm lev}`$: **yes**, with $`\tau_k=\tau`$, $`\zeta_{x,k}=1`$, $`M_{x,k}=N(x)M_k`$, $`V_{x,k}=e_0-\gamma_xM_k^2`$. All defining inequalities of the class hold without a further condition, for every member of $`\mathcal D`$: $`\tau>0`$, $`\zeta_{x,k}=1>0`$, and $`M_{x,k}>0`$ because $`N(x)>0`$ and $`M_k>0`$. This is a statement about the body part of $`\hat C+H^{(2)}`$; (10.10) states how well that operator reproduces the statistics. It is a member of $`\mathcal C`$ if and only if $`\gamma_x=0`$ for all $`x`$ (the $`M_k^2`$ are pairwise different).

*With the first corrections.* The hopping modulus $`\tau_k\zeta_{x,k}=\tau\lvert1-M_k^2c_x\rvert\ge\tau(1-2\epsilon_1^2)>\tfrac12\tau`$ is positive in R1 without a further condition ($`\lvert c_x\rvert\le2\varepsilon^2/\Delta_f^2`$ and $`2\epsilon_1<1`$), and $`V_{x,k}`$ is real. The coefficient of $`\sigma_3`$, which takes the place of $`M_{x,k}`$, is not positive in every member. With $`N_{\min}:=\min_xN(x)`$:

```math
\mu_{x,k}:=N(x)M_k+\gamma^{(3)}_xM_k^3;\qquad\mathrm{(P)}:\ \ \mu_{x,k}>0\ \ \text{for all }x,k;\qquad\mathrm{(P')}:\ \ \min_{x,k}\mu_{x,k}\gg\epsilon_1^2\bigl[(\epsilon_2+\epsilon_3)^2+\epsilon_1^2\bigr]\Delta_f;\qquad\lvert\gamma^{(3)}_x\rvert M_k^2\le\frac{\varepsilon_x^2\,\nu\,M_k^2}{\Delta_f^2}\le\varepsilon\,\epsilon_1\epsilon_3 .
\qquad\text{(10.27)}
```

In R1 the body part of $`\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}`$ is a member of $`\mathcal C_{\rm lev}`$ up to the hopping phase, with $`M_{x,k}=\mu_{x,k}`$ and $`\tau_k\zeta_{x,k}=\tau\lvert1-M_k^2c_x\rvert`$, **if and only if (P) holds**. (P) is the margin of the leading rest term $`N(x)M_k`$ against its first correction $`\gamma^{(3)}_xM_k^3`$; R1 does not imply it, because $`N(x)>0`$ has no lower bound in $`\mathcal D`$. Sufficient for (P): $`\varepsilon\,\epsilon_1\epsilon_3<N_{\min}`$, by the last relation of (10.27). (P′) is the margin against the remainder of (10.10): the dropped terms change the coefficient of $`\sigma_3`$ of an on-site block by at most their norm, so under (P′) they do not change its sign (order estimate).

*If (P) fails.* Such members exist in R1. Control: a field with two places, $`C_f=\Delta\lvert1\rangle\langle1\rvert`$, $`\varphi_0=\lvert0\rangle`$, and for all $`x`$ $`\Phi_x=n\,\mathbb 1+v\,(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert)+a\,\lvert1\rangle\langle1\rvert`$ with $`n>0`$, $`a<0`$. Then $`N(x)=n`$, $`\varepsilon=\lvert v\rvert`$, $`\nu=\lvert a\rvert`$, $`\gamma_x=v^2/\Delta`$, $`\gamma^{(3)}_x=a\,v^2/\Delta^2`$, and $`\mu_{x,k}<0`$ for all $`x`$, $`k`$ when $`n<\lvert a\rvert v^2M_0^2/\Delta^2`$, with $`\epsilon_1`$, $`\epsilon_2`$, $`\epsilon_3`$ as small as wanted. Where $`\mu_{x,k}<0`$:
- the class condition $`M_{x,k}>0`$ fails, and the body part with the first corrections is not a member of $`\mathcal C_{\rm lev}`$;
- the on-site eigenvalues of the level $`k`$ at $`x`$ are $`V_{x,k}\pm\lvert\mu_{x,k}\rvert`$; the upper one is $`V_{x,k}-\mu_{x,k}`$, with the branch place $`s=2`$, and $`V_{x,k}+\mu_{x,k}`$ is the lower one (it is the on-site eigenvalue of the branch place $`s=1`$ in every case);
- if $`\mu_{x,k}<0`$ for all $`x`$ of one level $`k`$, the exchange of the two branch places in that level (conjugation with $`\sigma_1`$ on the branch label, on $`\lvert f_k\rangle`$) turns the level block into one of the form of the class with $`M_{x,k}=\lvert\mu_{x,k}\rvert`$ and the same hopping block, and it acts on the start; if $`\mu_{x,k}`$ vanishes or changes sign along the chain, no such exchange does this.

The statements of this package that use the quoted results for members of $`\mathcal C_{\rm lev}`$ with the first corrections, or that call $`V_{x,k}+M_{x,k}`$ the upper on-site eigenvalue with the first corrections, are made under (P) only. For a member in which (P) fails, or holds without the margin (P′), they are not derived here. The leading-order statements remain statements about the body part of $`\hat C+H^{(2)}`$; where (P) fails at $`(x,k)`$, $`N(x)M_k\le\epsilon_1^2\epsilon_3\Delta_f`$, so the range of (10.10) on which that operator reproduces the statistics to an accuracy $`\eta`$ is at most of the order $`\eta/(N(x)M_k)`$, shorter than the inverse of the rest term of that level.

*The phase.* Under (P) the one term not of that form is the phase $`\arg(1-M_k^2c_x)=-M_k^2\mathrm{Im}\rho_{x+1,x}+O(\epsilon_1^4)`$ of the hopping, present iff $`\mathrm{Im}\rho_{x+1,x}\neq0`$. On the open chain the unitary $`U:=\sum_{x,k}e^{i\vartheta_{x,k}}P_x\otimes\mathbb 1_2\otimes\lvert f_k\rangle\langle f_k\rvert`$ with $`\vartheta_{x+1,k}-\vartheta_{x,k}=\arg(1-M_k^2c_x)`$ removes it from the contract: $`U^{\dagger}H_{\rm eff}U`$ has the hopping factors $`\lvert1-M_k^2c_x\rvert`$ and is otherwise unchanged. The unitary acts on the start as well: $`e^{-iH_{\rm eff}\lambda}(\phi\otimes\chi)=U\,e^{-iU^{\dagger}H_{\rm eff}U\lambda}\,(U^{\dagger}\phi\otimes\chi)`$. $`U`$ is diagonal in $`(x,s,k)`$ and is the identity on $`c`$, so the statistics of the readings of the position and of the branch label, and of every reading on $`c`$, are for the contract with the phase and the start $`\phi`$ those for the contract without the phase and the start $`U^{\dagger}\phi`$; for readings of the clock label, which are not diagonal in $`k`$, this does not hold. $`U^{\dagger}\phi\neq\phi`$ in general, also for a start in one level: there $`U^{\dagger}`$ multiplies the weight at $`x`$ by $`e^{-i\vartheta_{x,k}}`$, which changes the plane-wave labels of the start. The phase is therefore not without effect: it is equivalent to a change of the start that depends on the level. For the linear profiles of the field its effect on a branch start at rest is the velocity (10.25). (Beyond the order kept, at relative order $`\epsilon_2^2`$, hops over two sites and record-dependent terms appear.)

**(c)** By (10.2), $`\tilde\Phi_x`$, $`S`$ and $`\varphi_0`$ are unchanged under (2.20), and all coefficients are sesquilinear in $`\varphi_0`$. Hence $`\gamma_x`$, $`\rho_{xy}`$, $`c_x`$, $`\gamma^{(3)}_x`$, and with them $`H^{(2)}`$, $`H^{(2,1)}`$, $`H^{(3)}`$, each separately, are well defined: **yes**. In (10.11) the differences $`V_{x,k}-V_{x',k'}`$ are well defined, the common constant $`e_0`$ is not (it shifts by $`c`$), and $`N(x)`$ only in the sense of (10.2). $`H_{\rm eff}`$ is fixed by the off-diagonal choice of $`\mathcal S`$; a conjugation by a unitary $`\mathbb 1+O(\epsilon_1^2)`$ on $`\mathcal H_b\otimes\mathcal H_c`$ satisfies (10.8) equally and leaves the spectrum unchanged.

### Step 3. Fall, clock and relation (item 3)

*Class:* $`\Phi_x=N_0+xY`$, every $`N_0`$, $`Y`$, $`C_f`$, $`\varphi_0`$ as stated. *Regime:* R1, second order in $`\epsilon_1`$ with the first corrections in $`\epsilon_2`$, $`\epsilon_3`$, first order in $`Y`$, leading order in $`\kappa`$ in the convention of "Setup" (the plain gradient $`-\kappa\langle X\rangle`$ is kept). *Status:* closed forms of the body part of $`\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}`$; remainders as in (10.10). *Condition for the first corrections:* (10.28) below, the form of (P) for the linear profiles; every statement at leading order in $`\epsilon_2`$, $`\epsilon_3`$ holds for the whole class.

**(a)** Put $`\tilde N_0:=N_0-\mathbb 1_f`$, $`\tilde Y:=Y-g\,\mathbb 1_f`$, so $`\tilde\Phi_x=\tilde N_0+x\tilde Y`$, and $`\varepsilon_0:=\lVert\tilde N_0\varphi_0\rVert`$, $`\varepsilon_Y:=\lVert\tilde Y\varphi_0\rVert`$. To first order in $`Y`$: $`\gamma_x=\gamma_0+\gamma_1x`$, $`\rho_{xy}=\rho_0+x\rho_Y^{*}+y\rho_Y`$, $`\gamma^{(3)}_x=\gamma^{(3)}_0+\gamma^{(3)}_1x`$, $`c_x=2\rho_0+4\mathrm{Re}\rho_Y\,(x+\tfrac12)-i\mathrm{Im}\rho_Y`$, with

```math
\begin{aligned}
&\gamma_0:=\langle\tilde N_0S\tilde N_0\rangle,\quad \gamma_1:=2\mathrm{Re}\langle\tilde N_0S\tilde Y\rangle,\quad \rho_0:=\langle\tilde N_0S^2\tilde N_0\rangle\ge0,\quad \rho_Y:=\langle\tilde N_0S^2\tilde Y\rangle,\\
&\gamma^{(3)}_0:=\langle\tilde N_0S\tilde N_0S\tilde N_0\rangle,\quad \gamma^{(3)}_1:=\langle\tilde N_0S\tilde YS\tilde N_0\rangle+2\mathrm{Re}\langle\tilde N_0S\tilde N_0S\tilde Y\rangle;\\
&\tau_k=\tau\,(1-2\rho_0M_k^2),\quad \hat M_k=M_k\,(1+\gamma^{(3)}_0M_k^2),\quad G_k=g\,M_k+\gamma^{(3)}_1M_k^3,\quad \mathcal F_k=\gamma_1M_k^2,\quad g_{\zeta,k}=-4M_k^2\mathrm{Re}\rho_Y,\quad V_k=e_0-\gamma_0M_k^2\\
&\bigl(\text{the terms in }\rho_0,\ \rho_Y,\ \gamma^{(3)}_0,\ \gamma^{(3)}_1\text{: level data of a member of }\mathcal C_{\rm lev}\text{ under (10.28)}\bigr).
\end{aligned}
\qquad\text{(10.12)}
```

These follow from (10.11) by matching $`M_{x,k}=\hat M_k+G_kx`$, $`V_{x,k}=V_k-\mathcal F_kx`$, $`\tau_k\zeta_{x,k}=\tau(1-M_k^2\mathrm{Re}c_x)`$; $`\hat M_k`$ is the rest term of the level $`k`$ (the "$`M_k`$" of the level data). At leading order in $`\epsilon_2`$, $`\epsilon_3`$: $`\tau_k=\tau`$, $`\hat M_k=M_k`$, $`G_k=gM_k`$, $`g_{\zeta,k}=0`$, and $`\mathcal F_k`$, $`V_k`$ as above.

*Inequalities of the class.* The linear level profiles (10.12) are those of a member of $`\mathcal C_{\rm lev}`$ on the chain $`\lvert x\rvert\le L`$ if and only if $`\tau_k>0`$, $`M_{x,k}=\hat M_k+G_kx>0`$ for $`\lvert x\rvert\le L`$ and $`\zeta_{x,k}=1+g_{\zeta,k}(x+\tfrac12)>0`$ for $`-L\le x\le L-1`$. At leading order in $`\epsilon_2`$, $`\epsilon_3`$ they hold for every member of the class: $`M_{x,k}=M_kN(x)>0`$ by $`\lvert g\rvert(L+1)<1`$, $`\tau_k=\tau`$, $`\zeta_{x,k}=1`$. With the first corrections, $`\tau_k>0`$ holds in R1 ($`2\rho_0M_k^2\le2\epsilon_1^2<\tfrac12`$), and the other two are the conditions

```math
\hat M_k>\lvert G_k\rvert\,L\iff1+\gamma^{(3)}_0M_k^2>\bigl\lvert g+\gamma^{(3)}_1M_k^2\bigr\rvert\,L,\qquad\lvert g_{\zeta,k}\rvert\,(L-\tfrac12)<1\qquad\text{for all }k;\qquad\text{margins:}\quad\bigl(\lvert\gamma^{(3)}_0\rvert+\lvert\gamma^{(3)}_1\rvert L\bigr)M_{\max}^2\ll1-\lvert g\rvert L,\qquad M_0\,(1-\lvert g\rvert L)\gg\epsilon_1^2\bigl[(\epsilon_2+\epsilon_3)^2+\epsilon_1^2\bigr]\Delta_f .
\qquad\text{(10.28)}
```

The first margin is sufficient for the first relation, and it makes $`\lvert\gamma^{(3)}_0\rvert M_k^2\ll1`$, which the expansion of $`\tau_k^2/\hat M_k`$ in (10.13) and (10.22) uses; the second is the margin against the remainder of (10.10). Sufficient for the relation on $`g_{\zeta,k}`$: $`8\epsilon_1^2<1`$ (because $`L\,\varepsilon_Y\le\varepsilon_L+\varepsilon_0\le2\varepsilon`$ and $`\lvert\rho_Y\rvert\le\varepsilon_0\varepsilon_Y/\Delta_f^2`$). In what follows "(10.28)" means the two relations with the two margins. R1 does not imply it: the control of Step 2(b) with $`n=1`$ is a member of the class of this step ($`Y=0`$) in which $`\hat M_k<0`$ when $`\lvert a\rvert v^2M_k^2/\Delta^2>1`$, and R1 allows this ($`\lvert a\rvert v^2M_{\max}^2/\Delta^2=\lvert a\rvert\epsilon_1^2`$, which exceeds $`1`$ with $`\epsilon_3=\lvert a\rvert M_{\max}/\Delta`$ small when $`M_{\max}/\Delta\ll\epsilon_1^2`$). If (10.28) fails, the statements with the first corrections of (b) and (c) are not derived for that member (Step 2(b), "If (P) fails").

The phase of (10.11) is uniform, $`\theta_k=M_k^2\mathrm{Im}\rho_Y`$ (from here on $`\theta_k`$ is this phase; the angle of (5.6) of 04-ilang-time/05-moving-clock is not used by name); it shifts the plane-wave label of the level block, $`p\to p-\theta_k`$, and is of first order in $`Y`$ and independent of $`\lambda`$. It changes the drift acceleration $`a_{k,\sigma}`$ only at second order in $`Y`$, and at first order in $`Y`$ it gives a branch start at rest a velocity; both statements are derived in (b), (10.24), (10.25). The mean record $`\kappa\langle X\rangle x`$ of (8.19) of 04-ilang-time/08-maximal-speed adds $`-\kappa\langle X\rangle`$ to every $`\mathcal F_k`$ of the effective body contract. It is one of the first-order gradients and is kept ("Setup"): in (4.7) and (4.16) the $`\mathcal F_k`$ of (10.12) is replaced by $`\mathcal F_k-\kappa\langle X\rangle`$.

*Level offset.* The level is conserved, and on the level $`k`$ the offset is $`V_k`$ times the identity. For a start in one level it multiplies the state by the common phase $`e^{-iV_k\lambda}`$ (1.2), so no view and no reading changes: (4.7) and (4.16), derived with $`V_k=0`$, hold unchanged.

**(b)** Inserting (10.12) into (4.16), $`a_{k,\sigma}(0)=\frac{\tau_k^2}{\hat M_k}(\sigma\mathcal F_k-G_k)`$, and keeping the second order in $`\varepsilon`$, for $`\langle X\rangle=0`$ (for $`\langle X\rangle\neq0`$ see (10.22)); with the first corrections this uses (10.28), because (4.16) is quoted for members of $`\mathcal C_{\rm lev}`$ and $`1/\hat M_k`$ is expanded:

```math
\boxed{\;\langle X\rangle=0:\quad a_{k,\sigma}(0)=\tau^2\Bigl[-g+\sigma\,\gamma_1M_k+\beta\,M_k^2\Bigr],\qquad \beta:=g\,\bigl(4\rho_0+\gamma^{(3)}_0\bigr)-\gamma^{(3)}_1,\qquad \lvert\gamma_1\rvert M_k\le\frac{2\varepsilon_0\varepsilon_YM_{\max}}{\Delta_f},\quad \rho_0M_k^2\le\epsilon_1^2\qquad(\text{term in }\beta\text{: under (10.28)})\;}
\qquad\text{(10.13)}
```

The term in $`\gamma_1`$ is the leading order in $`\epsilon_2`$, $`\epsilon_3`$; the term in $`\beta`$ is their first correction (relative to the $`\gamma_1`$ term it carries $`M_{\max}/\Delta_f\le\epsilon_2`$, respectively $`\epsilon_3`$). These are drift accelerations of the description of $`b`$, $`c`$ with the contract $`H_{\rm eff}`$; the description with $`C`$ has the same position statistics within (10.10) on its range, and no rate in the description with $`C`$ is inferred beyond that.

*Control of the expansion.* Before the expansion, (4.16) with the level data (10.12) reads

```math
a_{k,\sigma}(0)=\tau^2\,\frac{\bigl(1-2\rho_0M_k^2\bigr)^2}{1+\gamma^{(3)}_0M_k^2}\,\Bigl[-g+\sigma\,\gamma_1M_k-\gamma^{(3)}_1M_k^2\Bigr]\qquad(\langle X\rangle=0;\ \text{with the first corrections, under (10.28)}),
\qquad\text{(10.32)}
```

which is exact in the level data. At leading order in $`\epsilon_2`$, $`\epsilon_3`$ the prefactor is $`1`$ and $`\gamma^{(3)}_1`$ is absent, so $`a_{k,\sigma}(0)=\tau^2[-g+\sigma\gamma_1M_k]`$ without any expansion: the term $`\sigma\gamma_1M_k`$ is added to $`-g`$ and is not treated as small against it. R1 does not bound $`\lvert\gamma_1\rvert M_k/\lvert g\rvert`$ ("Not small in R1"), so the level-dependent term can be of the size of $`-\tau^2g`$ or larger. (10.13) expands the prefactor of (10.32) only: $`2\rho_0M_k^2\le2\epsilon_1^2`$ is small in R1, and $`\lvert\gamma^{(3)}_0\rvert M_k^2\ll1`$ is the first margin of (10.28). The terms dropped are $`-\tau^2\bigl(\sigma\gamma_1M_k-\gamma^{(3)}_1M_k^2\bigr)\bigl(4\rho_0+\gamma^{(3)}_0\bigr)M_k^2`$ and $`\tau^2\lvert g\rvert\,O\bigl(\epsilon_1^4+(\gamma^{(3)}_0M_k^2)^2\bigr)`$; against the kept terms $`\sigma\gamma_1M_k`$ and $`\gamma^{(3)}_1M_k^2`$ they are of relative order $`\epsilon_1^2+\lvert\gamma^{(3)}_0\rvert M_k^2`$, the order of the remainder of (10.10) (the terms of fourth order of $`H_{\rm eff}`$ change $`\mathcal F_k`$ at the same relative order). So (10.13) is controlled by $`\epsilon_1`$ and by the margins of (10.28), with one restriction on the term in $`\beta`$: it exceeds what is dropped only if $`\lvert\gamma_1\rvert M_k\,\bigl(\epsilon_1^2+\lvert\gamma^{(3)}_0\rvert M_k^2\bigr)\ll\lvert\beta\rvert M_k^2`$, in particular for $`\gamma_1=0`$. No rate is divided by, and $`\gamma_0`$ does not enter: the level offsets do not change the fall.

Since the $`M_k`$ are pairwise different:

```math
\begin{aligned}
&\langle X\rangle=0,\ \text{leading order in }\epsilon_2,\epsilon_3\ (\text{every }N\ge2):\quad a_{k,+}(0)\ \text{level-independent}\iff\gamma_1=0\iff a_{k,-}(0)\ \text{level-independent}\iff\text{both, with the one value }-\tau^2g;\\
&\langle X\rangle=0,\ \text{with the first corrections, under (10.28)},\ N\ge3:\quad \text{each of the three}\iff\gamma_1=0\ \text{and}\ \beta=0;\\
&\langle X\rangle=0,\ \text{with the first corrections, under (10.28)},\ N=2:\quad \text{upper}\iff\gamma_1+\beta(M_0+M_1)=0,\quad \text{lower}\iff\gamma_1-\beta(M_0+M_1)=0,\quad \text{both (then one value)}\iff\gamma_1=\beta=0 .
\end{aligned}
\qquad\text{(10.14)}
```

(For $`N\ge3`$ a polynomial $`\sigma\gamma_1M+\beta M^2`$ with equal values at three points is constant.) The first line is an equivalence for the exact leading-order expression. The second and third lines are equivalences for the expression (10.13), that is for the terms kept; they decide the level dependence of (10.32) up to the terms dropped there, which vanish with $`\gamma_1`$ and $`\gamma^{(3)}_1`$ up to $`\tau^2\lvert g\rvert\,O(\epsilon_1^4+(\gamma^{(3)}_0M_k^2)^2)`$. Sufficient for $`\gamma_1=0`$: $`\varepsilon_0=0`$ or $`\varepsilon_Y=0`$; it also holds when $`\mathrm{Re}\langle\tilde N_0S\tilde Y\rangle`$ vanishes otherwise. *Order,* for $`\langle X\rangle=0`$: at first order in $`\epsilon_1`$ the fall from rest is level-independent in both branches, with the value $`-\tau^2g`$ ((10.1) and (4.22) with $`\mathcal F=m(g_m-g_\eta)=0`$). The independence is lost at second order in $`\epsilon_1`$, already at the leading order of the coefficient in $`\epsilon_2`$, by the branch-odd term $`\sigma\tau^2\gamma_1M_k`$, bilinear in $`\varepsilon_0`$ and $`\varepsilon_Y`$; if $`\gamma_1=0`$, it is lost at second order in $`\epsilon_1`$ and first order in $`\epsilon_2`$, $`\epsilon_3`$ by $`\tau^2\beta M_k^2`$ unless $`\beta=0`$.

*Records, every $`\langle X\rangle`$.* Through the order kept $`H_{\rm eff}-\hat C`$ acts as the identity on $`c`$, so the effective body contract of the description with $`H_{\rm eff}`$ is the body part of $`H_{\rm eff}`$ plus $`\kappa\langle X\rangle\hat x`$. Then (4.16) with $`\mathcal F_k-\kappa\langle X\rangle`$ gives

```math
a_{k,\sigma}(0)=\tau^2\Bigl[-g+\sigma\,\gamma_1M_k+\beta\,M_k^2\Bigr]+a^{\rm rec}_{k,\sigma},\qquad a^{\rm rec}_{k,\sigma}:=-\sigma\,\frac{\tau_k^2}{\hat M_k}\,\kappa\langle X\rangle=-\sigma\,\tau^2\,\kappa\langle X\rangle\Bigl[\frac1{M_k}-\bigl(4\rho_0+\gamma^{(3)}_0\bigr)M_k\Bigr]\qquad(\text{terms in }\beta,\ \rho_0,\ \gamma^{(3)}_0\text{: under (10.28)}).
\qquad\text{(10.22)}
```

*Class, regime, status:* as (10.13), for every $`\langle X\rangle`$; closed form. The expansion of $`\tau_k^2/\hat M_k`$ is that of (10.32), controlled by $`\epsilon_1^2`$ and the first margin of (10.28); $`\kappa\langle X\rangle/M_k`$ is not expanded, and at leading order in $`\epsilon_2`$, $`\epsilon_3`$ the record term $`-\sigma\tau^2\kappa\langle X\rangle/M_k`$ is exact. The record term is of zeroth order in $`\epsilon_1`$ (it is there for a sharp field), odd in the branch, and different for every two levels when $`\langle X\rangle\neq0`$ (the $`1/M_k`$ are pairwise different). *Size:* against $`-\tau^2g`$ it is $`\kappa\lvert\langle X\rangle\rvert/(\lvert g\rvert M_k)`$; against $`\sigma\tau^2\gamma_1M_k`$ it is $`\kappa\lvert\langle X\rangle\rvert/(\lvert\gamma_1\rvert M_k^2)`$, where $`\lvert\gamma_1\rvert M_k^2\le2\varepsilon_0\varepsilon_YM_k^2/\Delta_f`$ is of second order in $`\epsilon_1`$. With $`\gamma_1':=\gamma_1+\kappa\langle X\rangle\,(4\rho_0+\gamma^{(3)}_0)`$, $`a_{k,\sigma}(0)=a`$ for all $`k`$ if and only if the cubic polynomial $`\beta M^3+\sigma\gamma_1'M^2-(g+a/\tau^2)M-\sigma\kappa\langle X\rangle`$ vanishes at all $`M_k`$. Its constant term is the record term, so that for $`\langle X\rangle\neq0`$:

```math
\begin{aligned}
&\text{leading order in }\epsilon_2,\epsilon_3,\ N\ge3:\quad a_{k,\sigma}(0)\ \text{level-dependent in each branch};\\
&\text{leading order in }\epsilon_2,\epsilon_3,\ N=2:\quad \text{upper}\iff\gamma_1M_0M_1=-\kappa\langle X\rangle\iff\text{lower},\quad\text{with the two values }\tau^2\bigl[-g+\sigma\gamma_1(M_0+M_1)\bigr];\\
&\text{with the first corrections, under (10.28)}:\quad N\ge4:\ \text{level-dependent in each branch};\qquad N=3:\ \text{branch }\sigma\iff\sigma\kappa\langle X\rangle=\beta M_0M_1M_2\ \text{and}\ \sigma\gamma_1'=-\beta(M_0+M_1+M_2);\\
&\phantom{\text{with the first corrections, under (10.28)}:\quad}N=2:\ \text{branch }\sigma\iff\gamma_1'+\frac{\kappa\langle X\rangle}{M_0M_1}+\sigma\beta(M_0+M_1)=0;\\
&\text{every }N\ge2:\quad\text{both branches with one value}\ \Longrightarrow\ \langle X\rangle=0\ \ (\text{then (10.14)}).
\end{aligned}
\qquad\text{(10.23)}
```

(A polynomial of degree three, at leading order two, with more zeros than its degree vanishes identically, which needs $`\langle X\rangle=0`$; for both branches with one value, the sum and the difference of the two polynomials give $`\beta M_k^2=g+a/\tau^2`$ and $`\gamma_1'M_k^2=\kappa\langle X\rangle`$ for all $`k`$.) The lines at leading order are equivalences for the exact leading-order expression; the lines with the first corrections are equivalences for the expression (10.22), with the range stated after (10.14). So for $`\langle X\rangle\neq0`$ the statement "level-independent at first order in $`\epsilon_1`$" fails: already for $`\varepsilon=0`$, $`a_{k,\sigma}(0)=-\tau^2g-\sigma\tau^2\kappa\langle X\rangle/M_k`$ depends on the level for every $`N\ge2`$, as (4.22) requires ($`\mathcal F=-\kappa\langle X\rangle\neq m(g_m-g_\eta)=0`$). The equivalences (10.14) are replaced by (10.23), whose cases with independence are exceptional members in which the record term cancels against terms of second order in $`\epsilon_1`$. The condition $`\langle X\rangle=0`$ is read in the form of $`\mathcal D`$, in which the body has no plain term of its own; under (8.1) of 04-ilang-time/08-maximal-speed only the plain gradient of the effective body contract, here $`-\kappa\langle X\rangle`$, is well defined ((8.20) there).

*Velocity from the phase.* Take the level $`k`$ with all gradients set to zero and the uniform phase $`\theta_k`$ kept, on the infinite chain (the limit of a long chain at fixed $`\lambda`$ and start, as in 04-branch-fall). The computation of (5.5) of 04-ilang-time/05-moving-clock with the hopping factor $`e^{i\theta_k}`$ gives the level block $`-\tau_k\sin(p-\theta_k)\,\sigma_1+\hat M_k\sigma_3`$, with the eigenvalues $`\pm\omega_k(p-\theta_k)`$ and the eigenvectors $`\beta_{k,\pm}(p-\theta_k)`$. The position label acts on the plane-wave weights as $`i\,\partial_p`$, so $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda`$ is the mean of $`i[C^{(k)},\hat x]=-\tau_k\cos(p-\theta_k)\,\sigma_1`$: the rate itself is computed. The part of this operator that is diagonal in the eigenvectors is $`\pm\omega_k'(p-\theta_k)`$. The branch start $`B_{k,\sigma}[g]`$ is built with $`\beta_{k,\sigma}(p)`$, which contains the other eigenvector with an amplitude of first order in $`\theta_k`$, so the off-diagonal part contributes at first order as well, with the frequency $`2\omega_k`$. Evaluating the mean of the $`2\times2`$ block to first order in $`\theta_k`$ (where $`\tau_k\to\tau`$, $`\hat M_k\to M_k`$):

```math
\frac{\mathrm d\bar x_{\rm lab}}{\mathrm d\lambda}=\sigma\langle\omega_k'\rangle_g+v^{\rm ph}_{k,\sigma}(\lambda),\qquad v^{\rm ph}_{k,\sigma}(\lambda)=-\sigma\,\theta_k\Bigl\langle\omega_k''-\frac{\tau^2M_k^2\cos^2p}{\omega_k^3}\cos(2\omega_k\lambda)\Bigr\rangle_g,\qquad \theta_k=M_k^2\mathrm{Im}\rho_Y,\quad\lvert\rho_Y\rvert\le\frac{\varepsilon_0\varepsilon_Y}{\Delta_f^2},
\qquad\text{(10.24)}
```

with $`\omega_k''=\tau^2(M_k^2\cos2p-\tau^2\sin^4p)/\omega_k^3`$. With the gradients, the terms of (4.7) are added; the cross terms are of second order in the gradients. $`v^{\rm ph}_{k,\sigma}`$ is bounded for all $`\lambda\ge0`$, so it does not change the coefficient of $`\lambda`$: the drift accelerations (10.13), (10.22) are unchanged at first order in $`Y`$. For a start at rest the first term of (10.24) vanishes in the limit of a sharp label, and

```math
\boxed{\;\begin{aligned}
&\text{sharp label at fixed }\lambda:\quad v^{\rm ph}_{k,\sigma}(\lambda)=-\sigma\,\tau^2M_k\mathrm{Im}\rho_Y\,\bigl[1-\cos(2M_k\lambda)\bigr];\\
&\text{long window, before or after the sharp label}:\quad \bar v^{\rm ph}_{k,\sigma}=-\sigma\,\tau^2M_k\mathrm{Im}\rho_Y,\qquad \lvert\bar v^{\rm ph}_{k,\sigma}\rvert\le\tau^2M_k\,\frac{\varepsilon_0\varepsilon_Y}{\Delta_f^2}.
\end{aligned}\;}
\qquad\text{(10.25)}
```

*Order of the limits.* The growth of $`\lambda`$ and the limit of a sharp label do not commute for the velocity itself. With the sharp label first, the velocity is zero at $`\lambda=0`$, oscillates between $`0`$ and $`2\bar v^{\rm ph}_{k,\sigma}`$ and has no limit. With $`\lambda\to\infty`$ first, at a fixed smooth $`g`$, the oscillating term of (10.24) decays (stationary phase; $`\omega_k`$ is not constant because $`\tau>0`$), the limit is $`-\sigma\theta_k\langle\omega_k''\rangle_g`$, and the sharp label then gives $`\bar v^{\rm ph}_{k,\sigma}`$. The average over a window of length $`\Lambda`$ removes the oscillating term up to $`\tau^2\lvert\theta_k\rvert/(M_k^2\Lambda)`$ uniformly in $`g`$, so it commutes with the limit of a sharp label. (A start built with the eigenvectors $`\beta_{k,\sigma}(p-\theta_k)`$ of the block with the phase has the velocity $`\sigma\langle\omega_k'(p-\theta_k)\rangle_g`$ at every $`\lambda`$, at the label $`p_0=0`$ equal to $`\sigma\omega_k'(-\theta_k)`$, which is $`\bar v^{\rm ph}_{k,\sigma}`$ at the order kept.)

*Class, regime, status:* linear profiles of the field, branch starts at rest, every $`\langle X\rangle`$; R1, second order in $`\epsilon_1`$ (bilinear in $`\varepsilon_0`$, $`\varepsilon_Y`$) and first order in $`\epsilon_2`$ (the term comes from $`H^{(2,1)}`$; there is no term in $`\epsilon_3`$ at this order), first order in $`Y`$ (in $`\tilde Y`$; it does not contain $`g`$); under (10.28), whose first margin makes the rest term $`\hat M_k`$ of the level block positive and equal to $`M_k`$ at the order kept; exact coefficient at these orders, in the description with $`H_{\rm eff}`$, as stated after (10.13). It is a velocity and not a drift acceleration. It is odd in the branch and proportional to $`M_k`$, hence different for every two levels, and it vanishes if and only if $`\mathrm{Im}\rho_Y=0`$. Sufficient for that: $`\varepsilon_0=0`$, or $`\varepsilon_Y=0`$, or real matrices of $`C_f`$, $`N_0`$, $`Y`$ in one basis. It does not need $`\gamma_1\neq0`$: a field with two places, $`C_f=\tfrac12\Delta(\lvert1\rangle\langle1\rvert-\lvert0\rangle\langle0\rvert)`$, $`\varphi_0=\lvert0\rangle`$, $`N_0=\mathbb 1+\varepsilon_0(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert)`$, $`Y=g\,\mathbb 1+i\varepsilon_Y(\lvert1\rangle\langle0\rvert-\lvert0\rangle\langle1\rvert)`$, has $`\gamma_1=0`$ and $`\rho_Y=i\varepsilon_0\varepsilon_Y/\Delta^2`$. The level block of the level $`k`$ has zero group velocity at the label $`p=\theta_k`$, which depends on the level: a start with one position factor for two levels $`k\neq k'`$ is not at rest in both, and their window-averaged velocities differ by $`-\sigma\tau^2\mathrm{Im}\rho_Y\,(M_k-M_{k'})`$.

**(c)** With $`E^+_{x,k}=e_0+N(x)M_k-\gamma_xM_k^2+\gamma^{(3)}_xM_k^3`$:

```math
E^+_{x,k+1}-E^+_{x,k}=\frac{2\pi}{N\lambda_0}\Bigl[N(x)-\gamma_x\,(M_k+M_{k+1})+\gamma^{(3)}_x\bigl(M_k^2+M_kM_{k+1}+M_{k+1}^2\bigr)\Bigr]\qquad\bigl(\text{upper on-site eigenvalues with the cubic term: under (P) of (10.27) at }x\bigr).
\qquad\text{(10.15)}
```

*Orders and class.* (10.15) follows from (10.11) alone, so it holds for every member of $`\mathcal D`$ and every $`x`$, in R1: at second order in $`\epsilon_1`$, the term in $`\gamma_x`$ is the leading order in $`\epsilon_2`$, $`\epsilon_3`$ and the cubic term is the first correction in $`\epsilon_3`$; there is no term of first order in $`\epsilon_2`$, because $`H^{(2,1)}`$ has no on-site part. $`E^+_{x,k}:=V_{x,k}+M_{x,k}`$ is the on-site eigenvalue of the branch place $`s=1`$. It is the upper one at leading order for every member, and with the cubic term if and only if $`\mu_{x,k}>0`$ (Step 2(b)); for the linear profiles this is part of (10.28). (10.15) is a polynomial identity: nothing is expanded and no term is treated as small. Its bracket is not positive in every member: R1 does not bound $`\gamma_x(M_k+M_{k+1})`$ against $`N(x)`$ ("Not small in R1"), so a difference of neighbouring levels can vanish or be negative; (10.15) and (10.29) hold whatever the signs. Since $`E^+_{x,k}`$ is a cubic polynomial in $`M_k`$ and the $`M_k`$ are equally spaced:

```math
\begin{aligned}
&E^+_{x,k+2}-2E^+_{x,k+1}+E^+_{x,k}=2\Bigl(\frac{2\pi}{N\lambda_0}\Bigr)^2\bigl[-\gamma_x+3\,\gamma^{(3)}_xM_{k+1}\bigr]\qquad(0\le k\le N-3);\\
&\text{leading order in }\epsilon_2,\epsilon_3:\quad\text{differences (10.15) independent of }k\iff N=2\ \ \text{or}\ \ \gamma_x=0;\\
&\text{with the first corrections}:\quad\text{independent of }k\iff N=2,\ \ \text{or}\ \ N=3\ \text{and}\ \gamma_x=3\,\gamma^{(3)}_xM_1,\ \ \text{or}\ \ N\ge4\ \text{and}\ \gamma_x=\gamma^{(3)}_x=0 .
\end{aligned}
\qquad\text{(10.29)}
```

($`N=2`$ has one difference. $`N=3`$ has two, equal if and only if the one second difference vanishes. For $`N\ge4`$ the bracket must vanish at two different $`M_{k+1}`$.) So at leading order, for $`N\ge3`$ and $`\gamma_x\neq0`$: **no**; the second difference is $`-2\gamma_x(2\pi/N\lambda_0)^2`$. *Exceptional members.* A member with $`\gamma_x=0`$ and $`\gamma^{(3)}_x\neq0`$ (possible for an inner $`e_0`$, see after (10.9)) has equal differences at leading order and unequal ones with the first corrections, for every $`N\ge3`$ (the second difference is $`6\gamma^{(3)}_xM_{k+1}(2\pi/N\lambda_0)^2\neq0`$). For $`N=3`$, a member with $`\gamma_x=3\gamma^{(3)}_xM_1\neq0`$ has unequal differences at leading order and equal ones with the first corrections: the two orders cancel.

*Clock at leading order in $`\epsilon_2`$, $`\epsilon_3`$.* Clock of $`S_{\rm clock}(x_0)`$, at the orders of (3.36) (zeroth order in the gradients): the body part is then $`\hat C_b-\gamma_{x_0}\mathcal M^2`$, the two terms commute, and $`\mathcal M^2=m^2+\Sigma\,D-D(d_{N-1}-D)`$ with $`\Sigma:=M_0+M_{N-1}`$. The factor $`e^{i\gamma_{x_0}\Sigma D\lambda}`$ shifts every advance of the mixture (3.36) (taken with $`\eta^0=N(x_0)`$, $`m^0=mN(x_0)`$, $`\tau^0=\tau`$) by $`-\gamma_{x_0}\Sigma\lambda/\lambda_0`$, in both branch components alike; the factor $`e^{-i\gamma_{x_0}D(d_{N-1}-D)\lambda}`$ has phases in $`[0,\tfrac14\lvert\gamma_{x_0}\rvert d_{N-1}^2\lambda]`$ and is the identity for $`N=2`$. Hence

```math
\text{leading order in }\epsilon_2,\epsilon_3:\quad\text{clock statistics}=\text{ring-clock mixture (3.36) with rate }\bar r(x_0)\text{ in the wide-start limit, up to total variation }\le\tfrac12\lvert\gamma_{x_0}\rvert\,d_{N-1}^2\,\lambda;\qquad \text{accuracy }\eta\ \text{for}\ \lambda\le\frac{2\eta}{\lvert\gamma_{x_0}\rvert\,d_{N-1}^2}\ (N\ge3,\ \gamma_{x_0}\neq0),\ \ \text{no deviation at this order}\ (N=2\text{ or }\gamma_{x_0}=0).
\qquad\text{(10.16)}
```

*Status:* order estimate; $`\lvert\gamma_{x_0}\rvert d_{N-1}^2\le\epsilon_1^2\Delta_f\,(d_{N-1}/M_{\max})^2`$. The level dependence of $`\tau_k`$ changes $`\varsigma_W`$ of (3.23) only at relative order $`\epsilon_1^2`$. (10.16) is a statement about the description with $`\hat C+H^{(2)}`$, for every member of the class of this step, with $`\bar r(x_0)=\lambda_0^{-1}[N(x_0)-\gamma_{x_0}\Sigma]`$. "No deviation at this order" is not a statement for all $`\lambda`$ about the description with $`C`$ or with $`H_{\rm eff}`$: for $`N=2`$ or $`\gamma_{x_0}=0`$ the range is set by the next order, (10.30), and by the range of (10.10).

*Sign and vanishing of the mean rate.* The shift $`-\gamma_{x_0}\Sigma/\lambda_0`$ of the rate is not small against $`N(x_0)/\lambda_0`$ in R1, so $`\bar r(x_0)`$ can be positive, zero or negative. What "a ring clock with one rate" means in each case:

```math
\begin{aligned}
&\text{ring clock with the one rate }r\in\mathbb R:\quad\text{clock label in }N^{-1/2}\sum_{k}e^{-\frac{2\pi i}{N}\,r\,k\,\lambda}\lvert f_k\rangle\ \text{up to a common phase (the place }\lvert0\rangle\text{ advanced by }r\lambda\text{ places along the ring)};\\
&\lambda_0\,\bar r(x_0)=N(x_0)-\gamma_{x_0}\Sigma\ \ (\text{leading order in }\epsilon_2,\epsilon_3),\qquad\lvert\gamma_{x_0}\rvert\,\Sigma\le2\,\epsilon_1\varepsilon;\qquad\text{ticks within the range of (10.16)}:\ \ \lvert\bar r(x_0)\rvert\,\lambda\le\frac{2\eta\,\lvert N(x_0)-\gamma_{x_0}\Sigma\rvert}{\lambda_0\,\lvert\gamma_{x_0}\rvert\,d_{N-1}^2}.
\end{aligned}
\qquad\text{(10.33)}
```

For $`r>0`$ the label advances in the sense of the clock of Model D (for which $`r=1/\lambda_0`$), with the tick $`1/r`$. For $`r<0`$ it advances in the opposite sense, with the tick $`1/\lvert r\rvert`$. For $`r=0`$ the label stays in its start place: the statistics does not depend on $`\lambda`$, there is no tick, and a ratio of rates with this clock as the reference is not defined. R1 fixes none of the three cases. Sufficient for $`\bar r(x_0)>0`$: $`\gamma_{x_0}\le0`$, or $`2\epsilon_1\varepsilon<N_{\min}`$. $`\bar r(x_0)=0`$ needs $`\gamma_{x_0}\Sigma=N(x_0)`$; the member of (10.36) is a control. (10.16) and (10.30) hold in all three cases: their derivations factorise the evolution and bound a phase; they do not divide by $`\bar r`$ and do not use that $`\gamma_{x_0}\Sigma`$ is small against $`N(x_0)`$. What depends on the case is the sense of the advance and the number of ticks within the range, bounded in (10.33): where this number is below one, in particular for $`\bar r(x_0)=0`$, the statistics is that of a ring clock with one rate to the accuracy $`\eta`$, but this clock does not complete a tick on that range. At finite $`W`$ the mean advance of the mixture is $`\bigl[N(x_0)(1-\varsigma_W)-\gamma_{x_0}\Sigma\bigr]\lambda/\lambda_0`$ by (3.36), which vanishes at a different value of $`\gamma_{x_0}\Sigma`$. With the first corrections the same holds with $`\bar r`$ of (10.30).

*Clock with the first corrections (order estimate, wide start).* Take the wide-start limit at fixed $`\lambda`$ and zeroth order in the gradients. The plane-wave weight of $`S_{\rm clock}(x_0)`$ concentrates at $`p=0`$, where the level block of the level $`k`$ is its on-site block; the bare branch place $`s=1`$ is an eigenvector of it with the eigenvalue $`E^+_{x_0,k}`$, so the clock label is in the state $`N^{-1/2}\sum_ke^{-iE^+_{x_0,k}\lambda}\lvert f_k\rangle`$. Write $`E^+_{x_0,k}=E^+_{x_0,0}+\tfrac{2\pi}{N}\,\bar r(x_0)\,k+\delta E_k`$: the first two terms are those of a ring clock with the one rate $`\bar r(x_0)`$, and $`\delta E_0=\delta E_{N-1}=0`$. From the cubic polynomial of (10.15), with $`M_k-M_0=d_k`$:

```math
\begin{aligned}
&\bar r(x)=\frac1{\lambda_0}\Bigl[N(x)-\gamma_x\,\Sigma+\gamma^{(3)}_x\bigl(M_0^2+M_0M_{N-1}+M_{N-1}^2\bigr)\Bigr],\qquad
\delta E_k=d_k\,(d_{N-1}-d_k)\,\bigl[\gamma_{x_0}-\gamma^{(3)}_{x_0}\,(M_k+\Sigma)\bigr],\\
&\Xi_{x_0}:=\max_{0<k<N-1}\bigl\lvert\gamma_{x_0}-\gamma^{(3)}_{x_0}\,(M_k+\Sigma)\bigr\rvert\le\lvert\gamma_{x_0}\rvert+3\,\lvert\gamma^{(3)}_{x_0}\rvert\,M_{\max}\ \ (N\ge3),\qquad
\text{total variation}\le\tfrac12\,\Xi_{x_0}\,d_{N-1}^2\,\lambda,\qquad\text{accuracy }\eta\ \text{for}\ \lambda\le\frac{2\eta}{\Xi_{x_0}\,d_{N-1}^2}\ \ (N\ge3,\ \Xi_{x_0}\neq0).
\end{aligned}
\qquad\text{(10.30)}
```

(The clock state differs from that of the ring clock by at most $`\max_k\lvert\delta E_k\rvert\lambda\le\tfrac14\Xi_{x_0}d_{N-1}^2\lambda`$ in norm.) *Class, regime, status:* linear profiles of the field, starts $`S_{\rm clock}(x_0)`$, under (10.28) (then $`E^+_{x_0,k}`$ is the upper on-site eigenvalue; the computation uses only that $`s=1`$ is an on-site eigenvector); R1, second order in $`\epsilon_1`$ with the first correction in $`\epsilon_3`$, zeroth order in the gradients, wide-start limit at fixed $`\lambda`$; order estimate, in the description with $`\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}`$, on its range (10.10). At finite $`W`$ the corrections of (3.23) and (3.36) apply and are not extended here to the first corrections. *What the cubic term adds:* at most $`\tfrac32\lvert\gamma^{(3)}_{x_0}\rvert M_{\max}d_{N-1}^2\lambda\le\tfrac32\epsilon_1^2\epsilon_3\Delta_f(d_{N-1}/M_{\max})^2\lambda`$ to the total variation, of relative order $`\epsilon_3`$ against the bound of the quadratic term. *No restriction from the spacings:* if and only if $`N=2`$ or $`\Xi_{x_0}=0`$, and $`\Xi_{x_0}=0`$ exactly in the cases of (10.29) with the first corrections at $`x_0`$ ($`N=3`$ and $`\gamma_{x_0}=3\gamma^{(3)}_{x_0}M_1`$, or $`N\ge4`$ and $`\gamma_{x_0}=\gamma^{(3)}_{x_0}=0`$). The range is then that of (10.10), not all $`\lambda`$. For a member with $`\gamma_{x_0}=0\neq\gamma^{(3)}_{x_0}`$ and $`N\ge3`$ the range is $`\lambda\le2\eta/(\Xi_{x_0}d_{N-1}^2)`$ with $`\Xi_{x_0}=\lvert\gamma^{(3)}_{x_0}\rvert\max_{0<k<N-1}(M_k+\Sigma)`$.

**(d)** From (10.15), at leading order in $`\epsilon_2`$, $`\epsilon_3`$, $`\bar r(x)=\lambda_0^{-1}\bigl[N(x)-\gamma_x\Sigma\bigr]`$, which at first order in $`Y`$ is $`\bar r(x)=\lambda_0^{-1}\bigl[D_0+(g-\gamma_1\Sigma)\,x\bigr]`$ with $`D_0:=1-\gamma_0\Sigma=\lambda_0\,\bar r(0)`$. (At this order the body part is a member of $`\mathcal C_{\rm lev}`$ and $`E^+_{x,k}`$ is the upper on-site eigenvalue for every member of the class; (10.28) is not needed.) With $`v_{\max}^2/d_0^2=\tau^2`$, (4.24) for the body part of $`H_{\rm eff}`$ would read $`a_{k,+}(0)=-\tau^2\,(\bar r(x+1)-\bar r(x))/\bar r(x)`$. It divides by the comparison rate $`\bar r(0)`$. The quotient is not expanded, because R1 does not make $`\gamma_0\Sigma`$ small. For $`D_0\neq0`$, with $`a_{k,+}(0)=\tau^2[-g+\gamma_1M_k-\kappa\langle X\rangle/M_k]`$, which is exact at this order ((10.32), (10.22)):

```math
\boxed{\;D_0\neq0:\qquad\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\Big\vert_{x=0}=\frac{g-\gamma_1\Sigma}{D_0},\qquad
\mathcal R_k:=a_{k,+}(0)+\tau^2\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\Big\vert_{x=0}=\tau^2\Bigl[\gamma_1\Bigl(M_k-\frac{\Sigma}{D_0}\Bigr)+\frac{g\,\gamma_0\,\Sigma}{D_0}-\frac{\kappa\langle X\rangle}{M_k}\Bigr],\qquad D_0=1-\gamma_0\Sigma\;}
\qquad\text{(10.34)}
```

*Class, regime, status:* linear profiles of the field, every $`\langle X\rangle`$, branch starts at rest; R1, leading order in $`\epsilon_2`$, $`\epsilon_3`$, first order in $`Y`$; closed form, exact in $`\gamma_0\Sigma`$ (the numerator $`g-\gamma_1\Sigma`$ is of first order in $`Y`$, the denominator of zeroth order). Its remainder consists of the first corrections in $`\epsilon_2`$, $`\epsilon_3`$ and of the terms of fourth order of $`H_{\rm eff}`$, of relative order $`\epsilon_1^2`$ against the terms in $`\gamma_0`$, $`\gamma_1`$. The conditions:

```math
\begin{aligned}
&\text{comparison defined}\iff\bar r(0)\neq0\iff D_0\neq0\ \ (\gamma_0\Sigma\neq1);\qquad\text{margin against the terms not kept:}\quad\lvert D_0\rvert\gg\varepsilon\,\epsilon_1\,\bigl(\epsilon_3+\epsilon_1^2+\epsilon_2^2\bigr);\\
&\mathrm{(H)}:\quad\lvert\gamma_0\rvert\,\Sigma\ll1;\qquad\text{sufficient for (H) and for the margin}:\quad2\,\epsilon_1\varepsilon=\frac{2\,\epsilon_1^2\,\Delta_f}{M_{\max}}\ll1 .
\end{aligned}
\qquad\text{(10.35)}
```

The margin is an order estimate: the terms not kept change $`\lambda_0\bar r(0)`$ by the cubic term of (10.30), at most $`3\lvert\gamma^{(3)}_0\rvert M_{\max}^2\le3\varepsilon\epsilon_1\epsilon_3`$ by (10.27), and by the on-site part of the remainder of (10.10); there is no first correction in $`\epsilon_2`$. (H) is the hierarchy of the clock-spacing correction against the spacing itself; neither R1 nor (10.28) implies it, since $`\lvert\gamma_0\rvert\Sigma\le2\varepsilon_0^2M_{\max}/\Delta_f\le2\epsilon_1\varepsilon`$ and $`\varepsilon`$ is not small in R1. Under (H) the reciprocal is expanded, $`1/D_0=1+\gamma_0\Sigma+\dots`$, and (10.34) gives, for $`\langle X\rangle=0`$,

```math
\boxed{\;\mathcal R_k:=a_{k,+}(0)+\tau^2\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\Big\vert_{x=0}=\tau^2\Bigl[\gamma_1\,(M_k-\Sigma)+g\,\gamma_0\,\Sigma\Bigr]\ \ (\langle X\rangle=0;\ \text{under (H) of (10.35)}),\qquad \Sigma=M_0+M_{N-1}=2m+d_{N-1}\;}
\qquad\text{(10.17)}
```

up to $`\tau^2\bigl(\lvert\gamma_1\rvert+\lvert g\,\gamma_0\rvert\bigr)\Sigma\cdot O(\lvert\gamma_0\rvert\Sigma)`$, the first corrections in $`\epsilon_2`$, $`\epsilon_3`$ and $`O(\varepsilon^4)`$. Without (H), (10.17) is not derived and (10.34) is used; for $`D_0=0`$ neither applies.

**No**: for $`\langle X\rangle=0`$ and every member with $`D_0\neq0`$ (with the margin of (10.35)), (4.24) holds for all levels if and only if $`\gamma_1=0`$ and $`g\gamma_0=0`$. This follows from (10.34) without (H): the $`M_k`$ are pairwise different, so $`\gamma_1=0`$, and then $`g\gamma_0\Sigma/D_0=0`$ with $`\Sigma>0`$. Under the hypothesis of (4.24) (a level-independent $`a\neq0`$, which for $`\langle X\rangle=0`$ needs $`\gamma_1=0`$ and $`g\neq0`$) it holds iff $`\gamma_0=0`$; otherwise $`a=-\tau^2\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}\,(1-\gamma_0\Sigma)`$, exact in $`\gamma_0\Sigma`$ for $`D_0\neq0`$, and the leading deviation is $`d_0\mathcal R_k\hat e=d_0\tau^2g\gamma_0\Sigma\,D_0^{-1}\,\hat e`$, which is $`d_0\tau^2g\gamma_0\Sigma\,\hat e`$ under (H); it contains the data $`m`$, $`d_{N-1}`$ of the body. At first order in $`\epsilon_1`$ and for $`\langle X\rangle=0`$, (4.24) holds with $`r(x)=N(x)/\lambda_0`$.

*Members with a vanishing mean rate ($`D_0=0`$).* They exist in R1 with the margins of (10.28). Control: two levels with $`M_0=1`$, $`M_1=2`$, $`\lambda_0=\pi`$, and a field with two places, $`C_f=\Delta\lvert1\rangle\langle1\rvert`$, $`\varphi_0=\lvert0\rangle`$, $`\Phi_x=(1+gx)\mathbb 1+\sqrt{\Delta/3}\,(\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert)`$. Then $`\epsilon_1=2/\sqrt{3\Delta}`$, $`\epsilon_3=0`$, $`\gamma_0=\tfrac13`$, $`\gamma_1=\gamma^{(3)}_x=0`$, $`\Sigma=3`$, so for large $`\Delta`$ R1 and (10.28) hold while $`\varepsilon=\sqrt{\Delta/3}`$ is large, $`D_0=0`$ and $`\bar r(x)=g\,x/\lambda_0`$. For such a member the relative gradient of the mean rate at $`x=0`$ is not defined, the quotient form of (4.24) at $`x=0`$ has no meaning, and (10.17) is not a statement about it. What is defined is the form of (4.24) multiplied by the comparison rate:

```math
\bar r(0)\,a_{k,+}(0)+\tau^2\bigl[\bar r(1)-\bar r(0)\bigr]=\frac{\tau^2}{\lambda_0}\Bigl[D_0\Bigl(-g+\gamma_1M_k-\frac{\kappa\langle X\rangle}{M_k}\Bigr)+g-\gamma_1\Sigma\Bigr]\ \ \overset{D_0=0}{=}\ \ \tau^2\,\bar r(1)=\frac{\tau^2}{\lambda_0}\,(g-\gamma_1\Sigma)\qquad(\text{every }k,\ \text{every }\langle X\rangle).
\qquad\text{(10.36)}
```

For $`D_0=0`$ this form holds if and only if $`g=\gamma_1\Sigma`$, and then $`\bar r(x)=0`$ at every position at this order (no clock of the chain advances; both sides are zero). Otherwise it fails for every level, while the fall $`a_{k,+}(0)=\tau^2[-g+\gamma_1M_k-\kappa\langle X\rangle/M_k]`$ is finite; in the control the fall is $`-\tau^2g`$ in both levels, level-independent and not zero, and the mean rate has opposite signs on the two sides of $`x=0`$. The value $`D_0=0`$ is meant at the order kept: within the margin of (10.35) the terms not kept decide the sign of $`\bar r(0)`$, and neither (10.34) nor (10.36) is derived there.

*Negative mean rate ($`D_0<0`$, that is $`\gamma_0\Sigma>1`$, with the margin).* (10.34) and the equivalences derived from it hold unchanged; (10.17) does not. The ratio $`\bar r(1)/\bar r(0)`$ is defined, and the relative gradient of $`\lvert\bar r\rvert`$ equals that of $`\bar r`$ as long as $`\bar r(0)`$ and $`\bar r(1)`$ have the same sign. For $`\gamma_1=0`$, $`\langle X\rangle=0`$, $`g\neq0`$: $`a_{k,+}(0)=-\tau^2D_0\,\frac{\bar r(x+1)-\bar r(x)}{\bar r(x)}`$ with $`D_0<0`$, so the acceleration has the sign opposite to the one (4.24) states, and $`\lvert\mathcal R_k\rvert=\lvert a_{k,+}(0)\rvert\,\gamma_0\Sigma/\lvert D_0\rvert>\lvert a_{k,+}(0)\rvert`$: the defect is larger than the acceleration.

For every $`\langle X\rangle`$: the plain term $`\kappa\langle X\rangle x`$ is the same in all levels and drops out of (10.15), so $`\bar r`$ is unchanged, and the record term $`a^{\rm rec}_{k,+}`$ of (10.22) is added to the defect, as in (10.34). At leading order in $`\epsilon_2`$, $`\epsilon_3`$:

```math
\mathcal R_k=\tau^2\Bigl[\gamma_1\,(M_k-\Sigma)+g\,\gamma_0\,\Sigma-\frac{\kappa\langle X\rangle}{M_k}\Bigr]\qquad(\text{every }\langle X\rangle;\ \text{under (H) of (10.35)}).
\qquad\text{(10.26)}
```

*Class, regime, status:* as (10.17); closed form of the leading defect under (H), with the remainder stated after (10.17); the record term is not expanded. For $`\langle X\rangle\neq0`$, (4.24) fails already at zeroth order in $`\epsilon_1`$ (for a sharp field), with the level-dependent defect $`-\tau^2\kappa\langle X\rangle/M_k`$. For every member with $`D_0\neq0`$ (with the margin), by (10.34): (4.24) holds for all levels if and only if $`\gamma_1=0`$, $`g\gamma_0=0`$ and $`\langle X\rangle=0`$ for $`N\ge3`$ ($`M_k\mathcal R_k`$ is a quadratic polynomial in $`M_k`$ with three zeros), and if and only if $`\gamma_0\,(g-\gamma_1\Sigma)=0`$ and $`\gamma_1M_0M_1=-\kappa\langle X\rangle`$ for $`N=2`$ (the exceptional members of (10.23); here $`\Sigma=M_0+M_1`$). The first condition for $`N=2`$ is exact in $`\gamma_0\Sigma`$; in the expanded form (10.26), that is under (H) and through second order in $`\varepsilon`$, it reads $`g\gamma_0=0`$.

### Step 4. Example and control: independent cells (item 4)

*Class:* (a), (b): the cells, every $`\Delta_x>0`$, $`n_x>0`$, $`\varepsilon_x\ge0`$. (c): the subclass $`\mathcal L`$ of (10.31), which is the class of item 4(c) of the question; for the cells outside it the last paragraph of (c) states which results of (a), (b) hold. *Regime:* R1 for (a), (c); (b) is exact on site.

**(a)** $`\varphi_0=\bigotimes_x\lvert0\rangle`$ has $`e_0=-\tfrac12\sum_x\Delta_x`$, the lowest and simple eigenvalue of $`C_f`$; an excited eigenvector has a set of flipped cells. With $`\sigma^{(x)}_1:=\lvert0\rangle\langle1\rvert+\lvert1\rangle\langle0\rvert`$ on the cell $`x`$, $`\tilde\Phi_x=\varepsilon_x\sigma_1^{(x)}`$ and $`\tilde\Phi_x\varphi_0`$ is the eigenvector with the cell $`x`$ flipped, at $`e_0+\Delta_x`$:

```math
N(x)=n_x,\quad \lVert\tilde\Phi_x\varphi_0\rVert=\varepsilon_x,\quad \varepsilon=\max_x\varepsilon_x,\quad \Delta_f=\min_x\Delta_x,\quad \nu=\varepsilon,\quad
\gamma_x=\frac{\varepsilon_x^2}{\Delta_x},\quad \rho_{xy}=\delta_{xy}\frac{\varepsilon_x^2}{\Delta_x^2},\quad c_x=\frac12\Bigl(\frac{\varepsilon_x^2}{\Delta_x^2}+\frac{\varepsilon_{x+1}^2}{\Delta_{x+1}^2}\Bigr),\quad \gamma^{(3)}_x=0 .
\qquad\text{(10.18)}
```

So $`H^{(2)}=-\sum_x\frac{\varepsilon_x^2}{\Delta_x}P_x\otimes\mathbb 1_2\otimes\mathcal M^2`$, $`H^{(3)}=0`$, the hopping has the real factor $`1-M_k^2c_x`$, and the body part is a member of $`\mathcal C_{\rm lev}`$ with $`M_{x,k}=n_xM_k`$, $`V_{x,k}=e_0-\varepsilon_x^2M_k^2/\Delta_x`$, $`\tau_k\zeta_{x,k}=\tau(1-M_k^2c_x)`$; no term is outside the form. All inequalities of the class hold for every cell description in R1: $`\mu_{x,k}=n_xM_k>0`$, so (P) of (10.27) holds without a condition, and $`1-M_k^2c_x\ge1-\epsilon_1^2>0`$. The margin (P′) is a condition on the cells: $`M_0\min_xn_x\gg\epsilon_1^2[(\epsilon_2+\epsilon_3)^2+\epsilon_1^2]\Delta_f`$. The level profiles are those of $`\mathcal C_{\rm lev}`$ with a general dependence on $`x`$; they are linear only in the subclass of (c).

**(b)** In the basis $`(\lvert0\rangle,\lvert1\rangle)`$, $`C_{f_x}\pm M_k\Phi_x=\pm M_kn_x\mathbb 1-\Omega_{x,k}\bigl(\cos\alpha_{x,k}\,\sigma_3\mp\sin\alpha_{x,k}\,\sigma_1\bigr)`$ with $`\Omega_{x,k}\cos\alpha_{x,k}=\Delta_x/2`$, $`\Omega_{x,k}\sin\alpha_{x,k}=M_k\varepsilon_x`$. Exactly:

```math
\text{eigenvalues }\pm M_kn_x-\Omega_{x,k}\ (\text{lower}),\ \ \pm M_kn_x+\Omega_{x,k}\ (\text{upper}),\quad \Omega_{x,k}=\sqrt{\tfrac14\Delta_x^2+M_k^2\varepsilon_x^2};\qquad \text{lower eigenvector }\cos\tfrac{\alpha_{x,k}}2\lvert0\rangle\mp\sin\tfrac{\alpha_{x,k}}2\lvert1\rangle;\qquad \cos\tfrac{\alpha_{x,k}}2=\Bigl[\tfrac12\Bigl(1+\tfrac{\Delta_x}{2\Omega_{x,k}}\Bigr)\Bigr]^{1/2}.
\qquad\text{(10.19)}
```

*Comparison.* With the other cells in $`\lvert0\rangle`$ the field costs $`e_0+\tfrac12\Delta_x\pm M_kn_x-\Omega_{x,k}=e_0\pm M_kn_x-\frac{\varepsilon_x^2M_k^2}{\Delta_x}+\frac{\varepsilon_x^4M_k^4}{\Delta_x^3}-\dots`$: the part odd in the branch is $`n_xM_k`$ exactly (so $`\gamma_x^{(3)}=0`$), the even part reproduces $`-\gamma_xM_k^2`$ of (10.11), and the remainder has the relative size $`(M_k\varepsilon_x/\Delta_x)^2\le\epsilon_1^2`$. *Overlap:* $`\langle0\vert\text{lower}\rangle=\cos\tfrac{\alpha_{x,k}}2=1-\frac{M_k^2\varepsilon_x^2}{2\Delta_x^2}+O(\epsilon_1^4)`$, the same for both signs. *What it multiplies:* at leading order in $`\tau/\Delta_x`$ the cells follow the body; a hop from $`x`$ to $`x+1`$ returns the cell $`x`$ to $`\lvert0\rangle`$ and takes the cell $`x+1`$ to its lower eigenvector, so the hopping block of the level $`k`$, that is the motion term $`\tau`$, is multiplied by $`\cos\tfrac{\alpha_{x,k}}2\cos\tfrac{\alpha_{x+1,k}}2=1-M_k^2c_x+O(\epsilon_1^4)`$, in agreement with (10.18).

**(c)** The cells are not of the form $`N_0+xY`$ unless $`\varepsilon_x=0`$ for all $`x`$ (the $`\sigma_1^{(x)}`$ of more than two cells are linearly independent), so (10.11) is used directly. The quoted (4.16) is a statement for linear level profiles. By (10.18) the level profiles of the cells with $`n_x=1+gx`$ are linear for all levels if and only if $`\gamma_x`$ and $`c_x`$ are linear in $`x`$. This is not implied by $`n_x=1+gx`$. Item 4(c) of the question asks the evaluation for the cells with $`n_x=1+gx`$ whose level profiles are linear, and asks to name this subclass by conditions on the cell data. It is

```math
\mathcal L:\qquad n_x=1+g\,x,\qquad\frac{\varepsilon_x^2}{\Delta_x}=\gamma_0+\gamma_1\,x,\qquad c_x=\frac12\Bigl(\frac{\varepsilon_x^2}{\Delta_x^2}+\frac{\varepsilon_{x+1}^2}{\Delta_{x+1}^2}\Bigr)=\rho_0+\rho_1\,(x+\tfrac12)\qquad\text{for all }x\text{ of the chain},
\qquad\text{(10.31)}
```

with real numbers $`\gamma_0`$, $`\gamma_1`$, $`\rho_0`$, $`\rho_1`$ (in particular when $`\rho_{xx}=\rho_0+\rho_1x`$; equal cells are in $`\mathcal L`$ with $`\gamma_1=\rho_1=0`$). "First order in the gradients of the cell data" means: first order jointly in $`g`$, $`\gamma_1`$ and $`\rho_1`$, that is in the gradients $`G_k=gM_k`$, $`\mathcal F_k=\gamma_1M_k^2`$, $`g_{\zeta,k}=-\rho_1M_k^2`$ of the level $`k`$, in the sense of 04-branch-fall (at fixed $`\lambda`$, start and chain, followed by the limit of a long chain). For the cells of $`\mathcal L`$: $`\tau_k=\tau(1-\rho_0M_k^2)`$, $`g_{\zeta,k}=-\rho_1M_k^2`$, $`\hat M_k=M_k`$, $`G_k=gM_k`$, $`\mathcal F_k=\gamma_1M_k^2`$, $`V_k=e_0-\gamma_0M_k^2`$; the inequalities of the class hold by (a), and by (4.16), for $`\langle X\rangle=0`$,

```math
\text{cells of }\mathcal L:\qquad a_{k,\sigma}(0)=\tau^2\Bigl[-g+\sigma\,\gamma_1M_k+2g\,\rho_0M_k^2\Bigr]\ \ (\langle X\rangle=0),\qquad \gamma_1=\frac{\varepsilon_{x+1}^2}{\Delta_{x+1}}-\frac{\varepsilon_x^2}{\Delta_x}\ \ (\text{the same for all }x),\quad \rho_0=\tfrac12\,(c_{-1}+c_0)\ \ \Bigl(=\frac{\varepsilon_0^2}{\Delta_0^2},\ \text{the cell at }x=0,\ \text{if }\rho_{xx}\text{ is linear in }x\Bigr),
\qquad\text{(10.20)}
```

that is (10.13), (10.14) with $`\beta=2g\rho_0`$ (here $`\rho_{x+1,x}=0`$, whence $`\rho_0`$ in place of the $`2\rho_0`$ of (10.12)). Before the expansion it is $`a_{k,\sigma}(0)=\tau^2(1-\rho_0M_k^2)^2\,[-g+\sigma\gamma_1M_k]`$, the form (10.32) with the cell data; (10.20) drops $`-2\sigma\tau^2\gamma_1\rho_0M_k^3`$, of relative order $`\epsilon_1^2`$ against $`\sigma\gamma_1M_k`$, and $`\tau^2\lvert g\rvert\,O(\epsilon_1^4)`$, and the term in $`\rho_0`$ has the range stated after (10.32). For $`\langle X\rangle\neq0`$ the record term of (10.22) is added with the cell data, $`a^{\rm rec}_{k,\sigma}=-\sigma\tau^2\kappa\langle X\rangle\,[1/M_k-2\rho_0M_k]`$, and (10.23) applies with $`\gamma_1'=\gamma_1+2\rho_0\,\kappa\langle X\rangle`$. The hopping factors of every cell description are real, so for the cells of $`\mathcal L`$ $`\theta_k=0`$ and there is no velocity of the kind (10.25).

*Control, within $`\mathcal L`$,* for $`\langle X\rangle=0`$: cells of $`\mathcal L`$ with $`\varepsilon_x^2/\Delta_x=\gamma`$ for all $`x`$ ($`\gamma_1=0`$) against cells of $`\mathcal L`$ with $`\gamma_1\neq0`$. *Which cells with a constant $`\gamma`$ are in $`\mathcal L`$.* A constant $`\varepsilon_x^2/\Delta_x=\gamma`$ gives the second condition of (10.31) with $`\gamma_1=0`$, and not the third: $`c_x=\tfrac12\gamma\,(1/\Delta_x+1/\Delta_{x+1})`$. So cells with $`n_x=1+gx`$ and a constant $`\gamma`$ are in $`\mathcal L`$ if and only if $`\gamma=0`$ or $`1/\Delta_x+1/\Delta_{x+1}`$ is linear in $`x`$, that is $`1/\Delta_x=u+u'x+u''(-1)^x`$ with real numbers $`u`$, $`u'`$, $`u''`$ (equal cells: $`u'=u''=0`$). Cells with a constant $`\gamma>0`$ and, for example, $`1/\Delta_x`$ quadratic in $`x`$ are outside $`\mathcal L`$, and the control does not contain them. For constant $`\gamma`$ in $`\mathcal L`$, $`\mathcal F_k`$, the branch-odd term $`\sigma\tau^2\gamma_1M_k`$ and the $`\gamma_1`$ part of $`\mathcal R_k`$ vanish. What remains: the level offsets $`V_k=e_0-\gamma M_k^2`$, hence the unequal spacings (10.15) and the range (10.16); the mean rate $`\bar r(x)=\lambda_0^{-1}[n_x-\gamma\Sigma]`$, lowered at every position ($`\gamma\ge0`$) and of either sign, (10.33); the defect of (4.24), by (10.34) with the cell data (its derivation uses only $`\bar r(x)=\lambda_0^{-1}[n_x-\gamma_x\Sigma]`$ and the leading order of (10.20)), $`\mathcal R_k=\tau^2g\gamma\Sigma/(1-\gamma\Sigma)`$ for $`\gamma\Sigma\neq1`$, which is $`\tau^2g\gamma\Sigma`$ under (H), while for $`\gamma\Sigma=1`$ the comparison is not defined, (10.36); and the level-dependent hopping, $`a_{k,\sigma}(0)=-\tau^2g\,(1-2\rho_0M_k^2)`$, where $`\rho_0>0`$ when $`\gamma>0`$ (for equal cells $`\rho_0=\gamma/\Delta_0`$), level-dependent if and only if $`g\neq0`$ and $`\gamma>0`$. In $`\mathcal L`$, $`\gamma_x`$ depends on $`x`$ if and only if $`\gamma_1\neq0`$; then the fall from rest is level-dependent at the leading order in $`\epsilon_2`$, $`\epsilon_3`$ in each branch, by a term of opposite sign in the two branches ((10.14), first line). For $`\langle X\rangle\neq0`$ the record term $`a^{\rm rec}_{k,\sigma}`$ remains in both cases. For $`\varepsilon_x=0`$ for all $`x`$ every new term vanishes.

*Cells outside $`\mathcal L`$.* Admissible cells with $`n_x=1+gx`$ that are not in $`\mathcal L`$ exist: for example $`\Delta_x=\Delta`$ and $`\varepsilon_x^2/\Delta=\gamma_0+\delta\,(-1)^x`$ with $`0<\lvert\delta\rvert<\gamma_0`$, where $`\gamma_{x+1}-\gamma_x=-2\delta\,(-1)^x`$ alternates and is not one number $`\gamma_1`$. So outside $`\mathcal L`$ a dependence of $`\gamma_x`$ on $`x`$ is not described by a single $`\gamma_1`$, and (10.20) does not apply.
- *Results of items 4(a) and 4(b) that hold for them* (asked in item 4(c)): all of them, because they are stated for every $`x`$ and use no linearity. From (a): (10.18); $`H^{(3)}=0`$; the membership in $`\mathcal C_{\rm lev}`$ with level profiles that depend on $`x`$ in a general way, with all inequalities of the class, (P) without a condition and (P′) as a condition. From (b): the exact on-site solution (10.19), its comparison with item 2, the overlap, and the factor that the overlap puts on the hopping.
- *Further results stated for every $`x`$,* which hold for them as well: the answer of Step 2(c); and the spacings (10.15), (10.29) at every $`x`$ with $`\gamma^{(3)}_x=0`$, $`E^+_{x,k+1}-E^+_{x,k}=\frac{2\pi}{N\lambda_0}[n_x-\gamma_x(M_k+M_{k+1})]`$, independent of $`k`$ if and only if $`N=2`$ or $`\varepsilon_x=0`$. For cells with $`\varepsilon_x^2/\Delta_x=\gamma`$ for all $`x`$, in $`\mathcal L`$ or not: $`V_{x,k}=e_0-\gamma M_k^2`$ does not depend on $`x`$, so the on-site block has no level-dependent gradient; the level offsets and the factor $`1-M_k^2c_x`$ on the hopping remain.
- *Not asked and not stated:* the drift acceleration from rest of a cell description outside $`\mathcal L`$, its dependence on the level, the defect of (4.24), and the clock range (10.16), (10.30). The fall in level profiles that are not linear is outside the scope of the question (a later package): (4.7), (4.16) and (4.19) are quoted for linear level profiles, and (3.36) for linear profiles at zeroth order in their gradients. (10.20) and its control are results for $`\mathcal L`$.

### Step 5. Orders (item 5)

All rows: class $`\mathcal D`$ (rows 2–5: linear profiles of the field), regime R1, the ranges of $`\lambda`$ of (10.7), (10.10), (10.16), (10.30). The entries state what a field with its own contract changes. The third column (leading order in $`\epsilon_2`$, $`\epsilon_3`$) holds for every member of the class of its row, in row 4 for every member with a nonzero comparison rate, (10.35); the fourth column (first corrections) is stated under (P) of (10.27), in rows 2–5 under (10.28). Rows 2 and 4 are stated for $`\langle X\rangle=0`$: for $`\langle X\rangle\neq0`$ the fall from rest depends on the level and (4.24) has a defect already at zeroth order in $`\epsilon_1`$, also for a sharp field, by the record term of (10.22), (10.34), and the conditions of row 2 are those of (10.23).

| Quantity | Order $`\epsilon_1`$ | First change: order $`\epsilon_1^2`$, leading order in $`\epsilon_2`$, $`\epsilon_3`$ | Order $`\epsilon_1^2`$, first order in $`\epsilon_2`$, $`\epsilon_3`$ | Tags |
| --- | --- | --- | --- | --- |
| Factor that the body sees | $`N(x)`$ on $`G`$; no term linear in $`\epsilon_1`$ | factor unchanged; new on-site term $`-\gamma_xM_k^2\,\mathbb 1_2`$ (small against $`\Delta_f`$; not small against $`N(x)M_k`$ in R1) | factor $`N(x)+\gamma^{(3)}_xM_k^2`$ ($`\epsilon_3`$), positive if and only if (P); motion term times $`1-M_k^2c_x`$ ($`\epsilon_2`$) | (10.1), (10.7), (10.9), (10.10), (10.11), (10.27) |
| Fall from rest independent of the level, for $`\langle X\rangle=0`$ | holds, both branches, $`-\tau^2g`$ | lost iff $`\gamma_1\neq0`$: $`\sigma\tau^2\gamma_1M_k`$ (exact at this order; not small against $`\tau^2g`$ in R1) | if $`\gamma_1=0`$: lost iff $`\beta\neq0`$ ($`N\ge3`$): $`\tau^2\beta M_k^2`$; for $`\gamma_1\neq0`$ see after (10.32) | (10.13), (10.14), (10.22), (10.23), (10.28), (10.32), (4.22) |
| Clock a ring clock with one rate | holds, rate $`N(x)/\lambda_0`$ | spacings unequal iff $`\gamma_{x_0}\neq0`$ and $`N\ge3`$; range (10.16); rate $`\bar r`$ shifted by $`-\gamma_x\Sigma/\lambda_0`$, not small against $`N(x)/\lambda_0`$ in R1: $`\bar r`$ positive, zero or negative, (10.33) | cubic term $`\gamma^{(3)}_xM_k^3`$ in $`E^+_{x,k}`$: spacings unequal iff $`N\ge3`$ and $`\Xi_{x_0}\neq0`$ (equal for $`N=3`$, $`\gamma_{x_0}=3\gamma^{(3)}_{x_0}M_1`$, and for $`\gamma_{x_0}=\gamma^{(3)}_{x_0}=0`$); range (10.30), wide start; $`\bar r`$ shifted further by $`\gamma^{(3)}_x(M_0^2+M_0M_{N-1}+M_{N-1}^2)/\lambda_0`$ | (10.15), (10.16), (10.29), (10.30), (10.33), (3.23), (3.36) |
| Relation (4.24), for $`\langle X\rangle=0`$ | holds | defined iff $`D_0=1-\gamma_0\Sigma\neq0`$; defect (10.34), $`\mathcal R_k=\tau^2[\gamma_1(M_k-\Sigma/D_0)+g\gamma_0\Sigma/D_0]`$; under (H): $`\tau^2[\gamma_1(M_k-\Sigma)+g\gamma_0\Sigma]`$; for $`D_0\neq0`$ holds iff $`\gamma_1=0`$ and $`g\gamma_0=0`$; $`D_0=0`$: (10.36) | further defect from $`\beta`$ and $`\gamma^{(3)}_x`$ | (10.17), (10.26), (10.34), (10.35), (10.36), (4.24) |
| Velocity of a branch start at rest from the phase of the hopping (a velocity, not a drift acceleration), every $`\langle X\rangle`$ | none | none | $`\bar v^{\rm ph}_{k,\sigma}=-\sigma\tau^2M_k\mathrm{Im}\rho_Y`$ ($`\epsilon_2`$): odd in the branch, different for every two levels, present iff $`\mathrm{Im}\rho_Y\neq0`$ | (10.24), (10.25) |

```math
\text{rows 1–4: unchanged at order }\epsilon_1;\quad\text{first change at order }\epsilon_1^2\text{ with the coefficient at its leading order in }\epsilon_2,\ \epsilon_3,\ \text{of relative size }\lvert\gamma_x\rvert M_{\max}\le\epsilon_1\varepsilon=\epsilon_1^2\,\Delta_f/M_{\max}\ \ \bigl(\text{not a small number of R1; small under }2\epsilon_1\varepsilon\ll1\text{ of (10.35)}\bigr);\quad\text{row 5: first change at order }\epsilon_1^2\text{ and first order in }\epsilon_2 .
\qquad\text{(10.21)}
```

## Result

- **Regime of the order estimates.** Every order estimate of this package holds in R1, $`2\epsilon_1+2\epsilon_2+\epsilon_3<1`$ with weak records. R1 and the smallness of $`\epsilon_3=\nu M_{\max}/\Delta_f`$, a condition of this package in addition to the two small numbers of the question, are sufficient conditions for the construction used; they are not shown to be necessary, and the sharp field ($`\varepsilon=0`$) is exactly reducible for every $`\nu`$. For members of $`\mathcal D`$ outside R1 this package derives the R0 statements only ((10.1), (10.2), (10.4), first part of (10.7)). R1 does not make $`\varepsilon`$, $`\gamma_xM_{\max}`$ or $`\gamma^{(3)}_xM_{\max}^2`$ small; the hierarchies that do are conditions, named with the results that need them: (P), (P′) of (10.27), the margins of (10.28), and the nonzero comparison rate and (H) of (10.35).
- **Item 1.** (10.1): $`\hat C`$, exact, whole class; body part in $`\mathcal C`$ with $`m_x=mN(x)`$, $`\eta_x=N(x)`$, $`\zeta_x=1`$, $`V_x=e_0`$; admissible. (10.2): rules under (2.20). (10.4): bound $`\varepsilon M_{\max}\lambda`$, R0, all $`\lambda`$; (10.6): $`2\epsilon_1`$, R1, all $`\lambda`$, order estimate. (10.7): statistics as in a sharp field with $`N(x)`$ through first order in $`\epsilon_1`$ for $`\lambda\ll1/(\epsilon_1^2\Delta_f)`$.
- **Item 2.** (10.8)–(10.10): $`H_{\rm eff}=\hat C+H^{(2)}+H^{(2,1)}+H^{(3)}`$ with remainder and range, R1. (10.11): blocks. At leading order in $`\epsilon_2`$, $`\epsilon_3`$ the body part is a member of $`\mathcal C_{\rm lev}`$ for every member of $`\mathcal D`$. With the first corrections it is a member up to the hopping phase if and only if (P) of (10.27) holds, $`N(x)M_k+\gamma^{(3)}_xM_k^3>0`$ for all $`x`$, $`k`$, with the margin (P′) against the remainder; sufficient: $`\varepsilon\epsilon_1\epsilon_3<\min_xN(x)`$. Where (P) fails the class condition fails and $`V_{x,k}+M_{x,k}`$ is the lower on-site eigenvalue. The hopping phase is moved by a unitary from the contract into the start (a change of the start that depends on the level, not the identity for a start in one level); all new terms are well defined under (2.20).
- **Item 3.** (10.12): level data; with the first corrections they are level data of a member of $`\mathcal C_{\rm lev}`$ under (10.28). (10.13), (10.14): fall from rest and its level-independence, for $`\langle X\rangle=0`$; (10.32): the same before the expansion. At leading order in $`\epsilon_2`$, $`\epsilon_3`$ the fall is exact in $`\gamma_1M_k`$, which is not small against $`g`$ in R1; the term in $`\beta`$ and the lines with the first corrections are stated for the expression (10.13), and the term in $`\beta`$ exceeds the terms dropped for $`\gamma_1=0`$ or under the hierarchy stated after (10.32). (10.22), (10.23): the same for every $`\langle X\rangle`$, with the record term $`a^{\rm rec}_{k,\sigma}`$ of zeroth order in $`\epsilon_1`$; linear profiles, R1, closed form and conditions exact at the stated order; the parts with the first corrections under (10.28). (10.24), (10.25): the velocity of a branch start at rest from the hopping phase, $`\bar v^{\rm ph}_{k,\sigma}=-\sigma\tau^2M_k\mathrm{Im}\rho_Y`$; linear profiles, R1, under (10.28), second order in $`\epsilon_1`$, first order in $`\epsilon_2`$ and in $`Y`$, exact coefficient in the description with $`H_{\rm eff}`$; a velocity, not a drift acceleration. (10.15), (10.29): spacings and their independence of $`k`$, at leading order and with the first corrections; a spacing can vanish or be negative. (10.16): clock range at leading order in $`\epsilon_2`$, $`\epsilon_3`$; (10.30): rate, deviation and range with the cubic term, wide start. (10.33): the mean rate $`\bar r(x_0)`$ is positive, zero or negative in R1; (10.16), (10.30) hold in each case; for a zero rate the ring clock stands and is no reference for a ratio of rates. (10.34): relative gradient of the mean rate and defect of (4.24) with the denominator $`D_0=1-\gamma_0\Sigma`$ kept, every $`\langle X\rangle`$, leading order in $`\epsilon_2`$, $`\epsilon_3`$, for every member with $`D_0\neq0`$ and the margin of (10.35); for these members (4.24) holds for all levels if and only if $`\gamma_1=0`$, $`g\gamma_0=0`$ and $`\langle X\rangle=0`$ ($`N\ge3`$, and $`N=2`$ with $`\langle X\rangle=0`$), respectively $`\gamma_0(g-\gamma_1\Sigma)=0`$ and $`\gamma_1M_0M_1=-\kappa\langle X\rangle`$ ($`N=2`$). (10.17), (10.26): the expanded defect, under (H) of (10.35) only. (10.36): for $`D_0=0`$ the comparison is not defined; the form multiplied by the comparison rate holds if and only if $`g=\gamma_1\Sigma`$.
- **Item 4.** (10.18), (10.19): every cell description; exact on-site solution; member of $`\mathcal C_{\rm lev}`$ with (P) for every cell description. (10.31): the subclass $`\mathcal L`$ of item 4(c), named by conditions on the cell data. (10.20) with its control, inside $`\mathcal L`$ (fall for $`\langle X\rangle=0`$; record term by (10.22); no velocity of the kind (10.25); defect of (4.24) by (10.34)); cells with a constant $`\varepsilon_x^2/\Delta_x=\gamma`$ are in $`\mathcal L`$ if and only if $`\gamma=0`$ or $`1/\Delta_x+1/\Delta_{x+1}`$ is linear in $`x`$. For the cells outside $`\mathcal L`$ every result of items 4(a), 4(b) holds; their fall is outside the scope of the question and is not stated.
- **Item 5.** The table of Step 5 and (10.21).

## Consistency checks

1. **Dimensions.** $`\Phi_x`$, $`N`$, $`\varepsilon`$, $`g`$ are pure numbers; $`\tau`$, $`M_k`$, $`\Delta_f`$, $`e_0`$ are costs. Then $`\gamma_x`$ is an inverse cost and $`\gamma_xM_k^2`$ a cost; $`\rho_{xy}M_k^2`$, $`\gamma^{(3)}_xM_k^2`$, $`\gamma_1M_k`$, $`\beta M_k^2`$ are pure numbers like $`g`$; $`a_{k,\sigma}(0)`$ and $`\mathcal R_k`$ are $`\tau^2`$ times a number, as in (4.16). $`\kappa\langle X\rangle`$ is a cost, so $`\kappa\langle X\rangle/M_k`$ in (10.22), (10.26) is a pure number; $`\theta_k`$ is a pure number and $`\bar v^{\rm ph}_{k,\sigma}=\tau^2M_k\rho_Y`$ a cost, like $`\omega_k'`$, the dimension of $`\mathrm d\bar x_{\rm lab}/\mathrm d\lambda`$. $`\mu_{x,k}`$ is a cost; $`\Xi_{x_0}`$ is an inverse cost and $`\Xi_{x_0}d_{N-1}^2\lambda`$ a pure number. $`\gamma_0\Sigma`$, $`D_0`$ and $`\lambda_0\bar r`$ are pure numbers, and both sides of (10.36) are $`\tau^2/\lambda_0`$ times a number. Passed.
2. **Sharp field and commuting operators.** For $`\varepsilon=0`$: $`W\Pi_0=0`$, so $`\gamma_x=\rho_{xy}=\gamma^{(3)}_x=0`$, $`H_{\rm eff}=\hat C`$, $`Q_0\Psi=0`$ and $`p=\hat p`$ exactly, which is (2.3) with $`n_x=N(x)`$, $`e_f=e_0`$. If every $`\Phi_x`$ commutes with $`C_f`$, the simple eigenvector $`\varphi_0`$ is an eigenvector of every $`\Phi_x`$, so $`\varepsilon=0`$: all new terms need $`[\Phi_x,C_f]\neq0`$. For $`\varepsilon=0`$, (10.22) is $`a_{k,\sigma}(0)=-\tau^2g-\sigma\tau^2\kappa\langle X\rangle/M_k`$, which is (4.16) for the variant (a) with the plain gradient $`\mathcal F=-\kappa\langle X\rangle`$; it is level-independent iff $`\langle X\rangle=0`$, with the value $`-\tau^2g`$, as (4.22) states; and $`\theta_k=0`$, so (10.25) vanishes. For $`\varepsilon=0`$, (P) and (10.28) hold ($`\mu_{x,k}=N(x)M_k`$) and $`\Xi_{x_0}=0`$; $`D_0=1`$, and (10.34) is $`\mathcal R_k=-\tau^2\kappa\langle X\rangle/M_k`$. Passed.
3. **Exact on-site problems against the expansion.** Cell: the exact lower eigenvalue and overlap (10.19) reproduce $`-\gamma_xM_k^2`$, $`\gamma^{(3)}_x=0`$ and the hopping factor $`1-M_k^2c_x`$ of (10.18), derived independently from (10.9), (10.10). Two-place field of Step 2(b): the lower eigenvalue of $`C_f\pm M_k\Phi_x`$ is $`\pm nM_k+\tfrac12\bigl[(\Delta\pm M_ka)-\sqrt{(\Delta\pm M_ka)^2+4M_k^2v^2}\bigr]`$; at second order in $`v`$ its part odd in the branch is $`nM_k+\frac{a\,v^2M_k^3}{\Delta^2-M_k^2a^2}`$, which is $`\mu_{x,k}=nM_k+\gamma^{(3)}_xM_k^3`$ at leading order in $`M_ka/\Delta`$ and is negative for $`a<0`$ and $`n<\lvert a\rvert v^2M_k^2/\Delta^2`$. Two-place field of (10.36): the lower eigenvalue of $`C_f+M_k\Phi_x`$ is $`M_k(1+gx)+\tfrac12\bigl[\Delta-\sqrt{\Delta^2+\tfrac43M_k^2\Delta}\bigr]=M_k(1+gx)-\tfrac13M_k^2+\frac{M_k^4}{9\Delta}-\dots`$, so $`\lambda_0\bar r(x)=E^+_{x,1}-E^+_{x,0}=g\,x+\frac{5}{3\Delta}-\dots`$: zero at $`x=0`$ at the order kept, as (10.36) states, with the exact value $`\tfrac54\epsilon_1^2`$ there, of the order of the margin of (10.35) ($`\varepsilon\epsilon_1=\tfrac23`$). For $`\lvert\gamma_0\rvert\Sigma\to0`$, (10.34) reduces to (10.17), (10.26). Passed.

## Open issues

- (10.6), the R1 part of (10.7) and the remainders of (10.10) are order estimates: their constants, and the dependence of (10.7) on the number of readings, are not bounded explicitly.
- The accelerations (10.13), (10.20), (10.22) and the velocity (10.24), (10.25) are those of the description with $`H_{\rm eff}`$; for the description with $`C`$ only the agreement of the statistics within (10.10) is derived, not a statement about its acceleration or its velocity.
- Members in which (P) of (10.27), or (10.28) for the linear profiles, fails or holds without its margin: the statements with the first corrections are not derived for them. The exchange of the branch places of a level with a negative rest term is named in Step 2(b) but not worked out, and a rest term that changes sign along the chain is not treated.
- Members whose comparison rate vanishes within the margin of (10.35), $`\lvert D_0\rvert`$ not large against $`\varepsilon\epsilon_1(\epsilon_3+\epsilon_1^2+\epsilon_2^2)`$: the sign of the mean rate is decided by terms not kept, and neither (10.34) nor (10.36) is derived for them. The margin itself is an order estimate.
- With $`\gamma_1\neq0`$ the term $`\tau^2\beta M_k^2`$ of (10.13) is larger than the terms dropped after (10.32) only under the hierarchy stated there; the terms of fourth order of $`H_{\rm eff}`$, which are of the same size as the dropped terms, are not computed.
- Outside the scope of the question (item 4(c), "Out of scope"): the fall from rest, the defect of (4.24) and the clock range of cells with $`n_x=1+gx`$ whose $`\gamma_x`$ or $`c_x`$ is not linear in $`x`$ (for example an alternating $`\varepsilon_x^2/\Delta_x`$, or a constant $`\gamma>0`$ with $`1/\Delta_x`$ quadratic in $`x`$). They need a result for level profiles that are not linear (a later package).
- (10.16) has the orders of (3.36) (zeroth order in the gradients) and the leading order in $`\epsilon_2`$, $`\epsilon_3`$; (10.30) holds in the wide-start limit only. The loss of clock coherence by the level-dependent force $`\mathcal F_k`$ and by the level-dependent velocity (10.25), which separate the levels in position at first order in the gradients, is not treated.
- For profiles of the field that are not linear the phase of the hopping depends on $`x`$; its effect is given only as the change of the start of Step 2(b), and the velocity (10.24), (10.25) is derived for the linear profiles.
- Where $`2\epsilon_1+2\epsilon_2+\epsilon_3\ge1`$ (a slow field, or $`\epsilon_3`$ not small) the norm estimates of this package do not control the expansion, and only the R0 statements (10.1), (10.2), (10.4) and the first part of (10.7) are derived. Whether an effective description exists there is not determined, except for $`\varepsilon=0`$, where it is exact.

## Methods used

- Compression of the contract onto an eigenvector of the field
- Duhamel formula and norm bounds
- Schrieffer–Wolff block diagonalisation (nondegenerate perturbation theory with a gap), with a sufficient norm condition
- Sylvester equation, expansion in commutators with the body contract
- Rayleigh–Schrödinger second and third order with the reduced resolvent
- Exact diagonalisation of a two-place cell and of a two-place field
- Level blocks and linear level profiles of the class $`\mathcal C_{\rm lev}`$, with the inequalities of the class
- Unitary removal of a hopping phase, with its action on the start
- Velocity operator of a level block (commutator with the position label), stationary phase and window average
- Effective body contract with the mean record as a plain gradient
- Second differences and chord deviation of a cubic on equally spaced levels
- Quotient of rates kept unexpanded, with the zero of the denominator treated separately
- Linear recurrence for the cell data of a linear hopping profile
