# Loop data of the witness geometry in a recording medium

- **Subproject:** 03-ilang-space
- **Package:** 10-loop-data
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

**Setting** (question.md, from 05). Objects $`a`$ and $`c`$ of different types, each the only instance of its type; part $`A=\{a\}`$; recording contract $`C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; initial state $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for every $`h`$. Each $`K_h`$ is self-adjoint on $`\mathcal H_c`$ (because $`C=C^\dagger`$) and independent of $`\lambda`$ (A5). $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, $`\langle\chi\vert\chi\rangle=1`$.

**Inputs** (as quoted in question.md). From 02: $`G_{hh'}=\langle E_{h'}\vert E_h\rangle`$, $`W(h_1,\dots,h_k)=G_{h_1h_2}\cdots G_{h_kh_1}`$, rephasing invariance (2.9), (2.10), and $`W(h,h')=\lvert G_{hh'}\rvert^2`$ (2.11). From 05: $`G_{hh'}(\lambda)=\langle\chi\vert e^{\mathrm iK_{h'}\lambda}e^{-\mathrm iK_h\lambda}\vert\chi\rangle`$ (5.5); $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$ with $`\lvert u_h\rangle=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$ (5.10); the isometry (5.11); $`\langle\chi\vert u_h\rangle=0`$ (5.13). From 06: $`g_1,g_2`$ of (6.8) at $`B_{\beta_0}=0`$, i.e. $`M=K_h`$, $`M'=K_{h'}`$, $`D=K_h-K_{h'}`$.

**Notation.** On $`\mathcal H_c`$ (question.md):
```math
g(v,w)=\mathrm{Re}\langle v\vert w\rangle,\qquad
\omega(v,w)=\mathrm{Im}\langle v\vert w\rangle,\qquad
Jv=\mathrm i\,v,\qquad \lVert v\rVert^2=g(v,v)=\langle v\vert v\rangle .
\qquad\text{(10.1)}
```
$`g`$ and $`\omega`$ are real-bilinear; $`g`$ is symmetric and $`\omega`$ antisymmetric, since $`\langle w\vert v\rangle=\langle v\vert w\rangle^*`$. Throughout, $`\mathrm i`$ is the imaginary unit. In Steps 1–6 the loop index is $`j`$, taken cyclically ($`h_{k+1}:=h_1`$), and $`u_j:=u_{h_j}`$. In Steps 7–8, $`i,j`$ are lattice indices and the loop index is $`m`$. Local abbreviation: $`\Delta_{hh'}:=\langle K_h\rangle-\langle K_{h'}\rangle\in\mathbb R`$.

**Branch and range of validity.** $`\Phi`$ takes values in $`(-\pi,\pi]`$, and $`\mathrm{Arg}`$, $`\mathrm{Log}`$ are principal. Each $`G_{hh'}(\lambda)`$ is an entire function of $`\lambda`$ with $`G_{hh'}(0)=1`$ (finite dimension, A1). Hence for a given loop there is $`\lambda_0>0`$ such that for $`\lvert\lambda\rvert<\lambda_0`$ every $`\mathrm{Re}G_{h_jh_{j+1}}>0`$ and $`\sum_j\lvert\mathrm{Arg}G_{h_jh_{j+1}}\rvert<\pi`$. There $`W\neq0`$, every $`\mathrm{Log}G_{h_jh_{j+1}}`$ is analytic, and
```math
\Phi(h_1,\dots,h_k;\lambda)=\sum_{j=1}^k\mathrm{Arg}G_{h_jh_{j+1}}(\lambda)\qquad(\lvert\lambda\rvert<\lambda_0).
\qquad\text{(10.2)}
```
Every $`O(\lambda^n)`$ refers to $`\lambda\to0`$ in this range. Negative $`\lambda`$ is used only in Step 6(b), as a formal parameter of (1.9). Step 1 and (10.11) hold for every $`\lambda`$. $`\Phi`$ is a datum of the view by (2.9)–(2.10); it is not read as a field, flux or curvature (M1, M4).

## Derivation

### Step 1. The modulus is pairwise data (item 1a)

