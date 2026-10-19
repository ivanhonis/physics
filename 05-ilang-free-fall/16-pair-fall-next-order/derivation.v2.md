# Fall of the bound pair one order beyond leading order

- **Subproject:** 05-ilang-free-fall
- **Package:** 16-pair-fall-next-order
- **Version:** v2
- **Mode:** external regeneration
- **Date:** 2026-10-18

## Changes from previous version

- Setup and assumptions: the reconstructed notation of v1 is replaced by the definitions of 11-bound-pair and the regime $`\mathsf R`$ as now quoted in the question; the "Orders" paragraph is derived from $`\mathsf R`$. Reason: I1.
- Setup and assumptions, "Definitions of the question": $`\mathfrak m_i=M_i/\tau_i^2`$ now follows from $`a_i=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$; (4.16) agrees with it. Reason: I1.
- Step 1(b): the derivatives in $`M_i`$ are computed from the quoted definitions at fixed $`\tau_1,\tau_2`$ and binding, with $`\partial_{M_i}u=u\beta_i/a`$ as quoted. (16.2) is now the quoted definition of $`\Lambda`$, and the step checks that (11.5) applied to (14.7) reproduces (14.8) through order $`\epsilon^4`$. Reason: I1.
- Result, item 1: the sentence on $`\Lambda`$ is removed, since $`\Lambda`$ is an input definition, not a result. Step 5: the positivity of $`\gamma_m`$ now rests on $`\tau_i>0`$, $`M_i>0`$ of $`\mathsf R`$.
- Open issues: the first item (unverified notation) is closed. No coefficient of v1 changes.

## Response to verification

- I1: Accepted and fixed in "Setup and assumptions" (notation and regime $`\mathsf R`$, orders) and Step 1(b). The definitions quoted in the amended question coincide with those adopted in v1, including $`\partial_{M_i}u=u\beta_i/a`$ at fixed $`\tau_1,\tau_2`$ and binding; the coefficients (16.3)–(16.13) are unchanged, and the open issue is closed.

## Setup and assumptions

**Description (assumption of the package, M8, M9).** As in 13-pair-fall: two Model D bodies $`b_1,b_2`$ of different types, one medium, and a sharp stationary field with a linear profile that multiplies the rest and clock term of each part, $`(1+g_ix)\,G_i`$ with $`G_i=M_i\sigma^{(i)}_3`$ on the fixed clock levels $`k_1,k_2`$, and not the binding; operator (13.2) and gradient terms (13.3) of 13-pair-fall. Diagonal on-site binding with $`\hat w_{11}\neq0`$, of either sign $`\varsigma=\pm1`$; the bound level (11.12) at the band $`\mathcal B_{++}`$; regime $`\mathsf R`$ at fixed hatted data, hence fixed $`u\in(0,\infty)`$; packets at $`P_0=0`$; first order in $`(g_1,g_2,\kappa\langle X\rangle)`$, records at leading order in $`\kappa`$. Equal parameters of the two types are never assumed (M7). The controls are the ones fixed by the question: items 2 and 3 compare the pair with its cost and with its free parts.

**Definitions of the question.** $`\mathcal W:=\langle\mathcal K\rangle_0=g_1M_1\langle\sigma^{(1)}_3\rangle_0+g_2M_2\langle\sigma^{(2)}_3\rangle_0+2\kappa\langle X\rangle`$ and $`a_{\rm pair}=-E_b''(0)\,\mathcal W=-\mathcal W/\mathfrak m_b`$, so $`\mathfrak m_b=1/E_b''(0)`$; $`E_b'(0)=0`$ exactly (Step 6.1 of 13-pair-fall). $`a^{(i)}=-(g_iM_i+\kappa\langle X\rangle)/\mathfrak m_i`$, with $`\mathfrak m_i=M_i/\tau_i^2`$ by $`a_i=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$ (below); (4.16) of 04-branch-fall with $`G_k=g_iM_i`$, $`\mathcal F_k=-\kappa\langle X\rangle`$, $`\sigma=+`$ gives the same $`a^{(i)}`$. $`\bar a=(\mathfrak m_1a^{(1)}+\mathfrak m_2a^{(2)})/(\mathfrak m_1+\mathfrak m_2)`$.

