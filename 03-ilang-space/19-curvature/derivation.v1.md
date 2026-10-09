# Curvature of the derived background

- **Subproject:** 03-ilang-space
- **Package:** 19-curvature
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

**Model (question.md).** Probe $`a`$ with places $`h`$ labelled by $`x_h\in U\subseteq\mathbb R^k`$ ($`U`$ open). Medium $`c`$ with $`d_c:=\dim\mathcal H_c`$. Optional body $`b`$ at $`\beta_0`$ with $`B:=B_{\beta_0}`$ ($`B=0`$ without a body). All types are pairwise different, so (1.11) imposes nothing. The contract is $`C=\sum_h\lvert h\rangle\langle h\rvert_a\otimes K(x_h)\ \bigl(+\sum_\beta\lvert\beta\rangle\langle\beta\rvert_b\otimes B_\beta\bigr)`$ with $`x\mapsto K(x)`$ smooth and self-adjoint. The start is $`\lvert\phi\rangle_a(\otimes\lvert\beta_0\rangle_b)\otimes\lvert\chi\rangle_c`$ with $`\phi_h\neq0`$.

**Quoted inputs.** (3.5): $`\cos\alpha(x,x')=\sqrt{W(x,x')}`$. (5.6) for $`B=0`$ and (6.6) in general: $`W(h,h';\lambda)=\lvert\langle\chi\vert e^{\mathrm i(K_{h'}+B)\lambda}e^{-\mathrm i(K_h+B)\lambda}\vert\chi\rangle\rvert^2`$. (5.10): $`\alpha(h,h';\lambda)/\lambda\to d_0(h,h')=\lVert u_h-u_{h'}\rVert`$. (5.11): $`d_0`$ is the chord distance of the record set in $`(\mathcal H_c,g)`$. (6.9)–(6.11), with $`D=K_h-K_{h'}`$:
```math
W=1-\lambda^2\mathrm{Var}_\chi(D)+\lambda^3c_3^{(\beta_0)}+O(\lambda^4),\qquad
c_3^{(\beta_0)}=\underbrace{\mathrm{Im}\langle K_{h'}\tilde D^2\rangle}_{c_3^{(0)}}+\mathrm{Im}\langle B\tilde D^2\rangle .
```

**Notation.** $`\langle X\rangle`$, $`\tilde X`$, $`u(x)=\widetilde{K(x)}\chi`$ and $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$ are as in question.md. With $`g`$, the space $`\mathcal H_c`$ is a real Euclidean space $`E\cong\mathbb R^{2d_c}`$. In addition:
- $`M(x):=K(x)+B`$, so $`\psi_x(\lambda)=e^{-\mathrm iM(x)\lambda}\chi`$.
- Coordinate indices are $`a,b,m,n,p,q\in\{1,\dots,k\}`$, with summation convention; they are not object names. $`K_a:=\partial_aK(x)`$, $`K_{ab}:=\partial_a\partial_bK(x)`$, $`\tilde K_a:=K_a-\langle K_a\rangle`$.
- For self-adjoint $`X,Y`$: $`\mathrm{Cov}_\chi(X,Y):=\tfrac12\langle\{X,Y\}\rangle-\langle X\rangle\langle Y\rangle=g(\tilde X\chi,\tilde Y\chi)`$.
- Curvature convention: $`R_{abmn}`$ is normalized so that $`R_{abab}/(g_{aa}g_{bb}-g_{ab}^2)`$ is the sectional curvature of the plane $`(\partial_a,\partial_b)`$; the unit sphere has $`+1`$. For $`k=2`$, the Gaussian curvature is $`\kappa=R_{1212}/\det g`$. $`\hat\kappa`$ is the Gaussian curvature of $`\hat g`$, and $`\kappa_g=\lambda^{-2}\hat\kappa`$ is that of $`g=\lambda^2\hat g`$, because sectional curvatures scale inversely with a constant factor of the metric.

**Assumptions.** These are the setting of question.md and $`\lambda\ge0`$. Expansions in $`\lambda`$ are taken at fixed $`x`$ as $`\lambda\to0^+`$. They hold together with all $`x`$-derivatives and locally uniformly in $`x`$, because $`\hat g`$ is jointly smooth in $`(x,\lambda)`$ (Step 3). Curvatures are computed only where the metric is non-degenerate. The coordinates on $`U`$ are used only to state density and to differentiate (M5); all geometry comes from $`\alpha`$.

## Derivation

### Step 1. Dense family and the witness function on $`U`$

By (5.6) and (6.6), $`W(h,h';\lambda)=W(x_h,x_{h'};\lambda)`$, where $`W(x,x';\lambda)=\lvert\langle\psi_{x'}(\lambda)\vert\psi_x(\lambda)\rangle\rvert^2`$ is a single function on $`U\times U`$. It depends only on $`K(\cdot)`$, $`B`$ and $`\chi`$. It does not depend on $`\phi`$ or on which other places the description contains.

