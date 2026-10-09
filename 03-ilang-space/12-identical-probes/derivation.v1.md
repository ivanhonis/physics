# Identical probes: Law 5 for the records, single-instance and pair distances

- **Subproject:** 03-ilang-space
- **Package:** 12-identical-probes
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

- **Objects and spaces.** The probes $`p_1,p_2`$ are of type $`T`$ with $`d_T\ge2`$. The medium $`c`$ is the only instance of its type. $`\mathcal H=\mathcal H_T\otimes\mathcal H_T\otimes\mathcal H_c`$ in the order $`p_1,p_2,c`$. In $`\lvert ab\rangle\otimes\xi`$, $`a`$ is the place of $`p_1`$, $`b`$ the place of $`p_2`$, and $`\xi\in\mathcal H_c`$.
- **Contracts.** $`C=C^{(1)}+C^{(2)}`$, with $`C^{(1)}:=\sum_h\lvert h\rangle\langle h\rvert_{p_1}\otimes K^{(1)}_h`$ and $`C^{(2)}:=\sum_h\lvert h\rangle\langle h\rvert_{p_2}\otimes K^{(2)}_h`$ (identity on the other probe). Write $`\Delta_h:=K^{(1)}_h-K^{(2)}_h`$. When $`\Delta_h`$ does not depend on $`h`$ it is written $`\Delta`$, and $`K_h:=K^{(1)}_h`$. All operators are $`\lambda`$-independent (A5).
- **Admissible subspace.** $`c`$ is the only instance of its type, so (1.11) constrains only the pair $`(p_1,p_2)`$. I read $`\mathcal H_{\rm adm}`$ as the set of all vectors that obey (1.11): $`\mathcal H_{\rm adm}=\{\Psi:P_{12}\Psi=c_T\Psi\}`$. Its orthogonal projector is $`\Pi=\tfrac12(\mathbb 1+c_TP_{12})`$, and $`\Pi^\perp=\mathbb 1-\Pi`$ ($`P_{12}`$ is unitary and self-adjoint, $`P_{12}^2=\mathbb 1`$). Assumption: the description imposes no further restriction.
- **Medium notation.** $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$ and $`Q_\chi:=\mathbb 1_c-\lvert\chi\rangle\langle\chi\rvert`$. As in (5.10), $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle=Q_\chi K_h\lvert\chi\rangle`$.
- **Inputs, as quoted in question.md.**
  - From 02: (2.1), (2.2), (2.11), (2.16).
  - From 03: $`\approx`$, $`X_V`$, $`\alpha`$, (3.4), (3.5).
  - From 05: (5.10).
  - From 11: (11.6), (11.8) and the hypotheses of 11.
  - $`\alpha(h,h';\lambda):=\arccos\sqrt{W(h,h';\lambda)}`$ is evaluated on representatives, as in (3.5), (5.10) and (11.8).
- **Validity.** Item 1 holds for every $`\lambda`$. Items 2 and 3 are leading order, $`\lambda\to0^+`$. Item 4 holds at $`\lambda=0`$. Finite dimension throughout (A1).

## Derivation

### Step 1. The swap defect of $`C`$

$`C(\lvert ab\rangle\otimes\xi)=\lvert ab\rangle\otimes(K^{(1)}_a+K^{(2)}_b)\xi`$ and $`P_{12}(\lvert ab\rangle\otimes\xi)=\lvert ba\rangle\otimes\xi`$. Hence $`P_{12}CP_{12}(\lvert ab\rangle\otimes\xi)=\lvert ab\rangle\otimes(K^{(1)}_b+K^{(2)}_a)\xi`$, and

```math
D:=P_{12}CP_{12}-C=\sum_{a,b}\lvert ab\rangle\langle ab\rvert\otimes\bigl(\Delta_b-\Delta_a\bigr),
\qquad
D(\lvert ab\rangle\otimes\xi)=\lvert ab\rangle\otimes(\Delta_b-\Delta_a)\xi .
\qquad\text{(12.1)}
```

### Step 2. Invariance of $`\mathcal H_{\rm adm}`$ (item 1a)

(i) *Group and generator.* Suppose $`e^{-iC\lambda}\mathcal H_{\rm adm}\subseteq\mathcal H_{\rm adm}`$ for all $`\lambda`$. A subspace of a finite-dimensional space is closed, so the derivative at $`\lambda=0`$ gives $`C\mathcal H_{\rm adm}\subseteq\mathcal H_{\rm adm}`$. Conversely, $`C`$-invariance implies $`C^n`$-invariance, so the exponential series stays in $`\mathcal H_{\rm adm}`$.

(ii) *Generator.* For $`\Psi\in\mathcal H_{\rm adm}`$ we have $`P_{12}\Psi=c_T\Psi`$ and $`c_T^2=1`$, so

```math
D\Psi=c_TP_{12}C\Psi-C\Psi=-2\,\Pi^\perp C\Psi .
\qquad\text{(12.2)}
```

Hence $`D\mathcal H_{\rm adm}=0\iff\Pi^\perp C\Pi=0\iff C\mathcal H_{\rm adm}\subseteq\mathcal H_{\rm adm}`$. By (i), this is invariance for every $`\lambda`$. The argument holds for either family and for any $`C`$.

(iii) *This setting.* If $`\Delta_h=\Delta`$ for all $`h`$, then $`D=0`$ by (12.1). Conversely, let $`D\mathcal H_{\rm adm}=0`$. Take $`a\neq b`$ (possible since $`d_T\ge2`$) and any $`\xi`$. The vector $`\Psi=\lvert ab\rangle\otimes\xi+c_T\lvert ba\rangle\otimes\xi`$ is admissible, and by (12.1) $`D\Psi=\lvert ab\rangle\otimes(\Delta_b-\Delta_a)\xi-c_T\lvert ba\rangle\otimes(\Delta_b-\Delta_a)\xi`$. Since $`\lvert ab\rangle\perp\lvert ba\rangle`$, $`D\Psi=0`$ forces $`(\Delta_b-\Delta_a)\xi=0`$ for every $`\xi`$. Hence, for $`c_T=\pm1`$,

```math
e^{-iC\lambda}\mathcal H_{\rm adm}\subseteq\mathcal H_{\rm adm}\ \ \forall\lambda
\iff(P_{12}CP_{12}-C)\,\mathcal H_{\rm adm}=0
\iff\Delta_h=\Delta\ \text{ for all }h .
\qquad\text{(12.3)}
```

### Step 3. Swap invariance (item 1b)

By (12.1), $`D=0`$ iff $`\Delta_a=\Delta_b`$ for all $`a,b`$:

```math
P_{12}CP_{12}=C\iff\Delta_h\ \text{is independent of }h .
\qquad\text{(12.4)}
```

This is the condition of (12.3), not $`\Delta=0`$. For example, $`K^{(1)}_h=0`$ and $`K^{(2)}_h=-\Delta`$ with $`\Delta\neq0`$ give $`C=-\mathbb 1_{p_1p_2}\otimes\Delta`$, which commutes with $`P_{12}`$.

"Iff $`\Delta=0`$" holds for the termwise property instead. Since $`P_{12}C^{(1)}P_{12}=\sum_h\lvert h\rangle\langle h\rvert_{p_2}\otimes K^{(1)}_h`$,

```math
P_{12}C^{(1)}P_{12}=C^{(2)}\iff K^{(1)}_h=K^{(2)}_h\ \ \forall h\iff\Delta=0 .
\qquad\text{(12.5)}
```

(12.5) is a property of how $`C`$ is split into its two contract terms, and $`C`$ does not fix that split. By Step 1, $`C`$ fixes exactly the blocks $`K^{(1)}_a+K^{(2)}_b`$. If two splits have the same blocks for all $`a,b`$, then $`K^{(1)}_a-K'^{(1)}_a=K'^{(2)}_b-K^{(2)}_b`$ is independent of $`a`$ and $`b`$. So the freedom is exactly

```math
K^{(1)}_h\to K^{(1)}_h+X,\qquad K^{(2)}_h\to K^{(2)}_h-X,\qquad \Delta_h\to\Delta_h+2X,\qquad X=X^\dagger\ \text{on }\mathcal H_c .
\qquad\text{(12.6)}
```

This is the A5 freedom to assign the medium-only term to either contract. For $`h`$-independent $`\Delta`$, the choice $`X=-\Delta/2`$ gives a split with $`\Delta=0`$. Hence $`C`$ is swap-invariant iff it has a split with $`\Delta=0`$. The value of $`\Delta`$ is a convention of the description (M6); only its $`h`$-dependence is a property of $`C`$.

### Step 4. Decomposition (item 1c)

For $`h`$-independent $`\Delta`$ we have $`K^{(2)}_h=K_h-\Delta`$ and $`\sum_h\lvert h\rangle\langle h\rvert_{p_2}\otimes\Delta=\mathbb 1_{p_1p_2}\otimes\Delta`$. Hence

```math
C=\sum_h\bigl(\lvert h\rangle\langle h\rvert_{p_1}+\lvert h\rangle\langle h\rvert_{p_2}\bigr)\otimes K_h-\mathbb 1_{p_1p_2}\otimes\Delta .
\qquad\text{(12.7)}
```

The first term is the contract system with $`K^{(1)}_h=K^{(2)}_h=K_h`$, so it satisfies (12.5). The second term commutes with $`P_{12}`$. This agrees with (12.4).

### Step 5. Does the algebra of 11 carry over to the cut $`\{p_1\}\mid\{p_2,c\}`$?

Yes, for three reasons.

1. Among the quoted hypotheses of 11, only "no type has objects on both sides" refers to types. Its role is that the cut can be specified without labels (M6), and that a product of admissible factors is admissible. The results (11.6) and (11.8) are statements about four things: $`\mathcal H_A\otimes\mathcal H_{\bar A}`$, a product initial vector with $`\phi_h\neq0`$, the split $`C_A+C_{\bar A}+C_\partial`$, and the definitions (2.1), (2.2), (2.11), (3.5). None of these refers to types.
2. Other facts take over both roles of the type condition here.
   - *Admissibility.* For $`c_T=+1`$ the start $`\lvert\phi\rangle\otimes\lvert\phi\rangle\otimes\lvert\chi\rangle`$ is admissible, and by (12.3) $`\Psi(\lambda)\in\mathcal H_{\rm adm}`$ for all $`\lambda`$.
   - *Labels.* By (2.16) with $`\pi=(p_1\,p_2)`$, $`W^{\{p_2\}}(h,h';\lambda)=W^{\{p_1\}}(h,h';\lambda)`$. So the single-instance geometry does not depend on which probe is called $`p_1`$.
3. Across this cut the start is a product $`\lvert\phi\rangle_{p_1}\otimes\lvert\omega\rangle`$ with $`\lvert\omega\rangle:=\lvert\phi\rangle\otimes\lvert\chi\rangle\in\mathcal H_T\otimes\mathcal H_c`$ and $`\phi_h\neq0`$.

So (11.6) and (11.8) apply with $`\chi\to\omega`$. The derivation of 11 itself is not quoted. Step 6 therefore re-derives the leading order for the block-diagonal $`C`$ of this package from (2.1), (2.2), (2.11), (3.5), so that the carry-over can be checked without the text of 11.

### Step 6. Leading order for a block-diagonal contract and a product start

Let $`\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}`$, where $`h`$ runs over the joint places of $`A`$, and let

```math
C=\sum_h\lvert h\rangle\langle h\rvert\otimes M_h,\quad M_h=M_h^\dagger,\qquad
\lvert\Psi(0)\rangle=\lvert\Phi\rangle\otimes\lvert\omega\rangle,\quad \Phi_h\neq0\ \forall h,\quad \lVert\Phi\rVert=\lVert\omega\rVert=1 .
```

(a) $`C`$ commutes with every $`\lvert h\rangle\langle h\rvert\otimes\mathbb 1`$, so $`e^{-iC\lambda}=\sum_h\lvert h\rangle\langle h\rvert\otimes e^{-iM_h\lambda}`$. By (2.1),

```math
\lvert\psi_h(\lambda)\rangle=\Phi_h\,e^{-iM_h\lambda}\lvert\omega\rangle .
\qquad\text{(12.8)}
```

By (2.2), $`p_h=\lvert\Phi_h\rvert^2>0`$ for all $`\lambda`$, so every place lies in $`H_V`$. Also $`(V_A)_{hh'}=\Phi_h\Phi_{h'}^*F_{hh'}(\lambda)`$ with $`F_{hh'}(\lambda):=\langle\omega\vert e^{iM_{h'}\lambda}e^{-iM_h\lambda}\vert\omega\rangle`$. By (2.11), $`W(h,h';\lambda)=\lvert F_{hh'}(\lambda)\rvert^2`$ exactly.

(b) Set $`a:=M_h\omega`$ and $`b:=M_{h'}\omega`$. Expanding the exponentials to second order gives

```math
F=1-i\lambda\langle\omega\vert a-b\rangle+\lambda^2\bigl(\langle b\vert a\rangle-\tfrac12\lVert a\rVert^2-\tfrac12\lVert b\rVert^2\bigr)+O(\lambda^3).
```

Here $`\langle\omega\vert a-b\rangle`$ is real and $`F`$ is entire in $`\lambda`$. Hence

```math
W(h,h';\lambda)=1-\lambda^2\Bigl(\lVert a-b\rVert^2-\langle\omega\vert a-b\rangle^2\Bigr)+O(\lambda^3)
=1-\lambda^2\bigl\lVert Q_\omega(M_h-M_{h'})\omega\bigr\rVert^2+O(\lambda^3),
\qquad\text{(12.9)}
```

with $`Q_\omega:=\mathbb 1_{\bar A}-\lvert\omega\rangle\langle\omega\rvert`$. The second equality is Pythagoras, since $`\omega`$ is a unit vector.

(c) By (3.5), $`\sin^2\alpha=1-W=s^2\lambda^2+O(\lambda^3)`$ with $`s:=\lVert Q_\omega(M_h-M_{h'})\omega\rVert`$. So $`\sin\alpha/\lambda\to s`$. Since $`\alpha=\arcsin(\sin\alpha)=\sin\alpha+O(\sin^3\alpha)`$ on $`[0,\pi/2]`$,

```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=\bigl\lVert Q_\omega(M_h-M_{h'})\omega\bigr\rVert .
\qquad\text{(12.10)}
```

(d) *Relation to 11.* Write $`M_h=B_h+C_{\bar A}`$ with $`C_{\bar A}`$ independent of $`h`$, i.e. $`C_A=0`$ and $`C_\partial=\sum_h\lvert h\rangle\langle h\rvert\otimes B_h`$. Then $`C_{\bar A}`$ cancels in (12.10), and $`Q_\omega B_h\omega=\Phi_h^{-1}Q_\omega(\langle h\rvert\otimes\mathbb 1)C_\partial(\Phi\otimes\omega)`$. Hence

```math
\lvert\tilde u_h\rangle:=Q_\omega B_h\lvert\omega\rangle,\qquad
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=\lVert\tilde u_h-\tilde u_{h'}\rVert .
\qquad\text{(12.11)}
```

This is (11.6) and (11.8) with $`(\phi,\chi)\to(\Phi,\omega)`$. The derivation used only the tensor structure and (2.1), (2.2), (2.11), (3.5); the types of the objects entered nowhere. This confirms Step 5.

### Step 7. Single-instance distance (item 2)

Take $`A=\{p_1\}`$, $`\bar A=\{p_2,c\}`$, $`\Phi=\phi`$ and $`\omega=\phi\otimes\chi`$. By (12.7), $`C=\sum_h\lvert h\rangle\langle h\rvert_{p_1}\otimes M_h`$ with

```math
B_h=\mathbb 1_{p_2}\otimes K_h,\qquad C_{\bar A}=\sum_k\lvert k\rangle\langle k\rvert_{p_2}\otimes K_k-\mathbb 1_{p_2}\otimes\Delta .
```

In the language of 11, $`C_\partial=\sum_h\lvert h\rangle\langle h\rvert_{p_1}\otimes K_h`$ and $`C_A=0`$. Then

```math
\lvert\tilde u_h\rangle=Q_\omega\bigl(\lvert\phi\rangle\otimes K_h\lvert\chi\rangle\bigr)
=\lvert\phi\rangle\otimes K_h\lvert\chi\rangle-\langle K_h\rangle\,\lvert\phi\rangle\otimes\lvert\chi\rangle
=\lvert\phi\rangle\otimes\lvert u_h\rangle .
```

By (12.11) and $`\lVert\phi\rVert=1`$,

```math
d_0(h,h')=\lim_{\lambda\to0^+}\frac{\alpha^{\{p_1\}}(h,h';\lambda)}{\lambda}=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad\lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
\qquad\text{(12.12)}
```

This is the value (5.10) of a single probe recorded alone. By (2.16) the same holds for $`p_2`$.

- *No dependence on $`\phi`$:* $`\phi`$ enters only as the unit factor $`\lvert\phi\rangle`$ in $`\tilde u_h`$. The condition $`\phi_h\neq0`$ only ensures $`H_V=H_T`$.
- *No dependence on $`\Delta`$:* $`\Delta`$ enters only $`C_{\bar A}`$, which cancels in (12.10).
- *Conventions (M6):* choosing $`A=\{p_2\}`$ replaces $`K_h`$ by $`K^{(2)}_h=K_h-\Delta`$, and the split freedom (12.6) replaces $`K_h`$ by $`K_h+X`$. Both shift $`u_h`$ by an $`h`$-independent vector ($`-Q_\chi\Delta\chi`$ or $`Q_\chi X\chi`$), so (12.12) is unchanged.
- The $`h`$-independence of $`\Delta`$ enters only through admissibility (Step 5, point 2). For $`h`$-dependent $`\Delta_h`$, Step 6 would give different values for $`p_1`$ and $`p_2`$, as expected, since (2.16) does not hold outside $`\mathcal H_{\rm adm}`$.

### Step 8. Pair distance (item 3)

Take $`A=\{p_1,p_2\}`$ and $`\bar A=\{c\}`$, with joint places $`(h_1,h_2)`$. Then $`\Phi=\phi\otimes\phi`$ with $`\Phi_{h_1h_2}=\phi_{h_1}\phi_{h_2}\neq0`$, and $`\omega=\chi`$. By (12.1) and (12.7), $`C=\sum_{h_1h_2}\lvert h_1h_2\rangle\langle h_1h_2\rvert\otimes M_{h_1h_2}`$ with $`M_{h_1h_2}=K_{h_1}+K_{h_2}-\Delta`$. In (12.10), $`\Delta`$ cancels and $`Q_\chi K\chi=(K-\langle K\rangle)\chi`$, so

```math
d_0\bigl((h_1,h_2),(h_1',h_2')\bigr)=\bigl\lVert u_{h_1}+u_{h_2}-u_{h_1'}-u_{h_2'}\bigr\rVert .
\qquad\text{(12.13)}
```

*Swapped joint places.* (3.4) with $`a=p_1`$, $`b=p_2`$ holds for every admissible state, hence by (12.3) for $`\Psi(\lambda)`$ at every $`\lambda`$: $`\psi_{(h_1h_2)}=c_T\psi_{(h_2h_1)}`$. So $`p_{(h_1h_2)}=p_{(h_2h_1)}>0`$ and $`\lvert(V_A)_{(h_1h_2)(h_2h_1)}\rvert=\lVert\psi_{(h_1h_2)}\rVert^2`$. By (2.11),

```math
W\bigl((h_1,h_2),(h_2,h_1);\lambda\bigr)=1\qquad\forall\lambda .
\qquad\text{(12.14)}
```

So $`(h_1,h_2)\approx(h_2,h_1)`$: the two joint places are one point of $`X_V`$, exactly. (12.13) is symmetric under $`h_1\leftrightarrow h_2`$ and under $`h_1'\leftrightarrow h_2'`$, so it is well defined on these points.

*One-probe differences.* For two points that share one probe place, (12.14) allows the representatives $`(h_1,h_2)`$ and $`(h_1',h_2)`$. Then

```math
d_0\bigl((h_1,h_2),(h_1',h_2)\bigr)=\lVert u_{h_1}-u_{h_1'}\rVert=d_0(h_1,h_1') ,
\qquad\text{(12.15)}
```

which is the single-instance value (12.12) for every spectator place $`h_2`$.

### Step 9. The partner as a witness (item 4)

The state $`\Psi_0=\tfrac1{\sqrt2}(\lvert hh'\rangle+\lvert h'h\rangle)\otimes\lvert\chi\rangle`$ with $`h\neq h'`$ is admissible for $`c_T=+1`$. For $`A=\{p_1\}`$, (2.1) gives $`\psi_h=\tfrac1{\sqrt2}\lvert h'\rangle_{p_2}\otimes\lvert\chi\rangle`$, $`\psi_{h'}=\tfrac1{\sqrt2}\lvert h\rangle_{p_2}\otimes\lvert\chi\rangle`$, and $`\psi_k=0`$ for every other $`k`$. By (2.2), $`p_h=p_{h'}=\tfrac12`$ and $`(V_A)_{hh'}=\tfrac12\langle h\vert h'\rangle=0`$. By (2.11) and (3.5),

```math
W(h,h';0)=0,\qquad \alpha(h,h';0)=\pi/2 .
\qquad\text{(12.16)}
```

The companion branch states $`\lvert h'\rangle\otimes\lvert\chi\rangle`$ and $`\lvert h\rangle\otimes\lvert\chi\rangle`$ are orthogonal through the factor of $`p_2`$ alone; their medium factor is identical. So $`p_2`$ is a perfect witness for $`p_1`$, and by (2.16) $`p_1`$ is one for $`p_2`$.

*Consequence.* $`V_A(\lambda)`$ is continuous in $`\lambda`$ and $`p_h(0)>0`$. So as $`\lambda\to0^+`$, $`W(h,h';\lambda)\to0`$, $`\alpha\to\pi/2`$ and $`\alpha/\lambda\to\infty`$: there is no finite leading-order distance to compare with (5.10).

More generally, let the medium start uncorrelated: $`\Psi_0=\Phi\otimes\chi`$ with $`P_{12}\Phi=\Phi`$. By (2.11) and the equality case of Cauchy–Schwarz, $`W(h,h';0)=1`$ for all $`h,h'\in H_V`$ iff all nonzero $`\psi_h(0)`$ are parallel. That holds iff $`\Psi_0`$ is a product across $`\{p_1\}\mid\{p_2,c\}`$, i.e. iff $`\Phi=\phi\otimes\phi'`$. Then $`P_{12}\Phi=\Phi`$ reads $`\phi'\otimes\phi=\phi\otimes\phi'`$, which forces $`\phi'\propto\phi`$:

```math
W(\cdot,\cdot;0)\equiv1\ \text{on }H_V\iff\Phi=\lvert\phi\rangle\otimes\lvert\phi\rangle\ \ \text{(up to a phase)} .
\qquad\text{(12.17)}
```

Otherwise some pair has $`W(h,h';0)<1`$, and $`\alpha/\lambda\to\infty`$ for that pair. The agreement (12.12) with (5.10) therefore requires probes that are not correlated with each other.

## Result

1. **Law 5 and the records (either family).**
   - Invariance of $`\mathcal H_{\rm adm}`$ under the evolution $`\iff(P_{12}CP_{12}-C)\mathcal H_{\rm adm}=0\iff\Delta_h`$ is $`h`$-independent, (12.1)–(12.3).
   - Swap invariance $`P_{12}CP_{12}=C`$ holds iff $`\Delta_h`$ is $`h`$-independent (12.4), **not** iff $`\Delta=0`$. $`\Delta=0`$ characterizes the termwise property $`P_{12}C^{(1)}P_{12}=C^{(2)}`$ (12.5). The value of $`\Delta`$ is a split convention (12.6).
   - Decomposition: (12.7).
2. **Single instance.** The algebra of (11.6) and (11.8) carries over to the cut $`\{p_1\}\mid\{p_2,c\}`$ (Step 5; checked by (12.8)–(12.11)). $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$ (12.12) is the value (5.10). It is the same for both probes and does not depend on $`\phi`$, $`\Delta`$ or the split.
3. **Pair.** The distance is (12.13). Swapped joint places are one point, exactly (12.14). One-probe differences give the single-instance distance (12.15).
4. **Partner as witness.** $`W(h,h';0)=0`$ (12.16). With an uncorrelated medium, a finite single-instance $`d_0`$ for all pairs requires $`\Phi=\phi\otimes\phi`$ (12.17).

## Consistency checks

1. **All $`K_h`$ equal.** In Steps 7 and 8 the $`M_h`$ are then $`h`$-independent, so (12.8) gives $`W\equiv1`$ exactly for all $`\lambda`$. Consistently, (12.12) and (12.13) vanish, since $`u_h=u`$ for all $`h`$.
2. **Removing $`p_2`$.** Step 6 with $`A=\{p\}`$, $`\bar A=\{c\}`$, $`M_h=K_h`$ and $`\omega=\chi`$ gives $`\lVert Q_\chi(K_h-K_{h'})\chi\rVert=\lVert u_h-u_{h'}\rVert`$. This is (5.10), an independent input, so it checks Step 6. (12.12) shows that adding $`p_2`$ in the state $`\phi`$ changes nothing at leading order.
3. **Swap symmetry of the pair geometry.** (12.13) is invariant under $`h_1\leftrightarrow h_2`$, under $`h_1'\leftrightarrow h_2'`$, and under exchanging its two arguments. This matches (12.14), which follows from (3.4) independently of the expansion, and the swap invariance (12.4) of $`C`$.

## Open issues

- **Discrepancy with the expected result, item 1(b).** Swap invariance is equivalent to an $`h`$-independent $`\Delta_h`$ (12.4), not to $`\Delta=0`$. $`\Delta=0`$ is the termwise property (12.5), which depends on the split (12.6).
- **Joint places that differ in both probe places.** (12.13) is not a function of single-probe distances: $`d_0^2=d_0(h_1,h_1')^2+d_0(h_2,h_2')^2+2\,\mathrm{Re}\langle u_{h_1}-u_{h_1'}\vert u_{h_2}-u_{h_2'}\rangle`$. This matters for the common-space question; it is not analysed here.
- **Beyond leading order.** $`C_{\bar A}`$, and with it $`\Delta`$ and the partner's record, enters $`W`$ through commutators with $`B_h`$. This is not treated.
- **Reading of $`\mathcal H_{\rm adm}`$.** I took the full eigenspace of $`P_{12}`$. If a description restricts $`\mathcal H_{\rm adm}`$ further, the "only if" of (12.3) needs the test vectors of Step 2(iii) to be admissible.
- **$`c_T=-1`$.** Not treated beyond item 1. The start $`\phi\otimes\phi\otimes\chi`$ of item 2 is not admissible for $`c_T=-1`$.

## Methods used

- Invariant subspaces of a one-parameter unitary group; symmetrization projector
- Block diagonalization of an operator commuting with the place projectors
- Operator exponential, second-order Taylor expansion
- Partial trace and branch vectors; Cauchy–Schwarz equality case
- Factorization of rank-one tensors
