# INSTALLATION GUIDE — Legal Work Planner

**Platform-neutral external guide · standalone-first**

## 1. Installation model

Install one Planner method across hosts. Do not create separate Prompt-only and Connected Cores.

```text
PRT_PLANNER_CORE
+ PRT_PLANNER_IMPLEMENTATION
+ PRT_PLANNER_RENDERER
+ ANL_PLANNER_PROFILE
+ ANL_PLANNER_ENVIRONMENT
+ ANL_PLANNER_RESOURCES
+ optional ANL_PLANNER_MATTER
[+ optional 04_ON_DEMAND modules — never persistent, loaded on explicit request only]
```

The annexes are separate because they change for different reasons.

## 2. Where each artifact belongs

### PRT_PLANNER_CORE

Put in the highest-priority persistent instruction surface available to the Planner. It owns method, guards, state, permission/scope separation, direct-action rules and the Run Observability contract.

### PRT_PLANNER_IMPLEMENTATION

Persistent companion instruction. It tells the host how to resolve annexes, capabilities, connectors, runtime evidence and degradation.

### PRT_PLANNER_RENDERER

Persistent or Planner-specific rendering instruction. It may be lazy-loaded if the host supports it.

### ANL_PLANNER_PROFILE

User/role owner. Review when role, authority or stable workstyle changes.

### ANL_PLANNER_ENVIRONMENT

Technical owner/admin. Review when connectors/runtime/host capabilities change.

### ANL_PLANNER_RESOURCES

Workspace/resource owner. Review when material people/knowledge/method/tool resources change. Prefer authoritative references over copies.

### ANL_PLANNER_MATTER

Matter/project owner. Optional and local to the active matter.

### 04_ON_DEMAND modules

Optional method modules, currently `PRT_PLANNER_STRESS_TEST`. Keep them available to the host but do not install them persistently. The host loads a module only on an explicit user request for what it does (Implementation §6 ON_DEMAND); it is read-only and never changes the plan.

## 3. Host patterns

### A. Chat-only

The Planner can plan, maintain professional state and prepare manual actions. It cannot claim connector reads/writes. Explicit Run outputs degrade per the contract.

### B. File/project workspace

Provide compact annexes plus relevant work-item files. Do not dump all workspace content into prompt context.

### C. Retrieval-enabled host

Preferred context delivery:

```text
FRAME before PL2
PL2 without MAP retrieval
MAP at PL4
ON_DEMAND after selection
```

### D. Connected host

Resolve specific action capabilities in `ANL_PLANNER_ENVIRONMENT`. `CONNECTOR` alone proves nothing.

## 4. Resource installation

The Resource annex is MAP context. The host should make it easy to resolve references without injecting all linked material.

Examples:

- Profile says the user is responsible for matter strategy.
- Resources says where financing precedents live and who owns them.
- Environment says SharePoint search is available.
- Matter says this project uses a specific precedent folder and decision owner.

Those facts must not be merged into one maintenance surface.

## 5. Workstyle installation

Start with only four formal axes: work ownership, delegation threshold, focus style and decision style.

If an axis has never changed a plan, leave it `UNSPECIFIED`. Do not create a user taxonomy before evidence.

A preference may never override permission/authority.

## 6. Permission and scope

This is a hard installation check.

Permission is fail-closed and cannot be overridden by the user:

```text
LAW / PROFESSIONAL DUTY / BINDING POLICY
> ACCESS / CONFIDENTIALITY / DATA ZONE
> ROLE AUTHORITY
```

Only inside that boundary do current work instructions and preferences set scope/style.

## 7. Direct actions

For a direct action to RUN, all of the following must be grounded:

- specific capability = available;
- permitted use;
- current authorisation;
- bounded impact;
- truthful host result.

`UNKNOWN`/`NO`/missing capability cannot RUN.

First-pilot writes require explicit current instruction or current approval.

## 8. Run Observability

The Core contains the SILENT Run Observability contract, published as the English projection of contract snapshot `v0.1`.

Do not add another technical trace. Runtime facts override prompt inference.

The Planner carries no observability display mode. `plan_depth` does not change trace visibility.

Without runtime, explicit Run outputs must show only actual state and use `capture_level: DEGRADED` with named missing runtime fields.

## 9. Standalone installation

No specialist-suite component is required. If specialist research, legal or review adapters exist, they can be connected through typed handovers. Missing adapters degrade to local Planner functions and briefs.

## 10. Maintenance

Use the narrowest owner:

- user/role/workstyle -> Profile;
- connector/runtime -> Environment;
- workspace resource -> Resources;
- project-specific fact/allocation -> Matter;
- method behaviour -> Core only when generic doctrine truly changes.

The Run Observability block should be re-checked whenever this public edition is maintained against a newer contract snapshot.

## 11. Minimum installation tests

Do not treat clean documents as functional evidence. Run the Testing/Pilots suite. Minimum pre-write gate:

1. standalone completeness;

2. permission conflict;

3. chat-only no-simulated-action;

4. write capability UNKNOWN;

5. degraded RUN-TRACE with named missing fields.
