# Cut boundary: points, edges and the leading-order witness geometry

- **Subproject:** 03-ilang-space
- **Package:** 03-ilang-space/11-cut-boundary
- **Version:** v1
- **Mode:** new
- **Date:** 2026-10-08

## Setup and assumptions

- **Description.** A1–A7 hold, $`\mathcal H=\mathcal H_A\otimes\mathcal H_{\bar A}`$ with $`\bar A\neq\emptyset`$, and no type has objects on both sides of the cut. Every swap $`P_{ab}`$ therefore acts on one factor only, and Law 5 imposes no constraint across the cut. All contracts are independent of $`\lambda`$ (A5).
- **Splitting of the contract system.** We use
```math
C=C_A+C_{\bar A}+C_\partial,\qquad C_\partial=\sum_nA_n\otimes B_n ,
\tag{11.1}
```
  with $`A_n=A_n^\dagger`$ on $`\mathcal H_A`$ and $`B_n=B_n^\dagger`$ on $`\mathcal H_{\bar A}`$. We write $`C_A`$ also for $`C_A\otimes\mathbb 1_{\bar A}`$, and likewise for $`C_{\bar A}`$. A5 packs a single-object term into a pair term; we count such a term in $`C_A`$ or $`C_{\bar A}`$, according to the object it acts on (this is how item 4 (a) of the question reads). Step 3 shows that $`d_0`$ does not depend on this convention.
- **Definitions (question).** For item 2, the initial state is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$ with $`\phi_h\neq0`$ for every joint place $`h`$ of $`A`$, and $`\langle B\rangle:=\langle\chi\vert B\vert\chi\rangle`$. Then
```math
c_n(h):=\frac{\langle h\vert A_n\vert\phi\rangle}{\phi_h},\qquad \lvert\tilde u_n\rangle:=\bigl(B_n-\langle B_n\rangle\bigr)\lvert\chi\rangle,\qquad \lvert u_h\rangle:=\sum_nc_n(h)\,\lvert\tilde u_n\rangle .
\tag{11.2}
```
  Auxiliary notation: $`Q_\chi:=\mathbb 1_{\bar A}-\lvert\chi\rangle\langle\chi\rvert`$, and $`g(v,w)=\mathrm{Re}\langle v\vert w\rangle`$ on $`\mathcal H_{\bar A}`$, so that $`\lVert v\rVert^2=g(v,v)`$.
- **Inputs (as quoted).** These are (2.1), (2.2) and (2.11) of 02; (3.1) and (3.5) of 03, with the definitions of $`\approx`$, $`X_V`$ and $`\alpha`$; (4.1) and (4.3) of 04, with its order invariance; and (5.10) and (5.13) of 05.
- **Small $`\lambda`$.** $`\mathcal H`$ is finite-dimensional (A1), so $`\lambda\mapsto e^{-iC\lambda}`$ is analytic. $`O(\lambda^k)`$ means a norm bound, uniform over the finitely many places. An edge of $`N_V`$ joins two distinct points, as in (4.3).

## Derivation

### Step 1. No boundary (item 1, short argument)

(a) If $`\partial A=\emptyset`$, then $`C=C_A\otimes\mathbb 1+\mathbb 1\otimes C_{\bar A}`$. The two summands act on different factors and commute, so
```math
e^{-iC\lambda}=U_A(\lambda)\otimes U_{\bar A}(\lambda),\qquad U_A(\lambda)=e^{-iC_A\lambda},\quad U_{\bar A}(\lambda)=e^{-iC_{\bar A}\lambda}.
\tag{11.3}
```
Hence $`\lvert\Psi(\lambda)\rangle=U_A\lvert\psi_A\rangle\otimes U_{\bar A}\lvert\psi_{\bar A}\rangle`$ is a product for every $`\lambda`$. By (2.1), $`\lvert\psi_h(\lambda)\rangle=\langle h\vert U_A\psi_A\rangle\,U_{\bar A}\lvert\psi_{\bar A}\rangle`$, so all branch vectors are parallel. By (2.2), $`V_A=\lvert U_A\psi_A\rangle\langle U_A\psi_A\rvert`$ is pure. By (2.11), $`W(h,h')=1`$ for all $`h,h'\in H_V`$. By (3.1), all present places are $`\approx`$-equivalent, so $`X_V`$ has exactly one element. No two distinct points exist, so there is no edge.

