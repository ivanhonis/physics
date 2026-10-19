# Two types of bodies in one background: equal fall and equal clock response

- **Subproject:** 05-ilang-free-fall
- **Package:** 08-two-types
- **Version:** v5
- **Mode:** external regeneration
- **Date:** 2026-10-11

## Changes from previous version

External regeneration after `verification.r2.md` (external round 2; four minor issues, I1–I4). Only the passages that the four issues need are changed. No result of v4 is withdrawn: three statements that were stronger than what is proven are restated with their exact conditions (I1, I2, I4), and one characterization is completed (I3).

All tags (8.1)–(8.28) are kept; the new tag is (8.29). Two displays are restated under their old tags:
- (8.22): the family of descriptions carries a constant $`\beta_0\mathbb 1`$ on the bodies and the medium, and the condition $`\beta'_0=\beta_0-c`$ is added to $`C'_f=C_f+c\,\mathbb 1_f`$ (I3). The other two conditions, $`I`$ and (N) are unchanged.
- (8.13): the second line of v4 is split into two lines. Under (N) the value of $`\theta_i\gamma`$ is not well defined for $`\theta_i\neq0`$, and it is well defined, with the value $`0`$, for an uncoupled type $`\theta_i=0`$ (I4). The first line and the statement for the case in which (N) fails are unchanged.

All other displays, (8.1)–(8.12), (8.14)–(8.21) and (8.23)–(8.28), are unchanged. In particular the table (8.18) and its heading are unchanged; what is restated is the meaning of its entries, in the paragraph below it, with the new display (8.29). Changed passages, in the order of the text:

1. **Header.** Version and mode.
2. **Changes from previous version.** This section.
3. **Response to verification.** It answers I1–I4 of `verification.r2.md`. The section of v4, which answered the first round, is not carried over; its content is recorded in `derivation.v3.md`.
4. **Setup, "Regime and orders" (I2):** the last clause of the bullet "Delimitation"; the bullet "Ideal and finite-width response".
5. **Step 5(c) (I3, I4):**
   - paragraph "The replacements": the data of the family ($`\beta_0`$), the sentence "Item 5 is ...", and the sentence on what the total contract fixes; the display (8.22); one sentence added after it;
   - bullet "(N) holds": the list of replacements; one sentence added before "Those of (8.3) ..." (the constant $`c`$) and two after it (the value of $`\theta_i\gamma`$ for $`\theta_i\neq0`$; an uncoupled type);
   - the display (8.13);
   - bullet "(N) fails": the solution of (8.22) is given with $`c=0`$, and $`\theta_i\gamma`$ is named in the last sentence;
   - bullet "Well defined in every case": one sentence added (an uncoupled type).
6. **Step 8(c) (I1):** in the paragraph after (8.18) the first sentence is replaced by the restated meaning, the new display (8.29) and the paragraph after it. The other sentences of the v4 paragraph follow unchanged, as a paragraph of their own.
7. **Step 8(d) (I1):** one sentence added at the end of the paragraph after (8.20).
8. **Step 8(e) (I1):** in "Relative factor not detectable" the sentence "An equality of the magnitudes ..." is replaced by two sentences.
9. **Result:** item 3, the last sentence (I2); item 5, the sentence on (8.22) and (8.13) (I3, I4); item 6, the bullets for $`\mathfrak E_2`$, $`\mathfrak E_1`$ and $`\mathfrak E\setminus\mathfrak E_2`$ (I1); the line of controls, one control added (I1).
10. **Consistency checks:** check 2, one clause (I1); check 3, one sentence and one clause added (I1, I4).
11. **Open issues:** the sixth item (I2).
12. **JSON twin.**

Everything else is word for word that of v4: the Setup paragraphs "Setting", "Quoted inputs" and "Names", the first paragraph and the first two bullets of "Regime and orders" with (8.26), Steps 1–4, Steps 5(a), 5(b) and 5(d), Steps 6 and 7, the first paragraph of Step 8(c) with the table (8.18) and the display (8.28), the displays (8.19), (8.20), (8.21) and the text around them apart from the sentences named above, the class statement and the items 1, 2 and 4 of the Result, the consistency check 1, the other open issues and "Methods used".

## Response to verification

- **I1: Accepted and fixed in Step 8(c), the paragraph after (8.18) and (8.29); also in Step 8(d), Step 8(e), the Result (item 6) and the consistency checks 2 and 3.** "Same" and "not the same" are now statements about the class: "same" holds for every contract, and "not the same" says that the statement is not the same for every contract. (8.29) gives, for every contract, the truth value in every equivalent description of the last two columns. The truth value of FA can be changed iff $`(\mathrm L_1)`$, $`(\mathrm L_2)`$ and $`g_{\eta,1}g_{\eta,2}>0`$; that of RD iff $`g_{\eta,1}g_{\eta,2}>0`$; that of "$`v_1=v_2`$" for every contract. Otherwise FA fails in every description, and RD holds in every description for $`g_{\eta,1}=g_{\eta,2}=0`$ and fails in every description in the remaining cases. The sentence of Step 8(e) on the need of a convention is restricted to the contracts with these conditions.
- **I2: Accepted and fixed in the Setup ("Delimitation", "Ideal and finite-width response"), the Result (item 3) and the Open issues.** The finite-width rate is that of (3.36), which is quoted to first order in the level spacing of the clock. The bound is now stated as a bound on the width correction of this quoted rate, to that order; it does not control the remainder of the expansion in the level spacing, which is not quoted. That the ideal (wide-start) responses, and with them RL and RD, need no expansion in the level spacing is justified separately.
- **I3: Accepted and fixed in Step 5(c), (8.22).** The family now carries the constant $`\beta_0\mathbb 1`$ on the bodies and the medium, and (8.22) contains $`\beta'_0=\beta_0-c`$, as in (2.20). The list of replacements, the argument for (8.13) and the case in which (N) fails are restated with it.
- **I4: Accepted and fixed in Step 5(c), (8.13); also in the Result (item 5) and the consistency check 3.** Under (N) the value of $`\theta_i\gamma`$ is not well defined for $`\theta_i\neq0`$; for an uncoupled type, $`\theta_i=0`$, it is $`0`$ in every description of the family and therefore well defined. If (N) fails the exception does not apply.

## Setup and assumptions

**Setting (assumptions of this package, M8).** Objects $`b_1`$, $`b_2`$, $`c`$ (and $`f`$ in Step 5) of pairwise different types, one instance each; no swap condition applies and every unit vector is an admissible start. The contract is $`C=F_1+F_2`$ with $`F_i:=C_i+\kappa_i\,\hat x_i\otimes X`$, $`\kappa_i>0`$, and $`C_i`$ of the class $`\mathcal C`$ of 03-clock-and-fall: data $`\tau_i>0`$, $`m_i>0`$, $`N_i\ge2`$, $`\lambda_{0,i}>0`$, linear profiles with the gradients $`g_{m,i}`$, $`g_{\eta,i}`$, $`g_{\zeta,i}`$, $`\mathcal F_i`$ on a chain $`\lvert x\rvert\le L`$, $`L\ge1`$. The start is a product with the medium in $`\chi`$, $`\sigma_X>0`$. All profiles are those of $`C^{\rm eff}_i=C_i+\kappa_i\langle X\rangle\hat x_i`$, (8.19) of 04-ilang-time/08-maximal-speed; so $`\mathcal F_i=\mathcal F^{\rm own}_i-\kappa_i\langle X\rangle`$, with $`\mathcal F^{\rm own}_i`$ the gradient written in $`C_i`$.

**Quoted inputs and the quantities built from them.**
- (17.15) of 03-ilang-space/17-motion: $`u^{(i)}_x=\kappa_i\,x\,e`$, $`d_{0,i}=\kappa_i\sigma_X`$, $`\hat e=e/\sigma_X`$. (5.11) of 04-ilang-time/05-moving-clock at zero gradients: $`v_i=\tau_i\,d_{0,i}`$.
- (3.23): $`r_i(x)=\eta^{(i)}_x/\lambda_{0,i}`$ with $`\eta^{(i)}_x=1+g_{\eta,i}x`$ (wide start $`S_{\rm clock}(x)`$).
- (4.16): $`a^{(i)}_{k,\sigma}(0)=\frac{\tau_i^2}{M^{(i)}_k}\bigl(\sigma\mathcal F_i-G^{(i)}_k\bigr)`$, $`M^{(i)}_k=m_i+d^{(i)}_k`$, $`G^{(i)}_k=m_ig_{m,i}+d^{(i)}_kg_{\eta,i}`$, $`d^{(i)}_k=\frac{2\pi k}{N_i\lambda_{0,i}}`$; $`A^{(i)}_{k,\sigma}:=d_{0,i}\,a^{(i)}_{k,\sigma}(0)`$. Also (4.22), (4.24).
- (5.19), (5.20), (5.25) of 05-rate-comparison; (2.3), (2.20) of 02-field-object; (8.1), (8.20) of 04-ilang-time/08-maximal-speed.

**Regime and orders (A13).** Branch starts at rest; first order in the gradients; the drift acceleration of (4.16) (window average, then a sharp label); records at leading order in $`\kappa_i`$; rates in the wide-start form; $`\lambda\ge0`$. These observables are limits. They exist only in an asymptotic family of chains, starts and windows: with the chain $`\lvert x\rvert\le L`$, a start of the width $`W`$ around $`x_0`$ and an averaging window of the length $`\Lambda`$ in $`\lambda`$,

```math
\epsilon^{\rm g}_i:=L\,\max\Bigl(\lvert g_{m,i}\rvert,\ \lvert g_{\eta,i}\rvert,\ \lvert g_{\zeta,i}\rvert,\ \frac{\lvert\mathcal F_i\rvert}{m_i}\Bigr)\ll1,\qquad1\ll W\ll L,\qquad\Lambda\gg\frac1{m_i},\qquad\lvert x_0\rvert+W+\tau_i\Lambda\ll L .
\qquad\text{(8.26)}
```

