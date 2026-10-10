# Comparison of two ring clocks: joint readings, rates and environment coupling

- **Subproject:** 04-ilang-time
- **Package:** 04-clock-comparison
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-10

## Setup and assumptions

- **Objects.** Two single-object clocks $`K_1,K_2`$, the rest $`R`$, and in item 3 an environment part $`E`$. No two objects have the same type, so $`\mathcal H_{\rm adm}=\mathcal H`$ (1.11): every partition of joint places is an admissible reading, every post-reading state is admissible, and (2.14) applies.
- **Clocks.** For $`i=1,2`$ let $`\omega_i:=2\pi/(N_i\lambda_{0i})`$ and $`Q_i:=\sum_{k=0}^{N_i-1}k\,\lvert f^{(i)}_k\rangle\langle f^{(i)}_k\rvert`$, so $`C_{K_i}=\omega_iQ_i`$. This is (2.9) with $`\alpha_m=0`$, $`\varepsilon=0`$, $`\ell_k=k`$, hence $`\theta_m=0`$ and $`e^{-iC_{K_i}\lambda_{0i}}=S_i`$. By (2.12) with $`c=0`$ the cost spread is minimal. The reading of a clock is its place reading, $`\Pi_m=\lvert m\rangle\langle m\rvert`$.
- **Inputs** (02-clock@v2, quoted in question.md): (2.1) self-drivenness for $`C_\partial=\mathbb 1_K\otimes B`$; (2.4) reading statistics of a self-driven part; (2.9) the ring-clock contracts; (2.12) minimal spread; (2.13) the place distribution $`p(m;\lambda)=\sin^2(\pi\lambda/\lambda_0)/[N^2\sin^2(\pi(\lambda/\lambda_0-m)/N)]`$; (2.14) the view after a place reading, $`V_K\mapsto\lvert m\rangle\langle m\rvert`$.
- **Assumptions.** These are the setting of question.md. All contracts are independent of $`\lambda`$ (A5). Readings are applied at stated values of $`\lambda`$ (A8). Comparing readings at equal $`\lambda`$ uses the order of $`\lambda`$; whether that order can be detected (criterion 8) is not addressed. In item 3, (1.10) requires $`A\otimes B`$ to be a sum of pair terms. This holds, for example, when $`E`$ is a single object. Only the total $`C`$ enters below, so the booking convention of A5 plays no role.
- **Well-definedness (M6).** All results are reading probabilities or parameters of the contract. Common phases (1.2) drop out, and labels play no role because all types differ.
- **Notation.** $`x_i:=\lambda/\lambda_{0i}`$. A reading is *certain* at $`\lambda`$ if one outcome has probability $`1`$. $`\lfloor\cdot\rfloor`$ is the floor function.

## Derivation

### Step 1. Propagator of a minimal ring clock

Take one minimal ring clock with $`N`$ places, tick $`\lambda_0`$ and $`\omega=2\pi/(N\lambda_0)`$. We have $`e^{-iC_K\mu}\lvert f_k\rangle=e^{-2\pi ik\mu/(N\lambda_0)}\lvert f_k\rangle`$ and $`\langle m'\vert f_k\rangle\langle f_k\vert m\rangle=N^{-1}e^{2\pi ik(m'-m)/N}`$. The spectral decomposition then gives

```math
\langle m'\vert e^{-iC_K\mu}\vert m\rangle=u_N\Bigl(m'-m-\frac{\mu}{\lambda_0}\Bigr),\qquad
u_N(y):=\frac1N\sum_{k=0}^{N-1}e^{2\pi iky/N},\qquad
\lvert u_N(y)\rvert^2=P_N(y):=\frac{\sin^2(\pi y)}{N^2\sin^2(\pi y/N)} ,
\qquad\text{(4.1)}
```

where $`P_N`$ takes the value $`1`$ where the denominator vanishes. The modulus follows from the geometric sum, $`\lvert u_N(y)\rvert=\lvert1-e^{2\pi iy}\rvert/(N\lvert1-e^{2\pi iy/N}\rvert)`$, together with $`\lvert1-e^{i\phi}\rvert=2\lvert\sin(\phi/2)\rvert`$. Both $`u_N`$ and $`P_N`$ are $`N`$-periodic, so (4.1) depends on $`m'-m`$ only modulo $`N`$; $`P_N`$ is even. For $`m=0`$, $`P_N(m'-\mu/\lambda_0)`$ is (2.13).

