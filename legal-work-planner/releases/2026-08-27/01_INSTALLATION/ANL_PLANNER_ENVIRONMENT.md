# ANL_PLANNER_ENVIRONMENT — Host, Capability and Runtime Profile

**External working annex · standalone · no credentials**

## 0. Purpose and ownership

This annex describes what the **current host/runtime can technically do**. It does not grant permission or user authority.

| **Field** | **Value** |
|---|---|
| Environment name |  |
| Host / workspace |  |
| Technical owner |  |
| Created |  |
| Last verified |  |
| Review trigger | host/connector/runtime change |

## 1. Deployment capability

```text
CHAT_ONLY | FILE_ACCESS | CONNECTOR
```

The broad value never proves a specific action capability.

## 2. File / retrieval / code

| **Capability** | **YES / NO / UNKNOWN** | **Provider / source** | **Last verified** |
|---|---|---|---|
| File/context access |  |  |  |
| Selective retrieval |  |  |  |
| Phase-gated retrieval |  |  |  |
| Native web research |  |  |  |
| Enterprise search |  |  |  |
| Code/tool runtime |  |  |  |

## 3. Time and calendar

| **Capability** | **YES / NO / UNKNOWN** | **Provider / source** | **Last verified** |
|---|---|---|---|
| Read own calendar |  |  |  |
| Read meeting details |  |  |  |
| Find mutual availability |  |  |  |
| Create personal focus block |  |  |  |
| Create/update meeting invitation |  |  |  |

## 4. Tasks and collaboration

| **Capability** | **YES / NO / UNKNOWN** | **Provider / source** | **Last verified** |
|---|---|---|---|
| Read personal tasks |  |  |  |
| Create personal task |  |  |  |
| Create shared task |  |  |  |
| Assign shared task |  |  |  |
| Search collaboration messages |  |  |  |
| Read thread/channel |  |  |  |
| Send internal coordination message |  |  |  |

## 5. Email and knowledge

| **Capability** | **YES / NO / UNKNOWN** | **Provider / source** | **Last verified** |
|---|---|---|---|
| Search email |  |  |  |
| Read email |  |  |  |
| Create email draft |  |  |  |
| Send email |  |  |  |
| Search SharePoint/Drive/DMS |  |  |  |
| Retrieve/open document |  |  |  |

## 6. Specialist execution

| **Capability** | **YES / NO / UNKNOWN** | **Provider / source** | **Last verified** |
|---|---|---|---|
| Targeted external research |  |  |  |
| Internal/enterprise research |  |  |  |
| Specialist legal/review workflow |  |  |  |
| Approved existing tool invocation |  |  |  |

## 7. Direct-action capability rule

For execution:

```text
YES      = capability may be considered, subject to permission + current authorisation
NO       = cannot RUN
UNKNOWN  = cannot RUN
missing  = cannot RUN
```

Read capability does not imply write capability. `CONNECTOR` does not override a specific `NO` or `UNKNOWN`.

## 8. Run Observability — measured, not configured

Contract binding: Run Observability contract snapshot `v0.1`, as published in the Core.

The Planner measures as **SILENT** because it has neither `USER_MODE` nor `DISPLAY_DEPTH`. `plan_depth` must not be used as an observability disclosure axis.

Do **not** set `capture_level` as a user preference. The run contract determines it from actual runtime availability. Without runtime, explicit Run outputs must use:

```text
capture_level: DEGRADED
missing_fields:
  - [name every missing runtime field relevant to the requested output]
```

| **Runtime fact/capability** | **YES / NO / UNKNOWN** | **Provider/source** |
|---|---|---|
| runtime run identity (`run_id`/`execution_id`) |  |  |
| technical event stream |  |  |
| source/provider usage |  |  |
| state checkpoints |  |  |
| run bundle/export route |  |  |
| audit route |  |  |

Missing runtime values remain `UNAVAILABLE`/null and are not reconstructed. No second prompt-local technical trace is created.

## 9. Persistence / disclosure / anonymization

These are independent.

| **Axis** | **Environment policy / source** |
|---|---|
| Persistence |  |
| Disclosure clearance mechanism |  |
| Anonymization/cleaning capability |  |

Anonymization does not grant disclosure permission.

## 10. Secrets

Never place API keys, passwords, refresh tokens or other credentials in this annex. Authentication belongs to the host/runtime.
