# Question: 02-view-content

- **Subproject:** 03-ilang-space
- **Package:** 02-view-content
- **Equation tags:** (2.k)
- **Created:** 2026-10-07

## Goal

Determine exactly what the view $`V_A`$ (1.5) of a part $`A`$ retains of an admissible joint state $`\lvert\Psi\rangle`$, and which of the retained quantities are well defined in the sense of M6. The notation introduced below ($`p_h`$, $`H_V`$, $`\lvert\psi_h\rangle`$, $`G`$, $`W`$) is fixed for later packages.

1. **Basic properties.** Show that $`V_A`$ is a density operator on $`\mathcal H_A`$: self-adjoint, positive semidefinite, unit trace. Define the weights and the set of present places,
   ```math
   p_h:=\langle h\vert V_A\vert h\rangle,\qquad H_V:=\{h : p_h>0\},
   ```
   where $`h`$ runs over the joint places of $`A`$. Show that $`\langle h\vert V_A\vert h'\rangle=0`$ unless $`h,h'\in H_V`$. Show that for every local reading on $`A`$ (A4), whose classes come from a partition $`\{S^A_r\}`$ of the joint places of $`A`$, the outcome probability (1.3) equals $`\mathrm{Tr}\bigl(\Pi^A_r V_A\bigr)`$, with $`\Pi^A_r`$ the projector onto the span of $`S^A_r`$ in $`\mathcal H_A`$. This is the language's statement that the view gives the statistics of every local reading.

2. **The view as a Gram matrix.** For every joint place $`h`$ of $`A`$, define the branch vector
   ```math
   \lvert\psi_h\rangle:=\bigl(\langle h\rvert\otimes\mathbb 1_{\bar A}\bigr)\lvert\Psi\rangle\in\mathcal H_{\bar A}.
   ```
   Show that $`\langle h\vert V_A\vert h'\rangle=\langle\psi_{h'}\vert\psi_h\rangle`$ and $`\lVert\psi_h\rVert^2=p_h`$. Relate this to (1.6)–(1.7): $`\lvert\psi_h\rangle=a_h\lvert E_h\rangle`$.

3. **What the view does not see.** Show that two admissible states $`\lvert\Psi\rangle`$ and $`\lvert\Phi\rangle`$ have the same view of $`A`$, $`V_A(\Psi)=V_A(\Phi)`$, if and only if there is a unitary $`U`$ on $`\mathcal H_{\bar A}`$ with $`\lvert\varphi_h\rangle=U\lvert\psi_h\rangle`$ for every joint place $`h`$ of $`A`$, that is, $`\lvert\Phi\rangle=(\mathbb 1_A\otimes U)\lvert\Psi\rangle`$.

4. **Well-defined companion data.** The phase split between $`a_h`$ and $`\lvert E_h\rangle`$ in (1.6) is a convention. For $`h\in H_V`$ it is fixed only up to $`a_h\to e^{-i\theta_h}a_h`$, $`\lvert E_h\rangle\to e^{i\theta_h}\lvert E_h\rangle`$ with arbitrary real $`\theta_h`$. Define the branch Gram matrix on $`H_V`$, the overlap of (1.7):
   ```math
   G_{hh'}:=\langle E_{h'}\vert E_h\rangle,\qquad h,h'\in H_V .
   ```
   Under a change of convention it transforms by a rephasing, $`G_{hh'}\to e^{i(\theta_h-\theta_{h'})}G_{hh'}`$. By M6, a quantity built from $`G`$ is well defined only if it is invariant under every rephasing.
   - (a) Show that the cyclic products
     $`W(h_1,\dots,h_k):=G_{h_1h_2}G_{h_2h_3}\cdots G_{h_{k-1}h_k}G_{h_kh_1},\qquad k\ge1,\ h_i\in H_V,`$
     are invariant under every rephasing, and express them through matrix elements of $`V_A`$ alone.
   - (b) Completeness: show that two Gram matrices $`G`$ and $`G'`$ on the same $`H_V`$ are related by a rephasing if and only if all their cyclic products agree. Conclude that every well-defined quantity built from $`G`$ is a function of the cyclic products.

5. **Label-freedom.** Let $`\pi`$ be a permutation of the objects that maps every object to an object of the same type. Show that for every admissible state, $`V_{\pi(A)}(\Psi)`$ equals $`V_A(\Psi)`$ under the natural identification of $`\mathcal H_{\pi(A)}`$ with $`\mathcal H_A`$, which identifies the factor of object $`a\in A`$ with that of $`\pi(a)`$. Conclude that $`p_h`$ and the cyclic products do not change when the part is replaced by a part that differs only in which identical-type instances it contains.

## Inputs

None. The package builds only on the base problem.

## Assumptions

None beyond the base problem. The part $`A`$ and its companion $`\bar A`$ are both nonempty. $`\lambda`$ is fixed.

## Scope

- In scope: one part $`A`$ and one admissible state at fixed $`\lambda`$, with arbitrary types, families and contracts.
- Out of scope:
  - any distance, geometric or spatial reading of $`p_h`$, $`G`$ or $`W`$ (M1, M4), and the question of which entities are points;
  - evolution and dependence on $`\lambda`$;
  - which Gram matrices can occur under the family constraint (1.11), beyond item 5;
  - relations between views of parts that are not related by a permutation of identical-type instances.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: short argument. The standard fact that two families of vectors with the same Gram matrix are related by an isometry between their spans may be used without proof.
- Item 4 (a): derive.
- Item 4 (b): derive.
- Item 5: short argument.

## Expected result

- Item 1: the listed properties, and $`p(r)=\mathrm{Tr}\bigl(\Pi^A_r V_A\bigr)`$.
- Item 2: the identity $`\langle h\vert V_A\vert h'\rangle=\langle\psi_{h'}\vert\psi_h\rangle`$.
- Item 3: an if-and-only-if statement.
- Item 4: $`W`$ as a ratio of products of matrix elements of $`V_A`$, and the completeness statement as an if-and-only-if.
- Item 5: the equality of the two views and its consequence.

Give every main result a tag $`(2.k)`$.

Consistency checks, at most three, chosen from:
- the two-branch witness rule of Section 3 of the base problem is recovered as a special case of item 2;
- for a product state $`\lvert\Psi\rangle=\lvert\psi_A\rangle\otimes\lvert e\rangle`$ every cyclic product equals $`1`$: the companion witnesses nothing;
- for mutually orthogonal branch states $`G`$ is the identity on $`H_V`$, so every cyclic product that contains two different places vanishes.

## Code

None.