- *Meaning of the conditions.* The first three entries of $`\epsilon^{\rm g}_i`$ below $`1`$ are the positivity of the profiles (class $`\mathcal C`$). $`\lvert\mathcal F_i\rvert L\ll m_i`$ is the dimensionless condition on the scalar gradient: the variation of $`V^{(i)}_x`$ over the chain stays below the separation $`2M^{(i)}_k\ge2m_i`$ of the two branches, and $`\mathcal F_i/M^{(i)}_k`$ enters (4.16) as $`g_{m,i}`$ does. $`\Lambda\gg1/m_i`$ averages out the terms that oscillate at the frequencies $`\ge2m_i`$. The last condition keeps the start and its evolution during the window away from the ends of the chain; the labels move by at most $`\tau_i\max_x\zeta^{(i)}_x`$ per unit of $`\lambda`$.
- *Order of the limits.* (i) The first order in the gradients at fixed $`L`$, $`W`$, $`\Lambda`$: $`\varrho_i`$ and $`a^{(i)}_{k,\sigma}(0)`$ are the coefficients of the terms linear in the gradients. (ii) $`L\to\infty`$ at fixed $`x_0`$, $`W`$, $`\Lambda`$ (the chain on $`\mathbb Z`$, A1). (iii) $`\Lambda\to\infty`$. (iv) $`W\to\infty`$ (a sharp label for the fall, a wide start for the rate). The records are taken at leading order in $`\kappa_i`$ at fixed $`\lambda`$, chain and start. On a fixed finite chain (iii) and (iv) cannot be taken, because $`W\le L`$.
- *Delimitation.* Every equality of this package (FA, RL, RD, (8.2)–(8.21)) is an equality between these limiting coefficients. For a finite chain and finite $`W`$, $`\Lambda`$ and gradients it holds up to the errors of the quoted results, which this package does not bound. For one of them, the response of a clock at finite width, it bounds one part:
- *Ideal and finite-width response.* $`\varrho_i`$ is the ideal response, from the wide-start rate. The finite-width rate $`r_W=\frac{\eta_x}{\lambda_0}(1-\varsigma_W)`$ of (3.23) is that of (3.36), which is quoted at zeroth order in the gradients, with the local parameters, and to first order in the level spacing $`\eta^0\frac{2\pi}{N\lambda_0}`$ of the clock. The remainder of this expansion, and the range of the clock parameters and of $`\lambda`$ on which it is small, belong to 03-clock-and-fall and are not quoted. To this order in the level spacing the response at finite $`W`$ is $`\varrho_{i,W}`$, the first order of $`\bigl(r_W(x+1)-r_W(x)\bigr)/r_W(x)`$. By (3.36), $`\varsigma_W`$ depends on $`x`$ through $`\tau^0/\bar\mu`$ only, $`\lvert\partial\varsigma_W/\partial\ln(\tau^0/\bar\mu)\rvert\le2\varsigma_W`$, and the first-order change of $`\ln(\tau^0/\bar\mu)`$ per label is at most $`\lvert g_{\zeta,i}\rvert+\max(\lvert g_{m,i}\rvert,\lvert g_{\eta,i}\rvert)`$. Hence, to first order in the level spacing, $`\lvert\varrho_{i,W}-g_{\eta,i}\rvert\le4\,\frac{\varsigma_W}{1-\varsigma_W}\max(\lvert g_{m,i}\rvert,\lvert g_{\eta,i}\rvert,\lvert g_{\zeta,i}\rvert)`$ with $`\varsigma_W\le\delta_W^2\tau^{0\,2}/m_{x_0}^2=O(W^{-2})`$ by (3.23). This is a bound on the width correction of the quoted rate $`r_W`$. It does not control the terms of second and higher order in the level spacing in the clock statistics of a start of finite width, so it is not a bound on the whole difference between the response of the clock at finite $`W`$ and $`g_{\eta,i}`$. The finite-width response contains $`g_{m,i}`$ and $`g_{\zeta,i}`$; RL and RD are statements about the ideal responses. These use (3.23) in its wide-start form only, which needs no expansion in the level spacing: it is the difference $`\frac N{2\pi}\bigl(E^+_{x_0,k+1}-E^+_{x_0,k}\bigr)`$ of level values, and $`E^+_{x,k}=V_x+m_x+\eta_xd_k`$ is linear in $`k`$. The level values $`\pm\omega_k(p)`$, $`\omega_k(p)=\sqrt{M_k^2+\tau_k^2\sin^2p}`$, are not linear in $`k`$ for $`\sin p\neq0`$ only, and a wide start is concentrated at $`p=0`$.

**Names.** $`(\mathrm L_i)`$: $`\mathcal F_i=m_i(g_{m,i}-g_{\eta,i})`$. FA: the two types fall alike from rest. RL, RD: the clocks respond alike per label, per distance. A tag $`(8.k)`$ without a package name is a tag of this package; the three quoted tags of 04-ilang-time/08-maximal-speed always carry that name. The condition (N) on the field is defined in (8.22); the sets $`\mathfrak E_0\subset\mathfrak E_1\subset\mathfrak E_2\subset\mathfrak E`$ of equivalent descriptions are defined in (8.24), (8.25), (8.27).

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

The second row holds where the ratio exists: every ratio that exists is well defined, because $`s`$ and $`t`$ are common to the two types (there is one $`\lambda`$ and one $`X`$). For $`\tau_i`$, $`\kappa_i`$, $`d_{0,i}`$, $`v_i`$, which are positive, the ratio always exists. $`\varrho_i`$, $`\varrho_i/d_{0,i}`$, $`A^{(i)}_{k,+}`$ and $`A^{(i)}_{k,+}/v_i^2`$ can vanish. For such a quantity $`q_i`$ the ratio $`q_1/q_2`$ exists only for $`q_2\neq0`$; what is well defined in every case is the pair $`(q_1,q_2)`$ up to the common positive factor of (8.3), that is the sign and the vanishing of each $`q_i`$ and the equality $`q_1=q_2`$. The product $`A^{(i)}_{k,+}\,d_{0,i}/v_i^2`$ is well defined as well. Step 7 tests the ratios against a wider class of changes of description.

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

This statement is well defined: both sides scale by $`1/s^2`$ under (8.3), the labels belong to the types (A2), and their orientation is fixed by $`\kappa_i>0`$. It is not a statement about the space of 03-ilang-space (M2): it counts the own positions of each type. Its relation to FA follows from (8.4) and (8.6), which differ by the factors $`\kappa_i`$ and by the condition $`\neq0`$: FA $`\Longrightarrow`$ ((8.6) $`\iff\kappa_1=\kappa_2`$), and (8.6) $`\Longrightarrow`$ (FA $`\iff\kappa_1=\kappa_2`$ and $`g_{\eta,1}\neq0`$). In the first direction the common value is non-zero, so $`\kappa_1\tau_1^2g_{\eta,1}=\kappa_2\tau_2^2g_{\eta,2}`$ and $`\tau_1^2g_{\eta,1}=\tau_2^2g_{\eta,2}`$ hold together iff $`\kappa_1=\kappa_2`$, that is $`d_{0,1}=d_{0,2}`$. In the second direction, if the common value $`-\tau_i^2g_{\eta,i}`$ of (8.6) is non-zero, FA holds iff $`\kappa_1=\kappa_2`$; if it is zero ($`g_{\eta,1}=g_{\eta,2}=0`$), (8.6) holds and FA fails for all $`\kappa_1`$, $`\kappa_2`$, because FA requires $`A\neq0`$.

### Step 3. Clocks respond alike (item 3)

From (8.1) and $`d_{0,i}=\kappa_i\sigma_X`$:

```math
\text{RL}:\ \ \varrho_1=\varrho_2\iff g_{\eta,1}=g_{\eta,2};\qquad\text{RD}:\ \ \frac{\varrho_1}{d_{0,1}}=\frac{\varrho_2}{d_{0,2}}\iff\frac{g_{\eta,1}}{\kappa_1}=\frac{g_{\eta,2}}{\kappa_2} .
\qquad\text{(8.7)}
```

- *Same distance.* Two comparisons are to be kept apart.
  - *Slopes.* Positions $`x`$ and $`x+n`$ of the type $`i`$ are the distance $`\ell=n\,d_{0,i}`$ apart by (17.15) of 03-ilang-space/17-motion, and at first order $`\bigl(r_i(x+n)-r_i(x)\bigr)/r_i(x)=n\varrho_i=\ell\,\varrho_i/d_{0,i}`$. So $`\varrho_i/d_{0,i}`$ is the relative rate difference per distance of the background, and RD is the equality of these two slopes. It is defined for all $`\kappa_1`$, $`\kappa_2`$.
  - *Realizable intervals.* An interval of the type $`i`$ has the length $`n_i\,d_{0,i}`$ with an integer $`1\le n_i\le2L`$. With $`\Delta_i(n_i):=n_i\varrho_i`$ the first-order relative rate difference over it:

```math
\text{RD}\iff n_2\,d_{0,2}\,\Delta_1(n_1)=n_1\,d_{0,1}\,\Delta_2(n_2)\ \ \text{for all }1\le n_1,n_2\le2L;\qquad\text{intervals of equal length exist}\iff n_1\kappa_1=n_2\kappa_2\ \ \text{for some }1\le n_1,n_2\le2L .
\qquad\text{(8.23)}
```

The first part of (8.23) is (8.7) multiplied by $`n_1n_2d_{0,1}d_{0,2}>0`$. If intervals of equal length exist, RD holds iff the relative rate differences over two such intervals, one in the positions of each type, are equal. If none exist (for example $`\kappa_1/\kappa_2=\sqrt2`$, or a rational ratio whose reduced numerator or denominator exceeds $`2L`$), no two realizable intervals have the same length, and RD compares the slopes only: under RD the rate differences over any two intervals are in the ratio of their lengths. RL compares the clocks over $`d_{0,1}`$ for one type and over $`d_{0,2}`$ for the other.

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

**(b)** Insert (8.11) into (8.1)–(8.8); $`\varrho_i=\gamma\theta_i`$, and (8.1) reads $`A^{(i)}_{k,+}=-d_{0,i}\tau_i^2\bigl(\gamma\theta_i+\kappa_i\langle X\rangle/M^{(i)}_k\bigr)`$. The conditions below are written in the form of item 5 (Model D body contracts); for which fields their conditions on $`\theta_i`$ are well defined is determined in (c).
- *$`(\mathrm L_i)`$.* It reads $`\kappa_i\langle X\rangle=0`$, that is $`\langle X\rangle=0`$ ($`\kappa_i>0`$). It contains none of the six numbers and not $`\gamma`$: it is a condition on the start of the medium, the same for both types, and its well-defined form is $`\mathcal F_1=\mathcal F_2=0`$ for the effective contracts. For $`\langle X\rangle\neq0`$ it fails: $`M^{(i)}_0\neq M^{(i)}_1`$ ($`N_i\ge2`$), so $`A^{(i)}_{k,+}`$ depends on the level for every $`\theta_i`$ and $`\gamma`$. Then FA, (8.5) and (8.6), which all require a level-independent fall of each type, fail for all $`\theta_1`$, $`\theta_2`$, $`\gamma`$. The level-dependent term $`-\tau_i^2\kappa_i\langle X\rangle/M^{(i)}_k`$ of $`a^{(i)}_{k,+}(0)`$ is of the first order in $`\kappa_i`$ and of the first order in the gradients: it is the gradient $`\mathcal F_i`$, which the setting counts in $`V^{(i)}_x`$ and which (4.16) keeps. The leading order in the records does not remove it.
- *The other conditions*, for $`\gamma\neq0`$, each with the condition on $`\langle X\rangle`$ under which it holds. RL and RD contain only $`\varrho_i`$ and $`d_{0,i}`$ and do not need $`(\mathrm L_i)`$; neither does $`v_1=v_2`$, which is $`\tau_1\kappa_1=\tau_2\kappa_2`$.

