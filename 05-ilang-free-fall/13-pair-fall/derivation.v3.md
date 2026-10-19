# Fall of a bound pair of two bodies in a sharp field

- **Subproject:** 05-ilang-free-fall
- **Package:** 13-pair-fall
- **Version:** v3
- **Mode:** internal regeneration
- **Date:** 2026-10-11

## Changes from previous version

Trigger: `review.v2.md` (five minor issues, I1–I5, on statements with "all", "only", "unless", "in general", "not at all" and their exceptional members). No display (13.1)–(13.22) is changed, and no tag is renumbered or withdrawn. New tags: (13.23)–(13.26). Every sentence of v2 that is not listed here is kept word for word.

- **Header.** Version; this section is new.
- **I1 (the pair against one part for $`g_1\neq g_2`$).**
  - Step 6.4, third bullet: "Otherwise not at all" is replaced by the statement for both parts, and the member on which the pair falls like one part is added with the new display (13.23). Second bullet: "both of", "at leading order in $`\mathsf R`$" and the remark that $`u_*`$ is this member for the common gradient.
  - Step 7.3, bullet "Equal to $`\tau_i^2`$": "one special value of $`g_1/g_2`$" is replaced by the member (13.23). Table of item 5, first and third row, last column. Twin: (13.15), (13.19), (13.23).
- **I2 (two sets of data).**
  - Setup, "Notation added here": one bullet added (level data, clock data of the part $`i`$, the label $`[i]`$).
  - Step 7: one sentence at its head; the parenthesis under (13.17) is replaced by a sentence; one sentence under (13.18); the head of Step 7.3; one sentence in Step 7.4. Result, item 4 (now four bullets) and one sentence before the table of item 5. Twin: (13.17), (13.18).
  - Step 7.3, bullet "The same for $`i=1,2`$": "unless $`\tau_1/\bar M_1=\tau_2/\bar M_2`$" is replaced by the condition that (13.18) gives, the new display (13.26), with the members for which it reduces to $`\tau_1/\bar M_1=\tau_2/\bar M_2`$; the member $`a_{\rm pair}=0`$ is added.
- **I3 ($`g_i=0\neq g_j`$ and the member $`\varrho_i=0`$).** Step 7.3: the new display (13.24) (the two coefficients of $`\varrho_i`$), the list of the members on which $`\mathsf w_i^2`$ is and is not defined (this replaces "then $`\varrho_i\neq0`$ for small $`\epsilon`$"), the bullet "Range of (13.19)", and the value (13.25) for $`g_i=0\neq g_j`$ with its remainder and the three answers (this replaces the bullet "Exceptional: for $`g_i=0\neq g_j`$ ..."); one sentence added to the bullet "Derivatives used". Table, third row. Twin: (13.19), (13.24), (13.25).
- **I4 (a member for "do not commute").** Step 5.3: the first sentence and the first bullet are stated for the members with $`\mathsf f_i\neq0`$ and "in general" is removed; the sentence "That quantity depends ..." is stated for $`\mathsf f_i\neq0`$; a bullet "Members" is added (numerical, from the level of the script; new table of `code/v3/pair_fall_check.py`); the bullet on the exceptional members gets its numbers. Result, item 2(c); Open issues, second item; twin (13.11). The answer to item 2(c) is conditional, with numerical members.
- **I5 (summary sentences).** Step 6.2: the sentence "Equivalently ..." is replaced (exact form and leading-order form named). Step 6.5, last bullet, and Result, item 3, last two sentences: stated with their order and with the member without a fall.
- **Reading pass.** Every sentence of the text, the Result, the table and the twin with "all", "every", "iff", "only", "unless", "no", "not at all", "in general" or a range was read against the display it cites, on the trivial member and on the extreme members. Changed besides the above:
  - Setup, "Approximations and their range": one sentence on the trivial member (vanishing gradients).
  - Step 3.7: "The rests differ in general" is replaced by the members on which they differ and coincide.
  - Step 4.4: "in general" (twice) is replaced by the numerical sets on which the statements rest; path of the script.
  - Step 5.1: "neither small nor decaying in general" is replaced by what is shown (a decay is neither derived nor excluded).
  - Step 5.4: the condition $`E_b''(0)\neq0`$ for $`\mathfrak m_b`$; a member for "the class does not imply $`E_b'(0)=0`$" (numerical); one exceptional member added.
  - Step 5.5 and Result, item 2(d): "only" is made precise ($`E_b''`$, $`E_b'`$ are factors).
  - Step 6.3: how the limit in $`u`$ is taken. Step 6.4: one sentence under (13.15) (fixed ratio, trivial member); the ratio for $`w_{11}>0`$ in the first bullet. Step 6.5: "at a fixed binding" in the claim, "(for $`\mathsf N\neq0`$)". Step 6.6: "at leading order".
  - Step 7.4: the value of $`\mathsf w^2/\tau^2`$ for $`w_{11}>0`$; the member $`g_{\rm c}=0`$.
  - Result: first paragraph; item 1 (the dependence on $`\eta`$ on the trivial member); the head of item 2 and item 2(b) (which members are numerical). Table: second row, third column; third row, second column. Open issues: third and fourth item, one item added. Twin: (13.3), (13.9), (13.10), (13.12), (13.16), (13.20).
- **Code.** `code/v3/pair_fall_check.py` is the script of v2 with the paths changed and one table added (the members of I4). All numbers of v2 are reproduced. Changed in the section "Code": the bullets "File" and "Run", one sub-bullet under "What it does", the note on the data in "Item 4", the new bullets "Item 2c" and "Cross-checks".

## Setup and assumptions

- **Setting.** Objects, contract $`C`$, class $`\mathcal W`$, records, field, levels, bound level, packets, orders and the regime $`\mathsf R`$ are those of the question, used literally. Assumptions of the package (M8, A11): two Model D bodies, one medium with one operator and one strength, a binding of the class $`\mathcal W`$ without a factor of the field, the field coupled to the rest and clock terms only, the field start $`\varphi`$ sharp and stationary, and a packet of a bound level as the start (M9). Equal parameters of the two types are never assumed.
- **Inputs, as quoted in the question:** (11.1), (11.2), (11.5)–(11.9), (11.12)–(11.14), (11.16), (11.19)–(11.22) of 11-bound-pair; (8.10), (8.11) of 08-two-types; (2.1), (2.3) of 02-field-object; (4.7), (4.10), (4.11), (4.16), (4.24) of 04-branch-fall; (5.1), (5.5), (5.6), (5.11) of 04-ilang-time/05-moving-clock; (17.15) of 03-ilang-space/17-motion; (16.11) of 03-ilang-space/16-common-space. With (11.14) the question quotes the statement of Step 8 of 11-bound-pair on the differentiation of (11.12) in the data; it is used in Step 7.2.
- **Notation added here.**
  - The packet weight is written $`g(P)`$ and enters only through $`g`$, $`g'`$ and $`\langle F\rangle_g:=\int\mathrm dP\,\lvert g(P)\rvert^2F(P)`$. The common gradient ($`g`$ in the question) is written $`g_{\rm c}:=g_1=g_2`$.
  - $`\mathfrak h:=\ell^2(\mathbb Z)\otimes\mathbb C^2\otimes\mathbb C^2`$ is the fibre space; $`\lvert P;\psi\rangle(x_1,x_2)=(2\pi)^{-1/2}e^{iP(\eta x_1+(1-\eta)x_2)}\psi(x_1-x_2)`$, so that $`\langle P;\psi\vert P';\psi'\rangle=\delta(P-P')\langle\psi\vert\psi'\rangle`$ and $`\lVert\Phi_g\rVert=1`$.
  - $`\Gamma(P)>0`$ is the distance of $`E_b(P)`$ from the rest of the spectrum of $`H(P)`$; $`R_P:=Q_P(H(P)-E_b(P))^{-1}Q_P`$ with $`\lVert R_P\rVert=1/\Gamma(P)`$; $`\mathcal U_P(\lambda):=\mathbb 1-e^{-i(H(P)-E_b(P))\lambda}`$; $`I_g`$ as in (11.8); $`\Gamma_g:=\min_{I_g}\Gamma>0`$.
  - $`\mathsf b:=\lvert g_1\rvert M_1+\lvert g_2\rvert M_2+2\kappa\lvert\langle X\rangle\rvert`$, $`\mathsf d_\eta:=\lvert1-\eta\rvert\lvert g_1\rvert M_1+\lvert\eta\rvert\lvert g_2\rvert M_2+\lvert1-2\eta\rvert\kappa\lvert\langle X\rangle\rvert`$, $`\tau_{\min}:=\min(\tau_1,\tau_2)`$.
  - Two sets of data (Step 7). The **level data**: both parts on their levels, $`(M_1,M_2)=(M^{(1)}_{k_1},M^{(2)}_{k_2})`$; $`a_i`$, $`a`$, $`u`$, $`\Lambda`$, $`\mathfrak m_i`$, $`\tau_{\rm p}`$ without a label are taken with them, as in (13.13)–(13.16), (13.19), (13.20), (13.23). The **clock data of the part $`i`$**: the mean rest cost $`\bar M_i`$ for the part $`i`$, whose clock is read, and the level $`M_j=M^{(j)}_{k_j}`$ for the other part $`j\neq i`$; quantities taken with them carry the label $`[i]`$: $`a_{i[i]}:=\tau_i^2/(4\bar M_i)`$, $`a_{[i]}:=a_{i[i]}+a_j`$, $`u_{[i]}:=\lvert w\rvert/a_{[i]}`$, $`\Lambda_{[i]}:=1+\varsigma/\sqrt{1+u_{[i]}^2}`$. In (11.19), (11.20), (13.17), (13.18), (13.21), (13.22) the symbols $`M_i`$, $`a_i`$, $`a`$, $`u`$, $`\Lambda`$ are those of the clock data of the part $`i`$, as (11.20) states: there $`u=u_{[i]}`$ and $`\Lambda=\Lambda_{[i]}`$. The two sets coincide iff $`M^{(i)}_{k_i}=\bar M_i`$, which is possible only for odd $`N_i`$ and $`k_i=(N_i-1)/2`$. Both $`u`$ and $`u_{[i]}`$ are fixed in $`\mathsf R`$, and $`u_{[i]}/u=a/a_{[i]}`$ does not depend on the binding, so an ordered limit in $`u`$ is one in $`u_{[i]}`$ as well.
- **Standard facts used.**
  - F1 (first order in a term of the contract): $`e^{-i(H_0+\Delta)\lambda}=e^{-iH_0\lambda}-i\int_0^\lambda\mathrm ds\,e^{-iH_0(\lambda-s)}\Delta\,e^{-iH_0s}+O(\Delta^2)`$ at fixed $`\lambda`$.
  - F2 (isolated simple eigenvalue of an analytic family): $`E_b`$ and $`\psi_P`$ are analytic in $`P`$ and in the data, $`Q_P\psi_P'=-R_PV_\eta\psi_P`$, and $`\langle\psi_P\vert\psi_P'\rangle\in i\mathbb R`$.
  - F3: an eigenvector of $`H(P)`$ for an eigenvalue outside the bands (11.2) decays exponentially in $`\lvert r\rvert`$ (finite range of the hopping and of $`W`$), locally uniformly in $`P`$; hence $`\hat r\psi_P\in\mathfrak h`$.
  - F4 (long chain): at fixed $`\lambda`$ the first-order coefficients on the chain $`\lvert x_i\rvert\le L`$ converge for $`L\to\infty`$ to those of the infinite chain, because the hopping has range one and $`\Phi_g`$, $`\hat x_i\Phi_g`$ are square summable.
- **Approximations and their range.** First order in $`(g_1,g_2,\kappa\langle X\rangle)`$ at fixed $`\lambda`$ (the size of the second order is not estimated). Records at leading order in $`\kappa`$ with the convention of the question: the bodies evolve by $`C_{\rm bod}`$. Items 3 and 4 at leading order in $`\mathsf R`$ at fixed $`u`$; their remainders are not uniform in $`u`$. Trivial member: for $`g_1=g_2=0`$ and $`\kappa\langle X\rangle=0`$ every first-order quantity below is zero; a statement with "iff", "only", "no" or "not at all" names this member where it would be false on it.

## Derivation

### Step 1. Reduced contract (item 1a)

1. Every term of $`C`$ is the identity on $`\mathcal H_f`$, or $`\theta_i\,\hat x_i\otimes G_i\otimes\Phi`$, or $`C_f`$. With $`\Phi\varphi=\gamma\varphi`$ and $`C_f\varphi=e_f\varphi`$, for every $`\Psi\in\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_c`$ (the computation of (2.3) and (8.10); $`U`$ is carried along unchanged):

```math
C\,(\Psi\otimes\varphi)=\bigl((C_{\rm red}+e_f)\Psi\bigr)\otimes\varphi,\qquad C_{\rm red}=\sum_{i=1,2}\Bigl[A_i+\sum_xP^{(i)}_x\otimes(1+g_ix)\,G_i+\kappa\,\hat x_i\otimes X\Bigr]+U .
\qquad\text{(13.1)}
```