Since $`G_{h'h}=\langle E_h\vert E_{h'}\rangle=G_{hh'}^*`$, (2.11) reads $`W(h_j,h_{j+1})=G_{h_jh_{j+1}}G_{h_{j+1}h_j}=\lvert G_{h_jh_{j+1}}\rvert^2`$. Taking the squared modulus of the product that defines $`W`$,
```math
\lvert W(h_1,\dots,h_k)\rvert^2=\prod_{j=1}^k\lvert G_{h_jh_{j+1}}\rvert^2=\prod_{j=1}^kW(h_j,h_{j+1}) .
\qquad\text{(10.3)}
```
No expansion is used, so (10.3) holds exactly for every $`\lambda`$. Beyond the pairwise data, $`W`$ carries only its phase $`\Phi`$.

### Step 2. A single overlap to second order (item 1b)

(i) Expanding both exponentials in (5.5),
```math
e^{\mathrm iK_{h'}\lambda}e^{-\mathrm iK_h\lambda}=\mathbb 1-\mathrm i\lambda D+\lambda^2\bigl(K_{h'}K_h-\tfrac12K_h^2-\tfrac12K_{h'}^2\bigr)+O(\lambda^3),
```
and $`K_{h'}K_h-\tfrac12K_h^2-\tfrac12K_{h'}^2=-\tfrac12D^2-\tfrac12[K_h,K_{h'}]`$. Taking $`\langle\cdot\rangle`$ gives $`g_1=-\mathrm i\langle D\rangle`$ and $`g_2=-\frac12\bigl(\langle D^2\rangle+\langle[K_h,K_{h'}]\rangle\bigr)`$, in agreement with (6.8) at $`B_{\beta_0}=0`$.

(ii) By (5.10), $`K_h\lvert\chi\rangle=\lvert u_h\rangle+\langle K_h\rangle\lvert\chi\rangle`$, and $`\langle\chi\vert u_h\rangle=0`$ by (5.13). Since $`K_h=K_h^\dagger`$, $`\langle K_hK_{h'}\rangle=\langle K_h\chi\vert K_{h'}\chi\rangle=\langle u_h\vert u_{h'}\rangle+\langle K_h\rangle\langle K_{h'}\rangle`$. Also, $`D\lvert\chi\rangle=(u_h-u_{h'})+\Delta_{hh'}\lvert\chi\rangle`$ is an orthogonal decomposition. With (10.1) and (5.10), it follows that
```math
\langle[K_h,K_{h'}]\rangle=\langle u_h\vert u_{h'}\rangle-\langle u_{h'}\vert u_h\rangle=2\mathrm i\,\omega(u_h,u_{h'}),
\qquad
\langle D^2\rangle=\lVert D\chi\rVert^2=d_0(h,h')^2+\Delta_{hh'}^2 .
\qquad\text{(10.4)}
```

(iii) Inserting (10.4) and $`\langle D\rangle=\Delta_{hh'}`$ gives
```math
G_{hh'}(\lambda)=1-\mathrm i\lambda\Delta_{hh'}-\frac{\lambda^2}{2}\Bigl(d_0(h,h')^2+\Delta_{hh'}^2+2\mathrm i\,\omega(u_h,u_{h'})\Bigr)+O(\lambda^3).
\qquad\text{(10.5)}
```

(iv) Use $`\mathrm{Log}(1+x)=x-\tfrac12x^2+O(x^3)`$ with $`x^2=-\Delta_{hh'}^2\lambda^2+O(\lambda^3)`$. The $`\Delta_{hh'}^2`$ terms cancel:
```math
\mathrm{Log}G_{hh'}(\lambda)=-\mathrm i\lambda\Delta_{hh'}-\lambda^2\Bigl(\tfrac12d_0(h,h')^2+\mathrm i\,\omega(u_h,u_{h'})\Bigr)+O(\lambda^3).
\qquad\text{(10.6)}
```
The real part is $`\ln\lvert G_{hh'}\rvert=-\frac12\lambda^2d_0(h,h')^2+O(\lambda^3)`$. The imaginary part, rewritten with the antisymmetry of $`\omega`$, is the phase:
```math
\mathrm{Arg}G_{hh'}(\lambda)=-\lambda\bigl(\langle K_h\rangle-\langle K_{h'}\rangle\bigr)+\lambda^2\,\omega(u_{h'},u_h)+O(\lambda^3).
\qquad\text{(10.7)}
```
The phase of a single overlap depends on the phase convention of the branch states fixed in (5.5) (M6). Only cyclic sums of (10.7) are data (2.9).

### Step 3. The loop formula (item 1c)