**Limit.** Take a sequence of finite descriptions $`\mathcal D_\nu`$ (A1) with the same medium, $`\chi`$, $`K(\cdot)`$ and body. Let their label sets $`X_\nu=\{x_h\}`$ become dense: for every $`x\in U`$ there are $`x_\nu\in X_\nu`$ with $`x_\nu\to x`$. The witness weights of every $`\mathcal D_\nu`$ are restrictions of the same smooth function $`W`$ ($`K`$ is smooth and the exponential is entire). Hence $`W(x,x')=\lim_\nu W(x_\nu,x'_\nu)`$, and with it $`\alpha=\arccos\sqrt W`$, is fixed on all of $`U\times U`$. No further limit enters. On $`U`$, $`\alpha`$ is a pseudometric: points with $`W=1`$ are identified in $`X_V`$, as in 03.

### Step 2. The metric is the infinitesimal witness angle (item 1a)

Fix $`\lambda`$, $`x`$ and $`v`$, and let $`\psi(\varepsilon):=\psi_{x+\varepsilon v}(\lambda)`$. Write $`\dot\psi=v^a\partial_a\psi`$ and $`\ddot\psi`$ for the derivatives at $`\varepsilon=0`$. Differentiating $`\lVert\psi(\varepsilon)\rVert^2=1`$ once and twice gives $`\mathrm{Re}\langle\dot\psi\vert\psi\rangle=0`$ and $`\mathrm{Re}\langle\ddot\psi\vert\psi\rangle=-\lVert\dot\psi\rVert^2`$. Then
```math
W(x,x+\varepsilon v)=\bigl\lvert1+\varepsilon\langle\dot\psi\vert\psi\rangle+\tfrac{\varepsilon^2}{2}\langle\ddot\psi\vert\psi\rangle\bigr\rvert^2+O(\varepsilon^3)
=1-\varepsilon^2\bigl(\lVert\dot\psi\rVert^2-\lvert\langle\psi\vert\dot\psi\rangle\rvert^2\bigr)+O(\varepsilon^3).
```
The bracket equals $`g_{ab}v^av^b`$ for two reasons. First, $`\lVert\dot\psi\rVert^2=v^av^b\mathrm{Re}\langle\partial_a\psi\vert\partial_b\psi\rangle`$. Second, $`\langle\psi\vert\partial_a\psi\rangle`$ is purely imaginary, so $`\lvert\langle\psi\vert\dot\psi\rangle\rvert^2=v^av^b\langle\partial_a\psi\vert\psi\rangle\langle\psi\vert\partial_b\psi\rangle`$, and this product is real. Since $`\sin^2\alpha=1-W`$ and $`\alpha\to0`$:
```math
\alpha(x,x+\varepsilon v;\lambda)^2=\varepsilon^2g_{ab}(x;\lambda)v^av^b+O(\varepsilon^3),\qquad
\lim_{\varepsilon\to0^+}\frac{\alpha(x,x+\varepsilon v;\lambda)}{\varepsilon}=\sqrt{g_{ab}(x;\lambda)v^av^b}.
\tag{19.1}
```
By polarization, $`\alpha`$ determines $`g`$: the metric $`g`$ is the infinitesimal form of the witness angle. Because $`W`$ is invariant under $`\psi_x\to e^{\mathrm if(x)}\psi_x`$, so is $`g`$ (M6). Since $`\psi_x(0)=\chi`$ for every $`x`$, we have $`g(x;0)=0`$, which is why the rescaled metric $`\hat g`$ is needed.

### Step 3. Exact form of $`\hat g`$

Since $`\partial_aM=K_a`$, Duhamel's formula gives $`\partial_ae^{-\mathrm iM\lambda}=-\mathrm i\int_0^\lambda e^{-\mathrm iM(\lambda-s)}K_ae^{-\mathrm iMs}\,\mathrm ds`$. Hence $`e^{\mathrm iM\lambda}\partial_a\psi_x=-\mathrm i\lambda\bar K_a\chi`$, with the self-adjoint operator
```math
\bar K_a(x;\lambda):=\frac1\lambda\int_0^\lambda e^{\mathrm iM(x)s}K_a(x)\,e^{-\mathrm iM(x)s}\,\mathrm ds=\sum_{j\ge0}\frac{(\mathrm i\lambda)^j}{(j+1)!}\,\mathrm{ad}_M^{\,j}K_a,\qquad \mathrm{ad}_MX:=[M,X].
```
Insert this into the definition of $`g`$. The unitary $`e^{\mathrm iM\lambda}`$ is taken at the same $`x`$ in both factors, and $`\langle\psi_x\vert\partial_b\psi_x\rangle=-\mathrm i\lambda\langle\bar K_b\rangle`$. The result is
```math
\hat g_{ab}(x;\lambda)=\mathrm{Cov}_\chi\bigl(\bar K_a,\bar K_b\bigr)=g\bigl(\widetilde{\bar K_a}\chi,\widetilde{\bar K_b}\chi\bigr).
\tag{19.2}
```
This is exact for $`\lambda>0`$, entire in $`\lambda`$ and jointly smooth in $`(x,\lambda)`$. **Commuting case:** if $`[M(x),K_a(x)]=0`$ for all $`a`$, then $`\bar K_a=K_a`$ and
```math
\hat g_{ab}(x;\lambda)=\mathrm{Cov}_\chi(K_a,K_b)\qquad\text{for every }\lambda .
\tag{19.3}
```

