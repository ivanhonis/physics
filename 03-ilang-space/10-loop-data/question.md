# Question: 10-loop-data

- **Subproject:** 03-ilang-space
- **Package:** 10-loop-data
- **Equation tags:** (10.k)
- **Created:** 2026-10-08

## Goal

Determine the loop data of the witness geometry in a recording medium, and how they relate to the metric. The loop data are the phases of the cyclic products $W(h_1,\dots,h_k)$, $k\ge3$. They are well-defined data of the view by 02, and they are not fixed by the pairwise data. The notation introduced below ($\omega$, $J$, $\Phi$) is fixed for later packages.

**Setting.** The setting of 05-recording-contract:
- **Objects.** Two objects $a$ and $c$, of different types, each the only instance of its type; the part is $A=\{a\}$.
- **Contract.** The recording contract $C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$.
- **Initial state.** $\lvert\phi\rangle\otimes\lvert\chi\rangle$, with $\phi_h\neq0$ for every $h$.

On $\mathcal H_c$, use the real Euclidean structure $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$ of 05. Define the antisymmetric form $\omega(v,w):=\operatorname{Im}\langle v\vert w\rangle$ and the real-linear map $J v:=\mathrm i\,v$ (multiplication by the imaginary unit). For a closed sequence of places $h_1,\dots,h_k$ with $W(h_1,\dots,h_k)\neq0$, the loop phase is $\Phi(h_1,\dots,h_k;\lambda):=\arg W(h_1,\dots,h_k;\lambda)$.

1. **Loop data at small $\lambda$.**
   - (a) Show that the modulus of a cyclic product is fixed by the pairwise data, $\lvert W(h_1,\dots,h_k)\rvert^2=\prod_jW(h_j,h_{j+1})$ (indices mod $k$), exactly, for every $\lambda$. Only the phase is new.
   - (b) Derive the expansion of the overlaps' phases to second order in $\lambda$.
   - (c) Show that for every $k\ge3$
     $$\Phi(h_1,\dots,h_k;\lambda)=-\lambda^2\sum_{j=1}^{k}\omega\bigl(u_{h_j},u_{h_{j+1}}\bigr)+O(\lambda^3),$$
     and in particular, for a triangle,
     $$\Phi(h_1,h_2,h_3;\lambda)=-\lambda^2\,\omega\bigl(u_{h_2}-u_{h_1},\,u_{h_3}-u_{h_1}\bigr)+O(\lambda^3).$$
   - (d) Show that reversing the order of the loop reverses the sign of $\Phi$.

2. **Relation to the metric.** Show four things:
   - $\omega(v,w)=g(Jv,w)$;
   - $J$ is $g$-orthogonal with $J^2=-\mathbb 1$;
   - consequently $\lvert\Phi(h_1,h_2,h_3;\lambda)\rvert\le\lambda^2\,d_0(h_1,h_2)\,d_0(h_1,h_3)+O(\lambda^3)$;
   - the condition under which the leading term saturates this bound.

   State in what sense the loop data at leading order are fixed by the leading-order metric $d_0$ together with $J$, and in what sense they are not fixed by $d_0$ alone.

3. **When the loop data vanish.** Show that the $\lambda^2$ term of every loop phase vanishes in three cases:
   - (a) the record operators commute pairwise;
   - (b) the records are real: in some basis of $\mathcal H_c$ in which $\lvert\chi\rangle$ is real, every $K_h$ is real symmetric. In this case show also that $W(h_1,\dots,h_k;-\lambda)=W(h_1,\dots,h_k;\lambda)^*$, so the loop phase is an odd function of $\lambda$;
   - (c) the record vectors $u_{h_j}$ of the loop lie in one real line.

4. **Examples.**
   - (a) **Plane.** The qubit medium of 05-recording-contract, Step 8: $\lvert\chi\rangle=\lvert0\rangle$, $X=\sigma_x$, $Y=\sigma_y$, $K_{h_{(i,j)}}=iX+jY$. Show that $\Phi=-2\lambda^2A+O(\lambda^3)$ for every lattice triangle, where $A$ is the signed area of the triangle in the lattice coordinates $(i,j)$, with the orientation given by the order of the loop.
   - (b) **Line.** $K_{h_i}=iX$. Show that the $\lambda^2$ term of every loop phase vanishes.

## Inputs

From 02-view-content@v1. Notation fixed there: $G_{hh'}=\langle E_{h'}\vert E_h\rangle$, $W(h_1,\dots,h_k):=G_{h_1h_2}G_{h_2h_3}\cdots G_{h_{k-1}h_k}G_{h_kh_1}$, and the cyclic products are rephasing invariant (2.9).

