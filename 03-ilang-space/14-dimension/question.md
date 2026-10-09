# Question: 14-dimension

- **Subproject:** 03-ilang-space
- **Package:** 14-dimension
- **Equation tags:** (14.k)
- **Created:** 2026-10-08

## Goal

Determine what fixes the leading-order dimension $\dim_0$ (5.14) of the witness geometry when the medium consists of several recording channels. In particular, determine under which conditions $\dim_0=3$, and which of these conditions come with nonvanishing loop data. The notation introduced below ($c_1,\dots,c_m$, $K^{(c)}_h$, $u^{(c)}_h$, $\dim^{(c)}_0$) is fixed for later packages. "Dimension" means $\dim_0$ of 05-recording-contract; no further spatial meaning is attached to it (M1, M4).

**Setting.**
- **Objects.** A recorded object $a$ with places $h\in H$, $\lvert H\rvert=n$. The medium consists of cells $c_1,\dots,c_m$. All objects have pairwise different types, and each is the only instance of its type, so (1.11) imposes no constraint.
- **Initial state.** A product $\lvert\phi\rangle\otimes\lvert\chi_1\rangle\otimes\cdots\otimes\lvert\chi_m\rangle$, with $\phi_h\neq0$ for every $h$. Write $\lvert\chi\rangle:=\bigotimes_c\lvert\chi_c\rangle$, and $d_c:=\dim\mathcal H_{c}$ for cell $c$.
- **Contracts.** One recording contract per channel:
  $$C=\sum_{c=1}^m\sum_{h}\lvert h\rangle\langle h\rvert\otimes K^{(c)}_h ,$$
  with $K^{(c)}_h$ self-adjoint on cell $c$ and the identity on the other cells.
- **Notation.** $u^{(c)}_h:=\bigl(K^{(c)}_h-\langle\chi_c\vert K^{(c)}_h\vert\chi_c\rangle\bigr)\lvert\chi_c\rangle$ is the record vector of channel $c$ alone, and $\dim^{(c)}_0$ is the dimension of the real affine span of $\{u^{(c)}_h\}$.

1. **Several channels.**
   - (a) Determine the record vectors $u_h$ of the whole medium, the leading-order distance $d_0$ and $\dim_0$, in terms of the per-channel record vectors.
   - (b) Determine a necessary and sufficient condition under which $\dim_0=\sum_c\dim^{(c)}_0$.
   - (c) Determine the general relation between $\dim_0$ and the $\dim^{(c)}_0$.

2. **Commuting records in one channel.** Suppose the operators $K^{(c)}_h$, $h\in H$, of one channel commute pairwise. Determine:
   - the structure of the Gram matrix of the $u^{(c)}_h$, in particular whether it is real;
   - the largest possible value of $\dim^{(c)}_0$, in terms of the common spectral decomposition and the state $\lvert\chi_c\rangle$;
   - the $\lambda^2$ term of the loop phases contributed by this channel.

3. **Ways to obtain $\dim_0=3$.** Let $n\ge4$. Take three channel classes, using the quoted results of 07 for the generic classes and item 2 for the commuting class:
   - complex generic ($\mathrm{GUE}$-type records);
   - real ($\mathrm{GOE}$-type records, $\chi_c$ real);
   - commuting.

   Determine which combinations of channels and cell dimensions give $\dim_0=3$ generically within the chosen classes. For each combination, determine whether the $\lambda^2$ term of the loop phases can be nonzero. Among them, determine the smallest total medium dimension $\prod_cd_c$, both with and without nonzero loop data.