(b) Let $`\lvert\Psi(0)\rangle`$ be an arbitrary admissible state, with $`\rho_0=\lvert\Psi(0)\rangle\langle\Psi(0)\rvert`$. By (11.3), and by cyclicity of the partial trace in the traced factor, $`\mathrm{Tr}_{\bar A}[(X\otimes Y)\rho_0(X'\otimes Y^\dagger)]=X\mathrm{Tr}_{\bar A}[(\mathbb 1\otimes Y^\dagger Y)\rho_0]X'`$. With $`Y=U_{\bar A}`$ unitary, this gives
```math
V_A(\lambda)=U_A(\lambda)\,V_A(0)\,U_A(\lambda)^\dagger .
\tag{11.4}
```
A unitary conjugation preserves the spectrum, so the spectrum of $`V_A`$ does not depend on $`\lambda`$.

### Step 2. First-order branch vectors (item 2)

1. Analyticity gives $`\lvert\Psi(\lambda)\rangle=\lvert\phi\chi\rangle-i\lambda\,C\lvert\phi\chi\rangle+O(\lambda^2)`$. We apply $`\langle h\rvert\otimes\mathbb 1_{\bar A}`$ to each part of (11.1):
   - $`C_A`$ gives $`\langle h\vert C_A\vert\phi\rangle\lvert\chi\rangle`$;
   - $`C_{\bar A}`$ gives $`\phi_h\,C_{\bar A}\lvert\chi\rangle`$;
   - $`C_\partial`$ gives $`\sum_n\langle h\vert A_n\vert\phi\rangle B_n\lvert\chi\rangle=\phi_h\sum_nc_n(h)B_n\lvert\chi\rangle`$.

   With (2.1) this gives
```math
\frac{\lvert\psi_h(\lambda)\rangle}{\phi_h}=\lvert\chi\rangle-i\lambda\lvert v_h\rangle+O(\lambda^2),\qquad
\lvert v_h\rangle:=\gamma_h\lvert\chi\rangle+C_{\bar A}\lvert\chi\rangle+\sum_nc_n(h)B_n\lvert\chi\rangle,\qquad \gamma_h:=\frac{\langle h\vert C_A\vert\phi\rangle}{\phi_h}.
\tag{11.5}
```
   In particular $`p_h(\lambda)=\lvert\phi_h\rvert^2+O(\lambda)>0`$ for small $`\lambda`$, so every place is present.
2. Since $`Q_\chi\lvert\chi\rangle=0`$ and $`Q_\chi B_n\lvert\chi\rangle=\lvert\tilde u_n\rangle`$,
```math
Q_\chi\lvert v_h\rangle=Q_\chi C_{\bar A}\lvert\chi\rangle+\lvert u_h\rangle,\qquad
\lvert u_h\rangle=\frac{1}{\phi_h}\,Q_\chi\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)C_\partial\bigl(\lvert\phi\rangle\otimes\lvert\chi\rangle\bigr).
\tag{11.6}
```
   The second form shows that $`u_h`$ depends only on $`C_\partial`$, $`\phi`$ and $`\chi`$, and not on the chosen decomposition $`\sum_nA_n\otimes B_n`$. Changing the phase of $`\phi`$ leaves $`u_h`$ unchanged. Changing the phase of $`\chi`$ multiplies every $`u_h`$ by the same phase. Neither change affects $`\lVert u_h-u_{h'}\rVert`$ (M6).

### Step 3. The leading-order angle (item 2)

