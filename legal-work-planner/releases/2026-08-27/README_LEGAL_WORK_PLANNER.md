# LEGAL WORK PLANNER — External Bundle Overview

**Working external package · 2026-08-27 · standalone-first · no repository version assigned**

```text
PUBLIC RELEASE: 2026-08-27
RUN OBSERVABILITY CONTRACT SNAPSHOT: v0.1
STATUS: WORKING / NOT FIELD VALIDATED
```

## 1. What the Legal Work Planner is

Professional work often begins with an imperfect request, not a predefined workflow. The Planner turns that request into a proportionate, resource-aware work plan.

Its governing sequence is:

**Think first. Look at what is available second. Route third. Act fourth only where a bounded action is capability-resolved, permitted and currently authorised.**

The product sits between intake and specialist execution. It is broader than a task router and narrower than a matter-management/orchestration system.

## 2. Standalone promise

The three `PRT_` prompts contain the generic rules they need to run without any optional specialist adapter: intake, mid-run corrections, epistemic separation, anti-invention, phase/order discipline, Research Briefs, resource matching, direct-action gates, typed handovers, QC, rendering and Run Observability.

Specialist components may be attached as optional adapters. Their absence must not break ordinary planning.

## 3. Bundle map

| **Location** | **Document** | **Purpose** |
|---|---|---|
| (root) | [`README_LEGAL_WORK_PLANNER.md`](README_LEGAL_WORK_PLANNER.md) | bundle overview |
| (root) | [`USER_GUIDE_LEGAL_WORK_PLANNER.md`](USER_GUIDE_LEGAL_WORK_PLANNER.md) | detailed working manual |
| `01_INSTALLATION` | [`INSTALLATION_ASSISTANT.md`](01_INSTALLATION/INSTALLATION_ASSISTANT.md) | guided setup prompt/process |
| `01_INSTALLATION` | [`INSTALLATION_GUIDE.md`](01_INSTALLATION/INSTALLATION_GUIDE.md) | platform-neutral installation/maintenance |
| `01_INSTALLATION` | [`ANL_PLANNER_PROFILE.md`](01_INSTALLATION/ANL_PLANNER_PROFILE.md) | user, role, authority references and four workstyle axes |
| `01_INSTALLATION` | [`ANL_PLANNER_ENVIRONMENT.md`](01_INSTALLATION/ANL_PLANNER_ENVIRONMENT.md) | host, connector and runtime capabilities |
| `01_INSTALLATION` | [`ANL_PLANNER_RESOURCES.md`](01_INSTALLATION/ANL_PLANNER_RESOURCES.md) | people, knowledge, methods, tools/data resource MAP |
| `01_INSTALLATION` | [`ANL_PLANNER_MATTER.md`](01_INSTALLATION/ANL_PLANNER_MATTER.md) | optional matter/project-specific FRAME/MAP override |
| `02_PROMPTS` | [`PRT_PLANNER_CORE.md`](02_PROMPTS/PRT_PLANNER_CORE.md) | planning method, state, permissions, direct action, Run Observability contract |
| `02_PROMPTS` | [`PRT_PLANNER_IMPLEMENTATION.md`](02_PROMPTS/PRT_PLANNER_IMPLEMENTATION.md) | host/context/connector/runtime adapter rules |
| `02_PROMPTS` | [`PRT_PLANNER_RENDERER.md`](02_PROMPTS/PRT_PLANNER_RENDERER.md) | user-facing rendering |
| `03_TESTING` | [`TESTING_AND_PILOTS.md`](03_TESTING/TESTING_AND_PILOTS.md) | consolidated tests, pilots and evaluation template |
| `04_ON_DEMAND` | [`PRT_PLANNER_STRESS_TEST.md`](04_ON_DEMAND/PRT_PLANNER_STRESS_TEST.md) | optional on-demand plan stress test, read-only; not part of the persistent install |

The package uses four annexes because they have different owners/lifecycles. That is deliberate locality, not document sprawl.

## 4. Context architecture

```text
USER REQUEST
    |
    +-- PROFILE: who the user is / stable workstyle
    +-- MATTER: current objective / constraints / allocation
    |
    v
PRT_PLANNER_CORE
    |
    |  PL2 OPEN WORK SCAN -- before active resource inventory
    |
    +-- RESOURCES at PL4: people / knowledge / methods / tools / data
    +-- ENVIRONMENT: dynamic host capabilities / calendar / runtime
    +-- ON_DEMAND specialist detail
    |
    +-- optional bounded direct action
    |
    v
PRT_PLANNER_RENDERER
    |
    v
USEFUL PLAN / CHECKLIST / DECISION / ACTION RECEIPT
```

## 5. Permission is separate from scope

A current user instruction never outranks law, professional duty, binding policy, confidentiality/access or role authority.

Permission is fail-closed. Scope/style is resolved only inside what permission allows.

## 6. Resource MAP

`ANL_PLANNER_RESOURCES` restores the dedicated resource layer. It holds compact, sourced references to:

- people/teams/responsibility;
- institutional knowledge/precedents;
- methods/workflows;
- tools/data/systems;
- approved external resources;
- ON\_DEMAND detail.

The Planner must not consult this inventory to define PL2. Resources are matched after the work has been provisionally understood.

## 7. Workstyle

The first pilot uses only four formal axes: work ownership, delegation threshold, focus style and decision style. Each axis names exactly what it may calibrate.

Preferences do not create capability, authority, availability or responsibility.

## 8. Run Observability

The Core carries the **SILENT** Run Observability contract, published here as the English public projection of contract snapshot `v0.1`.

The Planner creates no second technical trace. Runtime facts override prompt inference. In no-runtime environments, explicit Run output degrades using `capture_level: DEGRADED` and named missing fields.

Audit reveals maintained evidence; it does not control execution. The direct-action gate remains the control.

## 9. Current evidence status

This is a working package, not a FINAL maturity claim. Planner pilots remain required. Connected write actions must pass negative-path tests before happy-path use.
