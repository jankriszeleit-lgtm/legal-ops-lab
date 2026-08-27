# LEGAL WORK PLANNER — Detailed User Guide

**External working manual · 2026-08-27**

## 1. Why use a Work Planner?

Professional work rarely arrives as a clean workflow. It arrives as something like:

"Please look at this before tomorrow and tell me what we should do."

Before specialist analysis begins, someone must decide what the assignment really means, what information matters, how the work should be broken down, what can be reused, who or what can help, what deserves research, what should be delegated, how much effort is justified and what should happen first.

The Legal Work Planner makes that step explicit without turning it into project-management bureaucracy.

Its first value is **better decisions about how work should be done**. Automation is optional.

## 2. The core sequence

The Planner follows a disciplined order:

```text
PL0  Intake
PL1  Frame
PL2  Open Work Scan
PL3  Approach Design
PL4  Resource Scan
PL5  Fit / Gap
PL6  Plan Synthesis
PL7  QC / Start
```

A useful shorthand is:

Understand -> Think -> Structure -> Explore -> Match -> Decide -> Plan.

The most important discipline is that **the resource inventory does not define the problem**. The Planner first asks what competent work may require; only then does it look at available people, knowledge, methods, tools and data.

## 3. Quick start

You normally do not need commands or forms. Describe the work as you would to a strong colleague.

Examples:

I need to review this amendment before Friday's internal call. Plan the work.

I have 45 minutes. Give me the fastest sensible plan and tell me what I should skip.

Plan this. I want to do the substantive analysis myself, but delegate the preparatory work if useful.

We have done similar matters before. Work out what we need first, then check which internal material is worth using.

Keep it light and turn the result into a checklist.

The Planner should normally give you a useful first plan before asking questions. It asks first only where a missing fact would make the plan materially misleading, unsafe or impossible to sequence.

## 4. What a good plan should tell you

A normal plan should make these questions easy to answer:

- What are we trying to achieve?
- What is the recommended route?
- What do I start with?
- What are the actual steps/workstreams?
- What inputs do I need?
- Who or what can help?
- What needs research, alignment, review or a decision?
- What can be delegated or automated?
- What capability gaps exist?
- When are we done?

For a 20-minute task this may be a short checklist. For a complex matter it may include workstreams, dependencies, allocation, research targets, resource choices and QC.

## 5. Work Item, Workstream, Action and Capability

### Work Item

The concrete professional demand the Planner is solving. It is smaller than a Matter/Project and usually larger than a single mechanical task.

### Workstream

A meaningful block within a complex Work Item, such as document review, factual reconstruction, research or decision preparation.

### Action

A concrete executable step.

### Capability

What must be possible for the action/workstream to be done well. A capability is not a specific tool.

This distinction matters because the Planner asks:

What must be possible?

before:

Which person, method, workflow or tool can provide it?

## 6. Planning depth

### LIGHT

Use for small/familiar work. Typical output:

- Goal;
- Recommended approach;
- Start here;
- two to five steps;
- one material resource/open point if useful;
- Done when.

A checklist may be the entire plan.

### STANDARD

For meaningful multi-step work. Adds workstreams, sequence, allocation, relevant QC, dependencies and targeted gaps/decisions.

### DEEP

For genuinely complex work. Uses progressive disclosure: executive plan first, then workstream detail, then planning detail. DEEP is not a technical trace mode.

You can steer depth naturally:

Keep this lightweight.

Give me the full workstream plan.

I need the assumptions and resource logic too.

## 7. The four configuration annexes

The Planner uses separate context files because different facts change at different times.

### 7.1 Profile — who you are and how you work

`ANL_PLANNER_PROFILE` contains role/authority references and stable workstyle calibration.

It distinguishes:

- **Can**: expertise/capability;
- **May**: permission/authority;
- **Responsible**: organisational ownership.

These are not interchangeable.

The first workstyle pilot has only four formal axes:

