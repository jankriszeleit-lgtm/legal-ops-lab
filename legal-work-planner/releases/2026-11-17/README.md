# Legal Work Planner — proposed public release 2026-11-17

```text
PUBLIC RELEASE: 2026-11-17
RUN OBSERVABILITY CONTRACT SNAPSHOT: v0.1
STATUS: WORKING / NOT FIELD VALIDATED
```

## Release metadata

| | |
|---|---|
| Release date | 2026-11-17 |
| Status | Proposed working public edition; pending PR review. Not a maturity claim. |
| License | CC BY 4.0 — see [`LICENSE.md`](../../../LICENSE.md) |
| Field validation | **Not field validated.** Pilots remain required. |
| Language | English |
| Canonical installation source | **Markdown**, the files in this directory |
| Optional generated installation formats | None published. Installation Markdown remains canonical. |
| Work Plan output | Canonical plan plus automatic non-canonical DOCX when the host can generate and deliver it; explicit failure otherwise. |

Markdown is the canonical source. Any other format that appears later is
generated from these files and does not carry independent authority. Where a
generated asset and this directory disagree, this directory is correct.

## Changes from 2026-08-27

This is a new dated release because automatic DOCX output changes the normal
plan-output contract. The published `2026-08-27` directory is preserved byte for
byte; its installed behaviour is not changed retroactively. Upgrade the three
prompts together and verify Environment capabilities. This PR creates no
GitHub Release/tag or generated installation asset.

- Core: canonical-first output on every creation/material update; no schema
  migration, planning-method change, second plan store or DOCX roundtrip.
- Renderer: full-plan reading copy even when chat is LIGHT/delta-only; explicit
  non-canonical notice, source/version/date and stable item IDs.
- Implementation/Environment: separate generation and actual file-delivery
  capabilities, truthful degradation, and stale-snapshot prevention.
- `05_HOST_ADAPTER`: executable standard-library JSON-to-DOCX reference writer,
  synthetic tests and integration instructions. CI also opens Word output with
  an independent reader. D-01–D-06 specify actual-host acceptance.

The PL0–PL7 method, professional-state model, direct-action gates and optional
read-only stress-test behaviour are retained. Core §21 (Run Observability
snapshot `v0.1`) is byte-identical to the preceding release.

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
| `04_ON_DEMAND` | [`PRT_PLANNER_STRESS_TEST.md`](04_ON_DEMAND/PRT_PLANNER_STRESS_TEST.md) | optional plan stress test; loaded on explicit request only, read-only; added 2026-10-09 |
| `05_HOST_ADAPTER` | [`README.md`](05_HOST_ADAPTER/README.md) | host integration, limitations and executable checks |
| `05_HOST_ADAPTER` | [`work_plan_docx.py`](05_HOST_ADAPTER/work_plan_docx.py) | one-way reference exporter for canonical JSON plans |

## Installation sources

Install the three prompts together, then the annexes. Bind the DOCX output
using [`05_HOST_ADAPTER/README.md`](05_HOST_ADAPTER/README.md) or an equivalent
native adapter; run D-01–D-06 before claiming host conformance.

Persistent installation sources:

- [`02_PROMPTS/PRT_PLANNER_CORE.md`](02_PROMPTS/PRT_PLANNER_CORE.md)
- [`02_PROMPTS/PRT_PLANNER_IMPLEMENTATION.md`](02_PROMPTS/PRT_PLANNER_IMPLEMENTATION.md)
- [`02_PROMPTS/PRT_PLANNER_RENDERER.md`](02_PROMPTS/PRT_PLANNER_RENDERER.md)
- [`01_INSTALLATION/ANL_PLANNER_PROFILE.md`](01_INSTALLATION/ANL_PLANNER_PROFILE.md)
- [`01_INSTALLATION/ANL_PLANNER_ENVIRONMENT.md`](01_INSTALLATION/ANL_PLANNER_ENVIRONMENT.md)
- [`01_INSTALLATION/ANL_PLANNER_RESOURCES.md`](01_INSTALLATION/ANL_PLANNER_RESOURCES.md)
- [`01_INSTALLATION/ANL_PLANNER_MATTER.md`](01_INSTALLATION/ANL_PLANNER_MATTER.md) — optional, per matter

Not part of the persistent installation:
[`04_ON_DEMAND/PRT_PLANNER_STRESS_TEST.md`](04_ON_DEMAND/PRT_PLANNER_STRESS_TEST.md)
is an optional method module the host loads only when the user explicitly asks
to stress-test an existing plan, for example *"Stress-test this plan as a
recommendation only; change nothing."* It never changes the plan and triggers
no replanning or action. Test home: IT-0 to IT-3 in
[`03_TESTING/TESTING_AND_PILOTS.md`](03_TESTING/TESTING_AND_PILOTS.md).

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

- versioning uses this release date; document presence is not field evidence;
- no concrete production-host binding or model pilot has been field validated;
- the reference writer accepts JSON professional plans; other native formats
  need their own equivalent host adapter;
- prompts alone cannot generate or attach files; generation and download
  delivery must both be verified on the host;
- source locking and cleanup of partially delivered files remain host duties;
- standalone completeness must be pilot-tested with specialist adapters
  removed;
- connected actions require host capability evidence; `UNKNOWN` capability is
  non-executable;
- standing write authority is disabled in the first pilot;
- prompt-local action receipts are not a persistent technical audit log;
- connected write actions must pass the negative-path tests before any
  happy-path use;
- full orchestration and live execution tracking are out of scope;
- the optional plan stress test module is a recommendation-only aid,
  plausibility-probed on two synthetic cases and not field validated; a
  designed tripwire is not a monitored one.

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