2. Hence $`e^{-iC\lambda}(\Psi\otimes\varphi)=e^{-ie_f\lambda}\,(e^{-iC_{\rm red}\lambda}\Psi)\otimes\varphi`$ for all $`\lambda`$: the view of $`\{b_1,b_2,c\}`$ is pure and evolves by $`C_{\rm red}`$ (exact, for this start of the field only).
3. $`C_{\rm red}`$ is the contract of an admissible description of $`b_1,b_2,c`$. It is self-adjoint and independent of $`\lambda`$; $`U`$ is a pair term of $`b_1,b_2`$; $`\kappa\,\hat x_i\otimes X`$ are pair terms of $`b_i,c`$; $`A_i+\sum_xP^{(i)}_x\otimes(1+g_ix)G_i`$ acts on one object and is included in a pair term (A5). Its position-dependent rest and clock term is then a property of the type of $`b_i`$ (A10).
4. A binding with a factor of the field needs a term on $`\mathcal H_{b_1}\otimes\mathcal H_{b_2}\otimes\mathcal H_f`$, for example $`\sum_{x_1,x_2}\lvert x_1\rangle\langle x_1\rvert\otimes\lvert x_2\rangle\langle x_2\rvert\otimes W(x_1-x_2)\otimes\Phi_{x_1x_2}`$, that is not a sum of pair terms. Decompose the operators of each object into $`\mathbb C\mathbb 1`$ and the traceless ones: a sum of pair terms has no component that is traceless on all three objects, while $`U'\otimes\Phi'`$ has one whenever $`U'\neq u_1\otimes\mathbb 1+\mathbb 1\otimes u_2`$ and $`\Phi'\notin\mathbb C\mathbb 1`$. Such a three-object term is not of the form (1.10).

### Step 2. The operator on the two bodies (item 1b)

1. The partial expectation of $`C-e_f`$ in $`\chi\otimes\varphi`$ is, by (13.1),

```math
C_{\rm bod}=C^{\rm D}_1+C^{\rm D}_2+U+\sum_{i=1,2}g_i\,\hat x_i\otimes G_i+\kappa\langle X\rangle\,(\hat x_1+\hat x_2).
\qquad\text{(13.2)}
```

2. $`[C_{\rm bod},D_i]=0`$, so the levels are conserved, and $`G_i=M_i\sigma^{(i)}_3`$ on the levels $`k_1,k_2`$. With $`\hat x_1=\hat X_\eta+(1-\eta)\hat r`$ and $`\hat x_2=\hat X_\eta-\eta\hat r`$ the gradient terms $`\Delta:=C_{\rm bod}-C_{\rm pair}`$ are

```math
\begin{aligned}
\Delta&=\hat X_\eta\,\mathcal K+\hat r\,\mathcal D_\eta,\qquad \mathcal K:=g_1M_1\sigma^{(1)}_3+g_2M_2\sigma^{(2)}_3+2\kappa\langle X\rangle,\\
\mathcal D_\eta&:=(1-\eta)\,g_1M_1\sigma^{(1)}_3-\eta\,g_2M_2\sigma^{(2)}_3+(1-2\eta)\,\kappa\langle X\rangle .
\end{aligned}
\qquad\text{(13.3)}
```

3. Well-definedness (M6). A replacement of the listed terms that leaves $`C`$ unchanged leaves $`\langle\chi\otimes\varphi\vert C\vert\chi\otimes\varphi\rangle`$ unchanged. It can change the listed $`C_f`$ by a multiple of $`\mathbb 1`$, hence $`e_f`$: $`C_{\rm bod}`$ is fixed by $`C`$, $`\chi`$, $`\varphi`$ up to an additive real constant, which drops out of everything below. Let $`b(x_1,x_2)`$ be the block of $`C_{\rm bod}`$ that is diagonal in both positions, an operator on the internal labels. For $`\lvert x_1-x_2\rvert>R`$ it is $`(1+g_1x_1)G_1+(1+g_2x_2)G_2+\kappa\langle X\rangle(x_1+x_2)`$ up to the constant. $`G_1`$ and $`G_2`$ are traceless and act on the labels of one body each, so the three parts are linearly independent: $`\kappa\langle X\rangle`$ is the normalized trace of $`b(x_1+1,x_2)-b(x_1,x_2)`$ (both arguments in that region), $`g_1G_1`$ is its traceless part, and $`G_1`$ is the traceless part of $`b(0,x_2)`$ on the labels of $`b_1`$; likewise for $`b_2`$.
   - $`g_1`$, $`g_2`$, $`\kappa\langle X\rangle`$: fixed by $`C_{\rm bod}`$, well defined, independent of $`\eta`$. They are the coefficients read from $`C_{\rm bod}`$. The listed numbers $`\gamma\theta_i`$ and $`\kappa\langle\chi\vert X\vert\chi\rangle`$ can change under a relisting such as $`X\to X-c`$, $`C^{\rm D}_i\to C^{\rm D}_i+\kappa c\,\hat x_i`$. Used: the label $`0`$ of the two types (A2) and the finite range of $`W`$.
   - The operator that multiplies the centre label, $`\mathcal K`$ (on all levels $`g_1G_1+g_2G_2+2\kappa\langle X\rangle`$): fixed by $`C_{\rm bod}`$, independent of $`\eta`$.
   - The operator that multiplies $`\hat r`$: fixed by $`C_{\rm bod}`$ once $`\eta`$ is given. It depends on the convention, $`\mathcal D_\eta=\mathcal D_0-\eta\,\mathcal K`$, and is independent of $`\eta`$ iff $`\mathcal K=0`$, i.e. (as $`M_i>0`$) iff all three gradients vanish.

### Step 3. First-order velocities from a bound level (item 2a)

Class: every $`W\in\mathcal W`$, all data, every bound level, every $`g\in\mathcal G(\mathcal P_0)`$, all gradients. On the levels $`k_1,k_2`$ write $`H_0:=C_{\rm pair}`$ and $`\Phi_g(\lambda):=e^{-iH_0\lambda}\Phi_g`$.

1. $`\Delta`$ is diagonal in the positions, so $`i[C_{\rm bod},\hat x_i]=V_i`$ and $`\mathrm d\bar m_i/\mathrm d\lambda=\langle V_i\rangle`$ in the evolved state, exactly. The first-order velocity $`v^{(1)}_i`$ is the part of this expectation that is linear in the gradients. By F1,

```math
v^{(1)}_i(\lambda)=2\,\mathrm{Re}\,\bigl\langle\Phi_g(\lambda)\big\vert V_i\big\vert\Phi^{(1)}(\lambda)\bigr\rangle,\qquad
\Phi^{(1)}(\lambda):=-i\int_0^\lambda\mathrm ds\;e^{-iH_0(\lambda-s)}\,\Delta\,\Phi_g(s),
\qquad\text{(13.4)}
```

and the same formula with $`V_i\to\hat r`$ gives the first-order change of $`\bar m_1-\bar m_2`$. On a finite chain all operators are bounded; the long-chain limit is F4, with (13.5).
2. In the fibres $`\Phi_g(s)`$ is $`g\,e^{-iE_bs}\psi_P`$, and $`\hat X_\eta`$ acts as $`i\partial_P`$ ($`g`$ has compact support in $`\mathcal P_0`$), so

```math
\Delta\,\Phi_g(s)\ \longleftrightarrow\ e^{-iE_b(P)s}\bigl[s\,E_b'\,g\,\mathcal K\psi_P+\xi_P\bigr],\qquad
\xi_P:=i\,g'\,\mathcal K\psi_P+i\,g\,\mathcal K\psi_P'+g\,\hat r\,\mathcal D_\eta\psi_P ,
\qquad\text{(13.5)}
```

a vector of $`\mathfrak h`$ with $`\int\mathrm dP\,\lVert\xi_P\rVert^2<\infty`$ (F2, F3, $`g\in C^1`$ with compact support).
3. Split (13.5) along $`\psi_P`$ and in $`Q_P\mathfrak h`$. On $`\psi_P`$ the propagator is $`e^{-iE_b(\lambda-s)}`$. On $`Q_P\mathfrak h`$, $`\int_0^\lambda\mathrm ds\,e^{-i(H-E_b)(\lambda-s)}=-iR_P\,\mathcal U_P(\lambda)`$ and $`\int_0^\lambda\mathrm ds\,s\,e^{-i(H-E_b)(\lambda-s)}=-i\lambda R_P+R_P^2\,\mathcal U_P(\lambda)`$.
4. Part along $`\psi_P`$. $`\langle V_i\rangle_P=E_b'`$ by (11.7), and $`\langle\mathcal K\rangle_P`$, $`\langle\hat r\mathcal D_\eta\rangle_P`$ are real. The terms with $`\lambda^2`$ and with $`\mathcal D_\eta`$ are imaginary and drop out. With $`2\,\mathrm{Re}\langle\psi_P\vert\mathcal K\vert\psi_P'\rangle=\partial_P\langle\mathcal K\rangle_P`$ the rest is $`\lambda\int\mathrm dP\,E_b'\,\partial_P\bigl(\lvert g\rvert^2\langle\mathcal K\rangle_P\bigr)=-\lambda\,\langle E_b''\langle\mathcal K\rangle\rangle_g`$ (partial integration).
5. Part in $`Q_P\mathfrak h`$. The term $`-i\lambda R_P`$ gives $`-\lambda\int\mathrm dP\,\lvert g\rvert^2E_b'\,2\,\mathrm{Re}\langle V_i\psi_P\vert R_P\vert\mathcal K\psi_P\rangle`$. Since $`V_1-V_2=i[H(P),\hat r]`$ and $`(H-E_b)\psi_P=0`$,

```math
\begin{aligned}
R_PV_1\psi_P&=R_PV_\eta\psi_P+i(1-\eta)\,Q_P\hat r\psi_P,\qquad R_PV_2\psi_P=R_PV_\eta\psi_P-i\eta\,Q_P\hat r\psi_P,\\
2\,\mathrm{Re}\,\langle V_i\psi_P\vert R_P\vert\mathcal K\psi_P\rangle&=-\partial_P\langle\mathcal K\rangle_P\qquad(i=1,2).
\end{aligned}
\qquad\text{(13.6)}
```

The second line holds because $`\partial_P\langle\mathcal K\rangle_P=-2\,\mathrm{Re}\langle\mathcal K\psi_P\vert R_P\vert V_\eta\psi_P\rangle`$ (F2) and $`\langle Q_P\hat r\psi_P\vert\mathcal K\psi_P\rangle=\langle\hat r\mathcal K\rangle_P-\langle\hat r\rangle_P\langle\mathcal K\rangle_P`$ is real ($`[\hat r,\mathcal K]=0`$).
6. Result, for $`i=1,2`$ and every $`\lambda`$:

```math
\boxed{\;v^{(1)}_i(\lambda)=\lambda\,\langle\alpha\rangle_g+\rho_i(\lambda)\;},\qquad \alpha(P):=-E_b''(P)\,\langle\mathcal K\rangle_P+E_b'(P)\,\partial_P\langle\mathcal K\rangle_P ,
\qquad\text{(13.7)}
```

```math
\alpha=g_1\alpha_1+g_2\alpha_2+\kappa\langle X\rangle\,\alpha_X,\qquad
\alpha_i(P)=-M_i\bigl[E_b''\,\langle\sigma^{(i)}_3\rangle_P-E_b'\,\partial_P\langle\sigma^{(i)}_3\rangle_P\bigr],\qquad \alpha_X(P)=-2E_b''(P),
\qquad\text{(13.8)}
```

```math
\begin{aligned}
\rho_i(\lambda)&=-2\,\mathrm{Re}\int\mathrm dP\,\Bigl[i\lvert g\rvert^2E_b'\,\langle V_i\psi_P\vert R_P^2\,\mathcal U_P(\lambda)\vert\mathcal K\psi_P\rangle+g^{*}\langle V_i\psi_P\vert R_P\,\mathcal U_P(\lambda)\vert\xi_P\rangle\Bigr],\\
\lvert\rho_i(\lambda)\rvert&\le\tau_i\,\mathsf B_g,\qquad \mathsf B_g:=\frac4{\Gamma_g}\Bigl[\mathsf b\Bigl(\frac{\tau_{\min}}{\Gamma_g}+\lVert g'\rVert_2+\max_{I_g}\lVert\psi_P'\rVert\Bigr)+\mathsf d_\eta\max_{I_g}\lVert\hat r\psi_P\rVert\Bigr].
\end{aligned}
\qquad\text{(13.9)}
```

The bound uses $`\lVert V_i\rVert\le\tau_i`$, $`\lvert E_b'\rvert\le\tau_{\min}`$, $`\lVert\mathcal U_P\rVert\le2`$, $`\lVert\mathcal K\rVert\le\mathsf b`$, $`\lVert\mathcal D_\eta\rVert\le\mathsf d_\eta`$ and $`\int\lvert g\rvert\lvert g'\rvert\le\lVert g'\rVert_2`$.
7. Status. Both parts have the same coefficient $`\langle\alpha\rangle_g`$ of the growing part. The rests of the two parts are not equal on the class, and $`\rho_i(0)=0`$: they differ for the numerical sets S2–S5 and for S1 with $`g_1`$ only (section "Code"), and they coincide under the conditions of Step 4.3, where $`\bar m_1-\bar m_2=0`$ (set S1 with the common or the plain gradient). The rest is bounded for all $`\lambda`$, in particular for all $`\lambda\ge0`$, under the conditions of the class alone: the level is isolated on the compact $`I_g\subset\mathcal P_0`$ ($`\Gamma_g>0`$) and $`g\in\mathcal G(\mathcal P_0)`$ ($`\lVert g'\rVert_2<\infty`$). $`\rho_i`$ does not depend on $`\eta`$ or on the phase of $`\psi_P`$; the single terms of the bound do. By (11.5) and F2, $`\langle\sigma^{(i)}_3\rangle_P=\partial E_b/\partial M_i`$ and $`\partial_P\langle\sigma^{(i)}_3\rangle_P=\partial E_b'/\partial M_i`$. Numerical check: section "Code".