```math
\begin{aligned}
&\text{every }\langle X\rangle,\ \gamma\neq0:\quad\text{RL}\iff\theta_1=\theta_2;\qquad\text{RD}\iff\frac{\theta_1}{\kappa_1}=\frac{\theta_2}{\kappa_2};\\
&\langle X\rangle=0,\ \gamma\neq0:\quad A^{(i)}=-\sigma_X\,\kappa_i\tau_i^2\,\theta_i\,\gamma;\qquad\text{FA and (8.5)}\iff\kappa_1\tau_1^2\theta_1=\kappa_2\tau_2^2\theta_2\neq0;\qquad(8.6)\iff\tau_1^2\theta_1=\tau_2^2\theta_2;\\
&\qquad\qquad\text{FA and RD}\iff\frac{\theta_1}{\kappa_1}=\frac{\theta_2}{\kappa_2}\neq0,\ \ \tau_1\kappa_1=\tau_2\kappa_2;\\
&\langle X\rangle\neq0:\quad(\mathrm L_i),\ \text{FA},\ (8.5),\ (8.6)\ \text{fail for all }\theta_1,\theta_2,\gamma;\qquad A^{(i)}_{k,+}=-\sigma_X\,\kappa_i\tau_i^2\,\theta_i\,\gamma\,\bigl(1+\epsilon^{(i)}_k\bigr),\\
&\qquad\qquad\epsilon^{(i)}_k:=\frac{\kappa_i\,\langle X\rangle}{M^{(i)}_k\,\gamma\theta_i},\qquad\lvert\epsilon^{(i)}_k\rvert\le\epsilon_i:=\frac{\kappa_i\,\lvert\langle X\rangle\rvert}{m_i\,\lvert\gamma\theta_i\rvert}\qquad(\gamma\theta_i\neq0).
\end{aligned}
\qquad\text{(8.12)}
```

For $`\langle X\rangle=0`$, (8.5) adds nothing to FA because $`\mathcal F_i=0`$ and $`g_{m,i}=g_{\eta,i}`$ hold already. For $`\langle X\rangle\neq0`$, $`\epsilon^{(i)}_k`$ is the level-dependent part of $`A^{(i)}_{k,+}`$ relative to the level-independent part; the bound uses $`M^{(i)}_k\ge m_i`$, and $`\epsilon^{(i)}_0\neq\epsilon^{(i)}_1`$. Exactly, $`A^{(1)}_{k,+}/A^{(2)}_{k',+}=\frac{\kappa_1\tau_1^2\theta_1}{\kappa_2\tau_2^2\theta_2}\cdot\frac{1+\epsilon^{(1)}_k}{1+\epsilon^{(2)}_{k'}}`$. So the condition $`\kappa_1\tau_1^2\theta_1=\kappa_2\tau_2^2\theta_2\neq0`$ then gives a fall that is alike only up to the relative deviations $`\epsilon^{(i)}_k`$. They are small on the range $`\kappa_i\lvert\langle X\rangle\rvert\ll m_i\lvert\gamma\theta_i\rvert`$ (with $`\lvert\gamma\theta_i\rvert L\ll1`$ for the first order); at fixed $`\langle X\rangle`$ and $`\gamma\theta_i\neq0`$ the bound $`\epsilon_i`$ is linear in $`\kappa_i`$, and it vanishes for no $`\kappa_i>0`$.

*Dependence on $`\gamma`$.* No condition of the first three lines of (8.12) contains $`\gamma`$: each holds for every sharp value $`\gamma\neq0`$ of the range (8.11) once it holds for one, RL and RD for every $`\langle X\rangle`$ and the others for $`\langle X\rangle=0`$. Only the common value $`A`$ is proportional to $`\gamma`$. For $`\langle X\rangle\neq0`$ the failures of the fourth line hold for every $`\gamma`$, and the accuracy of the approximate statement depends on $`\gamma`$ through $`\epsilon_i\propto1/\lvert\gamma\rvert`$. At $`\gamma=0`$, RL and RD hold trivially and FA fails ($`A=0`$ for $`\langle X\rangle=0`$, a level-dependent fall otherwise).

**(c)** *The replacements.* Let $`b_i:=\hat x_i\otimes\sigma_3\otimes(m_i\mathbb 1_{N_i}+D_i)`$, so that $`B_i=\theta_ib_i`$. Consider the descriptions with the data $`(\beta_0,\beta_i,\theta_i,\Phi,C_f)`$, in which the body contracts are $`C^{\rm D}_i+\beta_ib_i`$ (own gradients $`g_{m,i}=g_{\eta,i}=\beta_i`$) and the part of the contract on the bodies and the medium carries a constant $`\beta_0\mathbb 1`$ (a term that can be counted in any pair term, A5). Item 5 is $`\beta_0=\beta_i=0`$, and (2.20) leads out of it. Split $`\Phi=\bar\varphi\,\mathbb 1_f+\Phi^\circ`$ with $`\bar\varphi:=\mathrm{Tr}\Phi/d_f`$, so $`\mathrm{Tr}\Phi^\circ=0`$. The operators $`\mathbb 1`$, $`b_1`$, $`b_2`$ on the two bodies are linearly independent ($`\mathrm{Tr}b_i=0`$, $`b_i\neq0`$, and they act on different bodies). The total contract therefore fixes the operator on $`\mathcal H_f`$ that multiplies each of $`b_1`$, $`b_2`$, and the operator that multiplies $`\mathbb 1`$; in the latter a constant $`c`$, that of (2.20), can be moved between $`C_f`$ and $`\beta_0`$. Two descriptions of this family, with the same $`b_i`$ and the same terms between bodies and medium, have the same $`C`$ iff

```math
\theta'_i\,\Phi'^\circ=\theta_i\,\Phi^\circ,\qquad\beta'_i+\theta'_i\bar\varphi'=\beta_i+\theta_i\bar\varphi\quad(i=1,2),\qquad C'_f=C_f+c\,\mathbb 1_f,\quad\beta'_0=\beta_0-c\quad(c\in\mathbb R);\qquad(\mathrm N):\ \ I:=\sum_{i=1,2}\theta_i\,b_i\otimes\Phi^\circ\neq0\iff\Phi\notin\mathbb R\,\mathbb 1_f\ \text{and}\ (\theta_1,\theta_2)\neq(0,0).
\qquad\text{(8.22)}
```

The first two conditions state that the operator $`\beta_i\mathbb 1_f+\theta_i\Phi`$, which multiplies $`b_i`$, is the same in the two descriptions; the last two state the same for $`C_f+\beta_0\mathbb 1_f`$, which multiplies $`\mathbb 1`$. $`I`$ is the *interaction part* of $`C`$: the part that is not a sum of an operator on the bodies and the medium and an operator on the field.
- *(N) holds.* Let $`\theta_j\neq0`$. Then $`\theta'_j\Phi'^\circ=\theta_j\Phi^\circ\neq0`$, so $`\Phi'^\circ=t\,\Phi^\circ`$ with $`t:=\theta_j/\theta'_j\neq0`$, and $`\theta'_i=\theta_i/t`$ for both $`i`$. With $`\bar\varphi'=:t\bar\varphi+a`$ the second equation gives $`\beta'_i=\beta_i-a\theta'_i`$. So all replacements are compositions of: (2.20) for two bodies, $`\Phi\to\Phi+a\mathbb 1_f`$, $`C_f\to C_f+c\,\mathbb 1_f`$, $`\beta_i\to\beta_i-a\theta_i`$ (the body contract of the type $`i`$ gets $`-aB_i`$), $`\beta_0\to\beta_0-c`$ (the part on the bodies and the medium gets $`-c\,\mathbb 1`$), which keeps $`\theta_i`$ and gives $`\gamma\to\gamma+a`$, $`e_f\to e_f+c`$; and $`\Phi\to t\Phi`$, $`\theta_i\to\theta_i/t`$, $`\gamma\to t\gamma`$, $`t\neq0`$. There is one $`\Phi`$, so $`a`$ and $`t`$ are common to the two types. The constant $`c`$ enters no $`\theta_i`$ and not $`\gamma`$; it leaves $`e_f+\beta_0`$ unchanged, which enters the evolution through the common phase only (1.2). Those of (8.3) leave $`\theta_i`$ unchanged. For $`\theta_i\neq0`$ the first replacement gives $`\theta_i\gamma\to\theta_i\gamma+a\theta_i`$, which takes every real value. If $`\theta_i=0`$ for one type (an uncoupled type; then $`\theta_j\neq0`$ for the other), then $`\theta'_i=\theta_i/t=0`$ in every description of the family, so $`\theta_i\gamma=0`$ in every one of them. Hence

```math
\begin{aligned}
&\text{under (N), well defined: }\ \theta_1=\theta_2;\quad\text{the pair }(\theta_1,\theta_2)\text{ up to a common factor }t\neq0,\ \text{hence the value of }\theta_1/\theta_2\ \text{for }\theta_2\neq0;\quad\theta_1\,d_{0,2}=\theta_2\,d_{0,1}\ \Bigl(\text{that is }\frac{\theta_1}{d_{0,1}}=\frac{\theta_2}{d_{0,2}}\Bigr);\\
&\text{under (N), the value of }\theta_i\gamma:\quad\text{not well defined for }\theta_i\neq0\ \ (\theta_i\gamma\to\theta_i\gamma+a\theta_i);\qquad\text{well defined, with the value }0,\ \text{for }\theta_i=0\ \ (\text{an uncoupled type});\\
&\text{if (N) fails: none of the four is well defined.}
\end{aligned}
\qquad\text{(8.13)}
```