**Inputs, as quoted in the question.**
- (13.11) of 13-pair-fall at $`P_0=0`$: $`a_{\rm pair}=g_1\alpha_1+g_2\alpha_2+\kappa\langle X\rangle\,\alpha_X`$, $`\alpha_i=-M_i\bigl[E_b''\,\partial_{M_i}E_b-E_b'\,\partial_{M_i}E_b'\bigr]`$, $`\alpha_X=-2E_b''`$.
- (13.13) of 13-pair-fall, which defines $`r_1,r_2,r_X`$: $`a_{\rm pair}=\frac{\varsigma}{\bar s}\,\frac{g_1M_1(1+r_1)+g_2M_2(1+r_2)+2\kappa\langle X\rangle(1+r_X)}{\mathfrak m_1+\mathfrak m_2}`$.
- (11.5) of 11-bound-pair: $`\partial E_b/\partial M_i=\langle\sigma^{(i)}_3\rangle_P`$ (at fixed $`\tau_1,\tau_2`$ and binding).
- (14.7)–(14.10) and (14.12) of 14-pair-level-next-order: $`E_{\rm bind}=a(1+\varsigma\bar s)+\mathcal E_4+O(\epsilon^6)`$ with $`\mathcal E_4,\phi_A,\phi_B`$; $`\langle\sigma^{(i)}_3\rangle_0=1-\beta_i\Lambda+\beta_i\Xi_i+O(\epsilon^6)`$; $`E_b''(0)=-4\varsigma\nu a/\bar s+\nu\,\mathcal C+O(\epsilon^6)`$; $`\mathfrak m_b=-\varsigma(\mathfrak m_1+\mathfrak m_2)\bar s\bigl[1+\frac{\varsigma\bar s}{4a}\mathcal C+O(\epsilon^4)\bigr]`$; the expansions at $`\varsigma=-1`$, $`u\to0`$.

**Notation and regime (11-bound-pair and 14-pair-level-next-order, as quoted in the question).** The regime $`\mathsf R`$ is $`\tau_i=\epsilon\hat\tau_i`$, $`w_{s_1s_2}=\epsilon^2\hat w_{s_1s_2}`$ with fixed $`\hat\tau_i>0`$, $`\hat w_{s_1s_2}`$, $`M_i>0`$, and $`\epsilon\to0`$. $`a_i:=\tau_i^2/(4M_i)=1/(4\mathfrak m_i)`$, $`a:=a_1+a_2`$, $`w:=w_{11}`$, $`\varsigma:=\mathrm{sgn}w`$, $`u:=\lvert w\rvert/a`$, $`\Lambda:=1+\varsigma/\sqrt{1+u^2}`$. The derivative in (11.5) is taken at fixed $`\tau_1,\tau_2`$ and fixed binding $`W`$, so $`\partial_{M_i}u=u\beta_i/a`$. $`\beta_i,\beta,\nu,\bar s,\gamma_s,\gamma_c,\gamma_m`$ and $`\mathcal E_4,\phi_A,\phi_B,\Xi_i,\mathcal C`$ are those of the question. Elementary identities used below:
```math
M_i\beta_i=a_i,\qquad \sum_ia_i=a,\qquad \sum_ia_i\beta_i=\gamma_s,\qquad a\beta=\gamma_s+\gamma_m .
```

**Orders (A13).** In $`\mathsf R`$, $`a_i=\epsilon^2\hat\tau_i^2/(4M_i)`$, so $`a_i,a,\beta_i=O(\epsilon^2)`$ and $`\gamma_s,\gamma_c,\gamma_m=O(\epsilon^4)`$, while $`u=\lvert\hat w_{11}\rvert/\hat a`$ with $`\hat a:=\sum_i\hat\tau_i^2/(4M_i)`$ is fixed; hence $`\mathcal E_4,\mathcal C=O(\epsilon^4)`$ by (14.7), (14.9). Every $`O(\epsilon^n)`$ holds at fixed hatted data, hence at fixed $`u\in(0,\infty)`$, with constants that depend on the hatted data. In item 4, $`u\to0`$ is taken in the coefficients after $`\epsilon\to0`$; no statement is uniform in $`u`$.

## Derivation

### Step 1. Inertia and $`\Lambda`$ in usable form