By the triangle inequality, $`\lvert u_N(y)\rvert\le1`$. Equality holds iff all $`w^k`$, $`w=e^{2\pi iy/N}`$, are equal; since $`N\ge2`$, this means $`w=1`$:

```math
P_N(y)=1\iff y\in N\mathbb Z .
\qquad\text{(4.2)}
```

A clock started at $`\lvert m\rangle`$ and driven by $`C_K`$ therefore has a certain reading at $`\mu`$ iff $`\mu/\lambda_0=n\in\mathbb Z`$. The reading is then $`m+n\bmod N`$, in agreement with $`e^{-iC_K\lambda_0}=S`$ (2.9).

### Step 2. Joint distribution of two free clocks (item 1a)

With no term across $`K_1,K_2,R`$, we have $`C=C_{K_1}+C_{K_2}+C_R`$, each term extended by the identity. Operators acting on different factors commute, so $`e^{-iC\lambda}`$ factorizes and $`\lvert\Psi(\lambda)\rangle=e^{-iC_{K_1}\lambda}\lvert0\rangle\otimes e^{-iC_{K_2}\lambda}\lvert0\rangle\otimes e^{-iC_R\lambda}\chi`$. The class $`(m_1,m_2)`$ of the joint reading has the projector $`\Pi_{m_1}\otimes\Pi_{m_2}\otimes\mathbb 1_R`$. By (1.3) and (4.1),

```math
p(m_1,m_2;\lambda)=P_{N_1}(m_1-x_1)\,P_{N_2}(m_2-x_2),\qquad x_i=\lambda/\lambda_{0i}.
\qquad\text{(4.3)}
```

The two readings are independent. Equation (4.3) is (2.4) for the part $`K_1\cup K_2`$, which is self-driven by (2.1) with $`C_\partial=0`$.

### Step 3. Common certain readings (item 1b)

Define the **rate ratio**

```math
\rho:=\frac{\lambda_{01}}{\lambda_{02}},\qquad x_2=\rho\,x_1 .
\qquad\text{(4.4)}
```

1. A product of two numbers in $`[0,1]`$ equals $`1`$ iff both factors do. By (4.3) and (4.2), both readings are certain at $`\lambda`$ iff $`x_1\in\mathbb Z`$ and $`x_2\in\mathbb Z`$. The readings are then $`m_i\equiv x_i\pmod{N_i}`$.
2. If $`\lambda=n_1\lambda_{01}=n_2\lambda_{02}>0`$ with $`n_i\in\mathbb Z_{>0}`$, then $`\rho=n_2/n_1\in\mathbb Q`$. Conversely, let $`\rho=p/q`$ with $`p,q`$ coprime positive integers. Then $`n_1\lambda_{01}=n_2\lambda_{02}`$ iff $`n_1p=n_2q`$. Since $`q`$ divides $`n_1p`$ and $`\gcd(p,q)=1`$, this holds iff $`n_1=jq`$ and $`n_2=jp`$ with $`j\in\mathbb Z_{>0}`$.
3. Hence

```math
\Lambda_{12}=\{\,j\lambda_c : j=1,2,\dots\},\quad \lambda_c:=q\lambda_{01}=p\lambda_{02},\qquad
(m_1,m_2)\big|_{\lambda=j\lambda_c}=\bigl(jq\bmod N_1,\ jp\bmod N_2\bigr),
\qquad\text{(4.5)}
```

```math
\Lambda_{12}\neq\emptyset\iff\rho=\lambda_{01}/\lambda_{02}\in\mathbb Q .
\qquad\text{(4.6)}
```

### Step 4. The reading of $`K_2`$ at the certain readings of $`K_1`$ (item 1c)

1. At $`\lambda=n\lambda_{01}`$ we have $`x_1=n`$ and $`x_2=n\rho`$. By (4.3) and (4.2), $`K_1`$ reads $`n\bmod N_1`$ with certainty, and independently of that reading

