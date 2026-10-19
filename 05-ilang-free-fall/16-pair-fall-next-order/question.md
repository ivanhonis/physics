# Question: 16-pair-fall-next-order

- **Subproject:** 05-ilang-free-fall
- **Package:** 16-pair-fall-next-order
- **Equation tags:** (16.k)
- **Created:** 2026-10-18

## Goal

Determine the fall of the bound pair of 13-pair-fall one order beyond the leading order in the regime $`\mathsf R`$, using the bound level at the next order of 14-pair-level-next-order: the fall itself, the weight of the pair against its cost, and the fall against the falls of the free parts. It is the next order of criterion 9.

**Setting** (as in 13-pair-fall; quoted under "Inputs").
- Two Model D bodies $`b_1`$, $`b_2`$ of different types, one medium, and a sharp stationary field with a linear profile that multiplies the rest and clock term of each part, $`(1+g_ix)\,G_i`$, and not the binding. The operator on the two bodies is $`C_{\rm bod}`$ (13.2); its gradient terms are (13.3), with the gradients $`g_1`$, $`g_2`$, $`\kappa\langle X\rangle`$.
- Diagonal on-site binding with $`\hat w_{11}\neq0`$ (both signs), the bound level (11.12) at the band $`\mathcal B_{++}`$, the regime $`\mathsf R`$ at fixed hatted data (hence at a fixed $`u\in(0,\infty)`$), packets concentrated at total label $`P_0=0`$, both parts on fixed clock levels (the level data of 13-pair-fall). First order in $`(g_1,g_2,\kappa\langle X\rangle)`$; records at leading order in $`\kappa`$.
- $`a_{\rm pair}`$ is the drift acceleration of 13-pair-fall at $`P_0=0`$, (13.11). By Step 6.1 of 13-pair-fall, for this class $`E_b'(0)=0`$ exactly, so $`a_{\rm pair}=-E_b''(0)\,\langle\mathcal K\rangle_0`$ exactly; the **weight** of the pair is $`\mathcal W:=\langle\mathcal K\rangle_0=g_1M_1\langle\sigma^{(1)}_3\rangle_0+g_2M_2\langle\sigma^{(2)}_3\rangle_0+2\kappa\langle X\rangle`$, so $`a_{\rm pair}=-\mathcal W/\mathfrak m_b`$.
- The free part $`i`$ in the same field falls from rest, in its upper branch, with $`a^{(i)}:=-(g_iM_i+\kappa\langle X\rangle)/\mathfrak m_i`$: (4.16) with $`G_k=g_iM_i`$, $`\mathcal F_k=-\kappa\langle X\rangle`$, $`\tau_k=\tau_i`$, $`M_k=M_i`$. $`\bar a:=(\mathfrak m_1a^{(1)}+\mathfrak m_2a^{(2)})/(\mathfrak m_1+\mathfrak m_2)`$ is the inertia-weighted mean of the free falls.
- Notation of 11-bound-pair (added on 2026-10-18, after external round 1 of v1, which found it missing): the regime $`\mathsf R`$ is $`\tau_i=\epsilon\hat\tau_i`$, $`w_{s_1s_2}=\epsilon^2\hat w_{s_1s_2}`$ with fixed $`\hat\tau_i>0`$, $`\hat w_{s_1s_2}`$, $`M_i>0`$ and $`\epsilon\to0`$; $`a_i:=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$, $`a:=a_1+a_2`$, $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a`$, $`\Lambda:=1+\varsigma/\sqrt{1+u^2}`$; the derivative in (11.5) is taken at fixed $`\tau_1,\tau_2`$ and fixed binding $`W`$, so $`\partial_{M_i}u=u\beta_i/a`$.
- Notation of 14-pair-level-next-order: $`\beta_i:=a_i/M_i`$, $`\beta:=\beta_1+\beta_2`$, $`\nu:=a_1a_2/a^2`$, $`\bar s:=\sqrt{1+u^2}`$, $`\gamma_s:=\frac{a_1^2}{M_1}+\frac{a_2^2}{M_2}`$, $`\gamma_c:=\frac{a_2^2}{M_1}+\frac{a_1^2}{M_2}`$, $`\gamma_m:=a_1a_2\bigl(\frac1{M_1}+\frac1{M_2}\bigr)`$, and $`\mathcal E_4`$, $`\phi_A`$, $`\phi_B`$, $`\Xi_i`$, $`\mathcal C`$ as in (14.7)–(14.9).
- **"Next order"**: through relative order $`\epsilon^2`$ beyond the leading term, at fixed hatted data; the constants of the remainders may depend on the hatted data.

