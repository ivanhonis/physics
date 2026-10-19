# Question: 02-field-object

- **Subproject:** 05-ilang-free-fall
- **Package:** 02-field-object
- **Equation tags:** (2.k)
- **Created:** 2026-10-10

## Goal

Determine what it means in the language that a field acts on a body. For a general pair term between a body and a field object: determine the states of the field in which the body sees definite numbers in the place of the field's operators, what the body and the other objects see in such a state, and what they see when the field is static but not in such a state. This is criterion 1, and the static part of criterion 8.

**Setting.**
- **Objects.** A body $`b`$, a field $`f`$, and a set $`r`$ of further objects (for example a recording medium), possibly empty. All objects have pairwise different types and each is the only instance of its type, so $`\mathcal H_{\rm adm}=\mathcal H=\mathcal H_b\otimes\mathcal H_r\otimes\mathcal H_f`$.
- **Contract.**
  ```math
  C=C_{br}\otimes\mathbb 1_f+\sum_{j\in J}B_j\otimes\mathbb 1_r\otimes\Phi_j+\mathbb 1_{br}\otimes C_f ,
  ```
  where:
  - $`C_{br}`$ is self-adjoint on $`\mathcal H_b\otimes\mathcal H_r`$, a sum of pair terms among $`b`$ and the objects of $`r`$; it contains the body's own term;
  - $`J`$ is a finite index set, the $`B_j`$ are self-adjoint on $`\mathcal H_b`$ and the $`\Phi_j`$ self-adjoint on $`\mathcal H_f`$: this is the pair term between body and field;
  - $`C_f`$ is self-adjoint on $`\mathcal H_f`$, the field's own term (booked in the pair term by A5);
  - there is no contract between $`f`$ and the objects of $`r`$.

  The lapse-type pair term of the base problem is the case $`J=\{x\}`$ (the position labels of the body), $`B_x=\lvert x\rangle\langle x\rvert\otimes G`$.
- **Start.** $`\Psi_0=\Psi_{br}\otimes\varphi`$ at $`\lambda=0`$, with $`\Psi_{br}`$ any unit vector of $`\mathcal H_b\otimes\mathcal H_r`$ (a product or not) and $`\varphi`$ a unit vector of $`\mathcal H_f`$. Only $`\lambda\ge0`$ is used.
- **Sharp.** $`\varphi`$ is **sharp** for the family $`\{\Phi_j\}`$ if $`\Phi_j\varphi=n_j\varphi`$ for all $`j\in J`$, with real numbers $`n_j`$.
- **Readings.** Local readings on $`b`$ and on the objects of $`r`$, applied directly at stated values of $`\lambda`$ (A8), not represented by record objects. A **schedule** is a finite list of such readings with their values of $`\lambda`$; its statistics is the joint distribution of the outcomes. No reading is made on the field.
- **Reduced description.** A description without the field: the objects $`b`$ and $`r`$, a contract $`C_{\rm red}`$ on $`\mathcal H_b\otimes\mathcal H_r`$, and the start $`\Psi_{br}`$.

1. **Sharp and stationary field.** Let $`\varphi`$ be sharp with the numbers $`n_j`$, and let $`C_f\varphi=e_f\varphi`$.
   - (a) Determine $`\Psi(\lambda)`$ for every $`\Psi_{br}`$ and every $`\lambda\ge0`$. Determine the view of the part $`\{b\}\cup r`$ and the view of $`\{f\}`$, and whether the field becomes entangled with the other objects.
   - (b) Determine whether there is a reduced description whose schedules have, for every $`\Psi_{br}`$, the same statistics as the schedules of the full description; if there is, determine its contract $`C_{\rm red}`$.

2. **Sharp field in general.** Let $`\varphi`$ be sharp, without the condition $`C_f\varphi=e_f\varphi`$. Assume that the operators $`\mathbb 1_b`$ and $`B_j`$, $`j\in J`$, are linearly independent; say what changes if they are not.
   - (a) Determine the necessary and sufficient condition on $`(\varphi,C_f,\{\Phi_j\})`$ under which the view $`V`$ of $`\{b\}\cup r`$ is pure for every $`\Psi_{br}`$ and every $`\lambda\ge0`$. Determine whether a reduced description as in item 1(b) then exists, and its contract.
   - (b) Give an example in which $`\varphi`$ is sharp and the condition fails. For a sharp $`\varphi`$ for which the condition fails, determine the lowest power of $`\lambda`$ at which $`1-\mathrm{Tr}V^2`$ can be nonzero, with its coefficient in terms of the operators and the start.

3. **Static field that is not sharp.** Let the $`\Phi_j`$ commute with each other and with $`C_f`$, and let $`\varphi`$ be arbitrary.
   - (a) Determine the view of $`\{b\}\cup r`$ at every $`\lambda\ge0`$, for every $`\Psi_{br}`$, in terms of reduced descriptions.
   - (b) Determine the statistics of every schedule in terms of the statistics of reduced descriptions. Determine whether readings on $`b`$ and $`r`$ can distinguish this start from a start in which the field is sharp with numbers drawn at random with suitable probabilities.
   - (c) Determine the necessary and sufficient condition under which the view of $`\{b\}\cup r`$ is pure for every $`\Psi_{br}`$ and every $`\lambda\ge0`$. When it is not, determine the purity $`\mathrm{Tr}V^2`$ of that view in terms of the reduced evolutions.

