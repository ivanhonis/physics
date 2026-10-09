# Body recorded by another cell: the body-dependent witness data through links

- **Subproject:** 03-ilang-space
- **Package:** 08-cell-medium
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

**Setting (question.md).** The objects are $`p,b,c_1,c_2`$, with pairwise different types and one instance each, so (1.11) imposes nothing. The part is $`A=\{p\}`$. The contract system is

```math
C=\sum_h\lvert h\rangle\langle h\rvert_p\otimes K_h+\sum_\beta\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta+J,\qquad J=\sum_kP_k\otimes Q_k ,
```

with $`K_h`$ on $`c_1`$, $`B_\beta`$ on $`c_2`$ and $`J`$ on $`c_1c_2`$, all self-adjoint and extended by the identity. The initial state is $`\lvert\phi\rangle_p\otimes\lvert\beta_0\rangle_b\otimes\lvert\chi\rangle`$ with $`\lvert\chi\rangle=\lvert\chi_1\rangle\otimes\lvert\chi_2\rangle`$ and $`\phi_h\neq0`$. We write $`D=K_h-K_{h'}`$ (on $`c_1`$) and $`\tilde D=D-\langle D\rangle`$.

**Notation.**
- $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, and $`\langle\cdot\rangle_1,\langle\cdot\rangle_2`$ are the expectations in $`\lvert\chi_1\rangle,\lvert\chi_2\rangle`$.
- For self-adjoint $`X,Y`$: $`\tilde X=X-\langle X\rangle`$, $`\mathrm{Var}_\chi(X)=\langle\tilde X^2\rangle`$, $`\mathrm{Cov}_\chi(X,Y):=\tfrac12\langle\{\tilde X,\tilde Y\}\rangle=\tfrac12\langle\{\tilde X,Y\}\rangle`$, and $`\kappa_n(X)`$ is the $`n`$-th cumulant of $`X`$ in $`\lvert\chi\rangle`$.
- $`\mathrm i`$ is the imaginary unit. Plain $`i,j`$ are place indices (Item 5 only).
- **Body-dependent part.** For $`F\in\{W^{(\beta_0)},c_3^{(\beta_0)},c_4^{(\beta_0)},\alpha^{(\beta_0)}\}`$, $`\Delta F:=F-F\big|_{B_{\beta_0}=0}`$, with $`K_h`$, $`J`$ and $`\lvert\chi\rangle`$ held fixed.

**Inputs.** (2.1), (2.2), (2.11), (3.5), (5.10) and (6.6)–(6.12), as quoted in question.md.

**Assumptions.** A1 (finite dimension), A5 ($`\lambda`$-independent contracts), $`\lambda\ge0`$. Items 1, 2 are exact. Items 3–5 are expansions for $`\lambda\to0^+`$. All operators are bounded (A1), so the series used below converge for small $`\lambda`$ and their remainders are uniform.

**Applicability of 06.** The derivation of (6.6)–(6.12) uses only three facts: the two branch operators and the operator common to both branches are self-adjoint, they act on a finite-dimensional medium, and the medium starts in a unit vector. All three hold here:
- the medium is $`c_1c_2`$, with finite-dimensional space $`\mathcal H_{c_1}\otimes\mathcal H_{c_2}`$ (A1);
- the branch operators $`K_h\otimes\mathbb 1`$, $`K_{h'}\otimes\mathbb 1`$ and the common operator $`\mathbb 1\otimes B_{\beta_0}+J`$ are self-adjoint;
- $`\lvert\chi_1\rangle\otimes\lvert\chi_2\rangle`$ is a unit vector.

Hence (6.6)–(6.12) hold with $`\mathcal H_c\to\mathcal H_{c_1}\otimes\mathcal H_{c_2}`$, $`\lvert\chi\rangle\to\lvert\chi_1\rangle\otimes\lvert\chi_2\rangle`$ and $`B_{\beta_0}\to B_{\beta_0}+J`$. The hypothesis of (6.7) becomes $`[B_{\beta_0}+J,K_h]=[B_{\beta_0}+J,K_{h'}]=0`$. Step 1 checks the block structure that (6.6) rests on.

## Derivation