```math
p_2(m_2;n\lambda_{01})=P_{N_2}(m_2-n\rho)=\frac{\sin^2(\pi n\rho)}{N_2^2\sin^2\bigl(\pi(n\rho-m_2)/N_2\bigr)} .
\qquad\text{(4.7)}
```

2. If $`n\rho\in\mathbb Z`$, then by (4.2) the reading is certain at $`n\rho\bmod N_2`$.
3. If $`n\rho\notin\mathbb Z`$, the numerator is positive and independent of $`m_2`$, so we minimize $`\sin^2(\pi(m_2-n\rho)/N_2)`$. For each class $`m_2`$, choose the representative $`M\in\mathbb Z`$, $`M\equiv m_2`$, with $`\lvert M-n\rho\rvert\le N_2/2`$. The function $`t\mapsto\sin^2(\pi t/N_2)`$ is even, $`N_2`$-periodic and strictly increasing on $`[0,N_2/2]`$, so the maximum is attained exactly at the classes of the integers nearest to $`n\rho`$. There are two such integers iff $`n\rho\in\mathbb Z+\frac12`$.
4. With $`\delta_n:=\min_{M\in\mathbb Z}\lvert n\rho-M\rvert`$:

```math
m_2^{*}(n)=\begin{cases}\lfloor n\rho+\tfrac12\rfloor\bmod N_2, & n\rho\notin\mathbb Z+\tfrac12,\\[2pt] n\rho\pm\tfrac12\bmod N_2\ \text{(both)}, & n\rho\in\mathbb Z+\tfrac12,\end{cases}\qquad p_{\max}(n)=P_{N_2}(\delta_n).
\qquad\text{(4.8)}
```

The two places in the second case are distinct because $`N_2\ge2`$. In readings, the rate ratio means the following. At the $`n`$-th certain reading of $`K_1`$, the most probable reading of $`K_2`$ is the integer nearest to $`n\rho`$ (mod $`N_2`$): $`K_2`$ advances $`\rho`$ places per place of $`K_1`$. For $`\rho=p/q`$, the certain joint readings (4.5) advance by $`(q,p)`$ from one point of $`\Lambda_{12}`$ to the next. The ratio $`\rho`$ is dimensionless and fixed by the two contracts alone.

### Step 5. Coincidence of two identical clocks (item 2a)

Let $`N_1=N_2=N`$, $`\lambda_{01}=\lambda_{02}=\lambda_0`$ and $`x=\lambda/\lambda_0`$. By (4.3), $`P_=(\lambda)=\sum_{m\in\mathbb Z_N}P_N(m-x)^2`$.

1. By (4.1), $`P_N(m-x)=N^{-2}\sum_{k,k'=0}^{N-1}e^{2\pi i(k-k')(m-x)/N}=N^{-2}\sum_{\lvert d\rvert\le N-1}(N-\lvert d\rvert)\,e^{2\pi id(m-x)/N}`$, since exactly $`N-\lvert d\rvert`$ pairs have $`k-k'=d`$.
2. Square and sum over $`m`$, using $`\sum_m e^{2\pi i(d+d')m/N}=N`$ if $`d+d'\equiv0\pmod N`$ and $`0`$ otherwise. Since $`\lvert d+d'\rvert\le2N-2`$, the surviving terms have $`d+d'\in\{0,\pm N\}`$; for $`d+d'=\pm N`$ they carry the phase $`e^{\mp2\pi ix}`$:
```math
P_==\frac1{N^3}\Bigl[\sum_{\lvert d\rvert\le N-1}(N-\lvert d\rvert)^2+2\cos(2\pi x)\sum_{d=1}^{N-1}d(N-d)\Bigr].
```
3. The first sum is $`N^2+2\sum_{t=1}^{N-1}t^2=N(2N^2+1)/3`$, and $`\sum_{d=1}^{N-1}d(N-d)=N(N^2-1)/6`$. Hence