4. **Conventions (M6).** Let the operators $`\mathbb 1_b`$ and $`B_j`$, $`j\in J`$, be linearly independent.
   - (a) Determine all replacements of $`C_{br}`$, of the $`\Phi_j`$ and of $`C_f`$, at fixed $`B_j`$, that leave $`C`$ unchanged. Determine how the numbers $`n_j`$ and the contract $`C_{\rm red}`$ of item 1 change under them.
   - (b) Determine which of the following are well defined: the numbers $`n_j`$; their differences $`n_j-n_{j'}`$; the contract $`C_{\rm red}`$. For a lapse-type pair term and a set $`r`$ that contains a medium recording the position of the body through $`\sum_x\lvert x\rangle\langle x\rvert\otimes K_x`$, determine the same for the on-site block of $`C_{\rm red}`$ at a position $`x`$ and for the differences of these blocks between two positions. Here every replacement that leaves $`C`$ unchanged counts, including those that move a term diagonal in the positions of the body between the body's own term, its pair term with the medium and its pair term with the field (A5, M6).

5. **One object as recording medium and as field.** Let there be no separate field object: the body is recorded by a medium $`c`$ through $`\sum_x\lvert x\rangle\langle x\rvert\otimes K_x`$ with $`K_x=\kappa\,x\,X`$ as in (17.15), and the same pair term between $`b`$ and $`c`$ also contains the lapse-type term $`\sum_x\lvert x\rangle\langle x\rvert\otimes G\otimes\Phi_x`$ with $`\Phi_x=\mathbb 1_c+g\,x\,Y`$, where $`Y`$ is self-adjoint on $`\mathcal H_c`$, $`[X,Y]=0`$, $`g\neq0`$, and the medium has no further term. The medium starts in $`\chi`$.
   - (a) Determine the condition on $`\chi`$ under which the medium is sharp for the $`\Phi_x`$ and, at the same time, different positions have different record vectors ($`d_0>0`$ in (17.15)). Determine what the factor $`\Phi_x`$ then amounts to for the body.
   - (b) When the medium is not sharp for the $`\Phi_x`$, determine the view of the body in terms of reduced descriptions, and which profiles $`n_x`$ and which gradients of the records occur together in them.

## Inputs

From 03-ilang-space/17-motion@v2. Setting there: one body $`b`$ and a medium $`c`$, $`C=C_b\otimes\mathbb 1_c+\sum_h\lvert h\rangle\langle h\rvert\otimes K_h`$; the start is $`\lvert\phi\rangle\otimes\lvert\chi\rangle`$; $`\langle X\rangle:=\langle\chi\vert X\vert\chi\rangle`$, record vectors $`\lvert u_h\rangle:=(K_h-\langle K_h\rangle)\lvert\chi\rangle`$, distances $`d_0(h,h')=\lVert u_h-u_{h'}\rVert`$, and $`p_h`$ the place weights of the view of $`b`$.

Eq. (17.15), for the chain $`h_m`$, $`m\in\mathbb Z`$, with $`K_{h_m}=m\,X`$, $`X`$ self-adjoint on $`\mathcal H_c`$, $`\sigma_X:=(\langle X^2\rangle-\langle X\rangle^2)^{1/2}>0`$ and $`e:=(X-\langle X\rangle)\chi`$, so that $`\lVert e\rVert=\sigma_X`$ and $`u_{h_m}=m\,e`$:

```math
d_0(h_m,h_n)=\lvert m-n\rvert\,\sigma_X,\qquad \bar x=\bar m\,e,\quad \bar m:=\sum_mm\,p_{h_m},\qquad s^2=\sigma_X^2\sum_m(m-\bar m)^2p_{h_m} .
```

## Assumptions

- The setting and the definitions under "Goal". All contracts are independent of $`\lambda`$ (A5).
- No two objects have the same type, so every partition of joint places is an admissible reading and every state after a reading is admissible.
- The field starts unentangled with the other objects ($`\Psi_0=\Psi_{br}\otimes\varphi`$). The state $`\varphi`$ of the field is an assumption of each item and is named in it (A11, M9).

## Scope

- **Class.** Items 1–4 are asked for every contract of the stated form (every $`C_{br}`$, every finite family $`B_j`$, $`\Phi_j`$, every $`C_f`$) and every $`\Psi_{br}`$; the state $`\varphi`$ is as each item states. Item 5 is asked for the stated pair term and every $`\chi`$.
- **Controls.** Item 2(b) and item 3 are the controls of item 1: field states for which the body does not see definite numbers.
- In scope:
  - the exact evolution for a sharp field, and the reduced description;
  - the condition for a pure view of the body and the other objects;
  - a static field in an arbitrary state;
  - the conventions in the split between body and field;
  - one object as recording medium and field, in the stated form.
- Out of scope:
  - a field whose operators $`\Phi_j`$ do not commute with its own term, beyond item 2 (a later package);
  - which operator $`G`$ of a body the field multiplies, and the motion and the clock of a body in a given profile (03-clock-and-fall);
  - the source of the field and any effect of the body on the field's later action on other bodies;
  - starts in which the field is entangled with the other objects.

## Depth

- Item 1: short argument.
- Item 2: derive.
- Item 3: derive.
- Item 4: short argument.
- Item 5: short argument.

## Expected result

- Item 1: a closed form for the state and the two views, and a yes/no answer; a yes/no answer with a contract.
- Item 2: an equivalence with a contract; an example, a power of $`\lambda`$ and a coefficient.
- Item 3: a closed form; a closed form and a yes/no answer; an equivalence and a closed form.
- Item 4: the general form of the replacements and the transformation of each quantity; a list of well-defined quantities.
- Item 5: a condition and a statement; a closed form and a statement.

Give every main result a tag $`(2.k)`$.

Consistency checks, at most three: for example $`\Phi_j=\mathbb 1_f`$ for all $`j`$, a field with one place, and a two-place field with one index $`j`$.

## Code

None.