### Step 1. Exact evolution (Item 1)

The projectors $`\lvert h\rangle\langle h\rvert_p\otimes\lvert\beta\rangle\langle\beta\rvert_b`$ commute with every term of $`C`$: the first two terms are diagonal in the place bases of $`p`$ and $`b`$, and $`J`$ acts on neither object. For every $`\lvert\xi\rangle\in\mathcal H_{c_1}\otimes\mathcal H_{c_2}`$,

```math
C\bigl(\lvert h\rangle_p\lvert\beta\rangle_b\otimes\lvert\xi\rangle\bigr)=\lvert h\rangle_p\lvert\beta\rangle_b\otimes H_{h\beta}\lvert\xi\rangle,\qquad H_{h\beta}:=K_h+B_\beta+J .
\tag{8.1}
```

By (1.9), applied term by term, and writing $`H_h:=H_{h\beta_0}`$ (tensor factors labelled by object),

```math
\lvert\Psi(\lambda)\rangle=\lvert\beta_0\rangle_b\otimes\sum_h\phi_h\lvert h\rangle_p\otimes\lvert\chi_h(\lambda)\rangle,\qquad \lvert\chi_h(\lambda)\rangle:=e^{-\mathrm iH_h\lambda}\lvert\chi\rangle .
\tag{8.2}
```

The factor of $`b`$ is $`\lvert\beta_0\rangle`$ for every $`\lambda`$. So the body stays at $`\beta_0`$: its view is $`\lvert\beta_0\rangle\langle\beta_0\rvert`$, and every reading of $`b`$ gives $`\beta_0`$ with probability one.

By (2.1), $`\lvert\psi_h\rangle=\phi_h\lvert\beta_0\rangle\otimes\lvert\chi_h(\lambda)\rangle`$. Then (2.2) gives $`(V_A)_{hh'}=\phi_h\phi_{h'}^*\langle\chi_{h'}(\lambda)\vert\chi_h(\lambda)\rangle`$ and $`p_h=\lvert\phi_h\rvert^2>0`$, so $`H_V`$ contains every place. By (2.11),

```math
W^{(\beta_0)}(h,h';\lambda)=\bigl\lvert G^{(\beta_0)}_{hh'}(\lambda)\bigr\rvert^2,\qquad
G^{(\beta_0)}_{hh'}(\lambda)=\langle\chi\vert e^{\mathrm i(K_{h'}+B_{\beta_0}+J)\lambda}e^{-\mathrm i(K_h+B_{\beta_0}+J)\lambda}\vert\chi\rangle .
\tag{8.3}
```

This is (6.6) under the substitution above.

### Step 2. No link, no effect (Item 2)

Let $`J=0`$. The common operator $`\mathbb 1\otimes B_{\beta_0}`$ acts on $`c_2`$, so it commutes with $`K_h\otimes\mathbb 1`$ and $`K_{h'}\otimes\mathbb 1`$, and the hypothesis of (6.7) holds. By (6.7), $`G^{(\beta_0)}_{hh'}=\langle\chi_1\vert e^{\mathrm iK_{h'}\lambda}e^{-\mathrm iK_h\lambda}\vert\chi_1\rangle`$, which does not contain $`B_{\beta_0}`$ and is therefore also its value at $`B_{\beta_0}=0`$:

```math
J=0:\qquad \Delta W^{(\beta_0)}(h,h';\lambda)=0\qquad\text{for every }\lambda\ge0 .
\tag{8.4}
```

### Step 3. Expansion of $`W^{(\beta_0)}`$ to fourth order (Item 3)

Let $`M:=K_{h'}+B_{\beta_0}+J`$, so that $`K_h+B_{\beta_0}+J=M+D`$. Use BCH to third order, $`\ln(e^Se^T)=S+T+\tfrac12[S,T]+\tfrac1{12}\bigl([S,[S,T]]+[T,[T,S]]\bigr)+\dots`$, with $`S=\mathrm i\lambda M`$ and $`T=-\mathrm i\lambda(M+D)`$. The three correction terms are $`\tfrac{\lambda^2}{2}[M,D]`$, $`\tfrac{\mathrm i\lambda^3}{12}[M,[M,D]]`$ and $`\tfrac{\mathrm i\lambda^3}{12}\bigl([M,[M,D]]+[D,[M,D]]\bigr)`$. Hence