(a) Since $`\mathfrak m_b=1/E_b''(0)`$, (14.10) and $`\varsigma^2=1`$ give
```math
-\varsigma\bar s\,(\mathfrak m_1+\mathfrak m_2)\,E_b''(0)=\frac{-\varsigma\bar s\,(\mathfrak m_1+\mathfrak m_2)}{\mathfrak m_b}=1-\mu+O(\epsilon^4),\qquad \mu:=\frac{\varsigma\bar s}{4a}\,\mathcal C=O(\epsilon^2).
\qquad\text{(16.1)}
```
(14.9) gives the same with the leading factor $`4\nu a(\mathfrak m_1+\mathfrak m_2)=4\frac{a_1a_2}{a}\bigl(\frac1{4a_1}+\frac1{4a_2}\bigr)=1`$.

(b) By (11.5), $`\langle\sigma^{(i)}_3\rangle_0=\partial E_b(0)/\partial M_i`$ at fixed $`\tau_1,\tau_2`$ and fixed binding $`W`$, with $`E_b(0)=M_1+M_2+E_{\rm bind}`$ and $`E_{\rm bind}`$ of (14.7). From the definitions, at fixed $`\tau_j`$ and $`W`$: $`\partial_{M_i}a_j=-\delta_{ij}\beta_j`$, so $`\partial_{M_i}a=-\beta_i`$; $`\partial_{M_i}u=u\beta_i/a`$ (as quoted, since $`u=\lvert w\rvert/a`$); $`\partial_{M_i}\beta_i=-2\beta_i/M_i`$; hence $`\partial_{M_i}\gamma_s=\partial_{M_i}(a_i\beta_i)=-3\beta_i^2`$ and $`\partial_{M_i}(\gamma_s+\gamma_m)=\partial_{M_i}(a\beta)=-\beta_i(\beta+2a/M_i)`$. Inserted in $`\partial_{M_i}\mathcal E_4`$, these give $`\beta_i\Xi_i`$ of (14.8) term by term. The order-$`\epsilon^2`$ term is $`\partial_{M_i}[a(1+\varsigma\bar s)]=-\beta_i(1+\varsigma\bar s)+\varsigma\frac{u}{\bar s}\,u\beta_i=-\beta_i(1+\varsigma/\bar s)`$, by $`\bar s^2-u^2=1`$. This is $`-\beta_i\Lambda`$ of (14.8), with the quoted definition
```math
\Lambda=1+\frac{\varsigma}{\bar s}.
\qquad\text{(16.2)}
```
So (11.5) applied to (14.7) reproduces (14.8) through order $`\epsilon^4`$: the quoted inputs are consistent with the quoted definitions.

### Step 2. Item 1: the remainders $`r_1,r_2,r_X`$

At $`P_0=0`$, $`E_b'(0)=0`$ and (11.5) reduce (13.11) to $`\alpha_i=-M_iE_b''(0)\langle\sigma^{(i)}_3\rangle_0`$ and $`\alpha_X=-2E_b''(0)`$. Both (13.11) and (13.13) are linear in the three independent gradients $`g_1,g_2,\kappa\langle X\rangle`$. Equating their coefficients gives, exactly,
```math
1+r_i=-\varsigma\bar s\,(\mathfrak m_1+\mathfrak m_2)\,E_b''(0)\,\langle\sigma^{(i)}_3\rangle_0\quad(i=1,2),\qquad 1+r_X=-\varsigma\bar s\,(\mathfrak m_1+\mathfrak m_2)\,E_b''(0).
\qquad\text{(16.3)}
```
Insert (16.1), and (14.8) with (16.2), and keep the order $`\epsilon^2`$:
```math
r_i=-\beta_i\Bigl(1+\frac{\varsigma}{\bar s}\Bigr)-\frac{\varsigma\bar s}{4a}\,\mathcal C+O(\epsilon^4),\qquad r_X=-\frac{\varsigma\bar s}{4a}\,\mathcal C+O(\epsilon^4),
\qquad\text{(16.4)}
```
with $`\mathcal C`$ of (14.9). The first term of $`r_i`$ is the shift of $`\langle\sigma^{(i)}_3\rangle_0`$ from 1. The common term $`-\mu`$ is the relative change of $`1/\mathfrak m_b`$ beyond its leading value.

### Step 3. Item 2: weight against cost