- *(N) fails.* Then $`I=0`$ and $`C`$ is a sum of an operator on the bodies and the medium and of $`C_f`$: the field does not act on the bodies. (8.22) is solved, with $`c=0`$ ($`C'_f=C_f`$, $`\beta'_0=\beta_0`$), by every $`(\theta'_1,\theta'_2)\in\mathbb R^2`$ with a scalar $`\Phi'=\bar\varphi'\mathbb 1_f`$ and $`\beta'_i=\beta_i+\theta_i\bar\varphi-\theta'_i\bar\varphi'`$. For $`\Phi=0`$ the change $`(\theta_1,\theta_2)=(1,1)\to(2,1)`$ alters no operator of the description. So "$`\theta_1=\theta_2`$", $`\theta_1/\theta_2`$, "$`\theta_1/d_{0,1}=\theta_2/d_{0,2}`$" and $`\theta_i\gamma`$ (which is $`\theta'_i\bar\varphi'`$ in these descriptions, also for $`\theta_i=0`$) take every value among the descriptions of one $`C`$: no coupling can be read from the contract.
- *Well defined in every case.* The gradient of $`C_{\rm red}`$: $`\varrho_i=g_{\eta,i}=\beta_i+\theta_i\gamma=(\beta_i+\theta_i\bar\varphi)+\theta_i(\gamma-\bar\varphi)`$, where $`\theta_i(\gamma-\bar\varphi)`$ is the eigenvalue of $`\theta_i\Phi^\circ`$ on $`\varphi`$. It equals $`\theta_i\gamma`$ only in the descriptions with $`\beta_i=0`$ (Model D body contracts), a convention that fixes the zero of $`\Phi`$. For an uncoupled type under (N), $`\theta_i=0`$, no convention enters: $`\beta'_i=\beta_i`$ and $`\varrho_i=\beta_i`$ in every description. Under (N), differences $`\theta_i(\gamma-\gamma')`$ of two sharp values are well defined; a scalar $`\Phi`$ has one sharp value only.
- *Status of (8.12).* Its conditions on $`\theta_1`$, $`\theta_2`$ are statements about the pair up to a common factor, so they are well defined under (N). If (N) fails they hold in the form $`\beta_i=0`$, which $`C`$ does not fix; the well-defined statements are then those of Steps 1–4 for the gradients of $`C_{\rm red}`$.

**(d)** Let (N) hold. By (8.12), with $`\Theta_i:=v_i^2\theta_i/d_{0,i}=\sigma_X\kappa_i\tau_i^2\theta_i`$: by (8.1) and (8.11), $`A^{(i)}_{k,+}=-\Theta_i\gamma-d_{0,i}\tau_i^2\kappa_i\langle X\rangle/M^{(i)}_k`$, and the second term does not contain the field. With $`\gamma`$, $`\gamma'`$ two sharp values of the range (8.11):

```math
\begin{aligned}
&\text{common coupling for the fall:}\ \ \Theta_1=\Theta_2=:\Theta;\qquad\text{then, for every }\langle X\rangle:\ \ A^{(i)}_{k,+}(\gamma)-A^{(i)}_{k,+}(\gamma')=-\Theta\,(\gamma-\gamma')\ \ \text{for all }k,\ i;\\
&\qquad\langle X\rangle=0:\ \ A^{(i)}_{k,+}=-\Theta\gamma\ \ \text{for all }k,\ i,\ \ \text{and FA}\iff\Theta_1=\Theta_2\neq0\ \ (\gamma\neq0);\qquad\langle X\rangle\neq0:\ \ A^{(i)}_{k,+}=-\Theta\gamma\,\bigl(1+\epsilon^{(i)}_k\bigr)\ \ (\Theta\gamma\neq0),\ \ \text{FA fails};\\
&\text{common coupling for the clocks:}\ \ \frac{\theta_1}{d_{0,1}}=\frac{\theta_2}{d_{0,2}}\qquad(\text{RD for }\gamma\neq0,\ \text{for every }\langle X\rangle).
\end{aligned}
\qquad\text{(8.14)}
```

Both are well defined under (N), by (8.13) and (8.3). They coincide iff $`v_1=v_2`$. The name for the fall rests on the first line, which holds for every $`\langle X\rangle`$: the part of the fall that the field produces is the same for all levels, and it is the same for the two types iff $`\Theta_1=\Theta_2`$; that the whole fall is alike needs $`\langle X\rangle=0`$ and $`\Theta\gamma\neq0`$ in addition. Equal couplings per label, $`\theta_1=\theta_2\neq0`$, are RL only: they give RD iff $`\kappa_1=\kappa_2`$ and, for $`\langle X\rangle=0`$, FA iff $`\kappa_1\tau_1^2=\kappa_2\tau_2^2`$.

If (N) fails, no common coupling is defined: by (c) the numbers $`\theta_i`$, and with them $`\Theta_i`$ and $`\theta_i/d_{0,i}`$, are not fixed by $`C`$. The field then produces no part of the fall and no part of the response of the clocks ($`I=0`$). For a scalar $`\Phi`$ there is one sharp value, so the first line of (8.14) has no content; the fall and the responses are those of Steps 1–4 for the gradients of $`C_{\rm red}`$.

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

The statements of item 6(c) are formulated through the data of a description of the form of the setting. The Lemma lists all equivalent descriptions of that form (the set $`\mathfrak E_0`$). The Theorem after it lists all equivalent descriptions (the set $`\mathfrak E`$); (8.27) states what holds in each of them, and (8.25) what holds in those without a term between the two bodies (the set $`\mathfrak E_2`$).

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

**Theorem (all equivalences).** Let $`Q_i:=\sum_x(-1)^xP^{(i)}_x\otimes\sigma_3\otimes\mathbb 1_{N_i}`$; on the place $`h=(x,s,a)`$, with $`s=\pm1`$, it has the eigenvalue $`q_i(h)=(-1)^xs`$. Then, for the contract of the setting with both bodies of the class $`\mathcal C`$, $`\tau_i>0`$:

```math
\begin{aligned}
&\mathfrak D:=\Bigl\{\Delta=\mathbb 1\otimes\delta_0+Q_1\otimes\delta_1+Q_2\otimes\delta_2+\varepsilon_{12}\,Q_1Q_2\ :\ \delta_j=\delta_j^{\dagger}\ \text{on }\mathcal H_c,\ [\delta_j,X]=0,\ \varepsilon_{12}\in\mathbb R\Bigr\};\\
&\text{medium not read:}\quad(a_1,a_2;C')\ \text{is an equivalence}\iff C'=\frac{F_1}{a_1}+\frac{F_2}{a_2}+\Delta,\ \ \Delta\in\mathfrak D\qquad(\text{all }a_1,a_2>0);\\
&\text{medium read:}\quad\text{the equivalences are those of (5.19), and their }\Delta\text{ are exactly the }\Delta\in\mathfrak D\text{ with }\delta_0,\delta_1,\delta_2\text{ diagonal in the places of the medium};\\
&\mathfrak E:=\{\text{all these }C'\},\qquad\mathfrak E_0:=\{C'\in\mathfrak E:\ \Delta=c\,\mathbb 1\}\quad(\text{the descriptions of the form of the setting, (8.17)}).
\end{aligned}
\qquad\text{(8.24)}
```

*Proof.*

6. *Two classes of places.* Items 1 and 2 use readings of $`b_1`$ only. They hold for every equivalence, the medium read or not, and for every $`C'`$ that is a sum of pair terms. The entries of $`C_1`$ between different places are the clock entries $`s\,\eta_x\langle a\vert D_1\vert a'\rangle\neq0`$ between $`(x,s,a)`$ and $`(x,s,a')`$, and the hopping entries between $`(x,s,a)`$ and $`(x\pm1,-s,a)`$. They join the places of $`b_1`$ into exactly two classes, $`q_1(h)=+1`$ and $`q_1(h)=-1`$. By item 2, $`R_h`$ depends on $`h`$ only through $`q_1(h)`$. $`Q_1`$ is diagonal in the places and constant on the classes, so $`[Q_1,C]=0`$. The same holds for $`b_2`$.
7. *Form of $`C'`$.* $`a_iC'-C`$ is block diagonal in the places of $`b_i`$, so the part of $`C'`$ that is not diagonal in the places of $`b_i`$ is that of $`C_i/a_i`$. Hence $`C'=F_1/a_1+F_2/a_2+\Delta`$ with $`\Delta=\sum_{h_1,h_2}P_{h_1}P_{h_2}\otimes\Delta_{h_1h_2}`$, $`\Delta_{h_1h_2}`$ on $`\mathcal H_c`$. Now $`a_1C'-C=(a_1/a_2-1)F_2+a_1\Delta`$, and $`F_2`$ does not depend on $`h_1`$. By item 6, $`\Delta_{h_1h_2}`$ depends on $`h_1`$ only through $`q_1`$, and likewise on $`h_2`$ only through $`q_2`$: $`\Delta=\delta_0+Q_1\delta_1+Q_2\delta_2+Q_1Q_2\,\delta_{12}`$. Since $`C'`$, $`F_1`$, $`F_2`$ are sums of pair terms and $`\mathrm{Tr}Q_i=0`$, the traceless part of $`\delta_{12}`$, which would be a term of three objects, vanishes: $`\delta_{12}=\varepsilon_{12}\mathbb 1_c`$.
8. *$`[\delta_j,X]=0`$.* By item 1, $`W(\lambda)`$ is unitary and block diagonal in the places of $`b_1`$ for $`\lambda\ge0`$, and $`\dot W=-iW\,e^{-iC\lambda}Re^{iC\lambda}`$. So $`e^{-iC\lambda}Re^{iC\lambda}`$ is block diagonal. Because $`[F_1,F_2]=0`$, $`F_2`$ commutes with $`C`$, and $`e^{-iC\lambda}\Delta e^{iC\lambda}`$ is block diagonal in the places of $`b_1`$ for $`\lambda\ge0`$; so is its second derivative at $`0`$, $`-[C,[C,\Delta]]`$. With $`[Q_i,C]=0`$: $`[C,\Delta]=\sum_i\kappa_i\,\hat x_i\otimes Y`$, $`Y:=[X,\delta_0]+Q_1[X,\delta_1]+Q_2[X,\delta_2]`$, and the part of $`[C,[C,\Delta]]`$ that is not block diagonal in the places of $`b_1`$ is $`\kappa_1J_1Y`$. $`J_1`$ has entries in both classes, so $`J_1`$ and $`J_1Q_1`$ are linearly independent, as are $`\mathbb 1`$ and $`Q_2`$. Hence $`[X,\delta_0]=[X,\delta_1]=[X,\delta_2]=0`$ and $`\Delta\in\mathfrak D`$. For the medium read, (5.19) is complete and its $`\Delta`$ is diagonal in the joint places with $`[C,\Delta]=0`$. The arguments of items 6 and 7, applied to $`[C,\Delta]=0`$, give the form of item 7 with diagonal $`\delta_j`$, and $`\sum_i\kappa_i\hat x_i\otimes Y=0`$ gives $`[X,\delta_j]=0`$. Conversely every such $`\Delta`$ is admitted by (5.19).
9. *Sufficiency, medium not read.* Every $`\Delta\in\mathfrak D`$ commutes with $`F_1`$, $`F_2`$ and with the projectors of every reading of a body, because it is diagonal in the places of the bodies and $`[\delta_j,X]=0`$. By (5.20), $`F_1/a_1+F_2/a_2`$ is an equivalence. Adding $`\Delta`$ multiplies each evolution operator of a schedule by a factor $`e^{-i\Delta\mu}`$. These factors commute with all other factors and combine into one unitary, which does not change the norm that gives the statistics. $`\blacksquare`$