```math
e^{\mathrm iM\lambda}e^{-\mathrm i(M+D)\lambda}=e^{-\mathrm i\lambda\Omega},\qquad
\Omega=D+\lambda\Omega_1+\lambda^2\Omega_2+O(\lambda^3),\qquad
\Omega_1=\tfrac{\mathrm i}{2}[M,D],\quad \Omega_2=-\tfrac16[M,[M,D]]-\tfrac1{12}[D,[M,D]] ,
\tag{8.5}
```

where $`\Omega_1`$ and $`\Omega_2`$ are self-adjoint. The cumulant expansion $`\ln\langle e^{-\mathrm i\lambda\Omega}\rangle=\sum_n(-\mathrm i\lambda)^n\kappa_n(\Omega)/n!`$ has real $`\kappa_n`$, so the odd orders are imaginary. Since $`W=\lvert G\rvert^2`$, $`\ln W=2\mathrm{Re}\ln G`$, and

```math
\ln W^{(\beta_0)}=-\lambda^2\mathrm{Var}_\chi(\Omega)+\tfrac{\lambda^4}{12}\kappa_4(\Omega)+O(\lambda^6) .
\tag{8.6}
```

Insert (8.5):
- $`\mathrm{Var}_\chi(\Omega)=\mathrm{Var}_\chi(D)+2\lambda\mathrm{Cov}_\chi(D,\Omega_1)+\lambda^2\bigl[\mathrm{Var}_\chi(\Omega_1)+2\mathrm{Cov}_\chi(D,\Omega_2)\bigr]+O(\lambda^3)`$;
- $`\kappa_4(\Omega)=\kappa_4(D)+O(\lambda)`$.

Exponentiating,

```math
W^{(\beta_0)}=1-\lambda^2\mathrm{Var}_\chi(D)-2\lambda^3\mathrm{Cov}_\chi(D,\Omega_1)
+\lambda^4\Bigl[\tfrac12\mathrm{Var}_\chi(D)^2+\tfrac1{12}\kappa_4(D)-\mathrm{Var}_\chi(\Omega_1)-2\mathrm{Cov}_\chi(D,\Omega_2)\Bigr]+O(\lambda^5).
\tag{8.7}
```

**Check against (6.10).** Use $`[M,D]=[M,\tilde D]`$ and $`\{\tilde D,[M,\tilde D]\}=[M,\tilde D^2]`$. The $`\lambda^3`$ coefficient of (8.7) is then $`-\tfrac{\mathrm i}{2}\langle[M,\tilde D^2]\rangle=\mathrm{Im}\langle M\tilde D^2\rangle`$, which is (6.10) with $`B_{\beta_0}\to B_{\beta_0}+J`$.

### Step 4. Body-dependent part of $`c_3^{(\beta_0)}`$ (Item 3a)

By (6.11) with $`B_{\beta_0}\to B_{\beta_0}+J`$,
```math
c_3^{(\beta_0)}=\mathrm{Im}\langle K_{h'}\tilde D^2\rangle+\mathrm{Im}\langle J\tilde D^2\rangle+\mathrm{Im}\langle B_{\beta_0}\tilde D^2\rangle .
```
Only the last term contains $`B_{\beta_0}`$. Since $`B_{\beta_0}`$ acts on $`c_2`$ and $`\tilde D^2`$ on $`c_1`$,

```math
\Delta c_3^{(\beta_0)}=\mathrm{Im}\langle\chi\vert B_{\beta_0}\tilde D^2\vert\chi\rangle=\frac{\langle\chi\vert[B_{\beta_0},\tilde D^2]\vert\chi\rangle}{2\mathrm i}=0 .
\tag{8.8}
```

In the product state this is explicit: $`\langle B_{\beta_0}\tilde D^2\rangle=\langle B_{\beta_0}\rangle_2\langle\tilde D^2\rangle_1`$ is real.

### Step 5. Body-dependent part of $`c_4^{(\beta_0)}`$ (Item 3b)