For $`g_1=g_2=g_{\rm c}\neq0`$ and $`\langle X\rangle=0`$, $`\mathcal W/g_{\rm c}=\sum_iM_i\langle\sigma^{(i)}_3\rangle_0`$. With (14.8), (16.2), $`M_i\beta_i=a_i`$ and $`\sum_ia_i=a`$:
```math
\frac{\mathcal W}{g_{\rm c}}=M_1+M_2-a\Bigl(1+\frac{\varsigma}{\bar s}\Bigr)+\sum_ia_i\Xi_i+O(\epsilon^6).
\qquad\text{(16.5)}
```
Summing $`\Xi_i`$ of (14.8) with the elementary identities gives $`\sum_ia_i\Xi_i=\frac{\gamma_s}{2}(3\phi_A-u\phi_A')+\frac{\gamma_s+\gamma_m}{2}(3\phi_B-u\phi_B')`$. Now subtract $`E_b(0)`$ of (14.7). At order $`\epsilon^2`$ the difference is $`-a(1+\varsigma/\bar s)-a(1+\varsigma\bar s)=-\frac{a}{\bar s}(\varsigma\bar s^2+2\bar s+\varsigma)`$. At order $`\epsilon^4`$ it is $`\sum_ia_i\Xi_i-\mathcal E_4`$. Hence
```math
\frac{\mathcal W}{g_{\rm c}}-E_b(0)=-\frac{\varsigma a(\bar s+\varsigma)^2}{\bar s}+\mathcal V_4+O(\epsilon^6),\qquad \mathcal V_4:=\Bigl(u\frac{\partial}{\partial u}-4\Bigr)\mathcal E_4\Big|_{\gamma_s,\gamma_m}=\frac{\gamma_s}{2}\,\psi_A+\frac{\gamma_s+\gamma_m}{2}\,\psi_B,
\qquad\text{(16.6)}
```
where $`\psi=4\phi-u\phi'`$. With $`\bar s'=u/\bar s`$ this is
```math
\psi_A=8-2u^2+\frac{8\varsigma+10\varsigma u^2+u^3+2u^5}{\bar s^3},\qquad \psi_B=2u^2+\frac{2\varsigma u^2-u^3+3\varsigma u^4-2u^5}{\bar s^3}.
\qquad\text{(16.7)}
```
Reading of the order $`\epsilon^2`$: with $`E^{(2)}_{\rm bind}:=a(1+\varsigma\bar s)`$, (16.5) reads $`\mathcal W/g_{\rm c}=M_1+M_2-\frac{\varsigma}{\bar s}E^{(2)}_{\rm bind}+O(\epsilon^4)`$. The rest costs enter the weight with the factor 1, the binding cost with the factor $`-\varsigma/\bar s`$. This factor is $`1/\bar s<1`$ for $`\varsigma=-1`$ and $`-1/\bar s<0`$ for $`\varsigma=+1`$. The order-$`\epsilon^2`$ coefficient of (16.6) is nonzero for every $`u\in(0,\infty)`$ and both signs, since $`a>0`$ and $`\bar s+\varsigma\ge\bar s-1>0`$. Its sign is $`-\varsigma`$.

### Step 4. Item 3: pair against its parts

