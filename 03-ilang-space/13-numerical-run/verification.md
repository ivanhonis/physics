# External verification: 13-numerical-run

- **Subproject:** 03-ilang-space
- **Package:** 13-numerical-run
- **Verified version:** v1
- **External round:** 1 of 2
- **Date:** 2026-10-08T17:47:15+02:00
- **Focus points:** none

---
VERDICT: minor issues

## Summary

The computational formulas, ensemble normalizations, and supplied T1, T4, and T5 outputs are consistent with the stated decision rules. T3(a)’s failure is correctly retained rather than handled by changing the test, and the T5 closed form is correct. The remaining issues concern an unstated condition needed for Ilanguage admissibility and incomplete raw-output evidence in the supplied materials.

## Issues

### I1. Cell typing and admissibility under Law 5 are unspecified
- **Location:** Setup and assumptions; Steps 5–7
- **Severity:** minor
- **Problem:** The derivation does not specify whether the qubit cells are distinct types or identical-type instances. If they are identical-type instances, T4’s independently drawn product state is generally outside $`\mathcal H_{\rm adm}`$, and the cell-dependent records and chain contracts in T4/T5 generally do not preserve that subspace. Equal local Hilbert-space dimensions do not require equal types, so this is an unresolved model specification rather than an established numerical error.
- **Suggested fix:** Document the object types and families belonging to the precommitted descriptions, making explicit why the initial states and evolution satisfy A3/A6. If the cells were actually identical-type instances, report the affected parts as incompatible with the base model rather than silently treating their identifiers as data.

### I2. Cited T2 and T3 raw outputs are not supplied
- **Location:** Steps 3–4; `output/t2_dimension_distances.json` and `output/t3_loop_phases.json`
- **Severity:** minor
- **Problem:** The supplied materials include the computation scripts but omit these two cited output files. Consequently, the reported T2 statistics and rank diagnostics, and the T3 triangle-level errors and extended-precision diagnostic, cannot be checked against their saved raw values. The scripts implement the stated procedures, but that alone does not verify the reported numerical outputs.
- **Suggested fix:** Supply the unchanged JSON files from the reported run, including their per-sample/per-triangle values, diagnostics, slopes, and decisions.

## Focus points

None given.