1. Let $`f_h(\lambda):=(\psi_h/\phi_h)/\lVert\psi_h/\phi_h\rVert`$, a unit vector. By (2.2) and (2.11), $`W(h,h';\lambda)=\lvert\langle f_{h'}\vert f_h\rangle\rvert^2`$; the phases of $`\phi_h`$ drop out of the modulus. By (11.5), $`\lVert\psi_h/\phi_h\rVert^{-1}=1+O(\lambda)`$, so $`f_h=(1+O(\lambda))\lvert\chi\rangle-i\lambda\lvert v_h\rangle+O(\lambda^2)\to\lvert\chi\rangle`$. With (11.6), the common term $`Q_\chi C_{\bar A}\chi`$ cancels in differences: $`Q_\chi(f_h-f_{h'})=-i\lambda(u_h-u_{h'})+O(\lambda^2)`$. The standard fact quoted in the question then gives
```math
1-W(h,h';\lambda)=\lambda^2\lVert u_h-u_{h'}\rVert^2+O(\lambda^3).
\tag{11.7}
```
2. By (3.5), $`\sin^2\alpha=1-W`$ with $`\alpha\in[0,\pi/2]`$, and $`\alpha\to0`$ by (11.7). Hence $`(\alpha/\lambda)^2=(\alpha/\sin\alpha)^2\,(1-W)/\lambda^2\to d_0^2`$, where $`\alpha/\sin\alpha:=1`$ at $`\alpha=0`$. Therefore
```math
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert .
\tag{11.8}
```
3. **No dependence on $`C_A`$, $`C_{\bar A}`$.** In (11.5), $`C_A`$ enters only through $`\gamma_h\lvert\chi\rangle`$, which $`Q_\chi`$ removes. $`C_{\bar A}`$ enters only through $`C_{\bar A}\lvert\chi\rangle`$, which is the same for every $`h`$ and cancels in $`u_h-u_{h'}`$. So $`d_0`$ is fixed by $`C_\partial`$, $`\phi`$ and $`\chi`$ alone, via (11.6). The same argument settles the single-object convention of the Setup. A piece $`D\otimes\mathbb 1_{\bar A}`$ counted in $`C_\partial`$ adds $`\phi_h^{-1}\langle h\vert D\vert\phi\rangle\,Q_\chi\lvert\chi\rangle=0`$ to $`u_h`$. A piece $`\mathbb 1_A\otimes D'`$ adds $`Q_\chi D'\lvert\chi\rangle`$ to every $`u_h`$, which cancels in differences.
4. **Orthogonality.** $`\langle\chi\vert\tilde u_n\rangle=\langle B_n\rangle-\langle B_n\rangle\langle\chi\vert\chi\rangle=0`$. By linearity,
```math
\langle\chi\vert u_h\rangle=0\qquad\text{for every }h .
\tag{11.9}
```
   So $`\{u_h\}`$ is a finite configuration in the real Euclidean space $`(\mathrm{ran}Q_\chi,g)`$, which is $`g`$-orthogonal to $`\chi`$ and $`i\chi`$. $`d_0`$ is its Euclidean distance.