### Step 4. Mean label separation (item 2b)

1. The computation of Step 3 with $`V_i\to\hat r`$ ($`\langle\hat r\rangle_P`$ is real; (13.6) is not used) gives, for every member of the class of item 2,

```math
\begin{aligned}
(\bar m_1-\bar m_2)^{(1)}(\lambda)&=\lambda\,\langle\beta\rangle_g+\sigma(\lambda),\qquad \lvert\sigma(\lambda)\rvert\le\max_{I_g}\lVert\hat r\psi_P\rVert\;\mathsf B_g,\\
\beta(P)&:=-\langle\mathcal K\rangle_P\,\partial_P\langle\hat r\rangle_P-2E_b'(P)\,\mathrm{Re}\,\langle\hat r\psi_P\vert R_P\vert\mathcal K\psi_P\rangle ,
\end{aligned}
\qquad\text{(13.10)}
```

where $`\sigma`$ is the first line of (13.9) with $`V_i\psi_P\to\hat r\psi_P`$. There is no term $`\propto\lambda^2`$: the first-order relative velocity $`\rho_1-\rho_2=\langle\beta\rangle_g+\dot\sigma`$ has no growing part. This holds alike for the common gradient and for $`g_1\neq g_2`$.
2. Bounded case (sufficient condition). Let $`W(-r)^{*}=W(r)`$ for all $`r`$ (complex conjugate of the matrix in the branch basis); every diagonal on-site binding has this property. The antiunitary $`(\Theta\psi)(r):=\psi(-r)^{*}`$ then commutes with $`H(P)`$ for every $`P`$ and $`\eta`$ ($`\Theta S\Theta^{-1}=S^\dagger`$ in (11.1)) and with $`\mathcal K`$, and $`\Theta\hat r\Theta^{-1}=-\hat r`$. For a simple level $`\Theta\psi_P=e^{i\phi}\psi_P`$, hence $`\langle\hat r\rangle_P=0`$ for all $`P`$ and $`\langle\hat r\psi_P\vert R_P\vert\mathcal K\psi_P\rangle\in i\mathbb R`$. So $`\beta\equiv0`$, and the first-order change of the separation is $`\sigma(\lambda)`$: bounded for all $`\lambda\ge0`$, for all values of the gradients.
3. Vanishing case (sufficient condition). Let $`\tau_1=\tau_2`$, $`M_1=M_2`$, $`W(-r)=\mathsf S\,W(r)\,\mathsf S`$ with $`\mathsf S`$ the exchange of the two branch labels, and $`g_1=g_2`$ (any $`\kappa\langle X\rangle`$). The exchange $`\Sigma`$ of the labels of the two bodies then commutes with $`C_{\rm bod}`$ and with the joint shift, $`\Sigma\Phi_g=\pm\Phi_g`$ (simple level) and $`\Sigma\hat r\Sigma=-\hat r`$. Hence $`\bar m_1-\bar m_2=0`$ for all $`\lambda`$, to all orders in the gradients.
4. Otherwise. For a binding without the property of 2, $`\beta`$ need not vanish: for the numerical control (`code/v3/pair_fall_check.py`, set S5) $`\langle\beta\rangle_g\neq0`$ for each of the three gradients, and the first-order separation grows linearly in $`\lambda`$: the internal structure of the level follows the first-order change $`-\lambda\langle\mathcal K\rangle_P`$ of the total label. This rests on that numerical control, not on an analytic example. With the property of 2 and without the conditions of 3 the change is bounded and need not vanish (same file, sets S1–S4 except S1 with the common or the plain gradient: it relaxes to a non-zero value).

### Step 5. Drift acceleration (items 2c, 2d)

1. The first-order acceleration is $`a^{(1)}_i=\mathrm dv^{(1)}_i/\mathrm d\lambda=\langle\alpha\rangle_g+\dot\rho_i(\lambda)`$; $`\dot\rho_i`$ is bounded for every packet of the class. It is not shown to be small, and its decay for $`\lambda\to\infty`$ is neither derived nor excluded; in the numerical sets it is not negligible over the range of $`\lambda`$ used (section "Code": on half of the range the mean rates deviate from $`\langle\alpha\rangle_g`$ by up to $`1.2\cdot10^{-2}`$). Its window average is a difference quotient of the velocity, exactly: $`\overline{a^{(1)}_i}=\langle\alpha\rangle_g+[\rho_i(\lambda_1+\Lambda)-\rho_i(\lambda_1)]/\Lambda`$, so $`\lvert\overline{a^{(1)}_i}-\langle\alpha\rangle_g\rvert\le2\tau_i\mathsf B_g/\Lambda`$ for all $`\lambda_1\ge0`$, $`\Lambda>0`$.
2. Sharp total label. Class of sequences $`\mathcal S(P_0,I)`$: packets of $`\mathcal G(\mathcal P_0)`$ with supports in one compact interval $`I\subset\mathcal P_0`$, mean $`P_0`$ and $`\delta P\to0`$. Taylor's formula with $`\int(P-P_0)\lvert g\rvert^2=0`$ gives $`\lvert\langle\alpha\rangle_g-\alpha(P_0)\rvert\le\frac12\max_I\lvert\alpha''\rvert\,\delta P^2`$. Hence, with the window first and the sharp label second, for both parts:

```math
\boxed{\;a^{\rm drift}(P_0):=\lim_{\delta P\to0}\,\lim_{\Lambda\to\infty}\overline{a^{(1)}_i}=g_1\,\alpha_1(P_0)+g_2\,\alpha_2(P_0)+\kappa\langle X\rangle\,\alpha_X(P_0)\;},\qquad \alpha_i=-M_i\Bigl[E_b''\,\frac{\partial E_b}{\partial M_i}-E_b'\,\frac{\partial E_b'}{\partial M_i}\Bigr],\quad\alpha_X=-2E_b'' .
\qquad\text{(13.11)}
```

Here $`E_b'=\langle V_i\rangle_P`$ (11.7), $`\partial E_b/\partial M_i=\langle\sigma^{(i)}_3\rangle_P`$ (11.5), and $`E_b''=-\eta^2\langle A_1\rangle_P-(1-\eta)^2\langle A_2\rangle_P-2\mathcal S_\eta(P)`$ (11.9).
3. The other order. At a fixed window the limit $`\delta P\to0`$ does not exist on $`\mathcal S(P_0,I)`$ for every member of the class of item 2 and every window with $`\mathsf f_i\neq0`$, where $`\mathsf f_i`$ is defined in this item. The joint shift by $`n`$ labels, $`g\to g\,e^{-inP}`$, maps the class to itself with the same $`\lvert g\rvert^2`$. In (13.9) only the term with $`g'`$ changes: $`\rho_i\to\rho_i-2n\,\mathrm{Re}\langle F_{i,\lambda}\rangle_g`$ with $`F_{i,\lambda}(P):=\langle V_i\psi_P\vert R_P\,\mathcal U_P(\lambda)\vert\mathcal K\psi_P\rangle`$. The window averages of a sequence and of its shifted copy therefore differ by $`-\frac{2n}{\Lambda}\mathrm{Re}\langle F_{i,\lambda_1+\Lambda}-F_{i,\lambda_1}\rangle_g`$, which tends to $`-2n\,\mathsf f_i/\Lambda`$ with $`\mathsf f_i:=\mathrm{Re}\bigl[F_{i,\lambda_1+\Lambda}(P_0)-F_{i,\lambda_1}(P_0)\bigr]`$. For $`\mathsf f_i\neq0`$ two sequences that differ by a fixed shift have different limits, and a sequence shifted by $`n\to\infty`$ has none. On a subclass on which the limit exists it defines the window average of the first-order acceleration of a start with a sharp total label. For $`\mathsf f_i\neq0`$ that quantity depends on the place of the packet and, through $`\mathsf f_i`$, on the window and on the part, so it is not a property of the level; whether it tends to $`\alpha(P_0)`$ for $`\Lambda\to\infty`$ is not derived.
   - Answer to item 2(c) as amended. With the window first, both limits exist for every sequence of the class and give (13.11) (items 1 and 2). With the sharp total label first, the limit at a fixed window fails to exist for some sequences of the class whenever $`\mathsf f_i\neq0`$ for that window. Hence the two limits do not commute on $`\mathcal S(P_0,I)`$ for every member of the class of item 2 that has windows with $`\mathsf f_i\neq0`$ and arbitrarily large $`\Lambda`$: for it the other order is not defined on the class. The statement is conditional. The next two bullets give a sufficient condition and members that satisfy it; for the members of the fourth bullet nothing is decided.
   - What is shown for the other order. For a window with $`\mathsf f_i\neq0`$ the limit $`\delta P\to0`$ does not exist on the class; on a subclass on which it exists, its value depends on the place of the packet (the shift $`n`$). A sufficient condition for windows $`[0,\Lambda]`$ with $`\mathsf f_i\neq0`$ and arbitrarily large $`\Lambda`$ is $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$: for $`\lambda_1=0`$, $`\mathsf f_i=\mathrm{Re}\,F_{i,\Lambda}(P_0)`$; the mean of $`e^{-i(H(P_0)-E_b(P_0))\Lambda}`$ over $`\Lambda\in[0,T]`$ tends to zero on $`Q_{P_0}\mathfrak h`$ for $`T\to\infty`$ (mean ergodic theorem, simple level), so the mean of $`\mathsf f_i`$ tends to $`\mathrm{Re}\langle V_i\psi_{P_0}\vert R_{P_0}\vert\mathcal K\psi_{P_0}\rangle=-\tfrac12\partial_P\langle\mathcal K\rangle_{P_0}`$ by (13.6).
   - Members with $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$. They are numerical, from the numerical bound level of the script (table "other order" of `code/v3/pair_fall_check.py`, section "Code"); no analytic member is given. Here $`\partial_P\langle\mathcal K\rangle_P=g_1M_1\,\partial_P\langle\sigma^{(1)}_3\rangle_P+g_2M_2\,\partial_P\langle\sigma^{(2)}_3\rangle_P`$.
     - The control set S5 (binding of range 1 without symmetry) at $`P_0=0.2`$, the total label of its evolution: $`\partial_P\langle\sigma^{(1)}_3\rangle_{P_0}=-3.28\cdot10^{-2}`$ and $`\partial_P\langle\sigma^{(2)}_3\rangle_{P_0}=-3.89\cdot10^{-2}`$, so $`\partial_P\langle\mathcal K\rangle_{P_0}=-7.94\cdot10^{-2}\,g_{\rm c}`$ for the common gradient and $`-3.28\cdot10^{-2}\,g_1`$ for $`g_1`$ only. Directly, for the window $`[0,20]`$ and the common gradient: $`\mathsf f_1=1.20\cdot10^{-2}\,g_{\rm c}`$ and $`\mathsf f_2=-6.28\cdot10^{-2}\,g_{\rm c}`$.
     - The sets S1–S4 (diagonal on-site bindings) at $`P_0=0.2`$: $`\partial_P\langle\sigma^{(1)}_3\rangle_{P_0}=-2.10\cdot10^{-3}`$, $`-1.49\cdot10^{-3}`$, $`+1.66\cdot10^{-3}`$, $`-2.40\cdot10^{-2}`$, and $`\mathsf f_1\neq0`$, $`\mathsf f_2\neq0`$ for the three windows of the table, for the common gradient and for $`g_1`$ only.
     - The numbers change by less than $`3\cdot10^{-15}`$ with the range of the fibre and agree with a symmetric difference in $`P`$ to $`2\cdot10^{-10}`$. For these members the two limits do not commute; this is shown numerically, and for these members only.
   - Exceptional members, for which nothing is shown: windows with $`\mathsf f_i=0`$. This is every window if $`g_1=g_2=0`$ (then $`R_P\mathcal K\psi_P=0`$), and every window at $`P_0=0`$ if $`\mathcal R`$ of Step 6.1 commutes with $`H(0)`$: then $`\mathcal R\psi_0=\pm\psi_0`$, $`\mathcal RV_i(0)\mathcal R^{-1}=-V_i(0)`$ and $`[\mathcal R,\mathcal K]=0`$ give $`F_{i,\lambda}(0)=0`$. The second case contains every diagonal on-site binding, hence the levels of items 3 and 4 (numerically, for S1–S4 at $`P_0=0`$: $`\lvert\mathsf f_i\rvert\le1.5\cdot10^{-15}`$).
   - The evaluation of the other order is not asked (item 2(c) of the question) and is not given.