The contract $`C+\varepsilon Q_1`$ is the case $`a_1=a_2=1`$, $`\delta_1=\varepsilon\mathbb 1_c`$: its rest profile is $`m_x+\varepsilon(-1)^x`$, outside the linear profiles.

**What holds in which equivalent descriptions.** Let $`C'=F_1/a_1+F_2/a_2+\Delta\in\mathfrak E`$.
- *Statistics (every $`C'\in\mathfrak E`$).* By the definition of an equivalence with a schedule of one event, for every start the place statistics of $`b_i`$ under $`C'`$ at $`a_i\lambda`$ is that under $`C`$ at $`\lambda`$. So the mean position label and the clock statistics of a given start are the same functions after $`\lambda\to a_i\lambda`$, and a rate obeys $`r'_i=r_i/a_i`$ (5.25). The acceleration of the mean position label is therefore divided by $`a_i^2`$, and so is its drift value for a branch start of $`C`$ (the window $`\Lambda`$ becomes $`a_i\Lambda`$): $`a'^{(i)}_{k,\sigma}(0)=a^{(i)}_{k,\sigma}(0)/a_i^2`$.
- *Contract and records.* The entries of the body contract between different places are those of $`C_i/a_i`$ (item 7), in every $`C'\in\mathfrak E`$; in particular the hopping entries give $`\tau'_i=\tau_i/a_i`$. The operator that multiplies $`P^{(i)}_h`$ in $`C'`$ is $`\frac{\kappa_ix}{a_i}X+q_i(h)\,\bigl(\delta_i+\varepsilon_{12}Q_j\bigr)`$, $`j\neq i`$, plus an operator that does not depend on $`h`$.
  - *$`\varepsilon_{12}=0`$.* There is no contract between the two bodies, and $`C'`$ has the form of the setting of (8.1) of 04-ilang-time/08-maximal-speed: two bodies with the body contracts $`C_i/a_i`$ and a medium, and the record of the place $`h`$ of $`b_i`$ is $`\frac{\kappa_ix}{a_i}X+q_i(h)\,\delta_i`$, an operator on $`\mathcal H_c`$. The term $`\delta_0`$ of the medium alone is counted in the records of one type (A5) and shifts all record vectors of that type by one vector. So the record vector is $`\frac{\kappa_ix}{a_i}e+q_i(h)\,e_i`$ plus a constant, with $`e_i:=(\delta_i-\langle\delta_i\rangle)\chi`$. Two places joined by a hop have equal $`q_i`$ and the distance $`d_{0,i}/a_i`$; two places joined by a clock entry have the distance $`0`$. The bound (5.11) of 04-ilang-time/05-moving-clock at zero gradients is therefore $`\frac{\tau_i}{a_i}\cdot\frac{d_{0,i}}{a_i}`$. The mean position is $`\bar x'_i=\frac{d_{0,i}}{a_i}\bar x_{\rm lab}\hat e+\langle Q_i\rangle e_i`$ plus a constant, and $`\langle Q_i\rangle`$ is conserved.
  - *$`\varepsilon_{12}\neq0`$.* The part $`q_i(h)\,\varepsilon_{12}\,Q_j`$ acts on the other body, and it cannot be moved into the medium: $`Q_1Q_2`$ is traceless in each body and is the identity on the medium, while a pair term between a body and the medium is the identity on the other body. So in every list of pair terms of $`C'`$ the term between $`b_1`$ and $`b_2`$ contains $`\varepsilon_{12}Q_1Q_2`$ (the replacements of A5 move terms of a single object only). The record vectors $`(K_h-\langle K_h\rangle)\chi`$ of (17.15) of 03-ilang-space/17-motion, and the bound (5.11) of 04-ilang-time/05-moving-clock built on their distances, are defined for records that act on the medium, with the medium in $`\chi`$. For this $`C'`$ they are not defined, and neither are $`d'_{0,i}`$, $`v'_i`$, $`\bar x'_i`$ and $`A'^{(i)}_{k,\sigma}`$. This package does not extend these definitions (M2; a term between the two bodies is outside the scope of the question). What is proven for such a $`C'`$ is the bullet "Statistics" and the entries between different places.
- *Effective contracts.* $`(\mathbb 1\otimes\langle\chi\rvert)C'(\mathbb 1\otimes\lvert\chi\rangle)=\sum_i\bigl(C^{\rm eff}_i/a_i+\langle\delta_i\rangle Q_i\bigr)+\varepsilon_{12}Q_1Q_2+\langle\delta_0\rangle`$.

With $`p^{(i)}_h`$ the place weights of the view of $`b_i`$ and $`\bar x^{(i)}_{\rm lab}:=\sum_hx\,p^{(i)}_h`$ the mean position label:

```math
\begin{aligned}
&\text{every }C'\in\mathfrak E,\ \text{every start}:\quad p'^{(i)}_h(\lambda')=p^{(i)}_h\Bigl(\frac{\lambda'}{a_i}\Bigr),\qquad\frac{\mathrm d^2\bar x'^{(i)}_{\rm lab}}{\mathrm d\lambda'^2}(\lambda')=\frac1{a_i^2}\,\frac{\mathrm d^2\bar x^{(i)}_{\rm lab}}{\mathrm d\lambda^2}\Bigl(\frac{\lambda'}{a_i}\Bigr),\qquad r'_i=\frac{r_i}{a_i},\ \ \varrho'_i=\varrho_i,\qquad\tau'_i=\frac{\tau_i}{a_i};\\
&\mathfrak E_2:=\bigl\{C'\in\mathfrak E:\ \varepsilon_{12}=0\bigr\}:\quad\text{no contract between the two bodies; record vectors }u'^{(i)}_h=\frac{\kappa_i\,x}{a_i}\,e+q_i(h)\,e_i+\text{const};\\
&C'\in\mathfrak E\setminus\mathfrak E_2:\quad u'^{(i)}_h,\ d'_{0,i},\ v'_i,\ \bar x'_i,\ A'^{(i)}_{k,\sigma}\ \ \text{are not defined (the record of a place acts on the other body)}.
\end{aligned}
\qquad\text{(8.27)}
```

```math
\begin{aligned}
&\text{every }C'\in\mathfrak E_2,\ \text{every start}:\quad d'_{0,i}=\frac{d_{0,i}}{a_i}\ (\text{per hop}),\qquad v'_i=\frac{v_i}{a_i^2},\qquad r'_i=\frac{r_i}{a_i},\ \ \varrho'_i=\varrho_i,\qquad\frac{\mathrm d^2\bar x'_i}{\mathrm d\lambda'^2}(\lambda')=\frac1{a_i^3}\,\frac{\mathrm d^2\bar x_i}{\mathrm d\lambda^2}\Bigl(\frac{\lambda'}{a_i}\Bigr);\\
&\mathfrak E_1:=\bigl\{C'\in\mathfrak E:\ \varepsilon_{12}=0,\ \langle\chi\vert\delta_1\vert\chi\rangle=\langle\chi\vert\delta_2\vert\chi\rangle=0\bigr\}:\quad C'^{\rm eff}_i=\frac{C^{\rm eff}_i}{a_i}+c_i\,\mathbb 1;\qquad\mathfrak E_0\subset\mathfrak E_1\subset\mathfrak E_2\subset\mathfrak E .
\end{aligned}
\qquad\text{(8.25)}
```

Three forms of the statements of item 6(c) follow.
- *Own-data form:* the statement through the gradients, the condition $`(\mathrm L_i)`$, the levels and the branch starts of the effective body contracts of the description itself. It is defined for $`C'\in\mathfrak E_1`$: there the effective contracts are of the class $`\mathcal C`$ with linear profiles, they have the eigenvectors of $`C^{\rm eff}_i`$, and (8.16) holds for all its entries.
- *Transported form:* the statement for the starts of $`C`$ (its branch starts at rest and its starts $`S_{\rm clock}`$, as vectors; the places belong to the types), with the mean position $`\bar x'_i`$, the hop distance, the bound and the rates of $`C'`$. It is defined for every $`C'\in\mathfrak E_2`$, and by (8.25) $`d_{0,i}`$, $`v_i`$, $`\varrho_i`$ and $`A^{(i)}_{k,+}`$ (the coefficient of $`\hat e`$ in the drift acceleration of $`\bar x'_i`$) follow the rules (8.16). The clock levels are those of $`C`$, since $`\Delta`$ does not act on the clock label. On $`\mathfrak E_1`$ the two forms coincide.
- *Label form:* the statement for the starts of $`C`$ with the quantities of the first line of (8.27) only: the mean position label, the rates, and the entries of $`C'`$ between different places of a body. It contains no record vector, and it is defined for every $`C'\in\mathfrak E`$. RL has a label form. So has (4.24): divided by $`d_{0,i}`$, with $`v_i/d_{0,i}=\tau_i`$, it reads $`a^{(i)}_{k,+}(0)=-\tau_i^2\varrho_i`$. FA, RD and $`v_1=v_2`$ contain $`d_{0,i}`$ and have no label form. On $`\mathfrak E_2`$ the label form of a statement follows from its transported form.
- *Not defined outside $`\mathfrak E_1`$:* the gradients and $`(\mathrm L_i)`$ of the description and its branch starts. For $`\varepsilon_{12}=0`$, $`\langle\delta_i\rangle\neq0`$ the effective contract is $`C^{\rm eff}_i/a_i+\langle\delta_i\rangle Q_i`$, with the rest profile $`m_x/a_i+(-1)^x\langle\delta_i\rangle`$, which is not linear. For $`\varepsilon_{12}\neq0`$ there is a contract between the two bodies and no effective contract of a single body. In addition, for $`e_i\neq0`$ (also inside $`\mathfrak E_1`$) one position label has two record vectors, one for each class $`q_i=\pm1`$.
- *Not defined outside $`\mathfrak E_2`$:* the transported form, because it uses the record vectors; with it FA, RD, "$`v_1=v_2`$" and (4.24) in the form with $`v_{\max}`$ and $`d_0`$.
- *Not determined here:* whether a fall defined through the own stationary starts of a description outside $`\mathfrak E_1`$ has the transported values. Its level blocks have the four eigenvalues $`\pm\omega_k(p)/a_i\pm\langle\delta_i\rangle`$, and (4.16), (4.22), (4.24) are not derived for them. Nor is it determined whether the record vectors can be defined for a description with $`\varepsilon_{12}\neq0`$, and whether they then have the values of (8.25).