```math
P_=(\lambda)=\frac{2N^2+1+(N^2-1)\cos(2\pi\lambda/\lambda_0)}{3N^2}=1-\frac{2(N^2-1)}{3N^2}\,\sin^2\frac{\pi\lambda}{\lambda_0} .
\qquad\text{(4.9)}
```

4. Since $`N^2-1>0`$:

```math
\min_\lambda P_==\frac{N^2+2}{3N^2}\ \ \text{at}\ \lambda\in\lambda_0\bigl(\mathbb Z+\tfrac12\bigr),\qquad
P_=(\lambda)=1\iff\lambda\in\lambda_0\mathbb Z .
\qquad\text{(4.10)}
```

### Step 6. A second joint reading; synchronization (item 2b)

At $`\lambda_s`$ the state is $`\psi(\lambda_s)\otimes\psi(\lambda_s)\otimes\chi(\lambda_s)`$. Since $`\Pi_m\psi\propto\lvert m\rangle`$, the outcome $`(m_1,m_2)`$ leaves, by (1.3), the state $`\lvert m_1\rangle\otimes\lvert m_2\rangle\otimes\chi(\lambda_s)`$ up to a common phase, as in (2.14). The evolution (1.9) still factorizes. With $`\mu:=\lambda-\lambda_s`$, (4.1) gives

```math
p(m_1',m_2'\mid m_1,m_2;\lambda)=P_N\Bigl(m_1'-m_1-\frac{\mu}{\lambda_0}\Bigr)\,P_N\Bigl(m_2'-m_2-\frac{\mu}{\lambda_0}\Bigr).
\qquad\text{(4.11)}
```

Put $`j_i:=m_i'-m_i`$. The offset $`\Delta:=m_2-m_1`$ is reproduced, $`\Delta':=m_2'-m_1'\equiv\Delta`$, iff $`j_1\equiv j_2`$. Its probability is $`\sum_jP_N(j-\mu/\lambda_0)^2`$, which is the sum of Step 5 with $`x\to\mu/\lambda_0`$:

```math
\Pr[\Delta'\equiv\Delta]=P_=(\lambda-\lambda_s)=1-\frac{2(N^2-1)}{3N^2}\,\sin^2\frac{\pi(\lambda-\lambda_s)}{\lambda_0} .
\qquad\text{(4.12)}
```

By (4.10), this probability equals $`1`$ iff $`\lambda\in\lambda_s+\lambda_0\mathbb Z_{>0}`$. There the readings are $`(m_1+n,\,m_2+n)`$ with certainty, where $`n=(\lambda-\lambda_s)/\lambda_0`$. Thus one joint reading at any $`\lambda_s`$ synchronizes the two clocks up to the recorded offset $`\Delta`$: they reproduce $`\Delta`$ with certainty on $`\lambda_s+\lambda_0\mathbb Z_{>0}`$. They agree there ($`m_1'=m_2'`$ with certainty) iff $`\Delta=0`$, an outcome of probability $`P_=(\lambda_s)`$. If $`\lambda_s\notin\lambda_0\mathbb Z`$, the reading moves the points of certain readings from $`\lambda_0\mathbb Z`$ to $`\lambda_s+\lambda_0\mathbb Z`$ (Law 1).

### Step 7. One clock in an environment (item 3a)

Let $`C_E\lvert b\rangle=e_b\lvert b\rangle`$ and define $`C_b:=C_{K_1}+bA`$. For every $`\phi\in\mathcal H_{K_1}`$, $`C(\phi\otimes\lvert b\rangle)=\bigl((C_b+e_b)\phi\bigr)\otimes\lvert b\rangle`$. So $`\mathcal H_{K_1}\otimes\lvert b\rangle`$ is invariant under $`C`$, and $`e^{-iC\lambda}`$ acts on it as $`e^{-i(C_b+e_b)\lambda}`$. By (1.7), with the single branch state $`\lvert b\rangle`$,

```math
\lvert\Psi(\lambda)\rangle=e^{-ie_b\lambda}\bigl(e^{-iC_b\lambda}\lvert0\rangle\bigr)\otimes\lvert b\rangle,\qquad
V_{K_1}(\lambda)=e^{-iC_b\lambda}\lvert0\rangle\langle0\rvert e^{iC_b\lambda} .
\qquad\text{(4.13)}
```