For $`g_{\rm c}\neq0`$ and $`\langle X\rangle=0`$, $`\bar a=-g_{\rm c}(M_1+M_2)/(\mathfrak m_1+\mathfrak m_2)\neq0`$ and $`a_{\rm pair}=-\mathcal W/\mathfrak m_b`$. Define the relative changes
```math
\delta_W:=\frac{\mathcal W}{g_{\rm c}(M_1+M_2)}-1,\qquad \delta_{\mathfrak m}:=\frac{\mathfrak m_b}{\mathfrak m_1+\mathfrak m_2}-1 .
\qquad\text{(16.8)}
```
Then, exactly,
```math
\frac{a_{\rm pair}}{\bar a}-1=\frac{1+\delta_W}{1+\delta_{\mathfrak m}}-1=\frac{\delta_W-\delta_{\mathfrak m}}{1+\delta_{\mathfrak m}} .
\qquad\text{(16.9)}
```
By (16.5) and (14.10),
```math
\delta_W=-\frac{a}{M_1+M_2}\Bigl(1+\frac{\varsigma}{\bar s}\Bigr)+O(\epsilon^4),\qquad 1+\delta_{\mathfrak m}=-\varsigma\bar s\,(1+\mu)+O(\epsilon^4).
\qquad\text{(16.10)}
```
Here $`\delta_W=O(\epsilon^2)`$, while $`\delta_{\mathfrak m}=-1-\varsigma\bar s+O(\epsilon^2)`$ is of order one. Hence $`(1+\delta_W)/(1+\delta_{\mathfrak m})=-\frac{\varsigma}{\bar s}(1+\delta_W-\mu)+O(\epsilon^4)`$, and with $`\frac{\varsigma}{\bar s}\mu=\frac{\mathcal C}{4a}`$:
```math
\frac{a_{\rm pair}}{\bar a}-1=-1-\frac{\varsigma}{\bar s}+c_2+O(\epsilon^4),\qquad c_2:=\frac{\varsigma}{\bar s}\,\frac{a}{M_1+M_2}\Bigl(1+\frac{\varsigma}{\bar s}\Bigr)+\frac{\mathcal C}{4a}.
\qquad\text{(16.11)}
```
The leading term $`-1-\varsigma/\bar s`$ is nonzero for every $`u\in(0,\infty)`$ and both signs. It tends to 0 only for $`\varsigma=-1`$, $`u\to0`$. $`c_2=O(\epsilon^2)`$ is the relative correction.

### Step 5. Item 4: wide pair

Take $`\varsigma=-1`$. First $`\epsilon\to0`$ at fixed $`u`$ (Steps 3 and 4), then $`u\to0`$ in each coefficient, with $`\bar s^{-1}=1-\frac{u^2}{2}+\frac{3u^4}{8}+O(u^6)`$.

*Item 2.* $`\phi_A=u^3-\frac34u^4-\frac12u^5+O(u^6)`$ and $`\phi_B=-u^3+\frac12u^4+\frac12u^5+O(u^6)`$. The operator $`u\partial_u-4`$ multiplies $`u^n`$ by $`n-4`$. So $`\psi_A=u^3+\frac12u^5+O(u^6)`$ and $`\psi_B=-u^3-\frac12u^5+O(u^6)`$, and the $`\gamma_s`$ terms of $`\mathcal V_4`$ cancel through $`u^5`$. The order-$`\epsilon^2`$ coefficient is $`-\varsigma a(\bar s+\varsigma)^2/\bar s=a(\bar s-1)^2/\bar s`$. Hence
```math
\frac{a(\bar s-1)^2}{\bar s}=\frac a4\,u^4+O(u^6),\qquad \mathcal V_4=-\frac{\gamma_m}{2}\,u^3+O(u^5),\qquad \gamma_m=a_1a_2\Bigl(\frac1{M_1}+\frac1{M_2}\Bigr)>0 .
\qquad\text{(16.12)}
```
$`\gamma_m>0`$ for all data ($`a_i>0`$ since $`\tau_i>0`$, $`M_i>0`$ in $`\mathsf R`$), so the leading term of $`\mathcal V_4`$ vanishes on no data.

*Item 3.* At $`\varsigma=-1`$, $`c_2=-\frac{a}{\bar s(M_1+M_2)}\bigl(1-\frac1{\bar s}\bigr)+\frac{\mathcal C}{4a}`$. Insert $`1-\frac1{\bar s}=\frac{u^2}{2}+O(u^4)`$ and $`\mathcal C=2(\gamma_c-2\gamma_m)u^2+O(u^3)`$ from (14.12). Then write $`\gamma_c-2\gamma_m=\frac{a_2(a_2-2a_1)}{M_1}+\frac{a_1(a_1-2a_2)}{M_2}`$ and use $`x_2=1-x_1`$, $`y_1=1-y_2`$:
```math
c_2=K_2\,u^2+O(u^3),\qquad K_2=\frac{\gamma_c-2\gamma_m}{2a}-\frac{a}{2(M_1+M_2)}=\frac{a(M_1+M_2)}{2M_1M_2}\Bigl[(x_1-y_2)^2-2x_1x_2\Bigr],
\qquad\text{(16.13)}
```
with $`x_i:=a_i/a`$ and $`y_i:=M_i/(M_1+M_2)`$. By $`a_i=1/(4\mathfrak m_i)`$, $`x_1=\mathfrak m_2/(\mathfrak m_1+\mathfrak m_2)`$: $`x_1-y_2`$ is the inertia share minus the rest-cost share of body 2. The prefactor is positive, so $`K_2=0`$ if and only if $`(x_1-y_2)^2=2x_1x_2`$, that is $`3x_1^2-2(1+y_2)x_1+y_2^2=0`$, or
```math
x_1=\tfrac13\bigl(1+y_2\pm\sqrt{1+2y_1y_2}\bigr).
```
For every $`y_2\in(0,1)`$ both roots lie in $`(0,1)`$: $`x_1^+<1\iff 2y_1y_2<2y_1+y_1^2`$, and $`x_1^->0\iff 3y_2^2>0`$. So $`K_2`$ vanishes exactly on two surfaces of the data, and each surface meets every ratio $`M_1/M_2`$. Equal data of the two types ($`x_1=y_2=\frac12`$) give $`K_2=-a/(2M_1)\neq0`$. The correction taken relative to the leading value $`1/\bar s`$ of $`a_{\rm pair}/\bar a`$, namely $`\bar s\,c_2`$, has the same leading term $`K_2u^2`$.