### Step 4. Expansion in $`\lambda`$ (item 1b)

From the series, $`\bar K_a=K_a+\lambda\Delta_a+O(\lambda^2)`$ with $`\Delta_a:=\tfrac{\mathrm i}{2}[M,K_a]=\tfrac{\mathrm i}{2}[M,\tilde K_a]`$, which is self-adjoint. Expand (19.2) using the bilinearity of $`\mathrm{Cov}_\chi`$.

**Order 0.** Since $`\partial_au=\partial_a\bigl(K\chi-\langle K\rangle\chi\bigr)=\tilde K_a\chi`$,
```math
\hat g^{(0)}_{ab}(x)=\mathrm{Cov}_\chi(K_a,K_b)=g(\partial_au,\partial_bu),\qquad\text{i.e. }\ \hat g^{(0)}=u^*g .
\tag{19.4}
```
Thus $`\hat g^{(0)}`$ is the pullback by the record map of the flat metric of $`E`$. The quadratic form is $`\hat g^{(0)}(v,v)=\lVert v^a\partial_au\rVert^2=\mathrm{Var}_\chi(v^aK_a)`$, which vanishes iff $`\chi`$ is an eigenvector of $`v^aK_a`$. So $`\hat g^{(0)}(x)`$ is non-degenerate iff no nonzero real combination $`v^aK_a(x)`$ has $`\chi`$ as an eigenvector, i.e. iff $`u`$ is an immersion at $`x`$. Since $`\langle\chi\vert\tilde X\chi\rangle=0`$, the map $`u`$ and all its derivatives take values in $`\chi^\perp`$, a real subspace $`E_\perp\subset E`$ of dimension $`2(d_c-1)`$.

**Order 1.** $`\hat g^{(1)}_{ab}=\mathrm{Cov}_\chi(K_a,\Delta_b)+\mathrm{Cov}_\chi(\Delta_a,K_b)`$. Let $`X,Y,M`$ be self-adjoint with $`\langle X\rangle=\langle Y\rangle=0`$. Then $`\mathrm{Cov}_\chi(X,Z)=\tfrac12\langle\{X,Z\}\rangle`$, and the identity $`\{X,[M,Y]\}+\{[M,X],Y\}=[M,\{X,Y\}]`$ holds because the terms $`XMY`$ and $`YMX`$ cancel. Use it with $`X=\tilde K_a`$ and $`Y=\tilde K_b`$, together with $`\langle[M,Z]\rangle=2\mathrm i\mathrm{Im}\langle MZ\rangle`$ for self-adjoint $`Z`$, and split $`M=K+B`$. This gives $`\hat g^{(1)}=\hat g^{(1,0)}+\hat g^{(1,B)}`$ with
```math
\hat g^{(1,0)}_{ab}=\frac{\mathrm i}{4}\bigl\langle[K,\{\tilde K_a,\tilde K_b\}]\bigr\rangle=-\frac12\mathrm{Im}\bigl\langle K\{\tilde K_a,\tilde K_b\}\bigr\rangle ,
\tag{19.5}
```
```math
\hat g^{(1,B)}_{ab}=\frac{\mathrm i}{4}\bigl\langle[B,\{\tilde K_a,\tilde K_b\}]\bigr\rangle=-\frac12\mathrm{Im}\bigl\langle B\{\tilde K_a,\tilde K_b\}\bigr\rangle ,
\tag{19.6}
```
where every operator is taken at $`x`$. The body-free part (19.5) is all of $`\hat g^{(1)}`$ when $`B=0`$. The body part (19.6) is linear in $`B`$.

### Step 5. Relation to (5.10) and (6.9)–(6.11) (item 1c)