1. **Fall at the next order.** For every member of the class and all three gradients: determine the relative remainders $`r_1`$, $`r_2`$, $`r_X`$ of (13.13) at their leading order $`\epsilon^2`$, as explicit functions of the data.
2. **Weight against cost.** For the common gradient $`g_1=g_2=g_{\rm c}\neq0`$ and $`\langle X\rangle=0`$: determine $`\mathcal W/g_{\rm c}-E_b(0)`$, the difference between the weight per unit gradient and the total cost $`E_b(0)=M_1+M_2+E_{\rm bind}`$ of the level, at order $`\epsilon^2`$ and at order $`\epsilon^4`$.
3. **Pair against its parts.** For the common gradient $`g_{\rm c}\neq0`$ and $`\langle X\rangle=0`$: determine $`a_{\rm pair}/\bar a-1`$ through relative order $`\epsilon^2`$, written as the combination of the relative change of the weight against $`g_{\rm c}(M_1+M_2)`$ and the relative change of the inertia against $`\mathfrak m_1+\mathfrak m_2`$.
4. **Wide pair.** For $`w_{11}<0`$, in the ordered limit (first $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ in each coefficient): give the leading term in $`u`$ of the order-$`\epsilon^4`$ coefficient of item 2 and of the order-$`\epsilon^2`$ relative correction of item 3, on the data where that term's coefficient is not zero, and name the data where it vanishes. Further terms on those data are not asked (restricted on 2026-10-18: the programme needs the generic wide pair).

## Inputs

From 13-pair-fall@v6 (this subproject). Setting there: as under "Goal"; $`\hat X_\eta`$ is the centre label, $`\hat r`$ the label separation, $`G_i=M_i\sigma^{(i)}_3`$ on the levels $`k_1`$, $`k_2`$; $`\bar a`$ and $`a^{(i)}`$ as under "Goal".

Eq. (13.2) of 13-pair-fall:

```math
C_{\rm bod}=C^{\rm D}_1+C^{\rm D}_2+U+\sum_{i=1,2}g_i\,\hat x_i\otimes G_i+\kappa\langle X\rangle\,(\hat x_1+\hat x_2).
```

Eq. (13.3) of 13-pair-fall:

```math
\begin{aligned}
\Delta&=\hat X_\eta\,\mathcal K+\hat r\,\mathcal D_\eta,\qquad \mathcal K:=g_1M_1\sigma^{(1)}_3+g_2M_2\sigma^{(2)}_3+2\kappa\langle X\rangle,\\
\mathcal D_\eta&:=(1-\eta)\,g_1M_1\sigma^{(1)}_3-\eta\,g_2M_2\sigma^{(2)}_3+(1-2\eta)\,\kappa\langle X\rangle .
\end{aligned}
```

Eq. (13.11) of 13-pair-fall, the drift acceleration of both parts (window first, sharp total label second), for every binding of the class of 11-bound-pair and every bound level:

```math
\boxed{\;a^{\rm drift}(P_0):=\lim_{\delta P\to0}\,\lim_{\Lambda\to\infty}\overline{a^{(1)}_i}=g_1\,\alpha_1(P_0)+g_2\,\alpha_2(P_0)+\kappa\langle X\rangle\,\alpha_X(P_0)\;},\qquad \alpha_i=-M_i\Bigl[E_b''\,\frac{\partial E_b}{\partial M_i}-E_b'\,\frac{\partial E_b'}{\partial M_i}\Bigr],\quad\alpha_X=-2E_b'' .
```

Eq. (13.13) of 13-pair-fall, $`a_{\rm pair}:=a^{\rm drift}(0)`$ for the diagonal on-site binding in $`\mathsf R`$:

```math
\boxed{\;a_{\rm pair}=\frac{\varsigma}{\sqrt{1+u^2}}\;\frac{g_1M_1(1+r_1)+g_2M_2(1+r_2)+2\kappa\langle X\rangle(1+r_X)}{\mathfrak m_1+\mathfrak m_2}\;},\qquad r_1,r_2,r_X=O(\epsilon^2)\ \text{at fixed }u .
```

From 14-pair-level-next-order@v2 (this subproject). Setting there: the bound level of 11-bound-pair in $`\mathsf R`$ at fixed hatted data, notation as under "Goal".

Eq. (14.7) of 14-pair-level-next-order:

```math
E_{\rm bind}=a(1+\varsigma\bar s)+\mathcal E_4+O(\epsilon^6),\qquad \mathcal E_4=-\frac{\gamma_s}2\,\phi_A-\frac{\gamma_s+\gamma_m}2\,\phi_B,\qquad \phi_A=2-u^2+\frac{2\varsigma+u^3}{\bar s},\quad \phi_B=\frac{u^2(\varsigma+\bar s-u)}{\bar s}.
```

Eq. (14.8) of 14-pair-level-next-order:

```math
\langle\sigma^{(i)}_3\rangle_0=1-\beta_i\Lambda+\beta_i\,\Xi_i+O(\epsilon^6),\qquad \Xi_i=\frac32\beta_i\phi_A-\frac{\gamma_s}{2a}\,u\phi_A'+\frac12\Bigl(\beta+\frac{2a}{M_i}\Bigr)\phi_B-\frac\beta2\,u\phi_B',
```

Eq. (14.9) of 14-pair-level-next-order:

```math
\begin{aligned}
E_b''(0)={}&-\frac{4\varsigma\nu a}{\bar s}+\nu\,\mathcal C+O(\epsilon^6),\\
\mathcal C={}&\frac{2u^2}{\bar s^3}\bigl[\gamma_s(\varsigma+\bar s^3-u-u^3)-\gamma_m(\varsigma+\bar s^3-2u-u^3)\bigr]+4\gamma_m\Bigl(1+\frac\varsigma{\bar s}-2u^2+\frac{2u^3}{\bar s}\Bigr)+\frac{2u^2(\bar s-u)}{\bar s}(\gamma_c+\gamma_m).
\end{aligned}
```

Eq. (14.10) of 14-pair-level-next-order:

```math
\mathfrak m_b=-\varsigma(\mathfrak m_1+\mathfrak m_2)\sqrt{1+u^2}\,\Bigl[1+\frac{\varsigma\bar s}{4a}\,\mathcal C+O(\epsilon^4)\Bigr].
```

Eq. (14.12) of 14-pair-level-next-order, for $`\varsigma=-1`$ in the ordered limit $`u\to0`$ of the coefficients; $`\beta_2\Xi_2`$ by exchanging the labels 1 and 2 (also in the $`X_k`$):

