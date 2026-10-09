# Question: 24-background-stability

- **Subproject:** 03-ilang-space
- **Package:** 24-background-stability
- **Equation tags:** (24.k)
- **Created:** 2026-10-09

## Goal

Determine three things for the spaces derived at different values of $\lambda$:
- when they can be identified point by point;
- on which ranges of $\lambda$ the background is stable: its points, its neighbour graph and its distances;
- whether a body then has a trajectory.

This addresses criterion 7. The notions defined below (background at $\lambda$, identification, background interval, stability scale, trajectory, relative deviation) are fixed for later packages. They mean only what their definitions say (M1, M2, M4). $\lambda$ is the ordering parameter of the evolution, not a time (criterion 8).

**Setting.**
- **Recording setting of 05.** A probe $b$ of type $T$ with finitely many places $h$, the only instance of $T$; a medium $c$; the recording contract $C=\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$; and the start $\lvert\phi\rangle\otimes\lvert\chi\rangle$ with $\phi_h\neq0$ for all $h$.
- **Body of 17** (item 2). The same records, with a hopping term added: $C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h$ and $C_b=\sum_{h,h'}t_{hh'}\lvert h\rangle\langle h'\rvert$. The start is $\lvert\phi\rangle\otimes\lvert\chi\rangle$, and $p_h(\lambda)$ are the place weights of its view.

**Definitions.**
- **Background at $\lambda$.** The witness geometry of the recording setting at $\lambda$:
  - the partition $\mathcal P(\lambda)$ of the places into points, with $h\approx_\lambda h'$ iff $W(h,h';\lambda)=1$ (3.1)–(3.2) and $W$ given by (5.6);
  - the witness angle $\alpha(\cdot,\cdot;\lambda)$ on the points (3.5);
  - the neighbour graph $N_V(\lambda)$ (4.3).

  By (5.6) it depends only on the $K_h$ and $\chi$, not on $\phi$. It is the background that a static probe with these records sees, and the body of item 2 moves in it.