4. What multiplies the gradients. $`E_b''(P_0)`$ multiplies all three, but it is the whole coefficient only for $`\kappa\langle X\rangle`$: $`\alpha_X=-2E_b''`$, exactly, on the whole class. For $`g_i`$ it is weighted by $`M_i\,\partial E_b/\partial M_i=M_i\langle\sigma^{(i)}_3\rangle_{P_0}`$, and for $`E_b'(P_0)\neq0`$ the term $`M_iE_b'\,\partial E_b'/\partial M_i`$ enters in addition. Exceptional members:
   - $`E_b''(P_0)=0`$: $`\alpha_X=0`$, $`\alpha_i=M_iE_b'\,\partial E_b'/\partial M_i`$; at $`P_0=0`$ the inertia $`\mathfrak m_b`$ is not defined.
   - $`E_b'(P_0)=0`$: $`\alpha_i=-M_iE_b''\langle\sigma^{(i)}_3\rangle_{P_0}`$; at $`P_0=0`$ then, for $`E_b''(0)\neq0`$, $`a^{\rm drift}(0)=-\langle\mathcal K\rangle_0/\mathfrak m_b`$. The class does not imply $`E_b'(0)=0`$: the numerical level of the set S5 has $`E_b'(0)=-1.17\cdot10^{-4}`$ (section "Code"; a numerical member, not an analytic one). A sufficient condition for $`E_b'(0)=0`$ is $`W(-r)=\sigma^{(1)}_3\sigma^{(2)}_3W(r)\sigma^{(1)}_3\sigma^{(2)}_3`$ together with a level that the map $`P\to-P`$ takes to itself.
   - $`\partial E_b'/\partial M_i=\partial_P\langle\sigma^{(i)}_3\rangle_{P_0}=0`$: the additional term of $`\alpha_i`$ vanishes also for $`E_b'(P_0)\neq0`$.
   - $`\langle\sigma^{(i)}_3\rangle_{P_0}=0`$: the first term of $`\alpha_i`$ vanishes.
5. Common gradient (item 2d). With (11.6),

```math
\alpha_1+\alpha_2=-E_b''\,\mathcal M_P+E_b'\,\mathcal M_P',\qquad
\mathcal M_P:=M_1\langle\sigma^{(1)}_3\rangle_P+M_2\langle\sigma^{(2)}_3\rangle_P=E_b(P)-\langle A_1\rangle_P-\langle A_2\rangle_P-\langle U\rangle_P .
\qquad\text{(13.12)}
```

Of the five terms of the scaling relation only the two rest terms enter the coefficient of $`g_{\rm c}`$, through $`\mathcal M_P`$ and its derivative, next to the factors $`E_b''`$ and $`E_b'`$. The motion terms $`\langle A_i\rangle_P`$ and the binding term $`\langle U\rangle_P`$, which the field does not multiply, do not enter $`\mathcal M_P`$; $`\mathcal M_P=E_b(P)`$ iff $`\langle A_1\rangle_P+\langle A_2\rangle_P+\langle U\rangle_P=0`$.

### Step 6. Diagonal on-site binding in the regime $`\mathsf R`$ (item 3)

Class: every diagonal on-site binding with $`\hat w_{11}\neq0`$, the level (11.12), fixed hatted data, $`P_0=0`$.

1. At rest. $`(\mathcal R\psi)(r):=\sigma^{(1)}_3\sigma^{(2)}_3\psi(-r)`$ gives $`\mathcal RH(P)\mathcal R^{-1}=H(-P)`$ for a diagonal on-site binding, and by (11.12) the level near $`\mathcal B_{++}`$ is the only one for small $`\epsilon`$. So $`E_b(-P)=E_b(P)`$ and $`E_b'(0)=0`$, exactly. By (11.8), without gradients $`\mathrm d\bar m_i/\mathrm d\lambda=\langle E_b'\rangle_g=O(\delta P^2)`$ for all $`\lambda`$ (zero for even $`\lvert g\rvert^2`$): the pair is at rest in the sharp-total-label limit.
2. Closed form. (13.11) at $`P_0=0`$ is $`a_{\rm pair}:=a^{\rm drift}(0)=-E_b''(0)\bigl[g_1M_1\langle\sigma^{(1)}_3\rangle_0+g_2M_2\langle\sigma^{(2)}_3\rangle_0+2\kappa\langle X\rangle\bigr]`$, exactly. With (11.14) and (11.16):

```math
\boxed{\;a_{\rm pair}=\frac{\varsigma}{\sqrt{1+u^2}}\;\frac{g_1M_1(1+r_1)+g_2M_2(1+r_2)+2\kappa\langle X\rangle(1+r_X)}{\mathfrak m_1+\mathfrak m_2}\;},\qquad r_1,r_2,r_X=O(\epsilon^2)\ \text{at fixed }u .
\qquad\text{(13.13)}
```

With the curvature inertia $`\mathfrak m_b=1/E_b''(0)`$, which is defined for small $`\epsilon`$ ($`E_b''(0)\neq0`$ by (11.14)), the first line of this item is the exact form $`a_{\rm pair}=-\langle\mathcal K\rangle_0/\mathfrak m_b`$. At leading order in $`\mathsf R`$ it reads $`a_{\rm pair}=-(g_1M_1+g_2M_2+2\kappa\langle X\rangle)/\mathfrak m_b`$: with the exact $`\mathfrak m_b`$ the coefficient of $`\kappa\langle X\rangle`$ is exact, and the coefficient of $`g_i`$ carries the relative remainder $`\langle\sigma^{(i)}_3\rangle_0-1=-\frac{a_i}{M_i}\Lambda+O(\epsilon^4)`$. Since $`\mathfrak m_ia^{(i)}=-(g_iM_i+\kappa\langle X\rangle)`$, at leading order $`a_{\rm pair}=-\varsigma(1+u^2)^{-1/2}\,\bar a`$ with the inertia-weighted mean $`\bar a:=(\mathfrak m_1a^{(1)}+\mathfrak m_2a^{(2)})/(\mathfrak m_1+\mathfrak m_2)`$ of the free falls. Each coefficient is of order $`\epsilon^2`$; the remainders are not uniform in $`u`$.
3. Ordered limits of the leading coefficient (first $`\epsilon\to0`$ at fixed $`u`$, then $`u`$; the limit in $`u`$ is taken through the binding $`\hat w_{11}`$, at fixed $`\hat\tau_i`$, $`M_i`$ and gradients):

```math
u\to0:\ \ a_{\rm pair}\to-\varsigma\,\bar a\,\bigl[1-\tfrac12u^2+O(u^4)\bigr];\qquad
u\to\infty:\ \ a_{\rm pair}\to-\varsigma\,\frac{\bar a}{u}\,\bigl[1+O(u^{-2})\bigr]\to0 .
\qquad\text{(13.14)}
```

For $`w_{11}<0`$ the wide pair falls with $`\bar a`$: the sum of the weights $`g_iM_i+\kappa\langle X\rangle`$ over the sum of the inertias. For $`w_{11}>0`$ the level lies above the band, $`\mathfrak m_b<0`$, and the pair accelerates opposite to $`\bar a`$ at every $`u`$; by (4.7) its wide form $`-\bar a`$ is, at leading order, the same mean of the drift accelerations of the free parts at $`p=\pi/2`$ instead of at rest. A tight pair does not fall at this order: its inertia grows like $`u`$, its weight does not.
4. Ratios for $`\langle X\rangle=0`$ (item 3b), where $`a^{(i)}=-\tau_i^2g_i`$ and $`g_i\neq0`$:

```math
\frac{a_{\rm pair}}{a^{(i)}}=-\frac{\varsigma}{\sqrt{1+u^2}}\cdot\frac{g_1M_1+g_2M_2}{g_i\,\tau_i^2\,(\mathfrak m_1+\mathfrak m_2)}\,\bigl(1+O(\epsilon^2)\bigr),\qquad
\tau_{\rm p}^2:=\frac{M_1+M_2}{M_1/\tau_1^2+M_2/\tau_2^2}.
\qquad\text{(13.15)}
```

The factor $`1+O(\epsilon^2)`$ holds at a fixed ratio $`g_1:g_2`$ with $`g_1M_1+g_2M_2\neq0`$. For $`g_1=g_2=0`$ neither the pair nor a part falls, and no ratio is defined; the three cases have at least one non-zero gradient.
   - Common gradient, $`\tau_1=\tau_2`$ (the free parts fall alike): both ratios are $`-\varsigma/\sqrt{1+u^2}`$. For $`w_{11}<0`$ this is $`<1`$ at every fixed $`u`$. The pair falls like its parts neither exactly nor to any order in $`\epsilon`$ (the difference is of order $`\epsilon^0`$), but only in the ordered wide-pair limit, with the leading difference $`-\tfrac12u^2`$. For $`w_{11}>0`$: not at all (the ratio is $`-(1+u^2)^{-1/2}<0`$ at every $`u`$; it tends to $`-1`$ in the wide limit).
   - Common gradient, $`\tau_1\neq\tau_2`$ (the free parts differ, $`a^{(1)}/a^{(2)}=\tau_1^2/\tau_2^2`$): the ratios are $`-\varsigma(1+u^2)^{-1/2}\tau_{\rm p}^2/\tau_i^2`$, with $`\tau_{\rm p}^2`$ strictly between $`\tau_1^2`$ and $`\tau_2^2`$. The pair falls like both of its parts at no $`u`$ and in no limit. In the wide limit ($`w_{11}<0`$) the ratio differs from $`1`$ by $`M_j(\tau_j^2-\tau_i^2)/(M_i\tau_j^2+M_j\tau_i^2)`$, $`j\neq i`$. Exceptional: for the part with the smaller $`\tau_i`$ and $`w_{11}<0`$ the ratio is $`1`$, at leading order in $`\mathsf R`$, at the single value $`u_*=(\tau_{\rm p}^4/\tau_i^4-1)^{1/2}`$; this is the member (13.23) for $`g_1=g_2`$.
   - $`g_1\neq g_2`$: $`a_{\rm pair}=-\varsigma(1+u^2)^{-1/2}\bar a`$. If $`\tau_1^2g_1=\tau_2^2g_2`$ the free parts fall alike and the first case applies. Otherwise $`a^{(1)}\neq a^{(2)}`$, and the pair falls like both of its parts at no $`u`$ and in no limit: in the wide limit ($`w_{11}<0`$) $`a_{\rm pair}-a^{(1)}\to\mathfrak m_2(a^{(2)}-a^{(1)})/(\mathfrak m_1+\mathfrak m_2)`$. Exceptional members:
     - $`g_1M_1+g_2M_2=0`$: no fall at this order.
     - One part only. By (13.15), for $`g_i\neq0`$ and $`j\neq i`$, at leading order in $`\mathsf R`$,

```math
\frac{a_{\rm pair}}{a^{(i)}}=1\iff\frac{g_j}{g_i}=\mathsf z_i(u):=-\,\frac{M_i+\varsigma\sqrt{1+u^2}\;\tau_i^2\,(\mathfrak m_1+\mathfrak m_2)}{M_j},\qquad \tau_i^2\,(\mathfrak m_1+\mathfrak m_2)=M_i+M_j\,\frac{\tau_i^2}{\tau_j^2}.
\qquad\text{(13.23)}
```

   For given data and $`u`$ this is one value of $`g_j/g_i`$, for both signs of $`w_{11}`$. For $`w_{11}<0`$, $`\mathsf z_i(u)>\tau_i^2/\tau_j^2`$, and it tends to $`\tau_i^2/\tau_j^2`$, the first case, for $`u\to0`$. For $`w_{11}>0`$, $`\mathsf z_i(u)<-(2M_i+M_j\tau_i^2/\tau_j^2)/M_j<0`$: the two gradients have opposite signs. On this member $`a_{\rm pair}=a^{(i)}\neq a^{(j)}`$, because $`\mathsf z_i(u)\neq\tau_i^2/\tau_j^2`$ for $`u>0`$: it concerns one part only. The exact ratio $`a_{\rm pair}/a^{(i)}`$ is affine in $`g_j/g_i`$ with a non-zero slope, so the exact member is one value as well, $`\mathsf z_i(u)\,(1+O(\epsilon^2))`$.
5. Clock levels (item 3c). With $`u=4\lvert w\rvert\mathfrak m_1\mathfrak m_2/(\mathfrak m_1+\mathfrak m_2)`$, (13.13) reads