```math
\begin{aligned}
&\mathcal E_4=\tfrac12\gamma_m\,u^3+O(u^4),\qquad \nu\,\mathcal C=2\nu(\gamma_c-2\gamma_m)\,u^2+2\nu(5\gamma_m-\gamma_s-\gamma_c)\,u^3+\nu\bigl(3\gamma_s-\tfrac92\gamma_m\bigr)u^4+O(u^5),\\
&\frac{\varsigma\bar s}{4a}\,\mathcal C=-\frac{\gamma_c-2\gamma_m}{2a}\,u^2-\frac{5\gamma_m-\gamma_s-\gamma_c}{2a}\,u^3-\frac{6\gamma_s+2\gamma_c-13\gamma_m}{8a}\,u^4+O(u^5),\\
&\beta_1\Xi_1=\beta_1\bigl(X_3u^3+X_4u^4+X_5u^5\bigr)+O(u^6),\qquad X_3=\frac{a_2}{2a}\Bigl[\frac{a_1-2a_2}{M_1}+\frac{2a_1-a_2}{M_2}\Bigr],\\
&X_4=\frac{a_1^2-7a_1a_2+4a_2^2}{8aM_1}+\frac{3a_2(a_2-a_1)}{4aM_2},\qquad X_5=\frac{a_2}{4a}\Bigl[\frac{2a_2-3a_1}{M_1}+\frac{a_2-4a_1}{M_2}\Bigr],
\end{aligned}
```

From 11-bound-pair@v3 (this subproject). Eq. (11.5) of 11-bound-pair, for every simple isolated bound level and every $`P`$ of its interval:

```math
\frac{\partial E_b}{\partial M_i}=\langle\sigma^{(i)}_3\rangle_P,\qquad
\tau_i\frac{\partial E_b}{\partial\tau_i}=\langle A_i\rangle_P,\qquad
\frac{\partial E_b}{\partial\theta}\Big|_{\theta=1}=\langle U\rangle_P\qquad(i=1,2).
```

From 04-branch-fall@v3 (this subproject). Setting there: one body with linear level profiles $`M_{x,k}=M_k+G_kx`$, $`V_{x,k}=-\mathcal F_kx`$, a branch start at rest; the drift acceleration of the upper branch ($`\sigma=+`$) at rest:

```math
\boxed{\;a_{k,\sigma}(0)=\frac{\tau_k^2}{M_k}\,\bigl(\sigma\,\mathcal F_k-G_k\bigr)\;}
```

## Assumptions

- The setting under "Goal". The two bodies, the field model, the diagonal on-site binding, the regime $`\mathsf R`$, the bound level and the packets are assumptions of this package (M8, M9); equal parameters of the two types are never assumed (M7).
- The results of 13-pair-fall and 14-pair-level-next-order are used as quoted, with their classes and remainders.

## Scope

- **Class.** Item 1: every diagonal on-site binding with $`\hat w_{11}\neq0`$, all hatted data, all three gradients. Items 2–3: the same class with the common gradient and $`\langle X\rangle=0`$. Item 4: $`w_{11}<0`$, as restricted there.
- **Control.** Item 2 and item 3 compare with the free parts and with the cost; no further control is asked.
- Out of scope: second order in the gradients; joint limits in $`\epsilon`$ and $`u`$; the tight pair; the clocks of the parts; pairs of clock levels compared with each other; other bindings and other levels.

## Depth

- Item 1: derive (needed by items 2–3 and criterion 9).
- Item 2: short argument (needed by criterion 9: whether the binding cost is weighed like the rest cost).
- Item 3: short argument (needed by criterion 9: the fall of the pair against its parts at the next order).
- Item 4: short argument (needed by criterion 9: the wide pair, where the leading comparison holds).

## Expected result

- Item 1: three explicit leading coefficients.
- Item 2: two coefficients, of order $`\epsilon^2`$ and $`\epsilon^4`$.
- Item 3: an expression through relative order $`\epsilon^2`$, as a combination of two relative changes.
- Item 4: leading terms in $`u`$, with the data on which they vanish.

Give every main result a tag $`(16.k)`$.

Consistency checks, at most three: for example the ordered limit $`u\to0`$ against the free parts, $`\langle X\rangle`$ alone (its coefficient is $`-2E_b''(0)`$ exactly), and equal data of the two bodies.

## Code

None.