The first two terms of the $`\lambda^4`$ bracket in (8.7) do not contain $`M`$, so they are body-free. Operators on $`c_2`$ commute with operators on $`c_1`$, so $`[B_{\beta_0},D]=0`$ and $`[B_{\beta_0},[K_{h'},D]]=0`$. Hence

```math
[M,D]=[K_{h'}+J,D],\qquad [M,[M,D]]=[K_{h'}+J,[K_{h'}+J,D]]+[B_{\beta_0},[J,D]] .
\tag{8.9}
```

So $`\Omega_1`$ and $`[D,[M,D]]`$ are body-free, and the only body-dependent operator in (8.7) is $`\Delta\Omega_2=-\tfrac16[B_{\beta_0},[J,D]]`$. It enters linearly. With $`\mathrm{Cov}_\chi(D,Y)=\tfrac12\langle\{\tilde D,Y\}\rangle`$,

```math
\Delta c_4^{(\beta_0)}(h,h')=-2\mathrm{Cov}_\chi(D,\Delta\Omega_2)=\frac16\,\langle\chi\vert\{\tilde D,[B_{\beta_0},[J,D]]\}\vert\chi\rangle .
\tag{8.10}
```

**Product form.** Three identities give it:
- since $`D`$ acts on $`c_1`$, $`[B_{\beta_0},[J,D]]=\sum_k[P_k,D]\otimes[B_{\beta_0},Q_k]`$;
- $`\{\tilde D,[P_k,\tilde D]\}=[P_k,\tilde D^2]`$;
- for self-adjoint $`X,Y`$, $`\langle[X,Y]\rangle=2\mathrm i\mathrm{Im}\langle XY\rangle`$.

Then $`\langle[P_k,\tilde D^2]\rangle_1\langle[B_{\beta_0},Q_k]\rangle_2=(2\mathrm i)^2\mathrm{Im}\langle P_k\tilde D^2\rangle_1\mathrm{Im}\langle B_{\beta_0}Q_k\rangle_2`$, and

```math
\Delta c_4^{(\beta_0)}(h,h')=-\frac23\sum_k\mathrm{Im}\langle\chi_1\vert P_k\tilde D^2\vert\chi_1\rangle\,\mathrm{Im}\langle\chi_2\vert B_{\beta_0}Q_k\vert\chi_2\rangle .
\tag{8.11}
```

By (8.10), the result does not depend on the choice of decomposition of $`J`$.

### Step 6. Witness angle at order $`\lambda^3`$ (Item 3c)

By (5.10), $`u_h-u_{h'}=\tilde D\lvert\chi\rangle`$, so $`d_0^2=\mathrm{Var}_\chi(D)`$. Let $`d_0>0`$. By (3.5) with $`\alpha\in[0,\pi/2]`$, $`\sin\alpha=\sqrt{1-W}=\lambda d_0\bigl(1-\lambda c_3/d_0^2-\lambda^2c_4/d_0^2+O(\lambda^3)\bigr)^{1/2}`$. Expanding the square root and using $`\arcsin s=s+s^3/6+O(s^5)`$,

```math
\alpha^{(\beta_0)}=\lambda d_0-\lambda^2\frac{c_3^{(\beta_0)}}{2d_0}+\lambda^3\Bigl[\frac{d_0^3}{6}-\frac{(c_3^{(\beta_0)})^2}{8d_0^3}-\frac{c_4^{(\beta_0)}}{2d_0}\Bigr]+O(\lambda^4),
\tag{8.12}
```

whose $`\lambda^2`$ term is (6.12). Here $`d_0`$ is body-free, and $`c_3^{(\beta_0)}`$ is body-free by (8.8). Hence

```math
\Delta\alpha^{(\beta_0)}(h,h';\lambda)=-\lambda^3\,\frac{\Delta c_4^{(\beta_0)}(h,h')}{2d_0(h,h')}+O(\lambda^4).
\tag{8.13}
```

### Step 7. Chain of cells (Item 4)