4. **Examples.**
   - (a) **Cubic lattice.** The places are $h=(x,y,z)\in\{1,\dots,N\}^3$, $N\ge2$. Three qubit cells, each in $\lvert0\rangle$ ($\sigma_z\lvert0\rangle=\lvert0\rangle$), with $K^{(1)}_h=x\,\sigma_x^{(1)}$, $K^{(2)}_h=y\,\sigma_x^{(2)}$, $K^{(3)}_h=z\,\sigma_x^{(3)}$. Determine $d_0$, $\dim_0$ and the $\lambda^2$ term of the loop phase of every lattice triangle.
   - (b) **Plane plus line.** The same places. Two qubit cells in $\lvert0\rangle$, with $K^{(1)}_h=x\,\sigma_x^{(1)}+y\,\sigma_y^{(1)}$ and $K^{(2)}_h=z\,\sigma_x^{(2)}$. Determine $d_0$, $\dim_0$ and the $\lambda^2$ term of the loop phase of every lattice triangle.

## Inputs

From 05-recording-contract@v1. These hold in the setting of 05: one recorded object, one medium object, a recording contract $\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$, and the start $\lvert\phi\rangle\otimes\lvert\chi\rangle$.
- $g(v,w):=\operatorname{Re}\langle v\vert w\rangle$ makes $\mathcal H_c$ a real Euclidean space of dimension $2d_c$.
- $h\sim_0h'$ means $u_h=u_{h'}$.
- $\dim_0:=\dim_{\mathbb R}\operatorname{aff}_{\mathbb R}\{u_h\}$.

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

Eq. (5.14):

$$
\dim_0\le\min\bigl(d_{T(a)}-1,\;2d_c-2\bigr).
$$

From 07-random-records@v1. Here the $K_h$ are i.i.d. $\mathrm{GUE}(s)$ or $\mathrm{GOE}(s)$ in a basis $e_1=\lvert\chi\rangle,e_2,\dots,e_{d_c}$, and $n$ is the number of places.

Eq. (7.7), GUE:

$$
\dim_0=\min\bigl(n-1,\;2(d_c-1)\bigr)\qquad\text{almost surely},
$$

Eq. (7.11), GOE:

$$
\dim_0=\min\bigl(n-1,\;d_c-1\bigr)\qquad\text{almost surely}.
$$

From 10-loop-data@v1. These hold in the setting of 05. Notation fixed there: $\omega(v,w):=\operatorname{Im}\langle v\vert w\rangle$, $Jv:=\mathrm i\,v$, and the loop phase $\Phi:=\arg W$.

Eq. (10.8):

$$
\Phi(h_1,\dots,h_k;\lambda)=-\lambda^2\sum_{j=1}^k\omega\bigl(u_{h_j},u_{h_{j+1}}\bigr)+O(\lambda^3),\qquad k\ge3 .
$$

Eq. (10.12):

$$
\omega(v,w)=g(Jv,w),\qquad g(Jv,Jw)=g(v,w),\qquad J^2=-\mathbb 1 .
$$

## Assumptions

- The setting stated under "Goal". All contracts are independent of $\lambda$ (A5).
- Every statement is about the leading order at $\lambda\to0^+$. The setting of 05 is extended to a medium of several cells in a product state. State whether the quoted results (5.10)–(5.14) and (10.8) carry over to this setting, and why.
- "Generically within a class" means for almost every draw of the records of that class, with the class fixed per channel.

## Scope

- In scope:
  - $\dim_0$ for several channels, and the commuting class;
  - the classification of the ways to obtain $\dim_0=3$, with the loop data;
  - the two examples.
- Out of scope:
  - the large-scale dimension of the neighbour graph and continuum limits;
  - finite $\lambda$ and curvature;
  - channels that are entangled with each other initially, and contracts between cells;
  - any principle that would select a particular dimension;
  - any physical or spatial meaning beyond the definitions (M1, M4).

## Depth

- Item 1: derive.
- Item 2: derive.
- Item 3: short argument.
- Item 4: derive.

## Expected result

- Item 1: closed forms for $u_h$ and $d_0$, an if-and-only-if condition, and an inequality.
- Item 2: a statement about the Gram matrix, a bound with its attainment condition, and the loop term.
- Item 3: a table of the combinations, with loop data and minimal total dimension.
- Item 4: closed forms.

Give every main result a tag $(14.k)$.

Consistency checks, at most three: for example a single channel (reproducing the quoted one-channel results), and the reversal of a loop.

## Code

None.