Sum (10.7) around the loop, using (10.2). The first-order terms telescope, $`\sum_j(\langle K_{h_j}\rangle-\langle K_{h_{j+1}}\rangle)=0`$, and $`\sum_j\omega(u_{j+1},u_j)=-\sum_j\omega(u_j,u_{j+1})`$. Hence
```math
\Phi(h_1,\dots,h_k;\lambda)=-\lambda^2\sum_{j=1}^k\omega\bigl(u_{h_j},u_{h_{j+1}}\bigr)+O(\lambda^3),\qquad k\ge3 .
\qquad\text{(10.8)}
```
The sum is translation invariant. For every $`x\in\mathcal H_c`$, with $`S=\sum_ju_j=\sum_ju_{j+1}`$ and $`\omega(x,x)=0`$,
```math
\sum_j\omega(u_j+x,u_{j+1}+x)=\sum_j\omega(u_j,u_{j+1})+\omega(x,S)+\omega(S,x)=\sum_j\omega(u_j,u_{j+1}).
\qquad\text{(10.9)}
```
For $`k=3`$, take $`x=-u_1`$. The terms with a zero argument drop out, and
```math
\Phi(h_1,h_2,h_3;\lambda)=-\lambda^2\,\omega\bigl(u_{h_2}-u_{h_1},\,u_{h_3}-u_{h_1}\bigr)+O(\lambda^3).
\qquad\text{(10.10)}
```

### Step 4. Reversal (item 1d)

With $`G_{h'h}=G_{hh'}^*`$ (Step 1), for every $`\lambda`$,
```math
W(h_k,\dots,h_1)=\prod_{j=1}^kG_{h_{j+1}h_j}=\prod_{j=1}^kG_{h_jh_{j+1}}^*=W(h_1,\dots,h_k)^* .
\qquad\text{(10.11)}
```
Hence $`\Phi(h_k,\dots,h_1)=-\Phi(h_1,\dots,h_k)`$. This holds exactly for $`\lvert\lambda\rvert<\lambda_0`$, by (10.2) and $`\mathrm{Arg}z^*=-\mathrm{Arg}z`$ for $`\mathrm{Re}z>0`$, and modulo $`2\pi`$ wherever $`W\neq0`$. At order $`\lambda^2`$ it is the antisymmetry of $`\omega`$ in (10.8).

### Step 5. Relation to the metric (item 2)

(i) From (10.1), $`g(Jv,w)=\mathrm{Re}\bigl(-\mathrm i\langle v\vert w\rangle\bigr)=\mathrm{Im}\langle v\vert w\rangle`$, $`g(Jv,Jw)=\mathrm{Re}\langle v\vert w\rangle`$ and $`J^2v=-v`$. Thus
```math
\omega(v,w)=g(Jv,w),\qquad g(Jv,Jw)=g(v,w),\qquad J^2=-\mathbb 1 .
\qquad\text{(10.12)}
```

(ii) *Bound.* Cauchy–Schwarz for $`g`$, together with $`\lVert Jv\rVert=\lVert v\rVert`$, gives $`\lvert\omega(v,w)\rvert\le\lVert v\rVert\,\lVert w\rVert`$. Take $`v=u_{h_2}-u_{h_1}`$ and $`w=u_{h_3}-u_{h_1}`$. By (10.10) and (5.10),
```math
\lvert\Phi(h_1,h_2,h_3;\lambda)\rvert\le\lambda^2\,d_0(h_1,h_2)\,d_0(h_1,h_3)+O(\lambda^3).
\qquad\text{(10.13)}
```

(iii) *Saturation.* Cauchy–Schwarz is an equality iff $`Jv`$ and $`w`$ are real-linearly dependent. So the leading term saturates (10.13) iff
```math
u_{h_3}-u_{h_1}\in\mathbb R\,J\bigl(u_{h_2}-u_{h_1}\bigr)\qquad\text{or}\qquad u_{h_2}=u_{h_1} .
\qquad\text{(10.14)}
```
For $`w=tJv`$ the leading term is $`-\lambda^2t\lVert v\rVert^2`$. Since $`g(Jv,v)=\omega(v,v)=0`$, condition (10.14) splits into two parts. First, the two edges at $`h_1`$ are $`g`$-orthogonal. This is a condition on $`d_0`$ alone, because by polarization $`g(v,w)=\frac12\bigl[d_0(h_1,h_2)^2+d_0(h_1,h_3)^2-d_0(h_2,h_3)^2\bigr]`$. Second, $`w`$ lies in the complex line $`\mathbb Cv=\mathrm{span}_{\mathbb R}\{v,Jv\}`$, which is a condition that involves $`J`$.