Put $`x_h=x`$ and $`x_{h'}=x+\varepsilon v`$. Then $`D=-\varepsilon v^aK_a+O(\varepsilon^2)`$, $`\tilde D^2=\varepsilon^2(v^a\tilde K_a)^2+O(\varepsilon^3)`$, $`K_{h'}=K(x)+O(\varepsilon)`$, and $`v^av^b\{\tilde K_a,\tilde K_b\}=2(v^a\tilde K_a)^2`$. Inserting these into the quoted (6.9)–(6.11) and comparing with (19.4)–(19.6):
```math
\begin{aligned}
\mathrm{Var}_\chi(D)&=\varepsilon^2\,\hat g^{(0)}_{ab}v^av^b+O(\varepsilon^3),\\
c_3^{(0)}(h,h')&=-\varepsilon^2\,\hat g^{(1,0)}_{ab}v^av^b+O(\varepsilon^3),\\
\mathrm{Im}\langle B\tilde D^2\rangle&=-\varepsilon^2\,\hat g^{(1,B)}_{ab}v^av^b+O(\varepsilon^3).
\end{aligned}
\tag{19.7}
```
These relations can also be reached by an independent route. By (19.1) and Step 3, $`1-W=\varepsilon^2\lambda^2\bigl[\hat g^{(0)}+\lambda\hat g^{(1)}+O(\lambda^2)\bigr](v,v)+O(\varepsilon^3)`$, while (6.9) gives $`1-W=\lambda^2\mathrm{Var}_\chi(D)-\lambda^3c_3^{(\beta_0)}+O(\lambda^4)`$. Because $`W`$ is jointly smooth in $`(\varepsilon,\lambda)`$, the coefficients of $`\varepsilon^2\lambda^2`$ and $`\varepsilon^2\lambda^3`$ must agree. They do: Step 4 and the inputs from 06 agree, and the body-free and body parts match separately. In words:
- $`\hat g^{(0)}`$ is the infinitesimal form of $`d_0`$ in (5.10). Taking $`\lambda\to0`$ and $`\varepsilon\to0`$ in either order, $`\alpha/(\lambda\varepsilon)\to\sqrt{\hat g^{(0)}(v,v)}`$.
- By (5.11), $`\hat g^{(0)}`$ is the metric that the record set $`u(U)`$ inherits from $`E`$. It is intrinsic, whereas $`d_0`$ is the chord distance.
- $`-\hat g^{(1)}`$ is the infinitesimal form of the $`\lambda^3`$ coefficient $`c_3^{(\beta_0)}`$.

### Step 6. Curvature of $`\hat g^{(0)}`$ (item 2a)

By (19.4), wherever $`\hat g^{(0)}`$ is non-degenerate, $`(U,\hat g^{(0)})`$ is the immersed submanifold $`u(U)`$ of the flat space $`E`$, with the induced metric. Split the second derivatives into tangent and normal parts:
```math
\partial_a\partial_bu=\Gamma^p_{ab}\,\partial_pu+\mathrm{II}_{ab},\qquad g(\mathrm{II}_{ab},\partial_mu)=0 .
\tag{19.8}
```
Differentiating (19.4) gives $`\Gamma_{ab|m}:=g(\partial_a\partial_bu,\partial_mu)=\tfrac12(\partial_a\hat g^{(0)}_{bm}+\partial_b\hat g^{(0)}_{am}-\partial_m\hat g^{(0)}_{ab})`$. So $`\Gamma^p_{ab}=\hat g^{(0)pq}\Gamma_{ab|q}`$ are the Levi-Civita symbols of $`\hat g^{(0)}`$, and $`\mathrm{II}_{ab}=\partial_a\partial_bu-\hat g^{(0)pq}\Gamma_{ab|p}\partial_qu`$ is the second fundamental form. The Gauss equation for a flat ambient space (standard) then gives
```math
\begin{aligned}
\hat R^{(0)}_{abmn}&=g(\mathrm{II}_{am},\mathrm{II}_{bn})-g(\mathrm{II}_{an},\mathrm{II}_{bm})\\
&=g(\partial_a\partial_mu,\partial_b\partial_nu)-g(\partial_a\partial_nu,\partial_b\partial_mu)-\hat g^{(0)pq}\bigl(\Gamma_{am|p}\Gamma_{bn|q}-\Gamma_{an|p}\Gamma_{bm|q}\bigr),
\end{aligned}
\tag{19.9}
```
and for $`k=2`$
```math
\kappa^{(0)}=\frac{g(\mathrm{II}_{11},\mathrm{II}_{22})-g(\mathrm{II}_{12},\mathrm{II}_{12})}{\hat g^{(0)}_{11}\hat g^{(0)}_{22}-(\hat g^{(0)}_{12})^2}.
\tag{19.10}
```

### Step 7. Flatness (item 2b)

