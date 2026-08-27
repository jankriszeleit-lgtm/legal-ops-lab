# Legal Work Planner — public release 2026-08-27

```text
PUBLIC RELEASE: 2026-08-27
RUN OBSERVABILITY CONTRACT SNAPSHOT: v0.1
STATUS: WORKING / NOT FIELD VALIDATED
```

## Release metadata

| | |
|---|---|
| Release date | 2026-08-27 |
| Status | Working public edition. Not a maturity claim. |
| License | CC BY 4.0 — see [`LICENSE.md`](../../../LICENSE.md) |
| Field validation | **Not field validated.** Pilots remain required. |
| Language | English |
| Canonical installation source | **Markdown**, the files in this directory |
| Optional generated formats | None published. Word or PDF may later be attached to a GitHub Release as generated assets; if so they are build outputs, not a second source of truth. |

Markdown is the canonical source. Any other format that appears later is
generated from these files and does not carry independent authority. Where a
generated asset and this directory disagree, this directory is correct.

## Start here

Read [`README_LEGAL_WORK_PLANNER.md`](README_LEGAL_WORK_PLANNER.md) for what
the Planner is and how the parts fit together, then
[`USER_GUIDE_LEGAL_WORK_PLANNER.md`](USER_GUIDE_LEGAL_WORK_PLANNER.md) for the
working manual.

## Contents

| Location | Document | Purpose |
|---|---|---|
| (root) | [`README_LEGAL_WORK_PLANNER.md`](README_LEGAL_WORK_PLANNER.md) | bundle overview and context architecture |
| (root) | [`USER_GUIDE_LEGAL_WORK_PLANNER.md`](USER_GUIDE_LEGAL_WORK_PLANNER.md) | detailed working manual |
| `01_INSTALLATION` | [`INSTALLATION_GUIDE.md`](01_INSTALLATION/INSTALLATION_GUIDE.md) | platform-neutral installation and maintenance |
| `01_INSTALLATION` | [`INSTALLATION_ASSISTANT.md`](01_INSTALLATION/INSTALLATION_ASSISTANT.md) | guided setup prompt and process |
| `01_INSTALLATION` | [`ANL_PLANNER_PROFILE.md`](01_INSTALLATION/ANL_PLANNER_PROFILE.md) | user, role, authority and the four workstyle axes |
| `01_INSTALLATION` | [`ANL_PLANNER_ENVIRONMENT.md`](01_INSTALLATION/ANL_PLANNER_ENVIRONMENT.md) | host, connector and runtime capabilities |
| `01_INSTALLATION` | [`ANL_PLANNER_RESOURCES.md`](01_INSTALLATION/ANL_PLANNER_RESOURCES.md) | people, knowledge, methods, tools and data resource map |
| `01_INSTALLATION` | [`ANL_PLANNER_MATTER.md`](01_INSTALLATION/ANL_PLANNER_MATTER.md) | optional matter or project override |
| `02_PROMPTS` | [`PRT_PLANNER_CORE.md`](02_PROMPTS/PRT_PLANNER_CORE.md) | method, guards, state, permission and scope lattices, direct-action gates, Run Observability contract |
| `02_PROMPTS` | [`PRT_PLANNER_IMPLEMENTATION.md`](02_PROMPTS/PRT_PLANNER_IMPLEMENTATION.md) | host, context, connector and runtime adapter rules |
| `02_PROMPTS` | [`PRT_PLANNER_RENDERER.md`](02_PROMPTS/PRT_PLANNER_RENDERER.md) | user-facing rendering |
| `03_TESTING` | [`TESTING_AND_PILOTS.md`](03_TESTING/TESTING_AND_PILOTS.md) | test, pilot and evaluation specification |

## Installation sources

Install the three prompts together, then the annexes:

- [`02_PROMPTS/PRT_PLANNER_CORE.md`](02_PROMPTS/PRT_PLANNER_CORE.md)
- [`02_PROMPTS/PRT_PLANNER_IMPLEMENTATION.md`](02_PROMPTS/PRT_PLANNER_IMPLEMENTATION.md)
- [`02_PROMPTS/PRT_PLANNER_RENDERER.md`](02_PROMPTS/PRT_PLANNER_RENDERER.md)
- [`01_INSTALLATION/ANL_PLANNER_PROFILE.md`](01_INSTALLATION/ANL_PLANNER_PROFILE.md)
- [`01_INSTALLATION/ANL_PLANNER_ENVIRONMENT.md`](01_INSTALLATION/ANL_PLANNER_ENVIRONMENT.md)
- [`01_INSTALLATION/ANL_PLANNER_RESOURCES.md`](01_INSTALLATION/ANL_PLANNER_RESOURCES.md)
- [`01_INSTALLATION/ANL_PLANNER_MATTER.md`](01_INSTALLATION/ANL_PLANNER_MATTER.md) — optional, per matter

The four annexes ship as empty templates. They are separate because they have
different owners and lifecycles; merging them to reduce file count defeats the
locality-of-change design.

## Standalone

The public edition is standalone. The three `PRT_` prompts carry the generic
rules they need, and no specialist suite component is required in order to
plan. Specialist components may be attached as optional adapters, and their
absence is designed not to break ordinary planning.

## Known limitations

Stated by the package itself:

- no version is assigned beyond this release date, and document presence is
  not field evidence;
- standalone completeness must be pilot-tested with specialist adapters
  removed;
- connected actions require host capability evidence; `UNKNOWN` capability is
  non-executable;
- standing write authority is disabled in the first pilot;
- prompt-local action receipts are not a persistent technical audit log;
- connected write actions must pass the negative-path tests before any
  happy-path use;
- full orchestration and live execution tracking are out of scope.

Run the test suite in
[`03_TESTING/TESTING_AND_PILOTS.md`](03_TESTING/TESTING_AND_PILOTS.md) before
enabling connected writes. Do not treat clean documents as functional
evidence.

## Run Observability

The Core carries the **SILENT** Run Observability contract at snapshot `v0.1`,
published here as an English projection with identical functional semantics.
Audit and trace are evidence and receipt; they are not the execution control.
The control remains the capability, permission and authorisation gate in the
Core.

Conformance is checked by test M-01, which validates the declared snapshot
version and the required SILENT semantics.

Any material change to the observability semantics requires an explicit
snapshot-version update and corresponding update of M-01.
