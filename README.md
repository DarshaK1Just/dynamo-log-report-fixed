# dynamo/log-report — Fixed Harbor TB2 Task

A Terminal-Bench 2 (Harbor) task that asks an agent to parse an Apache-style access log and produce a small JSON summary report.

---

## Task overview

The agent is given `/app/access.log` (6 Apache Combined Log Format lines) and must write `/app/report.json` containing:

```json
{
  "total_requests": 6,
  "unique_ips": 3,
  "top_path": "/index.html"
}
```

---

## Directory structure

```
log-report/
├── task.toml                  # TB2 task manifest
├── instruction.md             # Agent-facing instructions with numbered success criteria
├── environment/
│   ├── Dockerfile             # Agent environment (digest-pinned base image)
│   └── access.log             # Input log file (6 lines, 3 unique IPs)
├── solution/
│   ├── solve.py               # Oracle implementation
│   └── solve.sh               # Oracle entrypoint
└── tests/
    ├── test.sh                # Verifier entrypoint — writes reward.txt + ctrf.json
    └── test_outputs.py        # 5 pytest tests, one per instruction.md success criterion
```

---

## Defects fixed

| # | File | Defect | Fix |
|---|------|--------|-----|
| 1 | `task.toml` | `artifacts` was a bare string at TOML root level | Changed to top-level array `["/app/report.json"]` |
| 2 | `task.toml` | Artifact path `/app/out.json` didn't match oracle output | Corrected to `/app/report.json` |
| 3 | `Dockerfile` | `FROM python:latest` — mutable, not reproducible | Pinned with `@sha256:ac2122…` |
| 4 | `Dockerfile` | `COPY solution_hint.py` leaked the solution into the agent image | Removed; file deleted from build context |
| 5 | `instruction.md` | Vague prose, no output path or schema stated | Rewrote with explicit path, JSON schema, 5 numbered criteria |
| 6 | `tests/test.sh` | Reward written to `/app/reward.txt` | Fixed to `/logs/verifier/reward.txt` |
| 7 | `tests/test.sh` | `ctrf.json` never emitted | Added `--ctrf /logs/verifier/ctrf.json` |
| 8 | `tests/test.sh` | `set -euo pipefail` caused exit before writing `reward=0` on failure | Removed; exit code captured explicitly |
| 9 | `tests/test_outputs.py` | Only checked file existence — any non-empty file passed | Added exact-value assertions for all three fields |
| 10 | `tests/test_outputs.py` | No check for extra keys | Added `test_no_extra_keys` (criterion 5) |

---

## Running locally

```bash
# Oracle (reference solution) — should score reward = 1
harbor run -p log-report -a oracle

# No-op agent — must score reward = 0
harbor run -p log-report --agent nop
```

Requires [Harbor](https://pypi.org/project/harbor/) (`pip install harbor`) and Docker.

---

## Expected verifier results

**Oracle run** — all 5 tests pass, `reward.txt = 1`

```
PASSED test_report_exists
PASSED test_total_requests
PASSED test_unique_ips
PASSED test_top_path
PASSED test_no_extra_keys
```

**Nop run** — all 5 tests fail, `reward.txt = 0`

```
FAILED test_report_exists   — report.json not found at /app/report.json
FAILED test_total_requests  — report.json not found at /app/report.json
FAILED test_unique_ips      — report.json not found at /app/report.json
FAILED test_top_path        — report.json not found at /app/report.json
FAILED test_no_extra_keys   — report.json not found at /app/report.json
```
