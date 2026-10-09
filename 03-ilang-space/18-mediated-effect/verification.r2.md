# External verification: 18-mediated-effect

- **Subproject:** 03-ilang-space
- **Package:** 18-mediated-effect
- **Verified version:** v2
- **External round:** 2 of 2
- **Date:** 2026-10-08T21:36:17+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The reduction, commutator-based locality argument, and leading generic influence coefficients are consistent with the stated model. The qubit calculation supports the order-\(\lambda^6\) weight changes and the order-\(\lambda^8\) position change, including the endpoint corrections. The remaining issues are an explicitly unresolved exceptional parameter choice and a dimensional check that conflates the position with the dimensionless index moment.

## Issues

### I1. Exceptional case lacks its leading position term
- **Location:** Step 10, Eq. (18.16), and Open issues.
- **Severity:** minor
- **Problem:** For \(m=2<n-1\) and \(t^2=8\), the displayed \(\lambda^8\) coefficient vanishes. The derivation correctly acknowledges this, but consequently does not determine the first nonzero term of \(\delta\bar x\) for this allowed parameter choice. Thus item 5 is answered generically rather than throughout its stated parameter range.
- **Suggested fix:** Determine the first nonzero position term in this exceptional case, or explicitly qualify the claimed completion of item 5 as excluding this unresolved case.

### I2. Restored dimensions omit the position-vector scale
- **Location:** Consistency check 1, discussion of Eq. (18.16).
- **Severity:** minor
- **Problem:** With \(K_{h_i}=i\kappa X\), the position vectors are \(u_{h_i}=i\kappa|1\rangle\), so \([\bar x]=[C]\). The stated restored factors \(m\sigma^2t^2\kappa^4\) and \(\sigma^2t^4\kappa^2\) are appropriate for the coefficient of the dimensionless moment \(\delta\langle\mathcal N\rangle\), not for \(\delta\bar x\). The latter requires an additional factor of \(\kappa\), and its \(\lambda^8\) coefficient has dimension \([C]^9\), not \([C]^8\).
- **Suggested fix:** Distinguish the dimensional check for \(\delta\langle\mathcal N\rangle\) from that for \(\delta\bar x\). For the position, restore bulk and endpoint factors proportional to \(m\sigma^2t^2\kappa^5\) and \(\sigma^2t^4\kappa^3\), respectively.

## Focus points

None given.