The same holds for any start $`\phi\otimes\lvert b'\rangle`$ with $`\lvert b'\rangle`$ a common eigenvector. Self-drivenness in the sense of 02-clock (with $`C_K=C_{K_1}`$ and $`C_\partial=A\otimes B`$):

```math
K_1\ \text{is self-driven}\iff B=0\ \ \text{or}\ \ A\in\mathbb R\,\mathbb 1 .
\qquad\text{(4.14)}
```

*If:* $`A=a\mathbb 1`$ gives $`C_\partial=\mathbb 1\otimes aB`$, and $`B=0`$ gives $`C_\partial=0`$; both are of the form (2.1).

*Only if:* let $`B\neq0`$ and $`A\notin\mathbb R\mathbb 1`$. The commuting self-adjoint operators $`B`$ and $`C_E`$ have a common eigenbasis, and since $`B\ne0`$ it contains some $`\lvert b'\rangle`$ with $`b'\neq0`$. For the starts $`\phi\otimes\lvert b'\rangle`$, (4.13) gives the view $`e^{-iC_{b'}\lambda}\lvert\phi\rangle\langle\phi\rvert e^{iC_{b'}\lambda}`$. Self-drivenness would require $`W(\lambda)=e^{iC_{K_1}\lambda}e^{-iC_{b'}\lambda}`$ to map every ray onto itself. An operator for which every vector is an eigenvector is a scalar, so $`W(\lambda)=c(\lambda)\mathbb 1`$ with $`c=\mathrm{Tr}W/N_1`$ smooth. Differentiating at $`\lambda=0`$ gives $`-ib'A=c'(0)\mathbb 1`$, a contradiction.

So, apart from these cases, $`K_1`$ is not self-driven. For a start in an eigenvector of $`B`$, its view still evolves like that of a self-driven clock, but with the contract $`C_b`$, which depends on the environment eigenvalue $`b`$.

### Step 8. Couplings that keep a minimal ring clock (item 3b)

1. The contract of a minimal ring clock with $`N_1`$ places and tick $`\lambda'`$ is $`\frac{2\pi}{N_1\lambda'}Q_1`$. Since $`Q_1\neq0`$, the contract fixes the tick. The condition reads: for every $`b\in\mathfrak B`$ there is $`\omega(b)>0`$ with $`C_{K_1}+bA=\omega(b)Q_1`$, where $`\omega(b)=2\pi/(N_1\lambda_{01}(b))`$.
2. *Necessity.* $`\mathfrak B`$ has two elements, so it contains some $`b\neq0`$. Then $`A=\frac{\omega(b)-\omega_1}{b}Q_1=\gamma C_{K_1}`$ with $`\gamma:=\frac{\omega(b)-\omega_1}{b\,\omega_1}\in\mathbb R`$. For every $`b'\in\mathfrak B`$, $`(1+\gamma b')\omega_1Q_1=\omega(b')Q_1`$, so $`\omega(b')=(1+\gamma b')\,\omega_1>0`$.
3. *Sufficiency.* If $`A=\gamma C_{K_1}`$ with $`1+\gamma b>0`$ on $`\mathfrak B`$, then $`C_{K_1}+bA=(1+\gamma b)\,\omega_1Q_1`$ is the contract of a minimal ring clock. Hence

```math
A=\gamma\,C_{K_1},\qquad\gamma\in\mathbb R,\qquad 1+\gamma b>0\ \ \text{for all } b\in\mathfrak B,
\qquad\text{(4.15)}
```

```math
\lambda_{01}(b)=\frac{\lambda_{01}}{1+\gamma b} .
\qquad\text{(4.16)}
```

4. By (4.13), the view of $`K_1`$ is then that of a minimal ring clock with tick $`\lambda_{01}(b)`$, and Step 1 applies with $`\lambda_0\to\lambda_{01}(b)`$. Suppose instead that the constant $`\varepsilon`$ of (2.9) is admitted; it changes the state only by a common phase (1.2). The condition then becomes $`C_{K_1}+bA=\varepsilon(b)\mathbb 1+\omega(b)Q_1`$. Since $`Q_1`$ and $`\mathbb 1`$ are linearly independent ($`N_1\ge2`$), the same steps give $`A=\gamma C_{K_1}+a_0\mathbb 1`$ with $`a_0\in\mathbb R`$, and the tick is again (4.16).