The probe and body projectors still commute with $`C`$, because the links act on cells only. So Step 1 holds with $`J\to J_{\rm ch}:=\sum_{k=1}^{L-1}J_k`$ and $`\lvert\chi\rangle=\lvert\chi_1\rangle\otimes\cdots\otimes\lvert\chi_L\rangle`$. Set $`M:=K_{h'}+B_{\beta_0}+J_{\rm ch}`$ and $`U(\lambda):=e^{\mathrm iM\lambda}e^{-\mathrm i(M+D)\lambda}`$. Then $`\mathrm dU/\mathrm d\lambda=-\mathrm iD(\lambda)U`$ with $`U(0)=\mathbb 1`$ and $`D(s):=e^{\mathrm iMs}De^{-\mathrm iMs}`$, so the Dyson series gives

```math
G^{(\beta_0)}_{hh'}=1-\mathrm i\!\int_0^\lambda\!\langle D(s)\rangle\,ds-\int_0^\lambda\!ds_1\!\int_0^{s_1}\!ds_2\,\langle D(s_1)D(s_2)\rangle+\dots,\qquad
D(s)=\sum_{n\ge0}\frac{(\mathrm is)^n}{n!}\mathrm{ad}_M^n(D).
\tag{8.14}
```

**Support counting.** $`\mathrm{ad}_M^n(D)`$ is a sum of words $`\mathrm{ad}_{Y_n}\cdots\mathrm{ad}_{Y_1}(D)`$ with letters $`Y_\ell\in\{K_{h'},B_{\beta_0},J_1,\dots,J_{L-1}\}`$. A commutator of operators with disjoint supports vanishes, and $`\mathrm{supp}[Y,Z]\subseteq\mathrm{supp}Y\cup\mathrm{supp}Z`$. By induction from $`\mathrm{supp}D=\{c_1\}`$:
- a nonzero word has support in $`\{c_1,\dots,c_{1+m}\}`$, where $`m`$ is the number of link letters in it;
- the letter $`B_{\beta_0}`$ (support $`\{c_{r+1}\}`$) gives a nonzero commutator only after at least $`r`$ link letters.

So the words that contain $`B_{\beta_0}`$ have $`n\ge r+1`$. For $`n=r+1`$ the only such word is $`J_1,\dots,J_r,B_{\beta_0}`$. Hence

```math
\delta D(s):=D(s)-D(s)\big|_{B_{\beta_0}=0}=\frac{(\mathrm is)^{r+1}}{(r+1)!}Z_r+O(s^{r+2}),\qquad
Z_r:=[B_{\beta_0},[J_r,[\cdots[J_1,D]\cdots]]],
\tag{8.15}
```

with $`Z_0=[B_{\beta_0},D]`$. Each $`\mathrm{ad}`$ of a self-adjoint letter exchanges self-adjoint and anti-self-adjoint operators, so $`\mathrm i^{r+1}Z_r`$ is self-adjoint.

**Order of $`\Delta W`$.** In (8.14), the first-order term gives $`\delta G=-\mathrm i\,a\,\lambda^{r+2}+O(\lambda^{r+3})`$ with real $`a=\langle\mathrm i^{r+1}Z_r\rangle/(r+2)!`$. Every higher Dyson term that contains $`\delta D`$ is $`O(\lambda^{r+3})`$. With $`G_0:=G\big|_{B_{\beta_0}=0}=1+O(\lambda)`$,

```math
\Delta W^{(\beta_0)}=2\mathrm{Re}\bigl(G_0^*\,\delta G\bigr)+\lvert\delta G\rvert^2=2\mathrm{Re}\bigl(-\mathrm i\,a\,\lambda^{r+2}\bigr)+O(\lambda^{r+3})=O(\lambda^{3+r}).
\tag{8.16}
```

- For $`L=2`$, $`r=1`$ this agrees with Steps 4–5.
- For $`r=0`$, $`Z_0=[B_{\beta_0},D]\neq0`$ in general, and the $`\lambda^3`$ coefficient is the term $`\mathrm{Im}\langle B_{\beta_0}\tilde D^2\rangle`$ of (6.11), taken with medium $`c_1\cdots c_L`$ and $`B_{\beta_0}\to B_{\beta_0}+J_{\rm ch}`$.
- Steps 4, 5 (operator form (8.10)) and 7 use only supports, not the product form of $`\lvert\chi\rangle`$.