(iv) *In what sense the leading loop data are fixed.* By (10.8), (10.9) and (10.12), the leading datum $`\Phi^{(2)}:=-\sum_jg(Ju_j,u_{j+1})`$ depends only on the differences of the record vectors in $`(\mathcal H_c,g)`$, which realize $`d_0`$ by (5.11), and on $`J`$. The metric $`d_0`$ fixes this configuration up to an isometry $`x\mapsto Rx+b`$ of $`(\mathcal H_c,g)`$ (a finite subset of a Euclidean space is fixed by its distances up to an ambient isometry). By (10.12), an orthogonal $`R`$ with $`RJ=JR`$ (a unitary map) leaves every $`\Phi^{(2)}`$ unchanged, and one with $`RJ=-JR`$ (an antiunitary map) reverses every sign. So, at leading order, the loop data are fixed by the $`d_0`$-configuration together with its position relative to $`J`$, up to unitary motions. By itself, $`d_0`$ fixes only $`g`$ on differences, and it bounds $`\Phi^{(2)}`$ by (10.13). It does not fix the loop data:
- *Sign.* In a basis in which $`\chi`$ is real, replace every $`K_h`$ by its entrywise conjugate. The new records are again self-adjoint and have the same $`\langle K_h\rangle`$. Then $`u_h\mapsto u_h^*`$, every $`d_0`$ is unchanged, and $`\omega(u_h^*,u_{h'}^*)=\mathrm{Im}\langle u_h\vert u_{h'}\rangle^*=-\omega(u_h,u_{h'})`$. Every $`\Phi^{(2)}`$ changes sign.
- *Magnitude, $`d_c\ge3`$.* Take orthonormal $`e_1,e_2\perp\chi`$. A record $`K=\lvert u\rangle\langle\chi\rvert+\lvert\chi\rangle\langle u\rvert`$ with $`u\perp\chi`$ has $`\langle K\rangle=0`$ and record vector $`u`$. The triangles with record vectors $`(0,e_1,\mathrm ie_1)`$ and $`(0,e_1,e_2)`$ have the same distances $`1,1,\sqrt2`$. By (10.10), however, the first has $`\Phi=-\lambda^2+O(\lambda^3)`$ and the second $`\Phi=O(\lambda^3)`$.

For $`d_c=2`$, all $`u_h`$ lie in the complex line $`\chi^\perp`$ (5.13). This is a real plane on which $`J`$ acts as a rotation by $`\pi/2`$. On it, $`\lvert g(Jv,w)\rvert`$ is twice the Euclidean area of the triangle, which $`d_0`$ fixes. Only the sign of $`\Phi^{(2)}`$ then needs $`J`$.

### Step 6. When the $`\lambda^2`$ term vanishes (item 3)

(a) *Commuting records.* If $`[K_{h_j},K_{h_{j+1}}]=0`$ for all $`j`$ (in particular, if the records commute pairwise), then (10.4) gives $`\omega(u_j,u_{j+1})=0`$, and the $`\lambda^2`$ term of (10.8) vanishes.

(b) *Real records.* Let $`\chi`$ be real and every $`K_h`$ real symmetric in some basis. Then $`u_h=(K_h-\langle K_h\rangle)\chi`$ is real, so $`\langle u_h\vert u_{h'}\rangle\in\mathbb R`$ and $`\omega(u_h,u_{h'})=0`$: the $`\lambda^2`$ term vanishes. Moreover, for real $`K`$ and real $`\lambda`$ the entrywise conjugate of $`e^{-\mathrm iK\lambda}`$ is $`e^{\mathrm iK\lambda}`$. Conjugating (5.5) entrywise therefore gives $`G_{hh'}(\lambda)^*=\chi^{\mathsf T}e^{-\mathrm iK_{h'}\lambda}e^{\mathrm iK_h\lambda}\chi=G_{hh'}(-\lambda)`$, and
```math
W(h_1,\dots,h_k;-\lambda)=W(h_1,\dots,h_k;\lambda)^* .
\qquad\text{(10.15)}
```
By (10.2), $`\Phi(-\lambda)=-\Phi(\lambda)`$ for $`\lvert\lambda\rvert<\lambda_0`$, where $`\Phi`$ is real-analytic. Its Taylor series therefore has only odd powers, and with (10.8), $`\Phi=O(\lambda^3)`$.