1. **Work ownership** — do you normally keep the core work yourself, balance it or delegate early?

2. **Delegation threshold** — how readily should the Planner propose delegation?

3. **Focus style** — long blocks, mixed blocks or short sprints?

4. **Decision style** — recommendation first or options first?

Each axis can change only named parts of the plan. A preference never gives the Planner authority or access.

### 7.2 Environment — what the host can technically do

`ANL_PLANNER_ENVIRONMENT` describes actual capabilities such as file access, retrieval, calendar read/write, tasks, collaboration, email, knowledge search, specialist execution and runtime observability.

`UNKNOWN` is not permission to try. For direct execution, UNKNOWN is non-executable.

### 7.3 Resources — what people/knowledge/methods/tools exist

`ANL_PLANNER_RESOURCES` is the dedicated Resource MAP. It may contain:

- people and teams;
- responsibilities/expertise;
- institutional knowledge and precedents;
- methods/workflows;
- tools/data/systems;
- approved external resources;
- pointers to ON\_DEMAND detail.

This annex is **not** consulted to define the Open Work Scan. Its purpose is to improve the plan after the work has been provisionally understood.

### 7.4 Matter — what is special about this project

`ANL_PLANNER_MATTER` is optional. Use it where a matter/project has a specific objective, deadline, allocation, decision owner, confidentiality/access constraint or resource override.

Do not put matter-specific changes into the general Profile or Resource MAP.

## 8. Permission vs scope: what a user instruction can and cannot do

The Planner uses two separate structures.

### Permission — fail closed

```text
Hard law / professional duty / binding policy
> access / confidentiality / data-zone constraints
> role authority limit
```

A user instruction cannot override these.

### Scope/style — only inside permission

```text
Current work-item instruction
> matter-specific context
> role profile defaults
> workstyle calibration
> workspace/resource defaults
> Planner defaults
```

So:

"Send it anyway; I'll take responsibility."

does not turn a prohibited/unauthorised action into an allowed one. The Planner must refuse, prepare a safer route or hand off.

## 9. Open Work Scan: the anti-tool-bias step

PL2 is intentionally open. The Planner asks what a competent professional might need to do without first looking at the tool/resource list.

Possible work needs include:

- factual clarification;
- document review;
- legal/specialist analysis;
- research;
- data work;
- stakeholder input;
- delegation;
- drafting;
- decision preparation;
- review/QC.

The list is provisional and open.

This protects the Planner against a common failure mode: seeing a tool and reshaping the problem to fit the tool.

## 10. Resource Scan and Institutional Alignment

At PL4 the Planner consults the resources that are relevant to the provisional work model.

A resource can be:

- a person/team;
- a precedent;
- an internal knowledge source;
- a method/workflow;
- a data source;
- a software tool;
- an external specialist/provider.

The Planner should say **how a resource helps**, not merely name it.

Institutional Alignment asks:

What do we already know or have that changes how this work should be done?

If the Planner can actually search an internal source, it may do so where bounded and permitted. If it cannot, it should give you a ready-to-run retrieval instruction rather than pretend it searched.

## 11. Research

The Planner owns the planning question:

- why research is needed;
- what question must be answered;
- scope/exclusions;
- what the answer will change.

A specialist Research workflow/provider owns source/verification method.

Without a specialist Research engine, the standalone Planner can still create a complete Research Brief. It must not invent research results.

Useful command:

Run the targeted research if you actually have access; otherwise give me the ready-to-run brief.

## 12. Capability matching and build decisions

For a material work step, the Planner can ask:

1. What capability is needed?

2. Is it already covered?

3. Does an existing resource fit?

4. Can it be configured or combined?

5. Is there a genuine gap?

Engineering escalation is:

**Reuse -> Configure -> Compose -> Extend -> Build.**

Build is not the default reward for finding a gap. Manual work and deferral remain valid.