```math
a_{\rm pair}=\varsigma\,\frac{g_1M_1+g_2M_2+2\kappa\langle X\rangle}{\sqrt{(\mathfrak m_1+\mathfrak m_2)^2+16\,w^2\,\mathfrak m_1^2\mathfrak m_2^2}}\,\bigl(1+O(\epsilon^2)\bigr),\qquad \mathfrak m_i=\frac{M^{(i)}_{k_i}}{\tau_i^2}.
\qquad\text{(13.16)}
```

   - Claim: at a fixed binding $`w_{11}\neq0`$ the leading coefficient is the same for all $`N_1N_2`$ pairs of levels iff $`g_1=g_2=0`$ and $`\kappa\langle X\rangle=0`$. Proof: call the numerator $`\mathsf N`$ and the root $`h`$. If $`\mathsf N=\varsigma c\,h`$ on four pairs $`\{M_1,M_1'\}\times\{M_2,M_2'\}`$ ($`N_i\ge2`$), take the mixed second difference. It is $`0`$ for $`\mathsf N`$ and strictly positive for $`h`$, because $`4h^3\,\partial_{\mathfrak m_1}\partial_{\mathfrak m_2}h=4q\bigl[(\mathfrak m_1+\mathfrak m_2)^2+(1+q)\mathfrak m_1\mathfrak m_2\bigr]>0`$ with $`q:=16w^2\mathfrak m_1\mathfrak m_2`$. So $`c=0`$, $`\mathsf N=0`$ on the four pairs, and all three gradients vanish.
   - Hence: for $`\langle X\rangle=0`$ iff $`g_1=g_2=0`$ (no fall); for $`\langle X\rangle\neq0`$ never.
   - Leading dependence (for $`\mathsf N\neq0`$): $`\partial\ln a_{\rm pair}/\partial\ln M_i=g_iM_i/\mathsf N-\mathfrak m_i/(\mathfrak m_1+\mathfrak m_2)-\frac{u^2}{1+u^2}\frac{a_i}{a}`$. For the common gradient with $`\tau_1=\tau_2=\tau`$ and $`\langle X\rangle=0`$ only the last term remains: $`a_{\rm pair}=\varsigma g_{\rm c}\tau^2/\sqrt{1+u^2}`$ with $`u=\frac{4\lvert w\rvert}{\tau^2}\frac{M_1M_2}{M_1+M_2}`$.
   - In the ordered wide-pair limit the leading coefficient $`\varsigma\mathsf N/(\mathfrak m_1+\mathfrak m_2)`$ is the same for all levels iff $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$ (two affine functions of $`M_1,M_2`$ that agree on the four pairs).
   - Comparison: a free part falls alike on all levels iff $`\langle X\rangle=0`$ (4.16). The pair with a non-zero fall does not, at any fixed binding $`w_{11}\neq0`$ (hence at any fixed $`u`$), because the binding $`w`$ does not scale with the levels while $`a`$ does. In the ordered wide-pair limit it does iff $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$ (previous bullet). Without a fall (all three gradients zero) the fall is the same for all levels trivially, for the pair and for its parts.
6. $`\langle X\rangle\neq0`$ (item 3d). It adds $`-2\kappa\langle X\rangle E_b''(P_0)`$ to the drift acceleration, exactly and on the whole class of item 2 (13.8). At $`P_0=0`$ this is $`-2\kappa\langle X\rangle/\mathfrak m_b`$, in $`\mathsf R`$ equal at leading order to $`\frac{\varsigma}{\sqrt{1+u^2}}\frac{2\kappa\langle X\rangle}{\mathfrak m_1+\mathfrak m_2}`$. For a free part it adds $`-\kappa\langle X\rangle/\mathfrak m_i`$ (4.16). In both cases the plain gradient enters as the sum of the plain gradients over the curvature inertia, without a factor $`\langle\sigma_3\rangle`$, and it makes the fall depend on the levels. For the pair it is in addition reduced by $`(1+u^2)^{-1/2}`$ against the inertia-weighted mean, and reversed for $`w_{11}>0`$.

### Step 7. Fall and the clocks of the parts (item 4)

Class as in Step 6, with $`\langle X\rangle=0`$. Two sets of data meet in this step (Setup): $`a_{\rm pair}`$ is taken with the level data, the rate of the clock of the part $`i`$ with the clock data of the part $`i`$.

1. Rate (item 4a). At the label $`x_0`$ put $`n_i:=1+g_ix_0>0`$. The operator $`(1+g_ix_0)G_i`$ is the rest and clock operator of Model D with $`m_i\to n_im_i`$ and $`\lambda_{0,i}\to\lambda_{0,i}/n_i`$, hence $`M^{(i)}_k\to n_iM^{(i)}_k`$ and $`\bar M_i\to n_i\bar M_i`$. The zeroth order in the gradients is the pair without gradients and with these data. It is invariant under the joint shift, so (11.19) applies to a packet placed at $`x_0`$: the reading of the clock label of the part $`i`$ is $`P_{N_i}(a;\vartheta_i)+\mathcal R_i`$ with the advance $`\vartheta_i=\Gamma_i(x_0)\,n_i\lambda/\lambda_{0,i}`$. The rate is $`\mathrm d\vartheta_i/\mathrm d\lambda`$. With (11.20):

```math
\begin{aligned}
r_i(x_0)&=\frac{1+g_ix_0}{\lambda_{0,i}}\;\Gamma_i(x_0),\qquad \Gamma_i(x_0)=1-\frac{\tau_i^2}{4\,n_i^2\bar M_i^2}\,\Lambda(x_0)+O(\epsilon^4),\\
\Lambda(x_0)&=1+\frac{\varsigma}{\sqrt{1+u(x_0)^2}},\qquad u(x_0)=\frac{\lvert w\rvert}{a_1/n_1+a_2/n_2}
\end{aligned}
\qquad\text{(13.17)}
```

Here $`a_1`$, $`a_2`$, $`u`$, $`\Lambda`$ are those of the clock data of the part $`i`$ ($`a_i`$ with $`\bar M_i`$ for the part that is read and $`M_j`$ for the other part): $`u(0)=u_{[i]}`$ and $`\Lambda(0)=\Lambda_{[i]}`$, not $`u`$ and $`\Lambda`$ of (13.13).
   - Conditions, from (11.19): the clock of the part $`i`$ starts in $`\lvert0\rangle`$; the other part is on its level; the positions and branches are in a packet of the bound level of the data at $`x_0`$ with mean total label $`0`$ and spread $`\delta P`$; leading order in $`\kappa`$.
   - Range of $`\lambda`$: $`\mathcal R_i`$ is small for $`\lambda\ll\lambda_{0,i}/\delta_i`$ (in $`\mathsf R`$ with $`\delta_i\to D_i/M_i`$) and $`\delta P^2(1+\lambda/\lambda_{0,i})\ll1`$.
   - As a statement on the pair in the field, (13.17) is the zeroth order in $`(\lvert g_1\rvert+\lvert g_2\rvert)\,s`$, where $`s\gtrsim1/(2\delta P)`$ is the width of the packet in labels. The first-order corrections to the reading are not derived here.
2. Relative change per label, to first order in the gradients ($`\varrho_i=\partial_{x_0}\ln r_i`$ at $`x_0=0`$):

```math
\varrho_i=g_i+\frac{\tau_i^2}{4\bar M_i^2}\Bigl[2\Lambda\,g_i+\frac{\varsigma\,u^2}{(1+u^2)^{3/2}}\,\frac{g_1a_1+g_2a_2}{a}\Bigr]+O(\epsilon^4)\,(\lvert g_1\rvert+\lvert g_2\rvert) .
\qquad\text{(13.18)}
```

In (13.18), as in (13.17), $`a_1`$, $`a_2`$, $`a`$, $`u`$, $`\Lambda`$ are those of the clock data of the part $`i`$ and carry the label $`[i]`$ wherever they meet the level data. At leading order $`\varrho_i=g_i`$, as for the free part. The term of order $`\epsilon^2`$ contains the gradient of the other part. Both are derived as follows.
   - Derivative used. $`\Gamma_i=\partial E_b(0)/\partial M_i`$, exactly, by (11.19) with (11.5), and at the label $`x_0`$ the data are $`n_1M_1`$, $`n_2M_2`$ with $`\tau_1`$, $`\tau_2`$ and $`W`$ unchanged (item 1). The rate is $`r_i=n_i\Gamma_i/\lambda_{0,i}`$, so its change with $`x_0`$ is the derivative of a known function of the data, not of an estimate. To first order in the gradients, without the expansion in $`\mathsf R`$ (with $`M_i=\bar M_i`$ for the part that is read, as in (13.17)):

```math
\varrho_i=g_i+\frac1{\Gamma_i}\sum_{j=1,2}g_j\,M_j\,\frac{\partial^2E_b(0)}{\partial M_j\,\partial M_i} .
\qquad\text{(13.21)}
```

   This uses the second derivatives of the level at $`P=0`$ in the rest costs $`M_1`$, $`M_2`$: one derivative in the data more than (11.14) and (11.20). A derivative of the remainder of (11.20) is thereby reduced to (11.12): that remainder is $`\partial/\partial M_i`$ of the remainder of (11.12).
   - Regime $`\mathsf R`$. (11.12) at $`P=0`$ is $`E_b(0)=M_1+M_2+\mathsf e(a)+\mathcal E`$ with $`\mathsf e(a):=a+\varsigma\sqrt{w^2+a^2}`$ and the remainder $`\mathcal E=O(\epsilon^4)`$. With $`\partial a/\partial M_j=-a_j/M_j`$, $`\mathsf e'=\Lambda`$ and $`\mathsf e''=\varsigma u^2/\bigl(a(1+u^2)^{3/2}\bigr)`$, for $`i,j=1,2`$:

```math
\frac{\partial^2E_b(0)}{\partial M_j\,\partial M_i}=\delta_{ij}\,\frac{2a_i}{M_i^2}\,\Lambda+\frac{a_i\,a_j}{M_iM_j}\cdot\frac{\varsigma\,u^2}{a\,(1+u^2)^{3/2}}+\frac{\partial^2\mathcal E}{\partial M_j\,\partial M_i},\qquad \frac{\partial^2\mathcal E}{\partial M_j\,\partial M_i}=O(\epsilon^4)\ \text{at fixed }u .
\qquad\text{(13.22)}
```

   The two explicit terms are of order $`\epsilon^2`$.
   - Remainder of (13.22). The statement of Step 8 of 11-bound-pair, quoted with (11.14): "$`E_b`$ is analytic in the data with a remainder bounded uniformly near real data, so (11.12) can be differentiated and the remainders stay $`O(\epsilon^4)`$." It is read here as: $`\mathcal E`$ is analytic in the data and $`\lvert\mathcal E\rvert\le c\,\epsilon^4`$ on a complex neighbourhood of the real data whose size does not depend on $`\epsilon`$. $`M_1`$ and $`M_2`$ are data that are fixed in $`\mathsf R`$, so Cauchy's estimate on a polydisc of radius $`\delta`$ in $`(M_1,M_2)`$ inside that neighbourhood gives $`\lvert\partial_{M_j}\partial_{M_i}\mathcal E\rvert\le2c\,\epsilon^4/\delta^2`$. In 11-bound-pair the statement serves the first derivatives in the data that give (11.14); for the second derivatives used here it is its premise that carries the estimate.
   - Result. Insert (13.22) in (13.21), with $`1/\Gamma_i=1+O(\epsilon^2)`$ by (11.20) and $`a_i/M_i=\tau_i^2/(4\bar M_i^2)`$ for the part that is read: this is (13.18). Its leading order, $`\varrho_i=g_i+O(\epsilon^2)(\lvert g_1\rvert+\lvert g_2\rvert)`$, uses only that the second derivatives (13.22) are of order $`\epsilon^2`$; its term of order $`\epsilon^2`$ uses their values, with the remainder $`O(\epsilon^4)`$. No assumption on a remainder is made. Numerical check of (13.22) and of the term of order $`\epsilon^2`$: section "Code".
3. The number $`\mathsf w_i^2`$ (item 4b). In this item $`u`$, $`\mathfrak m_i`$, $`\tau_{\rm p}`$ are those of the level data and come from $`a_{\rm pair}`$ (13.13); $`u_{[i]}`$, $`a_{[i]}`$ are those of the clock data of the part $`i`$ and come from $`\varrho_i`$ (13.18); $`j\neq i`$ is the other part. By (13.21), (13.22), $`\varrho_i`$ is linear in the two gradients:

```math
\varrho_i=g_i\,\bigl(1+O(\epsilon^2)\bigr)+\nu_i\,g_j\,\bigl(1+O(\epsilon^2)\bigr),\qquad \nu_i:=\frac{\tau_i^2}{4\bar M_i^2}\cdot\frac{\varsigma\,u_{[i]}^2}{(1+u_{[i]}^2)^{3/2}}\cdot\frac{a_j}{a_{[i]}} .
\qquad\text{(13.24)}
```

$`\nu_i`$ is the coefficient of the gradient of the other part in (13.18): of order $`\epsilon^2`$, non-zero, with the sign of $`w_{11}`$. The two factors $`1+O(\epsilon^2)`$ depend on the data, not on the gradients. $`\mathsf w_i^2`$ is defined where $`\varrho_i\neq0`$:
   - at a fixed ratio $`g_1:g_2`$ with $`g_i\neq0`$, for small $`\epsilon`$: there $`\varrho_i=g_i(1+O(\epsilon^2))\neq0`$, and (13.19) holds;
   - for $`g_i=0\neq g_j`$: there $`\varrho_i=\nu_i\,g_j\,(1+O(\epsilon^2))\neq0`$, and (13.25) holds;
   - not on the member $`\varrho_i=0`$ with $`g_j\neq0`$. By (13.24) it is the single ratio $`g_i/g_j=-\nu_i\,(1+O(\epsilon^2))`$: of order $`\epsilon^2`$, with the sign opposite to that of $`w_{11}`$. There $`a_{\rm pair}\neq0`$ by (13.13), and $`\lvert\mathsf w_i^2\rvert\to\infty`$ as the ratio is approached;
   - not for $`g_1=g_2=0`$, where $`\varrho_i=0`$ and $`a_{\rm pair}=0`$.

   For $`g_i\neq0`$ at a fixed ratio $`g_1:g_2`$:

```math
\mathsf w_i^2:=-\frac{a_{\rm pair}}{\varrho_i}=-\frac{\varsigma}{\sqrt{1+u^2}}\cdot\frac{g_1M_1+g_2M_2}{g_i\,(\mathfrak m_1+\mathfrak m_2)}\,\bigl(1+O(\epsilon^2)\bigr)\qquad\Bigl[\,=-\frac{\varsigma\,\tau_{\rm p}^2}{\sqrt{1+u^2}}\,\bigl(1+O(\epsilon^2)\bigr)\ \text{for } g_1=g_2\Bigr].
\qquad\text{(13.19)}
```

   - Range of (13.19). The factor $`1+O(\epsilon^2)`$ holds uniformly on every set of ratios with $`\lvert g_i\rvert\ge c\,\lvert g_j\rvert`$ and $`\lvert g_1M_1+g_2M_2\rvert\ge c\,(\lvert g_1\rvert M_1+\lvert g_2\rvert M_2)`$, with $`c>0`$ independent of $`\epsilon`$ ($`g_j=0`$ included). For smaller $`\lvert g_i/g_j\rvert`$ the right-hand side of (13.19) is to be multiplied by $`(1+\nu_ig_j/g_i)^{-1}`$, by (13.24); the factor $`1+O(\epsilon^2)`$ is then uniform on $`\lvert g_i+\nu_ig_j\rvert\ge c\,(\lvert g_i\rvert+\lvert\nu_ig_j\rvert)`$. The additional factor is $`1+O(\epsilon^2g_j/g_i)`$ for $`\lvert g_i/g_j\rvert\gg\epsilon^2`$, of order one for $`g_i/g_j`$ of order $`\epsilon^2`$, and it has its pole on the member $`\varrho_i=0`$.
   - Equal to $`\tau_i^2`$: no, except on one member. At leading order $`\varrho_i=g_i`$ and $`a^{(i)}=-\tau_i^2g_i`$, so $`\mathsf w_i^2=\tau_i^2`$ iff $`a_{\rm pair}=a^{(i)}`$, i.e. iff $`g_j/g_i=\mathsf z_i(u)`$ of (13.23): one value of the ratio of the gradients at given data and $`u`$, for both signs of $`w_{11}`$. For the common gradient $`\mathsf w_i^2/\tau_i^2=-\varsigma(1+u^2)^{-1/2}\tau_{\rm p}^2/\tau_i^2`$, which is $`\neq1`$ except at $`u_*`$ of Step 6 for one part; for $`w_{11}>0`$ it is negative.
   - The same for $`i=1,2`$: where both numbers are defined, $`\mathsf w_1^2/\mathsf w_2^2=\varrho_2/\varrho_1`$ (exact; both contain the same $`a_{\rm pair}`$), which is $`g_2/g_1`$ at leading order at a fixed ratio with $`g_1,g_2\neq0`$. So: the same at leading order iff $`g_1=g_2`$; exceptional is the member $`a_{\rm pair}=0`$ (at leading order $`g_1M_1+g_2M_2=0`$), where both numbers vanish. For $`g_1=g_2\neq0`$, (13.18) gives at relative order $`\epsilon^2`$

```math
\frac{\mathsf w_1^2}{\mathsf w_2^2}=\frac{\varrho_2}{\varrho_1}=1+\frac{\tau_2^2}{4\bar M_2^2}\,\mathsf y(u_{[2]})-\frac{\tau_1^2}{4\bar M_1^2}\,\mathsf y(u_{[1]})+O(\epsilon^4),\qquad \mathsf y(u):=2+\varsigma\,\frac{2+3u^2}{(1+u^2)^{3/2}} .
\qquad\text{(13.26)}
```

   $`\mathsf y(u)=2\Lambda+\varsigma u^2(1+u^2)^{-3/2}`$ is the bracket of (13.18) for $`g_1=g_2`$, and $`\mathsf y(u)>0`$ for $`u>0`$ and both signs, because $`(2+3u^2)^2<4(1+u^2)^3`$. So the two numbers are the same at relative order $`\epsilon^2`$ iff $`\tau_1^2\,\mathsf y(u_{[1]})/\bar M_1^2=\tau_2^2\,\mathsf y(u_{[2]})/\bar M_2^2`$. This reduces to $`\tau_1/\bar M_1=\tau_2/\bar M_2`$ for the members with $`u_{[1]}=u_{[2]}`$, i.e. $`\tau_1^2\,(1/\bar M_1-1/M_1)=\tau_2^2\,(1/\bar M_2-1/M_2)`$, in particular when each part is on the level with $`M^{(i)}_{k_i}=\bar M_i`$; and in the ordered limits $`u\to\infty`$ (both signs, $`\mathsf y\to2`$) and $`u\to0`$ for $`w_{11}>0`$ ($`\mathsf y\to4`$). For $`w_{11}<0`$ and $`u\to0`$, $`\mathsf y(u)=\tfrac34u^4+O(u^6)`$: both terms of order $`\epsilon^2`$ vanish in the limit.
   - Data of the pair: yes. It contains the binding ($`\varsigma`$, $`u`$) and the clock levels (through $`u`$, and through $`\tau_{\rm p}`$ if $`\tau_1\neq\tau_2`$).
   - The case $`g_i=0\neq g_j`$. The free part $`i`$ then does not fall and its clock rate does not change, so (4.24) is empty for it. In the pair, (13.13) divided by (13.24) gives

```math
\mathsf w_i^2=-\frac{\varsigma}{\sqrt{1+u^2}}\cdot\frac{M_j}{(\mathfrak m_1+\mathfrak m_2)\,\nu_i}\,\bigl(1+O(\epsilon^2)\bigr)=-\,4\,\frac{\bar M_i^2\,M_j}{M_i}\cdot\frac{u\,(1+u_{[i]}^2)^{3/2}}{u_{[i]}^3\,\sqrt{1+u^2}}\,\bigl(1+O(\epsilon^2)\bigr)\qquad(g_i=0\neq g_j),
\qquad\text{(13.25)}
```

   with $`M_i=M^{(i)}_{k_i}`$, $`M_j=M^{(j)}_{k_j}`$; for $`M^{(i)}_{k_i}=\bar M_i`$ it is $`-4M_iM_j(1+u^2)/u^2`$. The second form uses $`M_j/(\mathfrak m_1+\mathfrak m_2)=4a_1a_2M_j/a`$ and $`a_{[i]}/a=u/u_{[i]}`$. It is of order $`\epsilon^0`$, while (13.19) is of order $`\epsilon^2`$; its remainder is a relative $`O(\epsilon^2)`$ at fixed $`u`$, not uniform in $`u`$. The three answers for (13.25):
   - $`g_i=0\neq g_j`$, equal to $`\tau_i^2`$: no, at every fixed $`u`$ and in both ordered limits. It is negative for both signs of $`w_{11}`$, and $`\tau_i^2>0`$ is of order $`\epsilon^2`$. For $`u\to0`$ it grows like $`-u^{-2}`$; for $`u\to\infty`$ it tends to $`-4\bar M_i^2M_j/M_i`$.
   - $`g_i=0\neq g_j`$, the same for $`i=1,2`$: no. The other part has $`g_j\neq0`$ and the number $`\mathsf w_j^2`$ of (13.19), of order $`\epsilon^2`$: $`\mathsf w_i^2/\mathsf w_j^2=\varrho_j/\varrho_i=\nu_i^{-1}(1+O(\epsilon^2))`$, of order $`\epsilon^{-2}`$, with the sign of $`w_{11}`$.
   - $`g_i=0\neq g_j`$, data of the pair: yes. The binding (through $`u`$, $`u_{[i]}`$; not its sign at this order), the levels of both parts ($`M_i`$, $`M_j`$), and the mean rest cost $`\bar M_i`$ of the part that is read.
   - Derivatives used: (13.19) is (13.13) divided by (13.18). (13.13) uses (11.14) and (11.16): the first derivatives of (11.12) in $`M_i`$, and $`E_b''(0)`$. Of (13.18) only the leading order $`\varrho_i=g_i+O(\epsilon^2)(\lvert g_1\rvert+\lvert g_2\rvert)`$ enters, hence the second derivatives (13.22) only through their order $`\epsilon^2`$, not through their values. The factor $`1+O(\epsilon^2)`$ holds at a fixed ratio $`g_1:g_2`$ with $`g_i\neq0`$ and $`g_1M_1+g_2M_2\neq0`$. For $`g_1M_1+g_2M_2=0`$ the leading term vanishes (no fall at this order, Step 6.4); then $`\mathsf w_i^2=O(\epsilon^4)`$ by (13.13), and its value is not determined here. (13.24), (13.25), (13.26) and the place of the member $`\varrho_i=0`$ use the values of the second derivatives (13.22), with their remainder $`O(\epsilon^4)`$: the mixed one in (13.24), (13.25), all of them in (13.26).
4. Free parts alike with one speed (item 4c): $`g_1=g_2=g_{\rm c}`$ and $`\tau_1=\tau_2=\tau`$, so that $`a^{(i)}=-\tau^2g_{\rm c}`$ is (4.24) with $`v_{\max}=\tau d_0`$. Both parts of the pair have the drift acceleration $`a_{\rm pair}`$, and $`\bar x=d_0\,\bar m\,\hat e`$ for both (17.15). Hence

```math
\frac{\mathrm d^2\bar x}{\mathrm d\lambda^2}\Big\vert_{\rm drift}=-\,\frac{\mathsf w^2}{\tau^2}\;\frac{v_{\max}^2}{d_0}\;\varrho_i\;\hat e,\qquad \frac{\mathsf w^2}{\tau^2}=-\frac{\varsigma}{\sqrt{1+u^2}}\,\bigl(1+O(\epsilon^2)\bigr).
\qquad\text{(13.20)}
```

The pair obeys a relation of the form (4.24) in which $`v_{\max}^2`$ is replaced by $`-\varsigma\,v_{\max}^2/\sqrt{1+u^2}`$. With the speed $`\tau d_0`$ itself it holds neither exactly nor to any order in $`\epsilon`$ at fixed $`u`$. For $`w_{11}<0`$ it holds only in the ordered wide-pair limit, with the leading deviation $`\mathsf w^2/\tau^2-1=-\tfrac12u^2+O(u^4)`$; for $`w_{11}>0`$ not at all ($`\mathsf w^2/\tau^2=-(1+u^2)^{-1/2}<0`$ at every $`u`$; it tends to $`-1`$ in the wide limit). (13.20) is (13.19) for $`g_1=g_2=g_{\rm c}\neq0`$ and $`\tau_1=\tau_2`$, so it uses the same derivatives: (11.14), (11.16), and of (13.22) only the order $`\epsilon^2`$. In (13.20) $`u`$ is that of the level data; the clock data of the part $`i`$ enter through $`\varrho_i`$ (13.18) and change only the factor $`1+O(\epsilon^2)`$. For $`g_{\rm c}=0`$ both sides of (13.20) vanish, and the relation holds trivially with any speed.

## Result

Every statement is at first order in $`(g_1,g_2,\kappa\langle X\rangle)`$ at fixed $`\lambda`$, followed by the long chain, with the records at leading order in $`\kappa`$. "Derived" means derived here from the quoted inputs and standard facts; "numerical" means exhibited with the numerical level or the numerical evolution of the script (section "Code"). For vanishing gradients every first-order quantity is zero; a statement with "iff", "only" or "no" names this member where it would be false on it.

- **Item 1** (class: the contract $`C`$ of the question and the field start $`\varphi`$; exact; derived).
  - The two bodies and the medium evolve by $`C_{\rm red}`$ (13.1). It is the contract of an admissible description of $`b_1,b_2,c`$: yes. A binding with a factor of the field would need a term on three objects, which (1.10) does not contain.
  - $`C_{\rm bod}`$ is (13.2), fixed by $`C,\chi,\varphi`$ up to an additive constant; its gradient terms are (13.3).
  - Fixed by $`C_{\rm bod}`$ and well defined: $`g_1`$ yes; $`g_2`$ yes; $`\kappa\langle X\rangle`$ yes; the operator $`\mathcal K`$ at the centre label yes; the operator $`\mathcal D_\eta`$ at $`\hat r`$ yes, for given $`\eta`$. Of the five only $`\mathcal D_\eta=\mathcal D_0-\eta\,\mathcal K`$ depends on $`\eta`$, and it does iff at least one gradient is non-zero (for vanishing gradients $`\mathcal K=\mathcal D_\eta=0`$). The centre label $`\hat X_\eta`$ itself depends on $`\eta`$ in every case.