## Result

All results hold for the setting under "Setup and assumptions": both signs $`\varsigma=\pm1`$, fixed hatted data (fixed $`u\in(0,\infty)`$), first order in the gradients, records at leading order in $`\kappa`$, packets at $`P_0=0`$. Every $`O(\epsilon^n)`$ holds at fixed $`u`$, with constants that depend on the hatted data.

1. **Item 1 (formula; every diagonal on-site binding with $`\hat w_{11}\neq0`$, all three gradients).** Exactly, $`1+r_i=-\varsigma\bar s(\mathfrak m_1+\mathfrak m_2)E_b''(0)\langle\sigma^{(i)}_3\rangle_0`$ and $`1+r_X=-\varsigma\bar s(\mathfrak m_1+\mathfrak m_2)E_b''(0)`$ (16.3). At leading order, $`r_i=-\beta_i(1+\varsigma/\bar s)-\frac{\varsigma\bar s}{4a}\mathcal C+O(\epsilon^4)`$ and $`r_X=-\frac{\varsigma\bar s}{4a}\mathcal C+O(\epsilon^4)`$ (16.4), with $`\mathcal C`$ of (14.9).
2. **Item 2 (formula; common gradient $`g_{\rm c}\neq0`$, $`\langle X\rangle=0`$).** $`\mathcal W/g_{\rm c}-E_b(0)=-\varsigma a(\bar s+\varsigma)^2/\bar s+\mathcal V_4+O(\epsilon^6)`$, with $`\mathcal V_4=(u\partial_u-4)\mathcal E_4|_{\gamma_s,\gamma_m}=\frac{\gamma_s}2\psi_A+\frac{\gamma_s+\gamma_m}2\psi_B`$ (16.6) and $`\psi_A,\psi_B`$ of (16.7). At order $`\epsilon^2`$ the weight per unit gradient is $`M_1+M_2-\frac{\varsigma}{\bar s}\,a(1+\varsigma\bar s)`$. The binding cost is weighed with the factor $`-\varsigma/\bar s`$, not 1. The order-$`\epsilon^2`$ difference is nonzero for every $`u\in(0,\infty)`$ and both signs, and has the sign $`-\varsigma`$.
3. **Item 3 (formula; common gradient $`g_{\rm c}\neq0`$, $`\langle X\rangle=0`$).** Exactly, $`a_{\rm pair}/\bar a-1=(\delta_W-\delta_{\mathfrak m})/(1+\delta_{\mathfrak m})`$ (16.9). Here $`\delta_W`$ and $`\delta_{\mathfrak m}`$ (16.8) are the relative changes of the weight against $`g_{\rm c}(M_1+M_2)`$ and of the inertia against $`\mathfrak m_1+\mathfrak m_2`$, given by (16.10). Through relative order $`\epsilon^2`$, $`a_{\rm pair}/\bar a-1=-1-\varsigma/\bar s+c_2+O(\epsilon^4)`$, with $`c_2=\frac{\varsigma}{\bar s}\frac{a}{M_1+M_2}(1+\frac{\varsigma}{\bar s})+\frac{\mathcal C}{4a}`$ (16.11).
4. **Item 4 (formula; $`w_{11}<0`$, ordered limit: first $`\epsilon\to0`$ at fixed $`u`$, then $`u\to0`$ in each coefficient).** The order-$`\epsilon^2`$ coefficient of item 2 is $`\frac a4u^4+O(u^6)`$. The order-$`\epsilon^4`$ coefficient is $`-\frac12\gamma_mu^3+O(u^5)`$, and $`\gamma_m>0`$ for all data, so its leading term vanishes on no data (16.12). The order-$`\epsilon^2`$ correction of item 3 is $`c_2=K_2u^2+O(u^3)`$, with $`K_2=\frac{a(M_1+M_2)}{2M_1M_2}[(x_1-y_2)^2-2x_1x_2]`$, $`x_i=a_i/a`$, $`y_i=M_i/(M_1+M_2)`$ (16.13). $`K_2=0`$ if and only if $`a_1/a=\frac13\bigl(1+y_2\pm\sqrt{1+2y_1y_2}\bigr)`$. These are two surfaces of the data, each meeting every ratio $`M_1/M_2`$; equal data of the two types are not on them.