A deeper provider/tool comparison is a follow-on (`PL-MATCH`); an actual build is a separate engineering task.

## 13. Human allocation and delegation

Humans and AI/tools are resources, but responsibility is not interchangeable.

A plan may suggest:

- user performs core professional judgment;
- preparatory research/data work delegated;
- specialist consulted;
- validated workflow used for a repeatable subtask;
- human review inserted where stakes require it.

The Planner should state acceptance criteria when delegating: what should come back, enough when, and who remains responsible.

Your Profile can calibrate how readily delegation is proposed, but it cannot invent an available colleague or delegate authority you do not have.

## 14. Calendar-aware planning

Calendar access is not just automation. It can make the plan feasible.

After the Open Work Scan, the Planner may use calendar information to identify:

- uninterrupted focus windows;
- preparation buffers;
- existing meetings that can absorb a discussion;
- mutual availability;
- deadline pressure.

Example:

The review needs roughly two uninterrupted hours. Thursday has no clean block; Wednesday 14:00-16:00 is the best slot.

If calendar write is available and you explicitly authorised it:

**Done for you:** I reserved Wednesday 14:00-16:00.

If write capability is unavailable/UNKNOWN:

Wednesday 14:00-16:00 is the best slot. I have not booked it.

## 15. Direct actions

The Planner may perform bounded actions where all gates are satisfied.

### Read / inspect

Calendar, existing meeting, internal knowledge, email/task context.

### Personal / reversible write

Personal focus block, reminder or task. First pilot: current explicit instruction/approval required.

### Collaborative

Mutual availability, meeting invitation, shared task, scoped internal coordination. Direct internal send requires verified internal recipient membership.

### Consequential / external

Substantive client/counterparty communication, final filing/approval, destructive changes and tool deployment remain controlled/specialist work.

For any direct action:

```text
specific capability
+ permitted use
+ current authorisation
+ bounded impact
+ truthful host result
```

A claimed action without actual capability/result is `PL_ACTION_SIMULATED`.

## 16. Action batches

You can say:

Do the three actions you proposed.

The Planner must still check each action separately. One successful action cannot make a failed action look successful.

## 17. Useful steering phrases

### Keep it light

Keep this lightweight.

### Personal work

I want to do the substantive analysis myself; delegate only preparation.

### Delegation

Be aggressive about delegation, but keep final professional judgment with me.

### Plan only

Plan only. Do not change my calendar, tasks or messages.

### Calendar

Check my calendar after you have worked out what the task needs. If there is a clean block, show me the best option.

### Bounded write

If there is a clean 90-minute block tomorrow, reserve it for the review. Do not message anyone.

### Approval before collaboration

Find a slot with Sue but show it to me before sending an invitation.

### Institutional knowledge

Work out the approach first, then check what we already have internally that could change it.

### Research

Run only the research that could change the plan.

### Checklist

Turn this into a checklist.

### Replan

Replan based on this new information: [...].

## 18. Decisions

Where the plan needs a human decision, the Planner should not hide it in prose. A useful decision block is:

```text
Decision
Recommended
Why
Minimum condition
Fallback
```

The Planner recommends; it does not silently assume the user's decision.

## 19. Replanning

Professional work changes. A new document, moved meeting, corrected fact, changed deadline or research result may alter the plan.

`PL-REPLAN` should normally show:

- What changed;
- What stays the same;
- Updated next step.

Only affected parts should be patched unless the original frame collapses.

## 20. Closeout and learning

`PL-CLOSE` is optional. It asks:

- What was planned?
- What actually happened?
- What was unnecessary?
- What was missing?
- What should be reused?

This can reveal better methods, useful precedents or engineering needs. It is not live status tracking and must not claim work the Planner did not observe.

## 21. Run Observability

Run Observability is cross-cutting and separate from ordinary plan rendering. The Planner uses the repository-defined global commands:

- `RUN-TRACE`;
- `RUN-BUNDLE`;
- `RUN-EXPORT` (alias where supported);
- `RUN-AUDIT [CURRENT|execution_id]`;
- `TEST-RUN [label]`.

These do not advance the planning method.

The Core carries the **SILENT** contract at snapshot `v0.1`. Technical trace information is not added to normal user output.

### What the prompt maintains

Professional workflow state: intake, frame, Open Work Scan, plan decisions, resource use, decisions/overrides, action receipts, replanning and QC.

### What runtime must measure

Where supported: run/execution identity, timestamps, tool events, source access, provider usage, technical errors/metrics and persistence.

The Planner does not reconstruct missing runtime facts.

### Chat-only degradation

If you explicitly request `RUN-TRACE` without runtime, the output must name the gaps, for example:

```text
capture_level: DEGRADED
missing_fields:
  - run_id
  - execution_id
  - tool_events
  - provider_usage
```

The exact fields depend on what the host actually lacks.

### Audit is not the control

`RUN-AUDIT` reveals the maintained evidence. It does not make an unauthorised action safe. The capability/permission/authorisation gate is the control; the trace is evidence/receipt.

## 22. Standalone use

The public Planner does not require any specialist suite. If a specialist legal, review or research engine is absent, the Planner still plans and creates self-contained handoffs and briefs.

A simple standalone test is to load only the three `PRT_` prompts plus the relevant annexes and use a real small Work Item. Any instruction that requires a missing internal library/reference is a defect.

## 23. Practical example: 45-minute internal amendment preparation

Request:

I have 45 minutes before an internal amendment discussion. I want to do the legal judgment myself. Keep it light.

A good Planner response might:

1. define the decision the discussion needs;

2. reserve the user's time for the core document/issue review;

3. identify any preparatory extraction or internal-precedent lookup that could be delegated or run quickly;

4. avoid broad research unless it changes the decision;

5. end with the position/questions needed for the meeting.

If Resources says a relevant precedent folder exists, the Planner may use it at PL4. If Environment says it cannot access that source, it should instruct how to retrieve it rather than pretend it searched.

## 24. Practical example: complex review with data and research

A complex Work Item may require:

- understanding contractual mechanics;
- factual/data reconstruction;
- mapping facts against the contract;
- legal/specialist research;
- stakeholder clarification;
- decision/strategy;
- review/QC.

The Planner should first identify those needs, then map available methods, people, data and tools. If a gap exists, it should prefer reuse/configuration/composition before proposing a new build. This preserves the original Work Planner/Capability Layer concept.

## 25. What the Planner is not

It is not a generic autonomous agent, a full project-management system, a matter-management system, a live execution tracker or a substitute for specialist professional judgment.

The plan should remain useful even if you never maintain status after the first answer.

## 26. When something looks wrong

### The plan mirrors the tool list

Ask: "Redo the Open Work Scan without using the resource inventory; map resources only afterwards."

### The Planner asks too many questions

Ask it to proceed with explicit assumptions unless the missing point is blocking.

### A resource is treated as accessed merely because it is listed

Correct the access state. `KNOWN_TO_EXIST` is not `ACCESSIBLE`.

### A write is claimed but no connector/result exists

Treat as failure (`PL_ACTION_SIMULATED`) and run the negative pilot.

### Your workstyle seems to override professional constraints

It must not. Permission and responsibility win; workstyle is soft calibration.

### A trace looks complete in chat-only mode

Check `capture_level` and `missing_fields`. Technical runtime data must not be invented.

## 27. Recommended first adoption path

1. Install the three prompts.

2. Fill a lean Profile.

3. Fill Environment truthfully.

4. Add only the most useful Resource references.

5. Use Matter annex only where needed.

6. Run small planning pilots.

7. Tune Profile/Resources based on observed plan value.

8. Run direct-action negative tests.

9. Only then enable/try connected writes.

The Planner should earn complexity from real work, not from configuration ambition.
