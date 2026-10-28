# Review: 03-gas-grip v1

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Reviewed version:** v1
- **Date:** 2026-10-24

---
VERDICT: major errors

## Issues

### I1. The weight of the self-cost is not its own
- **Location:** Step 4, (3.6), the sentence after it, and the Result bullet (3.6); twin key result 3.6.
- **Severity:** major
- **Problem:** (3.6) is a rewriting of $`\Delta W=\Omega C^{\rm mark}(1+B^{\rm fg})`$. It assigns the factor $`\Omega(1+B^{\rm fg})`$ to the self-cost and to the first-order mark cost alike, but the weight of the first-order part is exactly $`\Delta W^{(1)}=\Omega ng_b`$ by (3.5). The weight beyond the first-order part, per unit of self-cost, follows from (3.13) and (3.5): $`\bigl(\Omega C^{\rm self}+\Omega_2n^2g_b^2\bigr)/C^{\rm self}=\Omega\bigl[1+(\ell(r)+\ell(r')-T_2)/(2\ell_0)\bigr]+O(\chi)`$. This ratio is the same for every affine grip and depends on the graph and the distance. So whether the field-made part of the cost is weighed like the first-order part is not decided by $`\alpha`$ alone, and the reading "the self-cost is weighed with $`\Omega(1+B^{\rm fg})`$" is a convention of the allocation, not a property of the self-cost.
- **Fix:** State (3.6) as the rewriting it is. Derive the weighing ratio of the self-cost alone against that of the first-order part, at leading order with its remainder, and its forms on the three graphs at the distances where they apply ($`\ell`$, $`\ell^{(2)}`$ and $`\ell_0`$ of each graph are lattice sums; derive their large-distance forms as standard mathematics). Say for which graphs and distances it tends to the ratio of the first-order part.

### I2. "iff $`\alpha=0`$" and "exactly $`F=\beta\Phi`$" omit the remaining breaking terms
- **Location:** (3.8), (3.11), Step 6 after (3.10), the Result bullets (3.8) and (3.11); twin key results 3.8 and 3.11.
- **Severity:** major
- **Problem:** Both criteria hold at leading order only. At $`\alpha=0`$ the first breaking terms remain: $`B^{\rm fg}`$ for the mark (and the ratio of I1 for the self-cost), $`\kappa^{\rm mid}+O(\eta K)`$ for the bond. Whether they vanish depends on the graph and the distance. For the bond the quoted (4.12) gives it: zero on the ring with the midpoint, small on the cubic torus for $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d`$, on the square torus only for $`d`$ large against $`\lvert\mathbf r\rvert`$ times a logarithm of $`L`$. For the mark it is not given (I1). The question asks for the first breaking term on the three graphs and for the grips for which the mark and the bond are weighed like the first-order part. As written, "exactly $`F=\beta\Phi`$" states a necessary condition as if it were the answer.
- **Fix:** Restate (3.8) and (3.11) as two statements: (i) at leading order, the condition $`\alpha=0`$; (ii) for $`\alpha=0`$, the graphs, distances and orders at which the remaining breaking terms of the mark (I1) and of the bond ((4.12)) vanish, and where they do not. Carry the same wording into the Result and the twin.
