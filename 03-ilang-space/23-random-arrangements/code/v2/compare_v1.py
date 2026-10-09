"""Package 23-random-arrangements, code v2: check that v2 reproduces every number saved by v1.

Run from the project root (after arrangements.py):
  .venv/Scripts/python.exe 03-ilang-space/23-random-arrangements/code/v2/compare_v1.py
Compares every leaf of code/v1/output/<part>.json with the same key path in code/v2/output/<part>.json
(exact equality; runtimes excluded).  Keys added in v2 are not compared.  Output: output/compare_v1.json.
"""
import json
from pathlib import Path

HERE = Path(__file__).parent
V1, V2 = HERE.parent / "v1" / "output", HERE / "output"


def leaves(a, b, path, diffs, count):
    if isinstance(a, dict):
        for k, v in a.items():
            if k == "runtime_s":
                continue
            if not isinstance(b, dict) or k not in b:
                diffs.append(dict(path=f"{path}/{k}", v1=v, v2="missing"))
                continue
            leaves(v, b[k], f"{path}/{k}", diffs, count)
    elif isinstance(a, list):
        if not isinstance(b, list) or len(a) != len(b):
            diffs.append(dict(path=path, v1=a, v2=b))
            return
        for i, (x, y) in enumerate(zip(a, b)):
            leaves(x, y, f"{path}[{i}]", diffs, count)
    else:
        count[0] += 1
        if a != b:
            diffs.append(dict(path=path, v1=a, v2=b))


res = {}
for part in ("T1", "T1b", "T2", "T3", "T4"):
    diffs, count = [], [0]
    leaves(json.loads((V1 / f"{part}.json").read_text()), json.loads((V2 / f"{part}.json").read_text()),
           part, diffs, count)
    res[part] = dict(n_leaves_compared=count[0], n_differences=len(diffs), differences=diffs[:50])
    print(f"{part}: {count[0]} values compared, {len(diffs)} differences")
res["all_identical"] = all(r["n_differences"] == 0 for r in res.values())
(V2 / "compare_v1.json").write_text(json.dumps(res, indent=1))