### Step 8. What is the same in every equivalent description (items 6c, 6d, 6e)

**(c)** Let $`C'\in\mathfrak E_2`$ with the factors $`a_1`$, $`a_2`$. By (8.25) it acts by (8.16): in the own-data form for $`C'\in\mathfrak E_1`$, in the transported form for every $`C'\in\mathfrak E_2`$. So in it: $`(\mathrm L_i)`$ is unchanged; FA reads $`(\mathrm L_i)`$ and $`A^{(1)}/a_1^3=A^{(2)}/a_2^3\neq0`$; $`v'_1=v'_2`$ reads $`v_1/a_1^2=v_2/a_2^2`$; RL is unchanged; RD reads $`a_1\varrho_1/d_{0,1}=a_2\varrho_2/d_{0,2}`$; and for (4.24) the hypothesis is unchanged ($`a'^{(i)}_{k,+}=a^{(i)}_{k,+}/a_i^2`$) and $`A'^{(i)}=A^{(i)}/a_i^3=-v_i^2\varrho_i/(a_i^3d_{0,i})=-v'^2_i\varrho'_i/d'_{0,i}`$. In the first column below $`a_1=a_2`$ by (8.15). In the other two all $`a_1,a_2>0`$ occur, already in $`\mathfrak E_0`$, and the equivalence $`a_1=2`$, $`a_2=1`$, $`\Delta=0`$ makes a true FA, a true $`v_1=v_2`$ and a true RD with $`\varrho_i\neq0`$ false ($`A'^{(1)}=A/8`$, $`v'_1=v/4`$, $`\varrho'_1/d'_{0,1}=2\varrho_1/d_{0,1}`$).

```math
\begin{aligned}
&\text{proven for: the own-data form and all }C'\in\mathfrak E_1\ (\text{in particular }\mathfrak E_0);\ \text{the transported form and all }C'\in\mathfrak E_2;\\
&\text{for all }C'\in\mathfrak E:\ \text{the rows RL and (4.24) in the label form (8.28); FA, }v_1=v_2\text{ and RD are not defined outside }\mathfrak E_2.\\
&\begin{array}{l|c|c|c}
\text{statement} & \text{read, }X\text{ not diagonal} & \text{read, }X\text{ diagonal} & \text{not read}\\\hline
\text{FA} & \text{same} & \text{not the same} & \text{not the same}\\
v_1=v_2 & \text{same} & \text{not the same} & \text{not the same}\\
\text{RL} & \text{same} & \text{same} & \text{same}\\
\text{RD} & \text{same} & \text{not the same} & \text{not the same}\\
\text{(4.24) for each type} & \text{same} & \text{same} & \text{same}
\end{array}
\end{aligned}
\qquad\text{(8.18)}
```

"Same" means that, for every contract $`C`$ of the class, the statement has the same truth value in $`C`$ and in every $`C'`$ of the named set. "Not the same" means that this does not hold for every contract of the class: for some contracts $`C`$ a description of $`\mathfrak E_0`$ changes the truth value. It does not mean that the truth value can be changed for every $`C`$. In the first column $`a_1=a_2`$, and every row is "same". In the other two columns all $`a_1,a_2>0`$ occur and, by the readings of FA, $`v'_1=v'_2`$ and RD at the beginning of (c), the truth value in $`C'`$ depends on $`C'`$ through $`a_1/a_2`$ only. With $`a_i>0`$, $`d_{0,i}>0`$, $`v_i>0`$, $`\varrho_i=g_{\eta,i}`$ and, under $`(\mathrm L_i)`$, $`A^{(i)}=-d_{0,i}\tau_i^2g_{\eta,i}`$ by (8.2), these readings give for every contract $`C`$ of the class:

```math
\begin{aligned}
&\text{second and third column of (8.18)}\ \ (\text{medium read with }X\text{ diagonal; medium not read}),\ \ C'\in\mathfrak E_2\ \text{with the factors }a_1,a_2\\
&(\text{transported form; own-data form for }C'\in\mathfrak E_1):\\
&\text{FA}:\quad\text{if }(\mathrm L_1),\ (\mathrm L_2)\ \text{and}\ g_{\eta,1}\,g_{\eta,2}>0:\ \ \text{FA holds in }C'\iff\Bigl(\frac{a_1}{a_2}\Bigr)^3=\frac{A^{(1)}}{A^{(2)}};\qquad\text{otherwise FA fails in }C\text{ and in every }C';\\
&v_1=v_2:\quad\text{for every }C:\ \ v'_1=v'_2\iff\Bigl(\frac{a_1}{a_2}\Bigr)^2=\frac{v_1}{v_2};\\
&\text{RD}:\quad\text{if }g_{\eta,1}\,g_{\eta,2}>0:\ \ \text{RD holds in }C'\iff\frac{a_1}{a_2}=\frac{\varrho_2\,d_{0,1}}{\varrho_1\,d_{0,2}};\qquad\text{if }g_{\eta,1}=g_{\eta,2}=0:\ \ \text{RD holds in }C\text{ and in every }C';\\
&\qquad\quad\ \text{otherwise }(g_{\eta,1}\,g_{\eta,2}<0,\ \text{or exactly one }g_{\eta,i}=0):\ \ \text{RD fails in }C\text{ and in every }C' .
\end{aligned}
\qquad\text{(8.29)}
```

For FA: if an $`(\mathrm L_i)`$ fails, FA fails in every $`C'`$, because $`(\mathrm L_i)`$ is unchanged; if both hold, $`A^{(1)}/a_1^3=A^{(2)}/a_2^3\neq0`$ has a solution $`a_1,a_2>0`$ iff $`A^{(1)}`$ and $`A^{(2)}`$ are non-zero and of one sign. In each line of (8.29) with an "iff" exactly one value of $`a_1/a_2`$ makes the statement true, and descriptions with this value and with every other value exist in $`\mathfrak E_0`$; so the truth value can be changed, from true to false and from false to true. Hence, in the second and third column, the truth value of FA can be changed iff $`(\mathrm L_1)`$, $`(\mathrm L_2)`$ and $`g_{\eta,1}g_{\eta,2}>0`$; that of RD iff $`g_{\eta,1}g_{\eta,2}>0`$, that is iff both responses are non-zero and of one sign; that of "$`v_1=v_2`$" for every contract of the class. For a contract for which the condition fails, FA, or RD, has the fixed truth value of (8.29) in $`C`$ and in every $`C'\in\mathfrak E_2`$. RL and (4.24) are the same for every contract in all three columns.

"$`v_1=v_2`$" is the same statement in both forms and is defined on $`\mathfrak E_2`$. For a description outside $`\mathfrak E_1`$ the own-data form of FA, RL, RD and (4.24) is not defined (Step 7), and the table makes no statement about it. For a description outside $`\mathfrak E_2`$ the transported form is not defined either, and the table makes no statement about FA, "$`v_1=v_2`$" and RD in it. What holds for all of $`\mathfrak E`$ is the label form, by (8.27):

```math
\begin{aligned}
&\text{label form, every }C'\in\mathfrak E\ \ (\text{defined: position labels, rates, entries between different places}):\qquad a'^{(i)}_{k,\sigma}(0)=\frac{a^{(i)}_{k,\sigma}(0)}{a_i^2},\quad\varrho'_i=\varrho_i,\quad\tau'_i=\frac{\tau_i}{a_i};\\
&\text{the same in }C\text{ and in every }C'\in\mathfrak E,\ \text{in all three columns of (8.18)}:\\
&\qquad a^{(i)}_{k,+}(0)\ \text{the same for all }k\ \ \bigl(\text{that is }(\mathrm L_i)\bigr),\qquad\mathrm{sign}a^{(i)}_{k,+}(0),\qquad\varrho_i,\qquad\text{RL},\qquad a^{(i)}_{k,+}(0)=-\tau_i^2\,\varrho_i\ \ \text{under }(\mathrm L_i);\\
&\text{FA},\ \text{RD},\ v_1=v_2:\quad\text{no label form; not defined for }C'\in\mathfrak E\setminus\mathfrak E_2 .
\end{aligned}
\qquad\text{(8.28)}
```

The last relation of the second line is the label form of (4.24), with the value of (4.22): $`a'^{(i)}_{k,+}(0)=-\tau_i^2\varrho_i/a_i^2=-\tau'^2_i\varrho'_i`$.

**(d)** Medium not read. By (8.25), in every $`C'\in\mathfrak E_2`$: $`v'_1=v'_2`$ iff $`a_1/a_2=\sqrt{v_1/v_2}`$, which has a solution for every pair, already in $`\mathfrak E_0`$; the common factor left free is the unit of $`\lambda`$. In such a description, with $`a_1=a_2\sqrt{v_1/v_2}`$ and the common speed $`v'=v_2/a_2^2`$,

```math
\begin{aligned}
&\text{medium not read},\ C'\in\mathfrak E_2\ \text{with }a_1=a_2\sqrt{v_1/v_2}\ \ (\text{transported form; own-data form for }C'\in\mathfrak E_1):\\
&A'^{(1)}_{k,+}=\Bigl(\frac{v_2}{v_1}\Bigr)^{3/2}\frac{A^{(1)}_{k,+}}{a_2^3},\quad A'^{(2)}_{k,+}=\frac{A^{(2)}_{k,+}}{a_2^3};\qquad\varrho'_i=\varrho_i;\qquad\frac{\varrho'_1}{d'_{0,1}}=a_2\sqrt{\frac{v_1}{v_2}}\;\frac{\varrho_1}{d_{0,1}},\quad\frac{\varrho'_2}{d'_{0,2}}=a_2\,\frac{\varrho_2}{d_{0,2}};\qquad A'^{(i)}=-v'^2\,\frac{\varrho_i}{d'_{0,i}}\ \ \text{under }(\mathrm L_i).
\end{aligned}
\qquad\text{(8.19)}
```

