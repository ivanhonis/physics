# Question: 11-cut-boundary

- **Subproject:** 03-ilang-space
- **Package:** 11-cut-boundary
- **Equation tags:** (11.k)
- **Created:** 2026-10-08

## Goal

Determine how the witness geometry of a part depends on the contracts that cross the cut between the part and its companion. In the language of this subproject:
- a cut is the split $A\mid\bar A$ of the objects into a part and its companion;
- the cut boundary $\partial A$ is the set of contracts that join an object of $A$ to an object of $\bar A$.

The question is when there are points and edges at all, and which contracts fix the geometry at leading order. The notation introduced below ($\partial A$, $C_A$, $C_{\bar A}$, $C_\partial$, $A_n$, $B_n$, $c_n(h)$, $\tilde u_n$, $u_h$) is fixed for later packages. "Edge" means the neighbour relation $\sim$ of 04-neighbours.

**Setting.**
- **Description.** A description satisfying A1–A7, a part $A$ and its nonempty companion $\bar A$. No type has objects on both sides of the cut, so the cut does not separate identical-type instances.
- **Contract system.** By A5, the contract system splits as $C=C_A+C_{\bar A}+C_\partial$:
  - $C_A$ is the sum of the contract terms whose objects both lie in $A$;
  - $C_{\bar A}$ is the sum of those whose objects both lie in $\bar A$;
  - $C_\partial$ is the sum of the contracts in $\partial A$.

  Write $C_\partial=\sum_nA_n\otimes B_n$ as a finite sum, with $A_n$ self-adjoint on $\mathcal H_A$ and $B_n$ self-adjoint on $\mathcal H_{\bar A}$; such a decomposition always exists. On $\mathcal H_{\bar A}$, use $g(v,w)=\operatorname{Re}\langle v\vert w\rangle$ as in 05-recording-contract.

1. **No boundary, no geometry.** Let $\partial A=\emptyset$.
   - (a) Show that a product initial state $\lvert\psi_A\rangle\otimes\lvert\psi_{\bar A}\rangle$ stays a product for every $\lambda$. Hence $V_A$ is pure, all present places form a single point, and there is no edge, for every $\lambda$.
   - (b) For an arbitrary admissible initial state, show that $V_A(\lambda)=U_A(\lambda)V_A(0)U_A(\lambda)^\dagger$ with $U_A(\lambda)=e^{-iC_A\lambda}$. Hence the spectrum of $V_A$ does not depend on $\lambda$.

2. **The boundary fixes the leading-order geometry.**
   - **Initial state.** A product $\lvert\phi\rangle\otimes\lvert\chi\rangle$ of unit vectors, with $\phi_h:=\langle h\vert\phi\rangle\neq0$ for every joint place $h$ of $A$.
   - **Generalized record vectors.** Define $\langle B\rangle:=\langle\chi\vert B\vert\chi\rangle$ and
     $$c_n(h):=\frac{\langle h\vert A_n\vert\phi\rangle}{\phi_h},\qquad \lvert\tilde u_n\rangle:=\bigl(B_n-\langle B_n\rangle\bigr)\lvert\chi\rangle,\qquad \lvert u_h\rangle:=\sum_nc_n(h)\,\lvert\tilde u_n\rangle .$$
   - **To show.** That
     $$\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h'):=\bigl\lVert u_h-u_{h'}\bigr\rVert ,$$
     that this limit depends neither on $C_A$ nor on $C_{\bar A}$, and that every $u_h$ is orthogonal to $\lvert\chi\rangle$.
   - **Recording-type special case.** If every $A_n$ is diagonal in the place basis of $A$, show that $u_h$ reduces to the record vector of (5.10) with $K_h:=\sum_n\langle h\vert A_n\vert h\rangle B_n$.

3. **Edges at small $\lambda$.** In the setting of item 2, assume the following:
   - the $u_h$ are pairwise distinct;
   - for all distinct places $x,y,x'$, $\max\bigl(d_0(x,y),d_0(y,x')\bigr)\neq d_0(x,x')$.

   Show that for all sufficiently small $\lambda>0$:
   - each place is its own point;
   - every two points are related;
   - the neighbour graph $N_V(\lambda)$ equals the relative-neighbourhood graph of the configuration $\{u_h\}$ with respect to $d_0$, in which $x\sim x'$ iff no third $y$ has $\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x')$.

4. **Examples.**
   - (a) **Internal motion does not enter at leading order.** $A=\{a\}$ with places $h_1,\dots,h_n$, and $\bar A=\{c\}$. The contracts are a recording contract $\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$ across the cut and an internal term $C_A=t\sum_{i=1}^{n-1}\bigl(\lvert h_i\rangle\langle h_{i+1}\rvert+\lvert h_{i+1}\rangle\langle h_i\rvert\bigr)$ on $a$, with real $t$. Show that $d_0$ equals the value of (5.10) for every $t$.
   - (b) **A crossing contract that moves weight.** $A=\{a\}$ with two places $h_1,h_2$, and $\bar A=\{c\}$. The only contract is $C_\partial=\bigl(\lvert h_1\rangle\langle h_2\rvert+\lvert h_2\rangle\langle h_1\rvert\bigr)\otimes B$, with $B$ self-adjoint on $\mathcal H_c$ and $\sigma_\chi(B):=\sqrt{\langle B^2\rangle-\langle B\rangle^2}>0$. Derive $d_0(h_1,h_2)$, and show that it depends on the state of $a$. In particular, show that $W(h_1,h_2;\lambda)=1$ exactly, for every $\lambda$, when $\phi_{h_1}=\phi_{h_2}$.