### Step 9. Two clocks in one environment (item 3c)

Let $`A_i=\gamma_iC_{K_i}`$ with $`1+\gamma_ib>0`$ on $`\mathfrak B`$. As in Step 7, $`\mathcal H_{K_1}\otimes\mathcal H_{K_2}\otimes\lvert b\rangle`$ is invariant, and $`C`$ acts on it as $`(1+\gamma_1b)C_{K_1}+(1+\gamma_2b)C_{K_2}+e_b`$. The two clock terms act on different factors, so the state is $`e^{-ie_b\lambda}\,e^{-i(1+\gamma_1b)C_{K_1}\lambda}\lvert0\rangle\otimes e^{-i(1+\gamma_2b)C_{K_2}\lambda}\lvert0\rangle\otimes\lvert b\rangle`$. This describes two free minimal ring clocks with ticks $`\lambda_{0i}(b)=\lambda_{0i}/(1+\gamma_ib)`$. Steps 2–4 hold with $`\lambda_{0i}\to\lambda_{0i}(b)`$, and (4.4) becomes

```math
\rho(b)=\frac{\lambda_{01}(b)}{\lambda_{02}(b)}=\rho\,\frac{1+\gamma_2b}{1+\gamma_1b} .
\qquad\text{(4.17)}
```

For $`b\neq b'`$: $`\rho(b)=\rho(b')`$ iff $`(1+\gamma_2b)(1+\gamma_1b')=(1+\gamma_2b')(1+\gamma_1b)`$ iff $`(\gamma_2-\gamma_1)(b-b')=0`$. Hence

```math
\rho(b)\ \text{is the same for all } b\in\mathfrak B\iff\gamma_1=\gamma_2,\quad\text{and then } \rho(b)=\rho .
\qquad\text{(4.18)}
```

Equivalently, $`A_i\otimes B=C_{K_i}\otimes\gamma B`$ with one $`\gamma`$ for both clocks: each clock couples through its own contract with a common strength, whatever $`N_i`$ and $`\lambda_{0i}`$. Written as $`A_i=g_iQ_i`$, the condition reads $`g_1N_1\lambda_{01}=g_2N_2\lambda_{02}`$, so equal coefficients $`g_1=g_2`$ suffice only if $`N_1\lambda_{01}=N_2\lambda_{02}`$. When (4.18) holds, the distribution (4.7) of $`K_2`$ at the certain readings of $`K_1`$ is the same for all $`b\in\mathfrak B`$, although each tick depends on $`b`$.

## Result