## Consistency checks

1. **Dimensions.** $`\beta_i`$, $`\mathcal C/a`$, $`\gamma/a`$ and $`a/M_i`$ are dimensionless, and so are $`r_i,r_X,\delta_W,\delta_{\mathfrak m},c_2,K_2`$. $`a`$, $`\gamma_s,\gamma_m`$ and $`\mathcal V_4`$ are costs, as is $`\mathcal W/g_{\rm c}-E_b(0)`$. Passed.
2. **Ordered limit $`u\to0`$ at $`\varsigma=-1`$ against the free parts.** $`\Lambda=1-1/\bar s\to0`$, and $`\mu=-\frac{\gamma_c-2\gamma_m}{2a}u^2+O(u^3)\to0`$ by (14.12). Therefore $`r_1,r_2,r_X\to0`$, $`1+\delta_{\mathfrak m}\to1`$, and $`-1+1/\bar s\to0`$ and $`c_2\to0`$. Both coefficients of item 2 also tend to 0. Coefficient by coefficient, the wide pair falls with $`\bar a`$ and weighs $`E_b(0)`$ per unit gradient. Passed.
3. **Independent route to (16.12).** From the $`X_k`$ of (14.12), with $`X^{(2)}_k`$ obtained by exchanging the labels: $`\sum_ia_iX^{(i)}_3=0`$, $`\sum_ia_iX^{(i)}_4=\frac{\gamma_s}8-\frac{\gamma_m}4`$ and $`\sum_ia_iX^{(i)}_5=-\frac{\gamma_m}2`$. From (14.7), $`\mathcal E_4=\frac{\gamma_m}2u^3+(\frac{\gamma_s}8-\frac{\gamma_m}4)u^4-\frac{\gamma_m}4u^5+O(u^6)`$. Then $`\mathcal V_4=\sum_ia_i\Xi_i-\mathcal E_4=-\frac{\gamma_m}2u^3+0\cdot u^4-\frac{\gamma_m}4u^5+O(u^6)`$, the same as from (16.7). Passed.

## Open issues

- Joint limits in $`\epsilon`$ and $`u`$ are out of scope. At $`\varsigma=-1`$ the order-$`\epsilon^2`$ coefficient of item 2 is $`O(u^4)`$ and the order-$`\epsilon^4`$ one is $`O(u^3)`$, so which one dominates depends on how $`\epsilon`$ and $`u`$ go to zero together.
- On the two surfaces where $`K_2=0`$, the leading term of $`c_2`$ is not determined (restricted by the question).
- Item 2 compares $`\mathcal W/g_{\rm c}`$ with $`E_b(0)`$ in the zero of the cost fixed by $`G_i=M_i\sigma^{(i)}_3`$. Couplings to other operators (criterion 6) are not treated.

## Methods used

- Hellmann–Feynman relation (11.5) summed over the rest terms
- Matching coefficients of expressions linear in the gradients
- Expansion in $`\epsilon`$ at fixed $`u`$; Euler-type operator $`u\partial_u-4`$
- Ordered limit and Taylor expansion of coefficients in $`u`$
- Zero set of a quadratic form in the data