### Step 8. Qubit example (Item 5)

**Basic quantities.** $`D=(i-j)X_1`$. Since $`\{\sigma_x,\sigma_z\}=0`$, $`X_1^2=2\cdot\mathbb 1`$, and $`\langle0\vert X_1\vert0\rangle=1`$. Hence

```math
\tilde D=(i-j)(X_1-\mathbb 1),\qquad \tilde D^2=(i-j)^2(3-2X_1),\qquad \mathrm{Var}_\chi(D)=(i-j)^2,\qquad d_0(h_i,h_j)=\lvert i-j\rvert .
\tag{8.17}
```

**$`c_3`$.** By (6.10) with $`B_{\beta_0}\to B_{\beta_0}+J`$, three terms contribute:
- $`K_{h_j}\tilde D^2=j(i-j)^2X_1(3-2X_1)`$ is a self-adjoint function of $`X_1`$, so its expectation is real;
- the $`B_{\beta_0}`$ term vanishes by (8.8);
- $`\langle J\tilde D^2\rangle`$ contains the factor $`\langle0\vert\sigma_x\vert0\rangle=0`$.

Hence

```math
c_3^{(\beta_0)}(h_i,h_j)=0 .
\tag{8.18}
```

**$`\Delta c_4`$.** Take $`P_1=g\sigma_y`$ and $`Q_1=\sigma_x`$. Using $`\sigma_y\sigma_x=-\mathrm i\sigma_z`$ and $`\sigma_y\sigma_z=\mathrm i\sigma_x`$:
- $`\sigma_y(3-2X_1)=3\sigma_y+2\mathrm i\sigma_z-2\mathrm i\sigma_x`$, whose expectation in $`\lvert0\rangle`$ is $`2\mathrm i`$, so $`\mathrm{Im}\langle P_1\tilde D^2\rangle_1=2g(i-j)^2`$;
- $`\mathrm{Im}\langle0\vert\beta_0\sigma_y\sigma_x\vert0\rangle=\mathrm{Im}(-\mathrm i\beta_0)=-\beta_0`$.

By (8.11),

```math
\Delta c_4^{(\beta_0)}(h_i,h_j)=-\tfrac23\cdot2g(i-j)^2\cdot(-\beta_0)=\tfrac43\,g\,\beta_0\,(i-j)^2 .
\tag{8.19}
```

The operator form (8.10) gives the same value: $`[B_{\beta_0},[J,D]]=4g\beta_0(i-j)(\sigma_x-\sigma_z)\otimes\sigma_z`$ and $`\langle\{\tilde D,\cdot\}\rangle=8g\beta_0(i-j)^2`$.

**Witness angle.** By (8.13) and (8.17), for $`i\neq j`$,

```math
\Delta\alpha^{(\beta_0)}(h_i,h_j;\lambda)=-\tfrac23\,g\,\beta_0\,\lvert i-j\rvert\,\lambda^3+O(\lambda^4).
\tag{8.20}
```

**Contrast with $`J=g\,\sigma_z\otimes\sigma_z`$.** Take $`P_1=g\sigma_z`$ and $`Q_1=\sigma_z`$. Then $`\lvert\chi_1\rangle=\lvert\chi_2\rangle=\lvert0\rangle`$ are eigenvectors of $`\sigma_z`$, so both factors of (8.11) vanish: $`\langle0\vert\sigma_z\tilde D^2\vert0\rangle=\langle0\vert\tilde D^2\vert0\rangle`$ is real, and $`\langle0\vert\sigma_y\sigma_z\vert0\rangle=\mathrm i\langle0\vert\sigma_x\vert0\rangle=0`$. Hence

```math
J=g\,\sigma_z\otimes\sigma_z:\qquad \Delta c_4^{(\beta_0)}(h_i,h_j)=0,\qquad \Delta W^{(\beta_0)}=O(\lambda^5),\qquad \Delta\alpha^{(\beta_0)}=O(\lambda^4).
\tag{8.21}
```

## Result