These hold in the own-data form for $`C'\in\mathfrak E_1`$ and in the transported form for $`C'\in\mathfrak E_2`$. Where the denominators do not vanish they give $`A'^{(1)}_{k,+}/A'^{(2)}_{k',+}=(v_2/v_1)^{3/2}A^{(1)}_{k,+}/A^{(2)}_{k',+}`$ and $`\frac{\varrho'_1/d'_{0,1}}{\varrho'_2/d'_{0,2}}=\sqrt{v_1/v_2}\,\frac{\varrho_1/d_{0,1}}{\varrho_2/d_{0,2}}`$; an acceleration or a response that vanishes in $`C`$ vanishes in every $`C'\in\mathfrak E_2`$. For $`C'\in\mathfrak E\setminus\mathfrak E_2`$ the bound $`v'_i`$ is not defined, so "$`v'_1=v'_2`$" and (8.19) make no statement about it; of (8.19) only $`\varrho'_i=\varrho_i`$ holds there, by (8.27).

A description in which the types fall alike needs a level-independent $`A'^{(i)}_{k,+}=A^{(i)}_{k,+}/a_i^3`$ for each type, that is $`(\mathrm L_i)`$, and $`(a_1/a_2)^3=A^{(1)}/A^{(2)}>0`$. By (8.24) and (8.25) every equivalent description in which FA is defined has the factors and the form used here, and $`\mathrm{sign}A^{(i)}=-\mathrm{sign}g_{\eta,i}`$ by (8.2), so

```math
\text{a description }C'\in\mathfrak E_2\text{ with FA (transported form) exists}\iff(\mathrm L_1),\ (\mathrm L_2)\ \ \text{and}\ \ g_{\eta,1}\,g_{\eta,2}>0 ;\qquad\text{in it}\quad\frac{v'_1}{v'_2}=\frac{v_1}{v_2}\Bigl(\frac{A^{(2)}}{A^{(1)}}\Bigr)^{2/3} .
\qquad\text{(8.20)}
```

(8.20) holds with "equivalent description" read as: a description of $`\mathfrak E_0`$; a description of $`\mathfrak E_1`$ with FA in the own-data form; a description of $`\mathfrak E_2`$ with FA in the transported form. The condition is the same in the three readings. In a description of $`\mathfrak E\setminus\mathfrak E_2`$ FA is not defined, and (8.20) makes no statement about it. The condition of (8.20) is the condition of (8.29) under which the truth value of FA can be changed; where it fails, FA fails in $`C`$ and in every $`C'\in\mathfrak E_2`$.

**(e)** *Relative factor detectable.* By (8.24) all equivalent descriptions are $`C/\alpha+\Delta`$ with $`\Delta\in\mathfrak D`$; those of $`\mathfrak E_0`$ are $`C/\alpha+c`$: a change of the unit of $`\lambda`$, (8.3) with $`s=\alpha`$. FA, $`v_1=v_2`$, RL, RD and every ratio of (8.3) that exists mean the same in $`C`$ and in every $`C'`$ of the named set, as in Steps 2–4: in the own-data form on $`\mathfrak E_1`$, in the transported form on $`\mathfrak E_2`$. For $`C'\in\mathfrak E\setminus\mathfrak E_2`$ only the label form is defined: the statements of (8.28) and, because $`a_1=a_2`$ here, the equality (8.6) of the accelerations in position labels mean the same in $`C`$ and in $`C'`$, while FA, RD and $`v_1=v_2`$ are not defined in it.

*Relative factor not detectable.* By (8.16) and (8.25) the following are the same in $`C`$ and in every $`C'`$ of the named set (own-data form on $`\mathfrak E_1`$, transported form on $`\mathfrak E_2`$): $`(\mathrm L_i)`$, $`\mathrm{sign}A^{(i)}`$ (the direction of the fall along $`\hat e`$), $`\varrho_i`$, the relation (4.24) of each type, RL, and the numbers $`A^{(i)}/v_i^{3/2}`$. For every $`C'\in\mathfrak E`$ the first five are the same in the label form (8.28), with $`\mathrm{sign}a^{(i)}_{k,+}(0)`$ in the place of $`\mathrm{sign}A^{(i)}`$; the numbers $`A^{(i)}/v_i^{3/2}`$ are not defined outside $`\mathfrak E_2`$. By (8.29), an equality of the magnitudes of the falls of a pair with $`(\mathrm L_1)`$, $`(\mathrm L_2)`$ and $`g_{\eta,1}g_{\eta,2}>0`$, and an equality of the responses per distance of a pair with $`g_{\eta,1}g_{\eta,2}>0`$, has a meaning only relative to a convention that fixes $`a_1/a_2`$. For a pair for which the respective condition fails, FA, or RD, has the truth value fixed in (8.29) in every description of $`\mathfrak E_2`$ and needs no convention. With the convention of equal maximal speeds, $`v'_1=v'_2`$, which is defined on $`\mathfrak E_2`$, FA and RD become by (8.8) one statement that no description of $`\mathfrak E_2`$ changes:

```math
\begin{aligned}
&\text{the same in }C\text{ and in every }C'\in\mathfrak E_2\ \ (\text{transported form; own-data form for }C'\in\mathfrak E_1):\\
&(\mathrm L_1),\ (\mathrm L_2)\quad\text{and}\quad\frac{A^{(1)}}{v_1^{3/2}}=\frac{A^{(2)}}{v_2^{3/2}}\neq0\iff(\mathrm L_1),\ (\mathrm L_2)\quad\text{and}\quad\varrho_1\sqrt{\frac{\tau_1}{\kappa_1}}=\varrho_2\sqrt{\frac{\tau_2}{\kappa_2}}\neq0 .
\end{aligned}
\qquad\text{(8.21)}
```

The second form uses $`A^{(i)}/v_i^{3/2}=-\varrho_i\sqrt{\tau_i/d_{0,i}}`$ from (8.2). Without a convention, "fall alike" can only mean (8.20): each type falls level-independently, and both in the same direction. The equal maximal speed is then a convention, not a condition (M7). In the label form this last meaning is defined for every $`C'\in\mathfrak E`$: by (8.28), $`(\mathrm L_i)`$ and the signs of $`a^{(i)}_{k,+}(0)`$ are the same in all of them.

## Result

Class: all pairs of bodies of the class $`\mathcal C`$ with linear profiles, all $`\kappa_i>0`$, every $`X`$, $`\chi`$ with $`\sigma_X>0`$. The results are equalities between the limiting coefficients of the asymptotic family (8.26): branch starts at rest, first order in the gradients ($`\epsilon^{\rm g}_i\ll1`$, which includes $`\lvert\mathcal F_i\rvert L\ll m_i`$), then a long chain, a long window, a sharp label and a wide start, at leading order in $`\kappa_i`$. On a fixed finite chain they hold up to the errors of the quoted results. Item 5: all pairs of Model D bodies, all $`\theta_i`$, every sharp stationary field state in the range (8.11); the statements about couplings hold for the fields with (N) of (8.22).

