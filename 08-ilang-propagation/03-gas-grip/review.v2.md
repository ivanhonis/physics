# Review: 03-gas-grip v2

- **Subproject:** 08-ilang-propagation
- **Package:** 03-gas-grip
- **Reviewed version:** v2
- **Date:** 2026-10-24

---
VERDICT: minor issues

## Issues

### I1. The conditions of (4.12) are missing where the bond criterion uses it
- **Location:** Step 6 after (3.11), the paragraph "Mark and bond together", the Result bullet (3.11); twin key result 3.11.
- **Severity:** minor
- **Problem:** "$`\kappa^{\rm mid}`$ is zero on the ring" holds at leading order in $`\eta`$ only for a source outside the arc between the two bodies, and the cubic-torus statement needs $`d\ll L`$ as well as $`\lvert\mathbf r\rvert,\lvert\mathbf r'\rvert\ll d`$. The question did not quote these conditions; it now carries them in a dated note (2026-10-24). As written, the ring case of (3.11)(ii) and of "mark and bond together" holds for every source position, which (4.12) does not give.
- **Fix:** Add the conditions of the note to (3.11)(ii), to "Mark and bond together", to the Result bullet (3.11) and to the twin. Nothing else changes.