(c) *Collinear record vectors.* Let $`u_{h_j}=x+t_je`$ with $`x,e\in\mathcal H_c`$ and $`t_j\in\mathbb R`$; the line need not pass through $`0`$. Applying (10.9) with $`-x`$ gives $`\sum_j\omega(u_j,u_{j+1})=\sum_jt_jt_{j+1}\,\omega(e,e)=0`$.

### Step 7. Plane (item 4a)

Here $`\chi=\lvert0\rangle`$, $`X\lvert0\rangle=\lvert1\rangle`$, $`Y\lvert0\rangle=\mathrm i\lvert1\rangle`$ and $`\langle0\vert X\vert0\rangle=\langle0\vert Y\vert0\rangle=0`$. For $`K_{h_{(i,j)}}=iX+jY`$ with $`i,j\in\mathbb Z`$, we get $`\langle K_{h_{(i,j)}}\rangle=0`$ and
```math
u_{h_{(i,j)}}=(i+\mathrm i\,j)\lvert1\rangle,\qquad
\omega\bigl((i+\mathrm i\,j)\lvert1\rangle,(i'+\mathrm i\,j')\lvert1\rangle\bigr)=\mathrm{Im}\bigl[(i-\mathrm i\,j)(i'+\mathrm i\,j')\bigr]=ij'-ji' ,
\qquad\text{(10.16)}
```
and the second identity holds for all real $`i,j,i',j'`$. Also, $`d_0(h_{(i,j)},h_{(i',j')})=\sqrt{(i-i')^2+(j-j')^2}`$ and $`J\bigl((i+\mathrm ij)\lvert1\rangle\bigr)=(-j+\mathrm ii)\lvert1\rangle`$, so $`J`$ acts on the labels as the rotation $`(i,j)\mapsto(-j,i)`$. Take a lattice triangle with vertices $`p_m=(i_m,j_m)`$, $`m=1,2,3`$. Since $`u_{h_{p}}`$ is linear in $`p`$, we have $`u_{h_{p_2}}-u_{h_{p_1}}=\bigl((i_2-i_1)+\mathrm i(j_2-j_1)\bigr)\lvert1\rangle`$, and likewise for $`p_3`$. Then (10.10) and (10.16) give
```math
\Phi(h_{p_1},h_{p_2},h_{p_3};\lambda)=-\lambda^2\bigl[(i_2-i_1)(j_3-j_1)-(j_2-j_1)(i_3-i_1)\bigr]+O(\lambda^3)=-2\lambda^2A+O(\lambda^3),
\qquad\text{(10.17)}
```
where $`A=\frac12\det(p_2-p_1,\,p_3-p_1)`$ is the signed area in the coordinates $`(i,j)`$. $`A`$ is positive when $`p_1\to p_2\to p_3`$ runs counterclockwise, with $`i`$ as the first axis and $`j`$ as the second. $`A`$ is computed from the labels by which the description specifies the records. By (5.11) and (10.16), these labels are isometric to the record vectors in the plane $`\chi^\perp`$, and the orientation is the one fixed by $`J`$. Nothing further is attributed to $`A`$.

### Step 8. Line (item 4b)

For $`K_{h_i}=iX`$ the records commute, so $`e^{\mathrm ii'X\lambda}e^{-\mathrm iiX\lambda}=e^{-\mathrm i(i-i')X\lambda}`$. With $`e^{-\mathrm itX}=\cos t\,\mathbb 1-\mathrm i\sin t\,X`$ and $`\langle0\vert X\vert0\rangle=0`$,
```math
G_{h_ih_{i'}}(\lambda)=\cos\bigl((i-i')\lambda\bigr),\qquad
W(h_{i_1},\dots,h_{i_k};\lambda)=\prod_{m=1}^k\cos\bigl((i_m-i_{m+1})\lambda\bigr).
\qquad\text{(10.18)}
```
$`W`$ is real and positive whenever $`\lvert\lambda\rvert\max_m\lvert i_m-i_{m+1}\rvert<\pi/2`$. There $`\Phi=0`$ identically, so in particular its $`\lambda^2`$ term vanishes. This agrees with Step 6, all three cases of which apply: (a) the records commute; (b) $`X`$ is real symmetric and $`\chi`$ is real; (c) $`u_{h_i}=i\lvert1\rangle\in\mathbb R\lvert1\rangle`$.

## Result