Eq. (2.10):

$$
W(h_1,\dots,h_k)=\frac{(V_A)_{h_1h_2}(V_A)_{h_2h_3}\cdots(V_A)_{h_kh_1}}{p_{h_1}p_{h_2}\cdots p_{h_k}}
=\frac{\langle\psi_{h_2}\vert\psi_{h_1}\rangle\langle\psi_{h_3}\vert\psi_{h_2}\rangle\cdots\langle\psi_{h_1}\vert\psi_{h_k}\rangle}{p_{h_1}p_{h_2}\cdots p_{h_k}} .
$$

Eq. (2.11):

$$
W(h)=1,\qquad W(h,h')=\lvert G_{hh'}\rvert^2=\frac{\lvert(V_A)_{hh'}\rvert^2}{p_hp_{h'}} .
$$

From 05-recording-contract@v1. These hold in the setting above. $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$ makes $\mathcal H_c$ a real Euclidean space of dimension $2d_c$.

Eq. (5.5):

$$
G_{hh'}(\lambda)=\langle E_{h'}\vert E_h\rangle=\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle,
\qquad
\bigl(V_A(\lambda)\bigr)_{hh'}=\phi_h\phi_{h'}^{*}\,G_{hh'}(\lambda).
$$

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

From 06-body-in-medium@v1. This is the third-order expansion of the overlap in the setting of 06, with
$$G=1+g_1\lambda+g_2\lambda^2+g_3\lambda^3+O(\lambda^4),\qquad M:=K_h+B_{\beta_0},\quad M':=K_{h'}+B_{\beta_0},\quad D=M-M'=K_h-K_{h'}.$$
For $B_{\beta_0}=0$ it is the expansion of $G_{hh'}$ of (5.5); $\mathrm i$ is the imaginary unit.

Eq. (6.8):

$$
g_1=-\mathrm i\langle D\rangle,\qquad g_2=-\tfrac12\bigl(\langle D^2\rangle+\langle[M,M']\rangle\bigr),\qquad g_3=\tfrac{\mathrm i}6\bigl\langle M^3-3M'M^2+3M'^2M-M'^3\bigr\rangle .
$$

## Assumptions

- The setting stated under "Goal". The contracts do not depend on $\lambda$ (A5).
- Item 1 (a) holds for every $\lambda$. Items 1 (b)–(d), 2 and 4 are expansions for $\lambda\to0^+$, and item 3 (b) is used for both signs of $\lambda$ as a formal parameter of (1.9).

## Scope

- In scope:
  - loop phases of cyclic products in the recording medium at small $\lambda$;
  - their relation to $d_0$, $\omega$ and $J$;
  - the cases in which they vanish;
  - the two examples.
- Out of scope:
  - orders $\lambda^3$ and beyond, except the oddness statement of item 3 (b);
  - curvature of the space of branch states, bodies and cells, and finite $\lambda$;
  - any reading of $\Phi$ as a physical field, flux or curvature (M1, M4).

## Depth

- Item 1: derive.
- Item 2: short argument.
- Item 3: short argument.
- Item 4: derive.

## Expected result

The main model expects the formulas stated in items 1, 2 and 4. Derive each one independently, and report any discrepancy in sign or factor.

- Item 1:
  - the exact modulus identity;
  - the expansion of the phase of a single overlap, $\arg G_{hh'}=-\lambda\bigl(\langle K_h\rangle-\langle K_{h'}\rangle\bigr)+\lambda^2\omega(u_{h'},u_h)+O(\lambda^3)$;
  - the loop formula;
  - the sign reversal.
- Item 2: the identities, the bound and its saturation condition. The saturation condition is expected to be $u_{h_3}-u_{h_1}\in\mathbb R\,J(u_{h_2}-u_{h_1})$ at leading order.
- Item 3: the three vanishing statements and the oddness for real records.
- Item 4: $\Phi=-2\lambda^2A+O(\lambda^3)$ in (a), and a vanishing $\lambda^2$ term in (b).

Give every main result a tag $(10.k)$.

Consistency checks, at most three, chosen from:
- at $\lambda=0$ every cyclic product equals $1$;
- reversing a loop gives the complex conjugate cyclic product, consistent with $W(h_1,h_3,h_2)=W(h_1,h_2,h_3)^*$;
- for the plane example, the unit lattice triangle $(0,0)\to(1,0)\to(0,1)$ gives $\Phi=-\lambda^2+O(\lambda^3)$.

## Code

None.