- **Identification.** If $\mathcal P(\lambda)=\mathcal P(\lambda')$, a point at $\lambda$ is identified with the point at $\lambda'$ that consists of the same places. The places are part of the type (A2), so this identification uses no convention.
- **Background interval.** An open interval $I\subseteq(0,\infty)$ on which $\mathcal P(\lambda)$ and $N_V(\lambda)$ are both constant.
- **Stability scale.** $\lambda_*:=\sup\{\Lambda>0:\ (0,\Lambda)\text{ is a background interval}\}$, or $0$ if no such $\Lambda$ exists.
- **Trajectory.** For the body of item 2, its point weights $P_x(\lambda):=\sum_{h\in x}p_h(\lambda)$ on the points $x$ of the background at $\lambda$. On a background interval, this is a curve of probability distributions over one fixed set of points.
- **Relative deviation.** $\delta(\lambda):=\max_{h\not\approx_0h'}\lvert\alpha(h,h';\lambda)/\lambda-d_0(h,h')\rvert/d_0(h,h')$, over the pairs with $d_0(h,h')>0$, with $d_0$ from (5.10).

1. **General structure** (recording setting).
   - (a) For two places $h\neq h'$, determine the set $Z(h,h'):=\{\lambda>0:\ W(h,h';\lambda)=1\}$. Determine whether it is always either all of $(0,\infty)$ or a discrete set. Characterize the first case, using (15.2).
   - (b) Determine how $\mathcal P(\lambda)$ depends on $\lambda$:
     - whether there is a partition $\mathcal P_{\rm gen}$ such that $\mathcal P(\lambda)=\mathcal P_{\rm gen}$ except on a discrete set $\Lambda_{\mathcal P}$;
     - what $\mathcal P(\lambda)$ can look like at $\lambda\in\Lambda_{\mathcal P}$, in particular whether points can only merge there or can also split.
   - (c) Determine whether $N_V(\lambda)$ changes only on a discrete set $\Lambda_N$, and under which condition on the records.
   - (d) Determine whether $\lambda_*>0$ always holds. Determine how $\lambda_*$ is related to $\Lambda_{\mathcal P}$, $\Lambda_N$ and the small-$\lambda$ graph of (11.11).

2. **Trajectories** (body of 17).
   - Determine whether the trajectory of the body is defined for every $\lambda\notin\Lambda_{\mathcal P}$.
   - Determine whether trajectories on background intervals that are separated by points of $\Lambda_{\mathcal P}$ join through the identification by places.
   - Determine what changes for the trajectory at the points of $\Lambda_N$.

3. **Examples.** For each, determine $\Lambda_{\mathcal P}$, $\Lambda_N$ (on the stated range), $\lambda_*$, and $\delta(\lambda)$ on $(0,\lambda_*)$.
   - (a) **Line, qubit medium.**
     - The family: places $h_1,\dots,h_n$ with $n\ge3$, $K_{h_i}=i\,\sigma_x$, $\mathcal H_c=\mathbb C^2$, $\chi=\lvert0\rangle$.
     - By (5.15)–(5.16), $\sigma_X=1$ and $F(s)=\cos^2s$.
     - Determine everything on $(0,\pi]$, and $\lambda_*$ as a function of $n$.
   - (b) **Line, general $X$.**
     - The family: $K_{h_i}=i\,X$ with $\sigma_X>0$ and $n\ge3$.
     - Determine $\Lambda_{\mathcal P}$ in terms of the spectral decomposition of $X$ in the state $\chi$, i.e. when $F(s)=1$ for some $s>0$.
     - Determine how $\lambda_*$ behaves as $n$ grows, with upper and lower bounds in terms of $F$.
   - (c) **Window medium** (15, 22).
     - The family: $K_{h_i}=\sum_{l\in w_i}\sigma_x^{[l]}$ with $m\ge2$ and $n\ge2m$.
     - Determine $\mathcal P(\lambda)$ and $N_V(\lambda)$ for every $\lambda>0$. (22.14)–(22.15) cover $(0,\pi/2)$.
     - Determine $\Lambda_{\mathcal P}$, $\Lambda_N$ and $\lambda_*$, and how $\lambda_*$ depends on $n$.

## Inputs

From 03-witness-distance@v1. $\varrho_h:=\lvert E_h\rangle\langle E_h\rvert$ is the companion projector of a present place. Eq. (3.1):

$$
\varrho_h:=\lvert E_h\rangle\langle E_h\rvert=\frac{\lvert\psi_h\rangle\langle\psi_h\rvert}{p_h},
\qquad
h\approx h'\;\Longleftrightarrow\;W(h,h')=1\;\Longleftrightarrow\;\varrho_h=\varrho_{h'} .
$$

Eq. (3.2):

$$
X_V:=H_V/{\approx},\qquad
\varrho_x:=\varrho_h,\qquad
W(x,x'):=W(h,h')=\operatorname{Tr}(\varrho_x\varrho_{x'})\qquad(h\in x,\ h'\in x'),
$$

Eq. (3.5), with $\alpha(x,x'):=\arccos\sqrt{W(x,x')}\in[0,\pi/2]$ a metric on $X_V$:

$$
\cos\alpha(x,x')=\sqrt{W(x,x')}=\frac{\lvert(V_A)_{hh'}\rvert}{\sqrt{p_h\,p_{h'}}}
=\frac{\lvert\langle h\vert V_A\vert h'\rangle\rvert}{\sqrt{\langle h\vert V_A\vert h\rangle\langle h'\vert V_A\vert h'\rangle}},\qquad h\in x,\ h'\in x' .
$$

From 04-neighbours@v1. Eq. (4.1):

$$
x\asymp x'\;:\Longleftrightarrow\;W(x,x')>0\;\Longleftrightarrow\;\alpha(x,x')<\pi/2 .
$$

Eq. (4.3):

$$
x\sim x'\;:\Longleftrightarrow\;x\asymp x'\ \text{ and there is no } y\in X_V \text{ with } \max\bigl(\alpha(x,y),\alpha(y,x')\bigr)<\alpha(x,x') .
$$

From 05-recording-contract@v1, in the setting of 05. Eq. (5.6):

$$
W(h,h';\lambda)=\bigl\lvert\langle\chi\vert e^{iK_{h'}\lambda}e^{-iK_h\lambda}\vert\chi\rangle\bigr\rvert^2 .
$$

Eq. (5.10):

$$
\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=d_0(h,h')=\bigl\lVert u_h-u_{h'}\bigr\rVert,
\qquad \lvert u_h\rangle=\bigl(K_h-\langle K_h\rangle\bigr)\lvert\chi\rangle .
$$

Eq. (5.15), for $K_{h_i}=iX$ with $\sigma_X^2=\operatorname{Var}_\chi X$:

$$
d_0(h_i,h_j)=\lvert i-j\rvert\,\sigma_X .
$$

Eq. (5.16):

$$
W(h_i,h_j;\lambda)=F\bigl((i-j)\lambda\bigr),\qquad F(s):=\bigl\lvert\langle\chi\vert e^{-\mathrm isX}\vert\chi\rangle\bigr\rvert^2 .
$$

From 11-cut-boundary@v1. In the recording setting, (11.11) holds for all sufficiently small $\lambda>0$ under two assumptions: the $u_h$ are pairwise distinct; and for all distinct places $x,y,x'$, $\max\bigl(d_0(x,y),d_0(y,x')\bigr)\neq d_0(x,x')$. Then every place is its own point, every two points are related, and

$$
x\sim x'\;\Longleftrightarrow\;\text{no }y\text{ with }\max\bigl(d_0(x,y),d_0(y,x')\bigr)<d_0(x,x') .
$$

From 15-bodies@v3, Step 1, verbatim: "Let $Y_1,Y_2$ be self-adjoint on $\mathcal H_c$, with $f_j(\lambda):=e^{-iY_j\lambda}\lvert\chi\rangle$, $a_j:=\tilde Y_j\lvert\chi\rangle$, and $\langle\chi\vert a_j\rangle=0$." "**(ii) Exact.** The two orbits are the same state for every $\lambda$ iff" Eq. (15.2), where $d_c=\dim\mathcal H_c$:

$$
(Y_1-Y_2)\,Y_1^n\lvert\chi\rangle=\mu_0\,Y_1^n\lvert\chi\rangle\quad(n=0,\dots,d_c-1),\qquad\mu_0:=\langle Y_1\rangle-\langle Y_2\rangle ,
$$

From 15, window medium: places $h_i$, the medium is one object whose places are bit strings of length $L$, $\chi=\lvert0\cdots0\rangle$, windows $w_i:=\{i,\dots,i+m-1\}$, and $K_{h_i}=\sum_{l\in w_i}\sigma_x^{[l]}$. Eq. (15.17), where $D$ is the two-body distance of 15:

$$
\lvert u_{h_i}\rangle=\sum_{l\in w_i}\lvert e_l\rangle,\qquad
d_0(h_i,h_j)=\sqrt{\lvert w_i\triangle w_j\rvert}=\sqrt{2\min(\lvert i-j\rvert,m)},\qquad
D=\sqrt{2\min(\lvert i_1-i_2\rvert,m)} .
$$

From 17-motion@v2, in the setting of 17. Eq. (17.1):

$$
i\,\frac{\mathrm d}{\mathrm d\lambda}\lvert\psi_h\rangle=\sum_{h'}t_{hh'}\lvert\psi_{h'}\rangle+K_h\lvert\psi_h\rangle,\qquad \lvert\psi_h(0)\rangle=\phi_h\lvert\chi\rangle .
$$

Eq. (17.2):

$$
d_0(h,h')=\lim_{\lambda\to0^+}\frac{\alpha(h,h';\lambda)}{\lambda}=\bigl\lVert u_h-u_{h'}\bigr\rVert,\qquad u_h=(K_h-\epsilon_h)\chi,\quad\text{independent of the }t_{hh'} .
$$

From 22-large-scale-geometry@v3, for the window medium and every $\lambda\in(0,\pi/2)$. Eq. (22.14):

$$
\alpha(h_i,h_j)=\alpha_k:=\arccos\bigl((\cos\lambda)^{2k}\bigr),\qquad k=\min(\lvert i-j\rvert,m),\qquad 0<\alpha_1<\dots<\alpha_m<\tfrac\pi2 .
$$

Eq. (22.15):

$$
h_i\sim h_j\iff\lvert i-j\rvert=1\ \ \text{or}\ \ \lvert i-j\rvert\ge2m-1 .
$$

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $\lambda$ (A5). Every description has finitely many places and a finite-dimensional medium (A1).
- "Discrete" means closed and locally finite in $(0,\infty)$.

## Scope

- In scope:
  - the background of the recording setting at every $\lambda>0$;
  - its identification across $\lambda$;
  - stability intervals;
  - trajectories of the body of 17 on this background;
  - the three examples.
- Out of scope:
  - media with internal contracts;
  - several bodies;
  - the body's own view at finite $\lambda$, which is not used to define the background;
  - a physical time (criterion 8);
  - any physical or spatial meaning beyond the definitions (M1, M2, M4).

## Depth

- Item 1(a), 1(b): derive.
- Item 1(c), 1(d): short argument.
- Item 2: short argument.
- Item 3(a), 3(c): derive.
- Item 3(b): derive. Standard facts on almost periodic functions may be used; state them.

## Expected result

- Item 1: a dichotomy with a characterization; a structure statement on $\mathcal P(\lambda)$; yes/no answers with conditions; a statement on $\lambda_*$.
- Item 2: yes/no answers with conditions.
- Item 3:
  - (a): explicit sets, a closed form for $\lambda_*(n)$, and a closed form or bound for $\delta$;
  - (b): a spectral condition, and bounds on $\lambda_*$ as $n$ grows;
  - (c): explicit $\mathcal P$, $N_V$ and sets for all $\lambda$, and $\lambda_*$ with its $n$-dependence.

Give every main result a tag $(24.k)$.

Consistency checks, at most three: for example $\lambda\to0$ against (5.10) and (11.11), and the periodicity in $\lambda$ of examples (a) and (c).

## Code

None.