- **Item 2** (class: every $`W\in\mathcal W`$, all data, every bound level, every $`g\in\mathcal G(\mathcal P_0)`$, all gradients; exact relations at first order; derived, except the members named "numerical").
  - (a) $`v^{(1)}_i=\lambda\langle\alpha\rangle_g+\rho_i(\lambda)`$ (13.7), (13.8), with the same coefficient for both parts, and $`\lvert\rho_i\rvert\le\tau_i\mathsf B_g`$ for all $`\lambda`$ (13.9).
  - (b) $`(\bar m_1-\bar m_2)^{(1)}=\lambda\langle\beta\rangle_g+\sigma(\lambda)`$ with bounded $`\sigma`$ (13.10). There is never a term $`\propto\lambda^2`$. It stays bounded if $`W(-r)^{*}=W(r)`$ (all diagonal on-site bindings); it is zero under the sufficient condition of Step 4.3; for a binding without that property it grows linearly for the control set S5 (numerical; no analytic example). The answer is the same for the common gradient and for $`g_1\neq g_2`$, except that the vanishing case needs $`g_1=g_2`$.
  - (c) $`a^{\rm drift}(P_0)=g_1\alpha_1+g_2\alpha_2+\kappa\langle X\rangle\alpha_X`$ at $`P_0`$ (13.11): window average first, then $`\delta P\to0`$ on $`\mathcal S(P_0,I)`$; in this order both limits exist for every sequence of the class. In the other order the limit at a fixed window does not exist on the class for every member and window with $`\mathsf f_i\neq0`$, and where it exists it depends on the place of the packet. So the two limits do not commute for every member with $`\partial_P\langle\mathcal K\rangle_{P_0}\neq0`$ (a sufficient condition). Such members exist: the levels of the sets S1–S5 at $`P_0=0.2`$, for the common gradient and for $`g_1`$ only (numerical, Step 5.3; no analytic member). Nothing is shown for the members with $`\mathsf f_i=0`$ for every window, which include $`g_1=g_2=0`$ and the levels of items 3 and 4 at $`P_0=0`$; the evaluation of that order is not asked. $`E_b''(P_0)`$ is not the only property of the level: $`\partial E_b/\partial M_i`$, $`E_b'`$ and $`\partial E_b'/\partial M_i`$ enter the coefficients of $`g_i`$.
  - (d) Of the terms of (11.6), the coefficient of the common gradient contains only the rest terms, through $`\mathcal M_P`$ and $`\mathcal M_P'`$ with the factors $`E_b''`$ and $`E_b'`$; its motion and binding terms do not enter (13.12).
- **Item 3** (class: diagonal on-site binding, $`\hat w_{11}\neq0`$, level (11.12), $`P_0=0`$; leading order in $`\mathsf R`$ at fixed $`u`$, then limits in $`u`$; derived from (11.14), (11.16)). Closed form (13.13), limits (13.14), ratios (13.15) with the member (13.23), levels (13.16). With a non-zero fall, for $`\langle X\rangle=0`$ and at leading order in $`\mathsf R`$: at no fixed $`u`$ does the pair fall like both of its parts; it does so only in the ordered wide-pair limit, for $`w_{11}<0`$ and free parts that fall alike ($`\tau_1^2g_1=\tau_2^2g_2`$). At a fixed $`u`$ it falls like one part $`i`$ only on the member $`g_j/g_i=\mathsf z_i(u)`$ of (13.23), which for the common gradient is $`u=u_*`$. At a fixed binding $`w_{11}\neq0`$ its fall is the same for all pairs of levels iff all three gradients vanish (no fall); in the ordered wide-pair limit iff $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$. Without a fall the pair and its parts agree trivially.
- **Item 4** (same class, $`\langle X\rangle=0`$; derived from (11.19), (11.20), and from (11.12) with the statement on its differentiation that is quoted with (11.14)).
  - Rate (13.17) and relative change (13.18), from (13.21), (13.22): both with the clock data of the part $`i`$ ($`u_{[i]}`$, $`\Lambda_{[i]}`$), not with the level data of (13.13).
  - Number $`\mathsf w_i^2`$: (13.19) at a fixed ratio $`g_1:g_2`$ with $`g_i\neq0`$, of order $`\epsilon^2`$; (13.25) for $`g_i=0\neq g_j`$, negative and of order $`\epsilon^0`$; not defined on the member $`g_i/g_j=-\nu_i(1+O(\epsilon^2))`$ of (13.24) and for $`g_1=g_2=0`$. It equals $`\tau_i^2`$ only on the member (13.23), and never for $`g_i=0\neq g_j`$. It is the same for both parts at leading order iff $`g_1=g_2`$ (or $`a_{\rm pair}=0`$), and then at relative order $`\epsilon^2`$ iff the condition of (13.26) holds. It contains the binding and the clock levels.
  - Relation (13.20), with $`u`$ of the level data.
  - No assumption on a remainder is used: (13.18) rests on the second derivatives of (11.12) in $`M_1,M_2`$ at $`P=0`$, with remainders $`O(\epsilon^4)`$ at fixed $`u`$. Its term of order $`\epsilon^2`$, and with it (13.24)–(13.26), uses their values (13.22); its leading order $`\varrho_i=g_i`$, and with it the factors $`1+O(\epsilon^2)`$ of (13.19) and (13.20), uses only that they are of order $`\epsilon^2`$.
- **Item 5.** In the table $`u`$ is that of the level data, and $`u_{[i]}`$ that of the clock data of the part $`i`$.

| | Free part $`i`$ (upper branch, at rest) | Bound pair (level (11.12), $`P_0=0`$, leading order in $`\mathsf R`$) | Pair agrees with its parts |
|---|---|---|---|
| Drift acceleration from rest | $`a^{(i)}=-(g_iM_i+\kappa\langle X\rangle)/\mathfrak m_i`$; (4.16), (8.11) | $`a_{\rm pair}=-\varsigma(1+u^2)^{-1/2}\,\bar a`$; (13.11), (13.13) | with a non-zero fall: like both parts at no fixed $`u`$; in the ordered limit $`u\to0`$ iff $`a^{(1)}=a^{(2)}`$ and $`w_{11}<0`$; like one part $`i`$ ($`\langle X\rangle=0`$, $`g_i\neq0`$) iff $`g_j/g_i=\mathsf z_i(u)`$, for both signs of $`w_{11}`$, which for the common gradient is $`u=u_*`$ ($`\tau_1\neq\tau_2`$, $`w_{11}<0`$, the part with the smaller $`\tau_i`$); without a fall: trivially; (13.14), (13.15), (13.23) |
| Independent of the clock levels | iff $`\langle X\rangle=0`$; (4.16) | at a fixed binding iff $`g_1=g_2=0`$ and $`\langle X\rangle=0`$ (no fall); (13.16) | at no fixed $`u`$ with a non-zero fall; in the ordered limit $`u\to0`$ iff $`\langle X\rangle=0`$ and $`\tau_1^2g_1=\tau_2^2g_2`$; (13.16) |
| Number that ties it to the relative change of a clock rate ($`\langle X\rangle=0`$) | $`\tau_i^2`$, defined for $`g_i\neq0`$, from $`a^{(i)}=-\tau_i^2g_i`$; (4.24) | fixed ratio with $`g_i\neq0`$: $`\mathsf w_i^2=-\varsigma(1+u^2)^{-1/2}(g_1M_1+g_2M_2)/(g_i(\mathfrak m_1+\mathfrak m_2))`$, of order $`\epsilon^2`$; $`g_i=0\neq g_j`$: $`\mathsf w_i^2=-4\bar M_i^2M_j\,u\,(1+u_{[i]}^2)^{3/2}/(M_i\,u_{[i]}^3\sqrt{1+u^2})`$, negative, of order $`\epsilon^0`$; not defined at $`g_i/g_j=-\nu_i(1+O(\epsilon^2))`$ and for $`g_1=g_2=0`$; (13.18), (13.19), (13.24), (13.25) | for $`g_1=g_2\neq0`$, $`\tau_1=\tau_2`$: $`\mathsf w^2/\tau^2=-\varsigma(1+u^2)^{-1/2}`$, equal to $`1`$ only for $`w_{11}<0`$ in the ordered limit $`u\to0`$; otherwise $`\mathsf w_i^2=\tau_i^2`$ only on the member $`g_j/g_i=\mathsf z_i(u)`$ (one part; for the common gradient $`u=u_*`$), and never for $`g_i=0\neq g_j`$; (13.19), (13.20), (13.23), (13.25) |

## Consistency checks

1. **One body, and no binding.** (13.8) applied to one free body on a level ($`E=\sigma\omega`$, $`\langle\sigma_3\rangle=\partial E/\partial M=\sigma M/\omega`$, $`\mathcal K=G\sigma_3-\mathcal F`$) gives $`\alpha=-GM(\omega\omega')'/\omega^2+\sigma\mathcal F\omega''=-GM\tau^2\cos2p/\omega^2+\sigma\mathcal F\tau^2(M^2\cos2p-\tau^2\sin^4p)/\omega^3`$. This is (4.7) with $`g_\zeta=0`$, for all $`p`$ and both branches. In the pair, the ordered limit of no binding ($`u\to0`$, $`w_{11}<0`$) of (13.13) is $`\bar a`$, equal to $`a^{(1)}=a^{(2)}`$ when the free parts fall alike. Passed.
2. **Common gradient against (11.6).** With (11.14) at $`P=0`$: $`\mathcal M_0=M_1+M_2-a\Lambda`$ from $`\langle\sigma^{(i)}_3\rangle_0`$, and $`E_b-\langle A_1\rangle_0-\langle A_2\rangle_0-\langle U\rangle_0=M_1+M_2+a+\varsigma\sqrt{w^2+a^2}-2a\Lambda-\varsigma w^2/\sqrt{w^2+a^2}=M_1+M_2-a\Lambda`$. Passed, in agreement with (13.12).
3. **Dimensions.** Labels and $`P`$ are pure numbers and costs are $`1/\lambda`$. $`g_i`$ is per label, $`\kappa\langle X\rangle`$ a cost per label, $`E_b''`$ and $`1/\mathfrak m`$ are costs. (13.8), (13.13): cost$`^2`$, i.e. labels$`/\lambda^2`$. (13.10): $`\beta`$ is a cost, i.e. labels$`/\lambda`$. (13.17): $`1/\lambda`$. (13.19): $`\mathsf w_i^2`$ is a cost$`^2`$, like $`\tau_i^2`$. Passed.

## Open issues

- The second order in the gradients, and the range of $`\lambda`$ over which the first order describes the motion, are not estimated (out of scope); (13.9) and (13.10) bound first-order terms only.
- Outside the scope of the question (item 2(c) as amended): the evaluation of the limits in the other order, with the sharp total label first. Not decided here: whether that order exists for the exceptional members of Step 5.3 ($`\mathsf f_i=0`$), among them the levels of items 3 and 4 at $`P_0=0`$. The members for which the two limits are shown not to commute are numerical (Step 5.3); an analytic member is not given.
- A binding of $`\mathcal W`$ with $`\beta\not\equiv0`$ is exhibited numerically (set S5), not analytically; the same holds for a level with $`E_b'(0)\neq0`$ (Step 5.4).
- The relative remainders $`O(\epsilon^2)`$ of (13.13)–(13.20) and of (13.23)–(13.26) are not determined (numerically up to 4 % for (13.13) and up to 7 % for (13.22) at $`\tau_i/M_i=0.2`$) and are not uniform in $`u`$.
- The first-order corrections to the clock reading of a pair in the field (the gradient across the packet) are not derived.
- The results hold for a binding and for motion terms without a factor of the field, the class of the question. Whether another admissible coupling makes the pair fall like its parts is outside this package.
- The remainder of (13.22) rests on the reading of the quoted statement of 11-bound-pair that is given in Step 7.2: a complex neighbourhood of the real data, $`M_1`$ and $`M_2`$ included, whose size does not depend on $`\epsilon`$. That statement is worded for the differentiation that gives (11.14); the second derivatives in $`M_1,M_2`$ follow from its premise, not from its wording. The numerical check finds the order $`\epsilon^4`$ for three sets (section "Code", item 4). (13.24)–(13.26) and the place of the member $`\varrho_i=0`$ use the values (13.22) and share this reading.
- Whether the rest $`\dot\rho_i`$ of the first-order acceleration decays for $`\lambda\to\infty`$ at a fixed packet is not derived (Step 5.1); the drift acceleration does not need it.

## Code

- **File:** `code/v3/pair_fall_check.py`, role: check. Outputs: `code/v3/output/summary.txt` (all numbers below), `code/v3/output/results.json`, `code/v3/output/first_order_motion.png`. It is the script of v2 with the paths changed and one table added (item 2c below); the evolution, its parameters and its numbers are those of v2.
- **What it does.**
  - It builds the fibre contract (11.1) on $`\lvert r\rvert\le48`$, finds the bound level attached to $`\mathcal B_{++}`$ on a grid of 161 values of $`P`$, and computes $`\alpha`$ (13.8) and $`\beta`$ (13.10) from it ($`E_b''`$ by (11.9); the reduced resolvent by full diagonalization).
  - It builds $`\Phi_g`$ with $`g\propto\cos^4\bigl(\pi(P-P_0)/(2P_c)\bigr)`$ on the chain $`\lvert x_i\rvert\le60`$ (121 sites, dimension 58564), evolves it by $`C_{\rm bod}`$ (13.2) with small gradients of both signs (Chebyshev expansion), and takes the symmetric difference.
  - The slope of a first-order quantity is its mean rate over $`[0,\lambda_{\max}]`$ with the weight $`\propto\sin^4(\pi\lambda/\lambda_{\max})`$. The sampling step is chosen so that no multiple of $`2\pi/\text{step}`$ lies near a frequency $`\lvert E_n(P)-E_b(P)\rvert`$ of the rest.
  - From the numerical level at $`P=0`$ (fibre $`\lvert r\rvert\le64`$) it computes the clock ratio $`\Gamma_i=\langle\sigma^{(i)}_3\rangle_0`$ and its derivative in the data, $`T_{ij}:=M_j\,\partial\Gamma_i/\partial M_j=M_j\,\partial^2E_b(0)/\partial M_j\partial M_i=-2M_j\,\mathrm{Re}\langle\sigma^{(i)}_3\psi_0\vert R_0\vert\sigma^{(j)}_3\psi_0\rangle`$, and compares them with (11.20), with (13.22) and, through (13.21), with (13.18).
  - From the numerical level at $`P=0`$ and $`P=0.2`$ (fibre $`\lvert r\rvert\le96`$) it computes $`\partial_P\langle\sigma^{(i)}_3\rangle_P=-2\,\mathrm{Re}\langle\sigma^{(i)}_3\psi_P\vert R_P\vert V_\eta\psi_P\rangle`$, $`\partial_P\langle\mathcal K\rangle_P`$ and $`\mathsf f_i=\mathrm{Re}\,F_{i,\Lambda}(P)`$ of Step 5.3 for the windows $`[0,\Lambda]`$, $`\Lambda=5,10,20`$, by the sum over the levels of the fibre, per unit gradient (common gradient; $`g_1`$ only), and checks the identity (13.6).