1. **One type.** (8.1): $`\varrho_i=g_{\eta,i}`$. (8.2): level-independent fall iff $`(\mathrm L_i)`$, value $`-v_i^2\varrho_i/d_{0,i}`$. (8.3) with its table: of the eight quantities only $`\varrho_i`$ is well defined; every ratio between the types that exists is well defined, and for the quantities that can vanish the pair up to a common positive factor is.
2. **Fall alike.** (8.4) in the data and through $`v_i`$ and the responses; (8.5) for both branches; (8.6) for the labels, well defined but not a statement about distances.
3. **Clocks.** (8.7); RD is the equality of the responses per distance and is defined for all $`\kappa_i`$; by (8.23) it compares two realizable intervals of equal length only if $`n_1\kappa_1=n_2\kappa_2`$ for integers $`1\le n_i\le2L`$. RL uses no common $`\lambda`$ of the two types, RD does. Both are statements about the ideal (wide-start) responses, which need no expansion in the level spacing of the clock. For the finite-width rate $`r_W`$ of (3.36), which is quoted to first order in the level spacing, the response differs from the ideal one by at most $`4\frac{\varsigma_W}{1-\varsigma_W}\max(\lvert g_{m,i}\rvert,\lvert g_{\eta,i}\rvert,\lvert g_{\zeta,i}\rvert)`$; this bounds the width correction to that order and does not control the remainder of the expansion in the level spacing.
4. **Relation.** (8.8): neither implies the other; controls (8.9); with $`(\mathrm L_i)`$ and $`\varrho_i\neq0`$, any two of FA, RD, $`v_1=v_2`$ imply the third.
5. **Common field.** Generator (8.10), gradients and range (8.11). Conditions (8.12): RL and RD are conditions on the six numbers for every $`\langle X\rangle`$; $`(\mathrm L_i)`$ is $`\langle X\rangle=0`$, a condition on the start of the medium; FA, (8.5) and (8.6) are conditions on the six numbers exactly for $`\langle X\rangle=0`$, and none of these conditions contains $`\gamma`$. For $`\langle X\rangle\neq0`$, FA, (8.5) and (8.6) fail for all couplings, and the fall is alike only up to the relative deviations $`\epsilon^{(i)}_k`$, $`\lvert\epsilon^{(i)}_k\rvert\le\kappa_i\lvert\langle X\rangle\rvert/(m_i\lvert\gamma\theta_i\rvert)`$. Replacements (8.22), with the constant that can be moved between $`C_f`$ and the part on the bodies and the medium, and their consequence (8.13): "$`\theta_1=\theta_2`$", the pair $`(\theta_1,\theta_2)`$ up to a common factor and "$`\theta_1/d_{0,1}=\theta_2/d_{0,2}`$" are well defined exactly for the fields with (N), that is $`\Phi\notin\mathbb R\mathbb 1_f`$ and $`(\theta_1,\theta_2)\neq(0,0)`$; under (N) the value of $`\theta_i\gamma`$ is not well defined for $`\theta_i\neq0`$, and it is $`0`$ in every description for an uncoupled type, $`\theta_i=0`$; if (N) fails, the field does not act on the bodies and no coupling statement is well defined. Common couplings (8.14), under (N): for the fall $`\Theta_1=\Theta_2`$, which makes the part of the fall produced by the field equal for all levels and both types for every $`\langle X\rangle`$, and the whole fall for $`\langle X\rangle=0`$; for the clocks $`\theta_1/d_{0,1}=\theta_2/d_{0,2}`$, for every $`\langle X\rangle`$.
6. **Equivalent descriptions.** Detectability (8.15); rules (8.16); the equivalent descriptions of the form of the setting, $`\mathfrak E_0`$, (8.17); all equivalent descriptions, $`\mathfrak E`$, (8.24): $`C'=F_1/a_1+F_2/a_2+\Delta`$ with $`\Delta\in\mathfrak D`$. The statements about them are proven for the nested sets $`\mathfrak E_0\subset\mathfrak E_1\subset\mathfrak E_2\subset\mathfrak E`$, each with the quantities that are defined in it:
   - *All of $`\mathfrak E`$, (8.27) and (8.28).* Defined: the position labels, the rates, the entries between different places of a body. For every start the place statistics, the mean position label and the rates are those of $`C`$ after $`\lambda\to a_i\lambda`$, and $`\tau'_i=\tau_i/a_i`$. The same in $`C`$ and in every $`C'\in\mathfrak E`$, with the medium read or not (label form): the level-independence of the acceleration in position labels (that is $`(\mathrm L_i)`$), its sign, $`\varrho_i`$, RL, and (4.24) in the form $`a^{(i)}_{k,+}(0)=-\tau_i^2\varrho_i`$.
   - *$`\mathfrak E_2`$ (no term between the two bodies, $`\varepsilon_{12}=0`$), (8.25).* Defined in addition: the record vectors in the medium, the hop distance, the bound and the mean position; they follow (8.16). The table (8.18), the values (8.19), the existence condition (8.20) and the meaning (8.21) are proven in the transported form (the starts of $`C`$) for all $`C'\in\mathfrak E_2`$. In (8.18), "same" holds for every contract of the class, and "not the same" says that the statement is not the same for every contract. (8.29) gives the truth value in every $`C'\in\mathfrak E_2`$ for every contract: with $`X`$ diagonal or the medium not read, the truth value of FA can be changed iff $`(\mathrm L_1)`$, $`(\mathrm L_2)`$ and $`g_{\eta,1}g_{\eta,2}>0`$, that of RD iff $`g_{\eta,1}g_{\eta,2}>0`$, and that of "$`v_1=v_2`$" for every contract; otherwise FA fails in every description, and RD holds in every description for $`g_{\eta,1}=g_{\eta,2}=0`$ and fails in every description in the remaining cases.
   - *$`\mathfrak E_1\supset\mathfrak E_0`$ (effective body contracts $`C^{\rm eff}_i/a_i+c_i`$).* Defined in addition: the gradients, $`(\mathrm L_i)`$ and the branch starts of the description itself. (8.18)–(8.21) and (8.29) are proven in the own-data form for all $`C'\in\mathfrak E_1`$.
   - *$`\mathfrak E\setminus\mathfrak E_2`$ ($`\varepsilon_{12}\neq0`$).* The record of a place of one body acts on the other body. The record vectors, the distances, the bound and the mean position are not defined, so FA, RD and "$`v_1=v_2`$" are not defined, and (8.18)–(8.21) and (8.29) make no statement about such a description beyond (8.28).
   - Outside $`\mathfrak E_1`$ the own-data form is not defined (no linear profiles, or a contract between the bodies), and it is not determined whether a fall defined through the own starts of such a description has the transported values.

Controls (M9): K1, K2 of (8.9); the columns of (8.18) (medium read against not read, $`X`$ diagonal against not diagonal); a pair with all gradients zero (FA fails and RD holds in every description) against K2 (both can be changed) for (8.29); $`\Phi=0`$ with $`(\theta_1,\theta_2)=(1,1)\to(2,1)`$ for (8.13); $`C+\varepsilon Q_1`$ for (8.17) against (8.24); $`\kappa_1/\kappa_2=\sqrt2`$ for (8.23); $`C+\varepsilon_{12}Q_1Q_2`$ for (8.25) against (8.27).

## Consistency checks

1. **Dimensions and $`a_1=a_2`$.** With costs in units of $`1/\lambda`$: $`d_{0,i}\sim\lambda^{-1}`$, $`v_i\sim\lambda^{-2}`$, $`A\sim\lambda^{-3}`$, and (8.2) gives $`\lambda^{-4}/\lambda^{-1}`$. The rules (8.16) with $`a_1=a_2=s`$ are (8.3) with $`t=1`$, and then every row of (8.18) is "same", as in its first column. Passed.
2. **Identical data.** For $`\tau_1=\tau_2`$, $`\kappa_1=\kappa_2`$ and equal gradients: $`v_1=v_2`$, RL and RD hold, and (8.4) reduces to $`(\mathrm L)`$ and $`g_\eta\neq0`$, as (8.8) states. With the medium not read, (5.20) with $`a_1\neq a_2`$ still gives a description without FA, as (8.18) states and as (8.29) gives with $`A^{(1)}=A^{(2)}\neq0`$. The contract $`C+\varepsilon Q_1`$ with $`a_1=a_2=1`$ is (8.24) with $`\delta_1=\varepsilon\mathbb 1_c`$: $`Q_1`$ commutes with $`C`$ because a hop changes $`(-1)^x`$ and $`s`$ together. For $`\varepsilon\neq0`$ it lies in $`\mathfrak E_2\setminus\mathfrak E_1`$, and (8.25) gives it the unchanged transported values, as its unchanged place statistics requires. The contract $`C+\varepsilon_{12}Q_1Q_2`$ lies in $`\mathfrak E\setminus\mathfrak E_2`$: its evolution operator is $`e^{-iC\lambda}e^{-i\varepsilon_{12}Q_1Q_2\lambda}`$, and the second factor is diagonal in the joint places and commutes with $`C`$, so every statistic is that of $`C`$, as (8.27) states with $`a_1=a_2=1`$. (8.25) makes no statement about it. Passed.
3. **One gradient zero.** For $`g_{\eta,2}=0`$ and $`(\mathrm L_2)`$: $`A^{(2)}=0`$, so FA fails by (8.4), RD holds iff $`g_{\eta,1}=0`$ by (8.7), and no equivalent description with FA exists by (8.20), in each of its three readings, in agreement with $`A'^{(2)}=A^{(2)}/a_2^3=0`$. This is a case of (8.29) in which no truth value of FA or RD can be changed: in every $`C'\in\mathfrak E_2`$ FA fails, and RD reads $`a_1\varrho_1/d_{0,1}=0`$, which holds iff $`g_{\eta,1}=0`$, as in $`C`$. In item 5 with $`\theta_2=0`$, $`\theta_1\neq0`$ and $`\Phi\notin\mathbb R\mathbb 1_f`$, (N) holds: the pair $`(\theta_1,0)`$ up to a factor is well defined, the quotient $`\theta_1/\theta_2`$ does not exist, and (8.11) gives $`\varrho_2=0`$; the type 2 is uncoupled and $`\theta_2\gamma=0`$ in every description, while $`\theta_1\gamma`$ is not well defined, as (8.13) states. Passed.

## Open issues

- Item 5: with Model D body contracts the effective gradient is $`\mathcal F_i=-\kappa_i\langle X\rangle`$, so the conditions for the fall in (8.12) and (8.14) are exact only for $`\langle X\rangle=0`$, a condition on the start of the medium and not on the six numbers. For $`\langle X\rangle\neq0`$ the fall of each type depends on the level and FA fails for all couplings; (8.12) gives the size of the level-dependent part and the range on which it is small.
- Outside $`\mathfrak E_1`$ (a staggered rest term $`\langle\delta_i\rangle Q_i`$, or a term $`\varepsilon_{12}Q_1Q_2`$ between the bodies) the statements in the own data of the description are not defined: (4.16), (4.22), (4.24) and (3.23) are not derived for such contracts. Whether a fall defined through the own stationary starts of such a description has the transported values of (8.25), or for $`\varepsilon_{12}\neq0`$ the label values of (8.27), is not determined here.
- For $`\varepsilon_{12}\neq0`$ (the set $`\mathfrak E\setminus\mathfrak E_2`$) the record of a place of one body acts on the other body. The record vectors, the distances, the bound and the mean position of 03-ilang-space and 04-ilang-time are quoted for records that act on the medium, and they are not defined for such a description; FA, RD, "$`v_1=v_2`$" and (8.19)–(8.21) are therefore not stated for it. Whether these notions can be extended to a description with a contract between the bodies, and whether they then take the values of $`C'-\varepsilon_{12}Q_1Q_2\in\mathfrak E_2`$, which has the same statistics for every schedule, is not determined here. A term between the two bodies is outside the scope of the question.
- The transported form and the label form refer to the starts of $`C`$. That the wide-start rate (3.23) follows (5.25) in every $`C'\in\mathfrak E`$ uses that it is a rate of a rule with the property (R), as the question presupposes by quoting (5.25) for item 6.
- If (N) fails, no coupling of the two types to the field is defined. A comparison of couplings needs a field operator that is not a multiple of $`\mathbb 1_f`$ and at least one non-zero coupling.
- All results are of first order in the gradients, from rest and at leading order in the records, and are equalities between the limiting coefficients of (8.26). The errors at finite $`L`$, $`W`$, $`\Lambda`$ are not bounded here. For the finite-width response only the width correction of the rate $`r_W`$ of (3.36) is bounded, to first order in the level spacing of the clock; the remainder of the expansion in the level spacing at finite $`W`$ is not quoted and is not bounded. The fall in motion, the lattice terms and a field that is not sharp are out of scope.
- The convention $`v'_1=v'_2`$ in (8.21) is a choice. Whether anything in the language selects it belongs to criterion 10.

## Methods used

- Level-independence conditions of the drift acceleration (linear algebra in the level index)
- Scaling analysis under changes of the unit of the evolution parameter and of operator normalisations
- Invariance under replacements of contract terms at fixed total contract
- Reduction of a contract on an eigenstate of the field operators
- Decomposition of an operator into scalar and traceless parts; linear independence of tensor factors
- Operator identities from equal reading statistics (polarisation), expansion of unitary groups to second order
- Connectivity argument for operators commuting with a hopping contract; the conserved operators of its classes of places
- Asymptotic families and order of limits