## Inputs

From 02-view-content@v1. Notation fixed there: $p_h:=\langle h\vert V_A\vert h\rangle$, $H_V:=\{h:p_h>0\}$, $\lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle$, $G_{hh'}=\langle E_{h'}\vert E_h\rangle$.

Eq. (2.1):

$$
\lvert\Psi\rangle=\sum_h\lvert h\rangle\otimes\lvert\psi_h\rangle,
\qquad
\lvert\psi_h\rangle=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle=\sum_r\Psi_{hr}\lvert r\rangle,
\qquad
\sum_h\lVert\psi_h\rVert^2=\lVert\Psi\rVert^2=1 .
$$

Eq. (2.2):

$$
V_A=\sum_{h,h'}\langle\psi_{h'}\vert\psi_h\rangle\,\lvert h\rangle\langle h'\rvert,
\qquad\text{i.e.}\qquad
(V_A)_{hh'}=\langle\psi_{h'}\vert\psi_h\rangle,
\qquad
p_h=\lVert\psi_h\rVert^2 .
$$

Eq. (2.11):

$$
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
$$

From 03-witness-distance@v1. Notation fixed there: $h\approx h'$ iff $W(h,h')=1$; $X_V:=H_V/{\approx}$; $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$; for places, $\alpha(h,h'):=\alpha([h],[h'])$.

Eq. (3.1):

$$
\varrho_h:=\lvert E_h\rangle\langle E_h\rvert=\frac{\lvert\psi_h\rangle\langle\psi_h\rvert}{p_h},
\qquad
h\approx h'\;\Longleftrightarrow\;W(h,h')=1\;\Longleftrightarrow\;\varrho_h=\varrho_{h'} .
$$

Eq. (3.5). Here $\alpha$ is a metric on $X_V$.

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 04-neighbours@v1. Also fixed there: the relation $\sim$ depends only on the order of the values of $\alpha$, and is unchanged under $\alpha\mapsto f\circ\alpha$ for every strictly increasing $f$ (Step 3 of 04).

Eq. (4.1):

$$
x\asymp x'\;:\Longleftrightarrow\;W(x,x')>0\;\Longleftrightarrow\;\alpha(x,x')<\pi/2 .
$$

Eq. (4.3):

$$
x\sim x'\;:\Longleftrightarrow\;x\asymp x'\ \text{ and there is no } y\in X_V \text{ with } \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x') .
$$

From 05-recording-contract@v1. These hold in the setting of 05: two objects $a$ and $c$, the recording contract $\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, and the initial state $\lvert\phi\rangle\otimes\lvert\chi\rangle$.

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

Eq. (5.11):

$$
\bigl(H_V/{\sim_0},\,d_0\bigr)\;\cong\;\bigl(\{u_h:h\in H_V\},\,\lVert\cdot\rVert\bigr)\subset(\mathcal H_c,g).
$$

Eq. (5.13):

$$
\langle\chi\vert u_h\rangle=\langle K_h\rangle-\langle K_h\rangle\langle\chi\vert\chi\rangle=0 ,
$$

## Assumptions

- The setting stated under "Goal". All contracts are independent of $\lambda$ (A5).
- Items 2, 3 and 4 (a) are statements for $\lambda\to0^+$. Item 1 and the exact statement of item 4 (b) hold for every $\lambda$.

## Scope

- In scope:
  - the role of the cut boundary $\partial A$ for points, edges and the leading-order geometry;
  - the generalized record vectors;
  - the two examples.
- Out of scope:
  - cuts that separate identical-type instances;
  - initial states correlated across the cut, beyond item 1 (b);
  - orders beyond the leading one, and finite $\lambda$ beyond item 1 and item 4 (b);
  - the deeper structure of $\bar A$, already treated as a light cone in 08-cell-medium;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: short argument.
- Item 2: derive. The standard fact may be used without proof: for unit vectors $e,e'$ close to $\lvert\chi\rangle$, $1-\lvert\langle e'\vert e\rangle\rvert^2$ equals the squared norm of the part of $e-e'$ orthogonal to $\lvert\chi\rangle$, up to terms of third order.
- Item 3: short argument.
- Item 4: derive.

## Expected result

The main model expects the following. Derive each statement independently, and report any discrepancy.

- Item 1: exact statements for every $\lambda$.
- Item 2: the limit formula, with $u_h\perp\chi$; no dependence on $C_A$ or $C_{\bar A}$; and the reduction to (5.10) in the recording-type case.
- Item 3: the relative-neighbourhood statement.
- Item 4:
  - (a) $d_0$ is independent of $t$;
  - (b) $d_0(h_1,h_2)=\bigl\lvert\phi_{h_2}/\phi_{h_1}-\phi_{h_1}/\phi_{h_2}\bigr\rvert\,\sigma_\chi(B)$, which vanishes for $\phi_{h_1}=\pm\phi_{h_2}$, and $W\equiv1$ for $\phi_{h_1}=\phi_{h_2}$.

Give every main result a tag $(11.k)$.

Consistency checks, at most three, chosen from:
- with $C_\partial=0$, item 2 gives $d_0\equiv0$, in agreement with item 1;
- in the recording-type case with $C_A=C_{\bar A}=0$, item 2 reproduces (5.10);
- in item 4 (b) with $\phi_{h_1}=\phi_{h_2}$, the exact evolution gives identical branch vectors.

## Code

None.