By (19.9), a sufficient condition for flatness is
```math
\partial_a\partial_bu(x)\in\mathrm{span}_{\mathbb R}\{\partial_1u(x),\dots,\partial_ku(x)\}\ \ \text{for all }x,a,b
\quad(\mathrm{II}\equiv0)\ \Longrightarrow\ \hat R^{(0)}\equiv0 .
\tag{19.11}
```
It holds in each of the following cases:
- (i) $`K`$ is affine, $`K(x)=K_0+x^aA_a`$. Then $`\partial_a\partial_bu=\tilde K_{ab}\chi=0`$, and $`\hat g^{(0)}_{ab}=\mathrm{Cov}_\chi(A_a,A_b)`$ is constant.
- (ii) $`k=2(d_c-1)`$, for example $`k=2`$ with a qubit medium. Then $`k`$ independent vectors $`\partial_pu`$ span $`E_\perp`$, which contains every $`\partial_a\partial_bu`$.
- (iii) $`k=1`$.

### Step 8. Dependence on the body and on $`\chi`$ (item 2c)

**Body.** (19.4) contains only $`K`$ and $`\chi`$; $`B`$ enters $`\hat g`$ first at order $`\lambda`$, through (19.6). Hence $`\hat g^{(0)}`$, $`\mathrm{II}`$, $`\hat R^{(0)}`$ and $`\kappa^{(0)}`$ are the same with and without a body, for every $`B`$.

**Medium state $`\chi`$.** Since $`\partial_a\partial_bu=\tilde K_{ab}\chi`$, every ingredient of (19.9) is a covariance in $`\chi`$:
```math
\hat g^{(0)}_{ab}=\mathrm{Cov}_\chi(K_a,K_b),\qquad
\Gamma_{ab|m}=\mathrm{Cov}_\chi(K_{ab},K_m),\qquad
g(\partial_a\partial_mu,\partial_b\partial_nu)=\mathrm{Cov}_\chi(K_{am},K_{bn}).
\tag{19.12}
```
So $`\hat g^{(0)}`$ and its curvature depend on $`\chi`$ only through the symmetrized covariance matrix of the operators $`\{K_a(x),K_{ab}(x)\}`$ in $`\chi`$, i.e. through their first and second moments. They are invariant under $`\chi\to e^{\mathrm i\theta}\chi`$ (M6). Otherwise they change with $`\chi`$, because $`\chi`$ selects the immersion $`u=\tilde K\chi`$. The metric degenerates where $`\chi`$ is an eigenvector of some $`v^aK_a`$. For affine $`K`$ the metric is flat for every $`\chi`$.

### Step 9. Body-induced curvature (item 3a)

Let $`k=2`$. By Step 3 and the non-degeneracy of $`\hat g^{(0)}`$, $`\hat\kappa(x;\lambda)=\kappa^{(0)}(x)+\lambda\,\dot\kappa[\hat g^{(1)}](x)+O(\lambda^2)`$, where $`\dot\kappa[h]:=\frac{\mathrm d}{\mathrm dt}\kappa[\hat g^{(0)}+th]\big|_{t=0}`$. We use the standard first variation of the scalar curvature, $`\dot S[h]=-\Delta\mathrm{tr}h+\nabla^a\nabla^bh_{ab}-R^{ab}h_{ab}`$. In two dimensions $`S=2\kappa`$ and $`R_{ab}=\kappa g_{ab}`$, so
```math
\dot\kappa[h]=\tfrac12\bigl(\nabla^a\nabla^bh_{ab}-\Delta\mathrm{tr}h-\kappa^{(0)}\mathrm{tr}h\bigr),
\tag{19.13}
```
where $`\nabla`$, $`\Delta=\nabla^a\nabla_a`$, the trace and the raising of indices all refer to $`\hat g^{(0)}`$. $`\dot\kappa`$ is linear in $`h`$, and $`\hat g^{(0)}`$ does not depend on the body (Step 8). Therefore
```math
\hat\kappa\big|_{B}-\hat\kappa\big|_{B=0}=\lambda\,\dot\kappa\bigl[\hat g^{(1,B)}\bigr]+O(\lambda^2),\qquad
\hat g^{(1,B)}_{ab}=-\tfrac12\mathrm{Im}\langle\chi\vert B\{\tilde K_a,\tilde K_b\}\vert\chi\rangle .
\tag{19.14}
```
For the curvature of $`g`$, the change is $`\lambda^{-1}\dot\kappa[\hat g^{(1,B)}]+O(1)`$, one order below the leading term $`\lambda^{-2}\kappa^{(0)}`$. If $`\hat g^{(0)}=\delta`$ in linear coordinates, (19.13) reduces to $`\dot\kappa[h]=\partial_1\partial_2h_{12}-\tfrac12(\partial_2^2h_{11}+\partial_1^2h_{22})`$.

### Step 10. Sufficient conditions for no change (item 3b)