- **Item 1.** Exact state (8.2); the body stays at $`\beta_0`$. The witness data are (8.3), i.e. (6.6) with $`B_{\beta_0}\to B_{\beta_0}+J`$ on the medium $`c_1c_2`$.
- **Item 2.** For $`J=0`$, $`\Delta W^{(\beta_0)}=0`$ exactly, for every $`\lambda`$ (8.4).
- **Item 3.**
  - (a) $`\Delta c_3^{(\beta_0)}=\mathrm{Im}\langle B_{\beta_0}\tilde D^2\rangle=0`$ (8.8).
  - (b) $`\Delta c_4^{(\beta_0)}=\tfrac16\langle\{\tilde D,[B_{\beta_0},[J,D]]\}\rangle=-\tfrac23\sum_k\mathrm{Im}\langle P_k\tilde D^2\rangle_1\mathrm{Im}\langle B_{\beta_0}Q_k\rangle_2`$ (8.10), (8.11).
  - (c) $`\Delta\alpha^{(\beta_0)}=-\lambda^3\Delta c_4^{(\beta_0)}/(2d_0)+O(\lambda^4)`$ (8.13); the full angle is (8.12).
- **Item 4.** On a chain, with the body recorded $`r`$ links away from the probe's cell, $`\Delta W^{(\beta_0)}=O(\lambda^{3+r})`$ (8.16). The leading body-dependent operator is the nested commutator $`Z_r`$ (8.15).
- **Item 5.**
  - $`c_3^{(\beta_0)}(h_i,h_j)=0`$ (8.18).
  - $`\Delta c_4^{(\beta_0)}=\tfrac43g\beta_0(i-j)^2`$ (8.19).
  - $`\Delta\alpha^{(\beta_0)}=-\tfrac23g\beta_0\lvert i-j\rvert\lambda^3+O(\lambda^4)`$ (8.20).
  - For $`J=g\,\sigma_z\otimes\sigma_z`$, $`\Delta c_4^{(\beta_0)}=0`$ (8.21).
- All expected formulas of question.md are reproduced, with no discrepancy in sign or factor.

## Consistency checks

1. **$`J=0`$.** (8.10) and (8.11) vanish because $`[J,D]=0`$, and $`\Delta c_3=0`$ by (8.8). This agrees with the exact statement (8.4) obtained from (6.7). On the chain, without links no word in (8.15) reaches $`c_{r+1}`$ for $`r\ge1`$.
2. **$`B_{\beta_0}=\beta_0\mathbb 1`$.** In (8.3) the factors $`e^{\pm\mathrm i\beta_0\lambda}`$ cancel, so $`\Delta W=0`$ for every $`\lambda`$. Consistently, $`[\beta_0\mathbb 1,\cdot]=0`$ in (8.10), and $`\mathrm{Im}\langle\beta_0Q_k\rangle_2=0`$ in (8.11).
3. **Body recorded by $`c_1`$ ($`r=0`$).** Then $`[B_{\beta_0},D]\neq0`$ in general. The support bound (8.16) allows $`O(\lambda^3)`$, and the coefficient is the term $`\mathrm{Im}\langle B_{\beta_0}\tilde D^2\rangle=\langle[B_{\beta_0},\tilde D^2]\rangle/(2\mathrm i)`$ of (6.11). This is also what the general $`\lambda^3`$ coefficient $`\mathrm{Im}\langle M\tilde D^2\rangle`$ of Step 3 gives.

## Open issues

- For $`r\ge2`$ only the bound (8.16) is shown. The coefficient of $`\lambda^{3+r}`$, and whether it is generically nonzero, are not computed.
- For $`J=g\,\sigma_z\otimes\sigma_z`$, the first nonzero body-dependent order is not determined.
- The operator results (8.8), (8.10) and (8.16) do not use the product form of $`\lvert\chi\rangle`$; only (8.11) does. Non-product medium states are outside the scope.

## Methods used

- Block diagonalization by conserved place projectors
- Baker–Campbell–Hausdorff formula to third order
- Cumulant expansion of $`\langle e^{-\mathrm i\lambda\Omega}\rangle`$
- Interaction picture and Dyson series
- Support counting of nested commutators
- Pauli-matrix algebra; expansion of $`\arcsin`$
