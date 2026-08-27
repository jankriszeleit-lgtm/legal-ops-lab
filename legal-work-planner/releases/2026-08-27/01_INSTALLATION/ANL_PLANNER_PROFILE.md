# ANL_PLANNER_PROFILE — User, Role and Workstyle Calibration

**External working annex · standalone · no repository version assigned**

## 0. Purpose and ownership

This annex tells the Planner **who the user is in the work context and how the user prefers to work**. It is calibration, not truth creation and not a permission grant.

| **Field** | **Value** |
|---|---|
| Profile name |  |
| User / role |  |
| Owner |  |
| Source(s) |  |
| Created |  |
| Last verified |  |
| Review trigger | role/authority change; material workstyle change |

Permission remains governed by the Core §2.1 lattice.

## 1. Professional role and context — FRAME

| **Field** | **Value / source** |
|---|---|
| Role / title |  |
| Organisation / team |  |
| Typical work |  |
| Typical audiences |  |
| Material confidentiality context |  |
| Typical output responsibility |  |

## 2. Can / May / Responsible

Do not infer one from another. Source any material authority or responsibility.

| **Topic** | **Can** | **May** | **Responsible** | **Source / owner** | **Last verified** |
|---|---|---|---|---|---|
| Core professional work |  |  |  |  |  |
| Approvals / release |  |  |  |  |  |
| External communication |  |  |  |  |  |
| Internal escalation |  |  |  |  |  |
| External advisers |  |  |  |  |  |
| Tool / AI use |  |  |  |  |  |

## 3. Role calibration

Every role calibration must name the Core target it may influence.

| **Calibration** | **Value** | **May influence** | **Source / note** |
|---|---|---|---|
| Risk / quality focus |  | PL7 QC; review emphasis |  |
| Review threshold |  | PL6/PL7 review step |  |
| Escalation triggers |  | decision/handoff planning |  |
| Preferred work products |  | PL6 output plan; Renderer |  |
| Audience/register default |  | Renderer only |  |

## 4. Workstyle — first-pilot axes only

These are preferences. They cannot create permission, authority, capability, availability or responsibility.

| **Axis** | **Value** | **Allowed target** | **Planning effect** |
|---|---|---|---|
| `work_ownership` | `PERSONAL_FIRST / BALANCED / DELEGATION_FIRST / UNSPECIFIED` | Core §9.3; §8.6 | personal vs delegated allocation emphasis |
| `delegation_threshold` | `LOW / MEDIUM / HIGH / UNSPECIFIED` | Core PL5/PL6 | when to propose delegation/briefing |
| `focus_style` | `LONG_BLOCKS / MIXED / SHORT_SPRINTS / UNSPECIFIED` | Core §13; §8.6 | grouping/splitting focus work |
| `decision_style` | `RECOMMENDATION_FIRST / OPTIONS_FIRST / UNSPECIFIED` | Core §15; Renderer | ordering of recommendation/options |

Rules:

1. A preference may not override Core §2.1.

2. A preference may make a direct action more conservative; never more permissive.

3. Plan depth, checklist view and Institutional Alignment are not workstyle axes; their dedicated mechanisms control them.

4. If an axis materially changes the plan, the Core records a `calibration_effect` with axis, target, effect and source.

5. An axis with no material target remains `UNSPECIFIED`; do not invent precision.

## 5. Optional working notes — non-authorising

Use sparingly for information that helps the Planner but has not earned a formal axis.

| **Note** | **May influence** | **Must not be treated as** |
|---|---|---|
|  |  | authority / availability / capability |

## 6. Update rule

Update this annex when the user's role/authority or stable working preference changes. Do **not** edit it merely because a matter has a different deadline, team or allocation; those belong in `ANL_PLANNER_MATTER`.