- **(V1)** $`\hat g^{(1,B)}\equiv0`$ on $`U`$. By (19.6) this holds if any of the following is true:
  - (a) $`B\chi=\beta\chi`$. Then $`\langle\chi\vert[B,Z]\vert\chi\rangle=0`$ for every $`Z`$.
  - (b) $`[B,K_a(x)]=0`$ for all $`a`$ and $`x`$.
  - (c) $`\{\tilde K_a,\tilde K_b\}\chi=z_{ab}\chi`$ for all $`a,b,x`$. Then $`z_{ab}`$ is real and $`\langle[B,Z]\rangle=z_{ab}\langle B\rangle-z_{ab}\langle B\rangle=0`$ for every $`B`$. In this case $`\hat g^{(1,0)}=0`$ as well.
- **(V2)** $`K`$ is affine. Then $`\tilde K_a`$ is constant, so $`\hat g^{(0)}`$ and $`\hat g^{(1,B)}`$ are constant in $`x`$, $`\kappa^{(0)}=0`$, and every term of (19.13) vanishes. Also $`\hat g^{(1,0)}`$ is affine in $`x`$, so $`\hat\kappa=O(\lambda^2)`$ altogether.
- **(V3)** $`\hat g^{(1,B)}=\mathcal L_\xi\hat g^{(0)}`$ for a vector field $`\xi`$ with $`\xi^a\partial_a\kappa^{(0)}=0`$. Differentiating $`\kappa[\Phi_t^*\hat g^{(0)}]=\kappa^{(0)}\circ\Phi_t`$, where $`\Phi_t`$ is the flow of $`\xi`$, gives $`\dot\kappa[\mathcal L_\xi\hat g^{(0)}]=\xi^a\partial_a\kappa^{(0)}=0`$.

```math
\text{(V1) or (V2) or (V3)}\ \Longrightarrow\ \hat\kappa\big|_B-\hat\kappa\big|_{B=0}=O(\lambda^2).
\tag{19.15}
```

### Step 11. Example 4(a): qubit plane

Without a body, use polar label coordinates $`(x,y)=r(\cos\phi,\sin\phi)`$. Then $`K=r\,n\cdot\sigma`$ with $`(n\cdot\sigma)^2=\mathbb 1`$ and $`(\cos\phi\,\sigma_x+\sin\phi\,\sigma_y)\lvert0\rangle=e^{\mathrm i\phi}\lvert1\rangle`$, so $`\psi_x=\cos t\,\lvert0\rangle+e^{\mathrm i\mu}\sin t\,\lvert1\rangle`$ with $`t=\lambda r`$ and $`\mu=\phi-\pi/2`$. For this form, $`\lVert\mathrm d\psi\rVert^2=\mathrm dt^2+\sin^2t\,\mathrm d\mu^2`$ and $`\langle\psi\vert\mathrm d\psi\rangle=\mathrm i\sin^2t\,\mathrm d\mu`$. The metric is therefore $`\mathrm dt^2+\tfrac14\sin^2(2t)\,\mathrm d\mu^2`$:
```math
g=\lambda^2\mathrm dr^2+\tfrac14\sin^2(2\lambda r)\,\mathrm d\phi^2,\qquad
g_{ab}=\lambda^2\frac{x^ax^b}{r^2}+\frac{\sin^2(2\lambda r)}{4r^2}\Bigl(\delta_{ab}-\frac{x^ax^b}{r^2}\Bigr),
\tag{19.16}
```
with $`(x^1,x^2)=(x,y)`$ and $`g_{ab}=\lambda^2\delta_{ab}`$ at $`r=0`$. The metric is non-degenerate except on the circles $`r=m\pi/(2\lambda)`$, $`m=1,2,\dots`$. For a metric $`\mathrm dr^2+f^2\mathrm d\phi^2`$ the Gaussian curvature is $`-f''/f`$; here $`\hat g`$ has $`f=\sin(2\lambda r)/(2\lambda)`$, so
```math
\hat\kappa=4\lambda^2,\qquad \kappa_g=4\qquad\text{wherever $g$ is non-degenerate, for every }\lambda>0 .
\tag{19.17}
```
**With a body.** Up to phase, every unit vector of $`\mathbb C^2`$ has the form $`\cos t\lvert0\rangle+e^{\mathrm i\mu}\sin t\lvert1\rangle`$. The computation above therefore shows that the Fubini–Study metric on $`\mathbb{CP}^1`$ is a round sphere of radius $`1/2`$, with curvature $`4`$. For any $`B`$, $`g=F^*g_{\rm FS}`$ with $`F(x)=[\psi_x(\lambda)]`$. Where $`g`$ is non-degenerate, $`\mathrm dF`$ is injective, so $`F`$ is a local diffeomorphism between 2-manifolds and hence a local isometry. By the Theorema egregium, $`\kappa_g=4`$.