- (4.1), (4.2): propagator $`u_N(m'-m-\mu/\lambda_0)`$ of a minimal ring clock, with $`\lvert u_N\rvert^2=P_N`$. A reading is certain iff $`\mu/\lambda_0\in\mathbb Z`$.
- (4.3): two free clocks give independent readings, $`p(m_1,m_2;\lambda)=P_{N_1}(m_1-\lambda/\lambda_{01})P_{N_2}(m_2-\lambda/\lambda_{02})`$.
- (4.4)–(4.6): rate ratio $`\rho=\lambda_{01}/\lambda_{02}`$. Both readings are certain exactly on $`\Lambda_{12}=\lambda_c\mathbb Z_{>0}`$, $`\lambda_c=q\lambda_{01}=p\lambda_{02}`$, with readings $`(jq\bmod N_1,jp\bmod N_2)`$. $`\Lambda_{12}\neq\emptyset`$ iff $`\rho\in\mathbb Q`$.
- (4.7), (4.8): at $`\lambda=n\lambda_{01}`$, $`K_2`$ is distributed as $`P_{N_2}(m_2-n\rho)`$, with most probable place(s) the integer(s) nearest to $`n\rho`$, mod $`N_2`$.
- (4.9), (4.10): identical clocks coincide with probability $`1-\frac{2(N^2-1)}{3N^2}\sin^2(\pi\lambda/\lambda_0)`$. Its minimum is $`(N^2+2)/(3N^2)`$, and it equals $`1`$ iff $`\lambda\in\lambda_0\mathbb Z`$.
- (4.11), (4.12): after a joint reading at $`\lambda_s`$, the readings are distributed as shifted products of $`P_N`$. The offset is kept with probability $`P_=(\lambda-\lambda_s)`$, which is $`1`$ iff $`\lambda\in\lambda_s+\lambda_0\mathbb Z_{>0}`$.
- (4.13), (4.14): in an eigenvector of $`B`$, the view of $`K_1`$ evolves under $`C_b=C_{K_1}+bA`$. $`K_1`$ is self-driven iff $`B=0`$ or $`A\propto\mathbb 1`$.
- (4.15), (4.16): $`C_{K_1}+bA`$ is a minimal ring clock for all $`b\in\mathfrak B`$ iff $`A=\gamma C_{K_1}`$ with $`1+\gamma b>0`$. Then $`\lambda_{01}(b)=\lambda_{01}/(1+\gamma b)`$.
- (4.17), (4.18): in a common environment $`\rho(b)=\rho(1+\gamma_2b)/(1+\gamma_1b)`$, which is independent of $`b`$ iff $`\gamma_1=\gamma_2`$.

## Consistency checks

1. **$`N=2`$.** By (4.1), $`P_2(y)=\cos^2(\pi y/2)`$, so $`P_==\cos^4+\sin^4=1-\frac12\sin^2(\pi x)`$, which is (4.9) with $`\frac{2(N^2-1)}{3N^2}=\frac12`$. Its minimum is $`\frac12=\frac{N^2+2}{3N^2}`$. For $`n\rho\in\mathbb Z+\frac12`$, (4.8) gives both places with $`P_2(\frac12)=\frac12`$. Passed.
2. **$`\lambda_{01}=\lambda_{02}`$ ($`\rho=1`$).** (4.5) gives $`\lambda_c=\lambda_{01}`$ and readings $`(j\bmod N_1,j\bmod N_2)`$. (4.7)–(4.8) give $`K_2`$ certain at $`n\bmod N_2`$ for every $`n`$, consistent with (4.5) and (4.2). For $`N_1=N_2`$, (4.9) equals $`1`$ exactly there. Passed.
3. **Dimensions and $`b=0`$.** By (1.9), $`[C]=[\lambda]^{-1}`$. Since $`A\otimes B`$ has the dimension of $`C_{K_1}`$, $`\gamma b`$ is dimensionless, and (4.16), (4.17) have the dimensions of $`\lambda`$ and $`1`$. At $`b=0`$ they give $`\lambda_{01}`$ and $`\rho`$. For $`\gamma=0`$, (4.14) gives self-drivenness and (4.13) reduces to $`C_b=C_{K_1}`$. Passed.

## Open issues

- Readings take values in $`\mathbb Z_{N_i}`$, so (4.5) and (4.8) give the advances $`jq`$, $`jp`$ and the nearest integer to $`n\rho`$ only modulo $`N_i`$. Recovering $`\rho`$ itself needs a count of turns (a record, or a sequence of readings); this is not derived.
- The statistics of a sequence of joint readings of two different clocks (each reading collapses $`K_2`$ by (2.14)) is not derived.
- Environment states that are superpositions of eigenvectors of $`B`$ are out of scope; in that case the view of $`K_1`$ is not pure.
- Choosing reading values of $`\lambda`$ and comparing readings at equal $`\lambda`$ uses the order of $`\lambda`$ (A8); whether it can be detected is criterion 8. The meaning of $`\gamma_1=\gamma_2`$ for criteria 4–6 is not addressed.

## Methods used

- spectral decomposition and functional calculus
- discrete Fourier analysis on $`\mathbb Z_N`$ (Dirichlet and Fejér-type kernels, orthogonality of characters)
- triangle inequality, monotonicity of $`\sin^2`$
- elementary number theory (coprime integers)
- invariant subspaces of a self-adjoint operator
- partial trace and projective reading (1.3)