1. Exact modulus identity (10.3); single-overlap phase (10.7); loop formula (10.8), with the triangle form (10.10); reversal (10.11).
2. $`\omega=g(J\cdot,\cdot)`$, $`J`$ is $`g`$-orthogonal and $`J^2=-\mathbb 1`$ (10.12). Bound (10.13); saturation iff (10.14). At leading order the loop data are fixed by the $`d_0`$-configuration together with $`J`$, up to unitary motions. They are not fixed by $`d_0`$ alone: $`d_0`$ never fixes the sign, and for $`d_c\ge3`$ it does not fix the magnitude either (Step 5(iv)).
3. The $`\lambda^2`$ term vanishes for commuting records, for real records, and for collinear record vectors (Step 6). For real records, $`W(-\lambda)=W(\lambda)^*`$ (10.15) and $`\Phi`$ is odd.
4. Plane: $`\Phi=-2\lambda^2A+O(\lambda^3)`$ (10.17). Line: $`\Phi\equiv0`$ for small $`\lambda`$ (10.18).

Every formula expected in question.md is confirmed; I found no discrepancy in sign or factor.

## Consistency checks

1. **$`\lambda=0`$ and dimensions.** At $`\lambda=0`$, $`E_h=\chi`$ for every $`h`$, so every $`G=1`$, $`W=1`$ and $`\Phi=0`$. This is consistent with (10.3) and with (10.8), which has no $`\lambda^0`$ or $`\lambda^1`$ term. In (5.5), $`\lambda K_h`$ is dimensionless, and $`u_h`$ has the dimension of $`K_h`$. Hence $`\lambda\Delta_{hh'}`$, $`\lambda^2d_0^2`$, $`\lambda^2\omega(u,u')`$ and both sides of (10.13) are dimensionless, as phases and log-moduli must be.
2. **Unit lattice triangle, exactly.** Take $`(0,0)\to(1,0)\to(0,1)`$, i.e. $`K=0,X,Y`$. Then $`G_{h_1h_2}=\langle0\vert e^{\mathrm iX\lambda}\vert0\rangle=\cos\lambda`$, $`G_{h_3h_1}=\langle0\vert e^{-\mathrm iY\lambda}\vert0\rangle=\cos\lambda`$, and $`G_{h_2h_3}=\langle0\vert e^{\mathrm iY\lambda}e^{-\mathrm iX\lambda}\vert0\rangle=\cos^2\lambda-\mathrm i\sin^2\lambda`$. So $`W=\cos^2\lambda\,(\cos^2\lambda-\mathrm i\sin^2\lambda)`$ and $`\Phi=-\arctan(\tan^2\lambda)=-\lambda^2+O(\lambda^4)`$. This agrees with (10.17) for $`A=\frac12`$, and with (10.7), since $`\lambda^2\omega(\mathrm i\lvert1\rangle,\lvert1\rangle)=-\lambda^2`$. Also, $`\lvert W\rvert^2=\cos^4\lambda\,(\cos^4\lambda+\sin^4\lambda)=W(h_1,h_2)W(h_2,h_3)W(h_3,h_1)`$, exactly as (10.3) requires.
3. **Saturation in the plane.** $`J`$ acts on the labels as the rotation by $`+\pi/2`$ (Step 7). So (10.14) says that $`p_3-p_1`$ is perpendicular to $`p_2-p_1`$, i.e. that the triangle has a right angle at $`p_1`$. In the Euclidean plane, $`2\lvert A\rvert=\lvert p_2-p_1\rvert\,\lvert p_3-p_1\rvert\,\lvert\sin\theta_1\rvert`$, which saturates (10.13) under exactly this condition. The unit triangle has its right angle at $`(0,0)`$ and gives $`\lvert\Phi\rvert=\lambda^2=\lambda^2\cdot1\cdot1`$.

## Open issues

- $`\lambda_0`$ depends on the loop. No statement is made at finite $`\lambda`$, nor beyond order $`\lambda^2`$, except the oddness for real records (out of scope).
- For commuting but non-real records, only the $`\lambda^2`$ term is shown to vanish. Whether the $`\lambda^3`$ term vanishes is not examined.
- (10.7) is the phase of a single overlap in the branch-state convention of (5.5). Only its cyclic sums are convention-free.

## Methods used

- Taylor expansion of matrix exponentials; principal logarithm of a near-unit analytic function
- Decomposition of a Hermitian inner product into a Euclidean form $`g`$, a symplectic form $`\omega`$ and a complex structure $`J`$
- Cauchy–Schwarz inequality and its equality case; polarization identity
- Complex conjugation symmetry for real operators
- Shoelace (determinant) formula for the signed area of a triangle