**Answer: no.** The Gaussian curvature does not change, for every self-adjoint $`B`$; the same holds for every $`K`$ and $`\chi`$ whenever $`d_c=2`$. Perturbatively, $`\{\sigma_a,\sigma_b\}=2\delta_{ab}`$, so (V1c) applies.

### Step 12. Example 4(b): commuting plane

$`K_1=\sigma_x^{(1)}`$ and $`K_2=\sigma_x^{(2)}`$ commute with $`K`$, so (19.3) holds for every $`\lambda`$. In $`\lvert00\rangle`$ we have $`\langle\sigma_x^{(a)}\rangle=0`$, $`(\sigma_x^{(a)})^2=\mathbb 1`$ and $`\langle\sigma_x^{(1)}\sigma_x^{(2)}\rangle=0`$. Hence
```math
g=\lambda^2(\mathrm dx^2+\mathrm dy^2),\qquad \hat g=\mathrm dx^2+\mathrm dy^2,\qquad \kappa_g=\hat\kappa=0\qquad\text{for every }\lambda,
\tag{19.18}
```
and the metric is non-degenerate everywhere. Direct check: $`W=\cos^2(\lambda(x-x'))\cos^2(\lambda(y-y'))`$, and its $`\varepsilon^2`$ coefficient gives (19.18) through (19.1).

### Step 13. Example 4(c): curved record map

Since $`u\in\mathrm{span}_{\mathbb C}\{e_2,e_3\}\perp e_1=\chi`$, we have $`K\chi=u`$ and $`\langle K\rangle=0`$: the record map is $`u`$ itself. The real vectors $`f_1=e_2`$, $`f_2=e_3`$, $`f_3=\mathrm ie_2`$ are $`g`$-orthonormal ($`g(e_2,\mathrm ie_2)=\mathrm{Re}\mathrm i=0`$). In them, $`u=R(\sin\theta\cos\varphi\,f_1+\sin\theta\sin\varphi\,f_2+\cos\theta\,f_3)`$, the round sphere of radius $`R`$ in $`E_3=\mathrm{span}_{\mathbb R}\{f_1,f_2,f_3\}`$. By (19.4),
```math
\hat g^{(0)}=R^2\bigl(\mathrm d\theta^2+\sin^2\theta\,\mathrm d\varphi^2\bigr),\qquad \kappa^{(0)}=\frac1{R^2}.
\tag{19.19}
```
The same value follows from (19.10). We have $`\partial_a\partial_bu\in E_3`$, and the normal of the tangent plane inside $`E_3`$ is $`u/R`$. Differentiating $`g(u,u)=R^2`$ twice gives $`g(\partial_a\partial_bu,u)=-\hat g^{(0)}_{ab}`$, so $`\mathrm{II}_{ab}=-\hat g^{(0)}_{ab}u/R^2`$ and $`\hat R^{(0)}_{1212}=R^{-2}\det\hat g^{(0)}`$.

**Body part.** $`K_a=\lvert\partial_au\rangle\langle e_1\rvert+\lvert e_1\rangle\langle\partial_au\rvert`$ has $`\langle K_a\rangle=0`$, so $`\tilde K_a=K_a`$. Moreover $`K_b\chi=\partial_bu`$ and $`K_a\partial_bu=\langle\partial_au\vert\partial_bu\rangle e_1`$. Hence
```math
\{\tilde K_a,\tilde K_b\}\chi=2\hat g^{(0)}_{ab}\,\chi\ \Longrightarrow\ \hat g^{(1,B)}=0\ \text{ for every self-adjoint $B$ on }\mathbb C^3,\qquad \hat g^{(1,0)}=0,
\tag{19.20}
```
by (V1c). So $`\hat g=\hat g^{(0)}+O(\lambda^2)`$ and $`\hat\kappa=R^{-2}+O(\lambda^2)`$ for every $`B`$.

## Result

1. **Item 1.** The background metric is the infinitesimal witness angle, $`\alpha(x,x+\varepsilon v)^2=\varepsilon^2g(v,v)+O(\varepsilon^3)`$ (19.1).
   - Exact form: $`\hat g_{ab}=\mathrm{Cov}_\chi(\bar K_a,\bar K_b)`$ (19.2); $`\hat g=\hat g^{(0)}`$ for all $`\lambda`$ in the commuting case (19.3).
   - Leading order: $`\hat g^{(0)}=u^*g`$ (19.4).
   - First order: $`\hat g^{(1)}=\frac{\mathrm i}{4}\langle[K+B,\{\tilde K_a,\tilde K_b\}]\rangle`$, split into the body-free part (19.5) and the body part (19.6).
   - Relation to earlier packages: (19.7). $`\hat g^{(0)}`$ is the infinitesimal $`d_0`$ of (5.10); $`-\hat g^{(1)}`$ is the infinitesimal $`c_3^{(\beta_0)}`$ of (6.10)–(6.11), part by part.