- **Sets.** Each with the common gradient, with $`g_1`$ only ($`g_2=0`$), and with a plain gradient in the place of $`\kappa\langle X\rangle`$.
  - S1: $`\tau_i=0.2`$, $`M_i=1`$, $`w_{11}=-0.02`$ ($`u=1.00`$). S2: $`\tau=(0.20,0.18)`$, $`M=(1,1.25)`$, $`w_{11}=-0.02`$ ($`u=1.21`$). S3: $`\tau=(0.20,0.17)`$, $`M=(1,0.9)`$, $`w_{11}=+0.022`$ ($`u=1.22`$). S4: $`\tau=(1,0.8)`$, $`M=(1,1.2)`$, $`w_{11}=-0.9`$. In all four the other $`w_{s_1s_2}`$ are non-zero, $`P_0=0`$ and $`P_c=0.5`$ ($`\delta P=0.106`$).
  - S5 (control): the data of S4 with a binding of range 1 that is neither diagonal nor symmetric, $`P_0=0.2`$, $`P_c=0.4`$ ($`\delta P=0.085`$).
  - Range: $`\lambda\le3000`$ (S1–S3), $`200`$ (S4), $`400`$ (S5). Gradients: $`5\cdot10^{-7}`$ (S1–S3), $`2\cdot10^{-6}`$ (S4, S5).
- **Item 2a.** The slopes of $`v^{(1)}_1`$ and $`v^{(1)}_2`$ agree with $`\langle\alpha\rangle_g`$ of (13.7), in all three configurations, to a relative $`2\cdot10^{-5}`$ (S1), $`1.3\cdot10^{-5}`$ (S2), $`6\cdot10^{-6}`$ (S3), $`4\cdot10^{-7}`$ (S4), $`3\cdot10^{-5}`$ (S5). The rest stays bounded, at most 3 % of the linear part at $`\lambda_{\max}`$.
- **Item 2b.** For S1–S4 the first-order separation stays bounded and relaxes to a constant (slope times $`\lambda_{\max}`$ below 0.5 % of its maximum). For S1 with the common and the plain gradient it is zero within the noise of the difference ($`3\cdot10^{-8}`$ against $`270`$ for $`g_1`$ only), as in Step 4.3. For S5 it grows linearly: slopes $`-0.08662`$, $`-0.02819`$, $`-0.07457`$ against $`\langle\beta\rangle_g=-0.08651`$, $`-0.02813`$, $`-0.07444`$; with $`\lambda\le600`$ the second slope is $`-0.028139`$.
- **Item 2c (members for the other order of the limits; I4 of the review of v2).** Table "other order": the numerical level of the five sets at $`P=0`$ and $`P=0.2`$; all numbers per unit gradient.
  - $`\partial_P\langle\sigma^{(i)}_3\rangle_P`$ at $`P=0.2`$, $`i=1,2`$: S1 $`-2.102\cdot10^{-3}`$ (both); S2 $`-1.490\cdot10^{-3}`$, $`-1.333\cdot10^{-3}`$; S3 $`+1.657\cdot10^{-3}`$, $`+1.946\cdot10^{-3}`$; S4 $`-2.398\cdot10^{-2}`$, $`-2.300\cdot10^{-2}`$; S5 $`-3.277\cdot10^{-2}`$, $`-3.888\cdot10^{-2}`$. Hence $`\partial_P\langle\mathcal K\rangle_P`$ for the common gradient: $`-4.20\cdot10^{-3}`$, $`-3.16\cdot10^{-3}`$, $`+3.41\cdot10^{-3}`$, $`-5.16\cdot10^{-2}`$, $`-7.94\cdot10^{-2}`$; for $`g_1`$ only it is $`M_1=1`$ times the first number of each set.
  - $`\mathsf f_i=\mathrm{Re}\,F_{i,\Lambda}(P)`$ at $`P=0.2`$ for $`\Lambda=5,10,20`$: non-zero for all sets, both parts, both configurations. S5 with the common gradient: $`\mathsf f_1=7.07\cdot10^{-2}`$, $`2.34\cdot10^{-2}`$, $`1.20\cdot10^{-2}`$ and $`\mathsf f_2=2.83\cdot10^{-2}`$, $`1.11\cdot10^{-1}`$, $`-6.28\cdot10^{-2}`$. The smallest value of the table is $`3.7\cdot10^{-6}`$ ($`\mathsf f_2`$ of S2 with $`g_1`$ only, $`\Lambda=5`$).
  - At $`P=0`$: for S1–S4 (symmetry $`\mathcal R`$ of Step 6.1) $`\lvert\partial_P\langle\sigma^{(i)}_3\rangle_0\rvert\le2.4\cdot10^{-17}`$ and $`\lvert\mathsf f_i\rvert\le1.5\cdot10^{-15}`$, the exceptional members of Step 5.3. For S5: $`E_b'(0)=-1.17\cdot10^{-4}`$, $`\partial_P\langle\mathcal K\rangle_0=3.36\cdot10^{-4}`$ for the common gradient, and $`\mathsf f_i\neq0`$.
  - Checks. The identity (13.6), $`2\,\mathrm{Re}\langle V_i\psi_P\vert R_P\vert\mathcal K\psi_P\rangle=-\partial_P\langle\mathcal K\rangle_P`$ for $`i=1,2`$, holds to $`3\cdot10^{-16}`$. A symmetric difference of $`\langle\sigma^{(i)}_3\rangle_P`$ in $`P`$ (step $`10^{-4}`$) agrees with the resolvent form to $`2\cdot10^{-10}`$. Fibre range $`64`$ against $`96`$: $`3\cdot10^{-15}`$. At these $`P`$ the level is outside the bands, with a distance to the rest of the spectrum of at least $`8\cdot10^{-3}`$.
  - Comparison for S1–S3 at $`P=0.2`$ (a check of the table; no statement of the derivation rests on it): the leading order obtained from (11.12) by one derivative in $`M_i`$ and one in $`P`$, $`\varsigma\,\frac{a_i}{M_i}\,\frac{2a_j\sin2P\,(w^2+a_j^2+a_ia_j\cos2P)}{(w^2+j(P)^2)^{3/2}}`$, deviates from the numbers above by $`8\cdot10^{-4}`$ (S1), up to $`3\cdot10^{-3}`$ (S2) and $`-4.3\cdot10^{-2}`$ (S3).
- **Item 3.** The coefficients of (13.13) deviate from those of the numerical level at $`P_0=0`$ by $`-5\cdot10^{-4}`$ to $`+2.5\cdot10^{-3}`$ (S1), up to $`2.9\cdot10^{-3}`$ (S2), and $`-2.2\cdot10^{-2}`$ to $`-3.8\cdot10^{-2}`$ (S3), against $`(\tau_i/M_i)^2\le0.04`$. With $`\tau\to s\tau`$, $`w\to s^2w`$ and $`s=1,\tfrac12,\tfrac14`$ the deviations fall by factors $`3.8`$ to $`4.5`$ per step. The slopes of the evolution agree, to the same deviations, with (13.13) averaged over the packet through (11.12).
- **Item 4 (the derivative of the clock ratio in the data; I1 of the review of v1).** Sets S1–S3 and their scalings $`\tau\to s\tau`$, $`w\to s^2w`$, $`s=1,\tfrac12,\tfrac14`$. In this table the rest costs $`M_i`$ of the set are used for the part that is read as well ($`\bar M_i=M_i`$), so the clock data and the level data coincide.
  - The four numbers $`T_{ij}`$ deviate from (13.22) by a relative $`5.4\cdot10^{-3}`$ to $`1.1\cdot10^{-2}`$ (S1, S2) and $`-2.7\cdot10^{-2}`$ to $`-7.0\cdot10^{-2}`$ (S3) at $`s=1`$. Per step in $`s`$ the relative deviations fall by factors $`3.8`$ to $`4.0`$ and the absolute ones by $`15`$ to $`16`$: the remainder of (13.22) is of order $`\epsilon^4`$, as Step 7.2 states.
  - $`\varrho_i-g_i`$ from (13.21), for the common gradient, $`g_1`$ only and $`g_2`$ only, deviates from the term of order $`\epsilon^2`$ of (13.18) by up to $`1.6\cdot10^{-2}`$ (S1, S2) and $`5.5\cdot10^{-2}`$ (S3) at $`s=1`$, with factors $`3.9`$ to $`4.0`$ per step. The column of the common gradient is the term $`\frac{\tau_i^2}{4\bar M_i^2}\mathsf y`$ of (13.26); the columns of the gradient of the other part are $`\nu_i`$ of (13.24).
  - $`1-\Gamma_i`$ deviates from (11.20) by $`7\cdot10^{-3}`$ to $`9\cdot10^{-3}`$ (S1, S2) and $`-4\cdot10^{-2}`$ (S3) at $`s=1`$, with factors $`3.9`$ to $`4.0`$ per step.
  - Checks: a symmetric difference of $`\Gamma_i`$ in $`M_j`$ (relative step $`10^{-4}`$) agrees with the resolvent form to $`7\cdot10^{-8}`$; fibre range $`48`$ against $`64`$: $`5\cdot10^{-12}`$.
- **Cross-checks of (13.23) and (13.25).** They are formed here from numbers that the script prints; the script does not print them, and no statement rests on them.
  - (13.25), part $`2`$ with $`g_2=0\neq g_1`$ and $`\bar M_i=M_i`$: minus the coefficient of $`g_1`$ of the level at $`P_0=0`$, divided by $`T_{21}/\Gamma_2`$, is $`-7.927`$ (S1), $`-8.314`$ (S2), $`-5.868`$ (S3), against $`-4M_1M_2(1+u^2)/u^2=-8`$, $`-8.395`$, $`-6.017`$: deviations $`-0.9`$ %, $`-1.0`$ %, $`-2.5`$ %, and a negative number for both signs of $`w_{11}`$.
  - (13.23), S2: with the coefficients $`-9.9939\cdot10^{-3}`$ of $`g_1`$ and $`-1.25145\cdot10^{-2}`$ of $`g_2`$ of the level at $`P_0=0`$ and $`a^{(1)}=-0.04\,g_1`$, the pair falls like the part $`1`$ at $`g_2/g_1=2.3977`$, against $`\mathsf z_1(u)=2.3994`$.
- **Convergence** (configuration $`g_1`$ only; relative change of the slopes).
  - Chain: $`45`$ against $`60`$: $`3\cdot10^{-7}`$ (S1), $`5\cdot10^{-8}`$ (S4); $`75`$ against $`60`$: $`1.5\cdot10^{-6}`$ (S5).
  - Gradient doubled: $`2\cdot10^{-6}`$. Other sampling step: below $`10^{-6}`$. Fibre range $`48`$ against $`64`$: $`10^{-13}`$ in $`\alpha`$.
  - Narrower packet ($`P_c=0.35`$): the same agreement with its own $`\langle\alpha\rangle_g`$.
  - Range of $`\lambda`$: on half of the range the slopes deviate by up to $`1.2\cdot10^{-2}`$; the full range reduces this to the values of item 2a.
- **Run.** Once, in the foreground: 366 s. No package was installed.

## Methods used

- Reduction of a contract on an eigenstate of the field operators; partial expectation
- Fibre decomposition under the joint shift of two bodies
- First-order perturbation theory in a term of the contract (Duhamel formula)
- Perturbation theory of an isolated simple eigenvalue; reduced resolvent
- Commutator identities for velocity operators; Hellmann–Feynman relations
- Antiunitary and exchange symmetries of the fibre contract
- Window averaging of bounded oscillating terms; packets with a sharp total label
- Leading-order expansion in a scaling regime with ordered limits
- Mixed second differences (strict supermodularity) for a uniqueness argument
- Numerical evolution by a Chebyshev expansion with a symmetric difference in the gradients
- Second derivatives of an eigenvalue in the data; Cauchy estimate for the derivatives of an analytic remainder
- Mean ergodic theorem for the time average of a unitary group