5. **Recording type.** If every $`A_n`$ is diagonal, then $`\langle h\vert A_n\vert\phi\rangle=\langle h\vert A_n\vert h\rangle\phi_h`$, so $`c_n(h)=\langle h\vert A_n\vert h\rangle\in\mathbb R`$. Since $`\langle\cdot\rangle`$ is linear,
```math
\lvert u_h\rangle=\sum_n\langle h\vert A_n\vert h\rangle\bigl(B_n-\langle B_n\rangle\bigr)\lvert\chi\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle,\qquad K_h:=\sum_n\langle h\vert A_n\vert h\rangle B_n=K_h^\dagger .
\tag{11.10}
```
   Here $`C_\partial=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$ is a recording contract, and (11.10) is the record vector of (5.10). Correspondingly, (11.9) becomes (5.13).

### Step 4. Edges at small $`\lambda`$ (item 3, short argument)

There are finitely many places (A1), so finitely many conditions each hold for $`\lambda`$ below a positive threshold. The minimum of these thresholds is positive.

1. If $`u_h\neq u_{h'}`$, then $`d_0(h,h')>0`$. By (11.8), $`\alpha(h,h';\lambda)>0`$, so $`W<1`$ and $`h\not\approx h'`$ by (3.1). Together with Step 2, $`H_V`$ is the set of all places, and each place is its own point.
2. $`\alpha\to0<\pi/2`$, so $`x\asymp x'`$ for every pair by (4.1).
3. Take distinct $`x,y,x'`$. The quantity $`\lambda^{-1}\bigl[\max(\alpha(x,y),\alpha(y,x'))-\alpha(x,x')\bigr]`$ tends to $`\max(d_0(x,y),d_0(y,x'))-d_0(x,x')`$, which is $`\neq0`$ by assumption. So for small $`\lambda`$ the bracket has the sign of its limit. The choices $`y=x`$ and $`y=x'`$ never satisfy the strict inequality of (4.3), because $`\alpha(x,x)=0`$. With point 2, (4.3) becomes
```math
x\sim x'\;\Longleftrightarrow\;\text{no }y\text{ with }\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x') .
\tag{11.11}
```
   So $`N_V(\lambda)`$ is the relative-neighbourhood graph of $`\{u_h\}`$ in $`(\mathrm{ran}Q_\chi,\lVert\cdot\rVert)`$. This agrees with the order invariance of 04: at small $`\lambda`$, the order of the $`\alpha`$ values is the order of the $`d_0`$ values.

### Step 5. Example (a): internal motion (item 4 (a))

Take $`A_i=\lvert h_i\rangle\langle h_i\rvert`$ and $`B_i=K_{h_i}`$, for $`i=1,\dots,n`$. Here $`K_h=K_h^\dagger`$, as required by $`C=C^\dagger`$. This decomposition is diagonal, so (11.10) applies with $`K_{h_i}`$ itself. The term $`C_A`$ enters (11.5) only through
```math
\gamma_{h_i}=t\,\frac{\phi_{h_{i-1}}+\phi_{h_{i+1}}}{\phi_{h_i}}\qquad(\phi_{h_0}=\phi_{h_{n+1}}:=0),
```
multiplied by $`\lvert\chi\rangle`$, and $`Q_\chi`$ removes it (Step 3.3). Hence, for every real $`t`$,
```math
d_0(h_i,h_j)=\bigl\lVert(K_{h_i}-\langle K_{h_i}\rangle)\chi-(K_{h_j}-\langle K_{h_j}\rangle)\chi\bigr\rVert ,
\tag{11.12}
```
which is the value of (5.10), i.e. the value at $`t=0`$.

### Step 6. Example (b): a crossing contract that moves weight (item 4 (b))

1. **Leading order.** There is one term, $`A_1=X:=\lvert h_1\rangle\langle h_2\rvert+\lvert h_2\rangle\langle h_1\rvert`$ with $`B_1=B`$. From $`\langle h_1\vert X\vert\phi\rangle=\phi_{h_2}`$ and $`\langle h_2\vert X\vert\phi\rangle=\phi_{h_1}`$ we get $`c_1(h_1)=\phi_{h_2}/\phi_{h_1}`$ and $`c_1(h_2)=\phi_{h_1}/\phi_{h_2}`$. Also $`\lVert\tilde u_1\rVert^2=\langle\chi\vert(B-\langle B\rangle)^2\vert\chi\rangle=\langle B^2\rangle-\langle B\rangle^2=\sigma_\chi(B)^2`$. Then $`u_{h_1}-u_{h_2}=(c_1(h_1)-c_1(h_2))\tilde u_1`$ gives
```math
d_0(h_1,h_2)=\Bigl\lvert\frac{\phi_{h_2}}{\phi_{h_1}}-\frac{\phi_{h_1}}{\phi_{h_2}}\Bigr\rvert\,\sigma_\chi(B).
\tag{11.13}
```
2. **Dependence on the state of $`a`$.** Write $`\phi_{h_2}/\phi_{h_1}=\rho e^{i\beta}`$ with $`\rho>0`$. Then
```math
d_0(h_1,h_2)^2=\Bigl[(\rho-\rho^{-1})^2+4\sin^2\beta\Bigr]\sigma_\chi(B)^2 .
\tag{11.14}
```
   As $`\phi`$ varies, this takes every value in $`[0,\infty)`$, and it depends on both the weight ratio $`\rho`$ and the relative phase $`\beta`$. Since $`\sigma_\chi(B)>0`$, it vanishes iff $`\rho=1`$ and $`\sin\beta=0`$, i.e. iff $`\phi_{h_2}=\pm\phi_{h_1}`$. In contrast, the recording vectors (11.10) do not involve $`\phi`$ at all.
3. **Exact evolution.** Here $`C=X\otimes B`$. Let $`\lvert\pm\rangle:=(\lvert h_1\rangle\pm\lvert h_2\rangle)/\sqrt2`$, so $`X\lvert\pm\rangle=\pm\lvert\pm\rangle`$, and let $`\phi_\pm:=(\phi_{h_1}\pm\phi_{h_2})/\sqrt2`$. On $`\lvert\pm\rangle\otimes\mathcal H_c`$, $`C`$ acts as $`\pm B`$. Therefore
```math
\lvert\Psi(\lambda)\rangle=\phi_+\lvert+\rangle\otimes e^{-iB\lambda}\lvert\chi\rangle+\phi_-\lvert-\rangle\otimes e^{iB\lambda}\lvert\chi\rangle,\qquad
\lvert\psi_{h_{1,2}}(\lambda)\rangle=\tfrac{1}{\sqrt2}\bigl(\phi_+e^{-iB\lambda}\pm\phi_-e^{iB\lambda}\bigr)\lvert\chi\rangle .
\tag{11.15}
```
   If $`\phi_{h_1}=\phi_{h_2}`$, then $`\phi_-=0`$ and $`\psi_{h_1}(\lambda)=\psi_{h_2}(\lambda)`$, with $`p_{h_1}=p_{h_2}=1/2`$. If $`\phi_{h_1}=-\phi_{h_2}`$, then $`\phi_+=0`$ and $`\psi_{h_2}=-\psi_{h_1}`$. In both cases (2.11) gives
```math
W(h_1,h_2;\lambda)=1\qquad\text{for every }\lambda .
\tag{11.16}
```
   So $`h_1\approx h_2`$: there is one point and no edge, although $`\partial A\neq\emptyset`$.

## Result

- **Item 1.** If $`\partial A=\emptyset`$, a product state stays a product (11.3). $`V_A`$ is then pure, $`X_V`$ is a single point and there is no edge, for every $`\lambda`$. For any admissible initial state, $`V_A(\lambda)=U_AV_A(0)U_A^\dagger`$ (11.4), so its spectrum is constant.
- **Item 2.** For the product initial state $`\phi\otimes\chi`$, $`\lim_{\lambda\to0^+}\alpha/\lambda=d_0=\lVert u_h-u_{h'}\rVert`$ (11.8). Here $`u_h`$ is fixed by $`C_\partial`$, $`\phi`$ and $`\chi`$ alone (11.6), so it is independent of $`C_A`$, of $`C_{\bar A}`$ and of the decomposition of $`C_\partial`$, and $`u_h\perp\chi`$ (11.9). In the recording-type case, $`u_h=(K_h-\langle K_h\rangle)\chi`$ (11.10), which is (5.10).
- **Item 3.** Under the two genericity assumptions and for small $`\lambda>0`$: every place is a point, every pair is related, and $`N_V(\lambda)`$ is the relative-neighbourhood graph of $`\{u_h\}`$ with respect to $`d_0`$ (11.11).
- **Item 4.** (a) $`d_0`$ is the value of (5.10) for every $`t`$ (11.12). (b) $`d_0(h_1,h_2)=\lvert\phi_{h_2}/\phi_{h_1}-\phi_{h_1}/\phi_{h_2}\rvert\,\sigma_\chi(B)`$ (11.13, 11.14). It depends on the weights and the relative phase of $`a`$, and it vanishes iff $`\phi_{h_1}=\pm\phi_{h_2}`$. In both of these cases, $`W\equiv1`$ exactly (11.16).

## Consistency checks

1. **Scaling (dimensions).** Under $`C\to sC`$ and $`\lambda\to\lambda/s`$, $`\Psi(\lambda)`$ and $`\alpha`$ are unchanged. By (11.6), $`u_h\to su_h`$, so $`d_0\to sd_0`$ and $`\lambda d_0`$ is invariant, as it must be for an angle. In (11.13), the prefactor is dimensionless and $`\sigma_\chi(sB)=\lvert s\rvert\sigma_\chi(B)`$.
2. **$`C_\partial=0`$.** Then (11.6) gives $`u_h=0`$, so $`d_0\equiv0`$. This agrees with item 1 (a), where $`W\equiv1`$ and $`\alpha\equiv0`$ exactly.
3. **Example (b), exact against first order.** Expanding (11.15) gives $`\psi_{h_1}=\phi_{h_1}\chi-i\lambda\,\phi_{h_2}B\chi+O(\lambda^2)`$. This is (11.5) with $`c_1(h_1)=\phi_{h_2}/\phi_{h_1}`$. For $`\phi_{h_1}=\pm\phi_{h_2}`$, the exact branch vectors coincide up to sign, consistent with $`d_0=0`$ from (11.13).

## Open issues

- **Identical-type objects inside $`A`$.** Suppose $`A`$ contains two objects $`a,b`$ of one type $`T`$ with $`d_T\ge2`$.
  - If $`T`$ is sign-changing, every admissible $`\phi`$ vanishes on places with $`h_a=h_b`$. The hypothesis $`\phi_h\neq0`$ of item 2 then cannot hold.
  - If $`T`$ is swap-invariant, $`P_{ab}\Psi(\lambda)=\Psi(\lambda)`$ (A3) gives $`\psi_{P_{ab}h}=\psi_h`$, hence $`W(h,P_{ab}h)\equiv1`$. By (11.8), $`u_{P_{ab}h}=u_h`$, so the distinctness hypothesis of item 3 fails.

  Items 2 and 3, stated on places, are therefore informative only if $`A`$ has no two objects of a common type with $`d_T\ge2`$. A version on classes of places is not derived here.
- Ties in the condition of item 3, higher orders in $`\lambda`$, finite $`\lambda`$ beyond items 1 and 4 (b), and initial states correlated across the cut are out of scope.
- **Comparison with the expected result.** There is no discrepancy. The only addition is that $`W\equiv1`$ also holds for $`\phi_{h_1}=-\phi_{h_2}`$ (11.16).

## Methods used

- tensor-product factorization of $`e^{-iC\lambda}`$; cyclicity of the partial trace
- first-order Taylor expansion of the evolution; projection orthogonal to a reference vector
- small-angle expansion of $`1-\lvert\langle e'\vert e\rangle\rvert^2`$
- operator decomposition $`\sum_nA_n\otimes B_n`$; spectral decomposition of a two-level operator
- sign stability of limits on finite sets; relative-neighbourhood graph