2. **Item 2.** The curvature of $`\hat g^{(0)}`$ is given by the Gauss equation of the record surface $`u(U)\subset(\mathcal H_c,g)`$, (19.8)–(19.10).
   - Flatness holds if $`\mathrm{II}\equiv0`$ (19.11), in particular for affine $`K`$, for $`k=2(d_c-1)`$, or for $`k=1`$.
   - $`\hat g^{(0)}`$ and its curvature do not depend on the body. They depend on $`\chi`$ only through the covariances (19.12).
3. **Item 3.** The body changes $`\hat\kappa`$ at order $`\lambda`$ by $`\lambda\,\dot\kappa[\hat g^{(1,B)}]`$, given by (19.13)–(19.14). This change vanishes under (V1), (V2) or (V3), see (19.15).
4. **Item 4.**
   - (a) Without a body, $`g=\lambda^2\mathrm dr^2+\frac14\sin^2(2\lambda r)\mathrm d\phi^2`$, with $`\kappa_g=4`$ and $`\hat\kappa=4\lambda^2`$ (19.16)–(19.17). With a body, the curvature does not change, for any $`B`$.
   - (b) $`g=\lambda^2(\mathrm dx^2+\mathrm dy^2)`$, flat for every $`\lambda`$ (19.18).
   - (c) $`\hat g^{(0)}=R^2(\mathrm d\theta^2+\sin^2\theta\,\mathrm d\varphi^2)`$ with $`\kappa^{(0)}=R^{-2}`$ (19.19), and $`\hat g^{(1,B)}=0`$ for every $`B`$ (19.20).

## Consistency checks

1. **Scaling and dimensions.** Under $`(K,B)\to(sK,sB)`$ we have $`\psi_x(\lambda)\to\psi_x(s\lambda)`$, so $`\hat g(\lambda)\to s^2\hat g(s\lambda)`$. This requires $`\hat g^{(0)}\to s^2\hat g^{(0)}`$ and $`\hat g^{(1)}\to s^3\hat g^{(1)}`$; indeed (19.4) is quadratic and (19.5)–(19.6) are cubic in $`(K,B)`$. In (19.10), $`\mathrm{II}\sim s`$ and $`\det\hat g^{(0)}\sim s^4`$, so $`\kappa^{(0)}\sim s^{-2}`$. This matches $`R\to sR`$ in (19.19), and in 4(a) $`\kappa_g=4`$ is scale-invariant. Dimensions: $`\lambda K`$ is dimensionless, so $`\hat g^{(0)}`$ and $`\lambda\hat g^{(1)}`$ both carry $`[K]^2`$.
2. **Special cases.** For $`k=1`$, (19.9) vanishes by antisymmetry, as every 1-dimensional metric must. For $`B=\beta\mathbb 1`$, the body only adds a global phase to $`\psi_x`$; consistently, (19.6) gives $`\hat g^{(1,B)}=0`$.
3. **Exact versus perturbative (4a).** Expanding (19.16) gives $`\hat g=\delta+O(\lambda^2)`$. This matches (19.4), since $`\mathrm{Cov}_{\lvert0\rangle}(\sigma_a,\sigma_b)=\delta_{ab}`$, and (19.5), which vanishes because $`\{\sigma_a,\sigma_b\}=2\delta_{ab}`$. Correspondingly $`\hat\kappa=4\lambda^2`$ has no terms of order $`1`$ or $`\lambda`$, in line with (19.11) and (19.15).

## Open issues

- The order-$`\lambda^2`$ terms of $`\hat g`$ and $`\hat\kappa`$ are not computed. In 4(a) and 4(c) the body affects $`\hat\kappa`$ at most at order $`\lambda^2`$; in 4(a) it has no effect at all. No example with a nonzero first-order body-induced curvature is exhibited. Such an example needs non-affine $`K`$, $`d_c\ge3`$, and violation of (V1)–(V3).
- The conditions (V1)–(V3) and (19.11) are sufficient, not necessary.
- Global questions are not addressed: the degeneracy sets (for example the circles in 4(a)), and the relation between the geodesic distance of $`g`$ and $`\alpha`$.

## Methods used

- Fubini–Study metric, Taylor expansion of overlaps, polarization
- Duhamel formula, adjoint series, symmetrized covariances
- Induced metric of an immersion, Gauss equation, second fundamental form
- First variation of scalar curvature, Lie-derivative (diffeomorphism) invariance
- Theorema egregium, curvature of $`\mathrm dr^2+f^2\mathrm d\phi^2`$, Bloch parametrization of $`\mathbb{CP}^1`$
