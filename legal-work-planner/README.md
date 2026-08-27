# Legal Work Planner

The Legal Work Planner is a prompt-first planning method for professional legal work.

Its central rule is:

> Think first. Look at what is available second. Route third. Act fourth only where a bounded direct action is useful, capability-resolved and authorised.

## Public-release scope

This directory is intended to hold publishable Planner releases such as:

- user guide;
- installation guide;
- public configuration templates;
- standalone operative prompts;
- public testing and pilot material.

The public edition is standalone and does not require non-public companion materials.

## Release layout

Markdown is the canonical public source. Each release is a directory under
`releases/`, readable directly on GitHub.

```text
legal-work-planner/
├── README.md
└── releases/
    └── YYYY-MM-DD/
        ├── README.md                          release metadata and index
        ├── README_LEGAL_WORK_PLANNER.md       bundle overview
        ├── USER_GUIDE_LEGAL_WORK_PLANNER.md   working manual
        ├── 01_INSTALLATION/
        ├── 02_PROMPTS/
        └── 03_TESTING/
```

A release should state:

- release date;
- status;
- license;
- field-validation status;
- known limitations;
- the canonical installation source;
- any optional generated formats.

## Source-of-truth rule

Markdown in the release directory is the canonical installation source.

Other formats — Word, PDF — may later be attached to a GitHub Release as
generated assets. They are build outputs. They are not maintained as a
parallel source of truth, and where a generated asset disagrees with the
release directory, the release directory is correct.

## Releases

### 2026-08-27 — first public edition

Location: [`releases/2026-08-27/`](releases/2026-08-27/)

| | |
|---|---|
| Release date | 2026-08-27 |
| Status | Working public edition. Not a maturity claim. |
| License | CC BY 4.0, per the repository [`LICENSE.md`](../LICENSE.md) |
| Field validation | **Not field validated.** Pilots remain required. |
| Language | English |
| Canonical installation source | Markdown |
| Optional generated formats | None published |
| Run Observability contract | Snapshot `v0.1`, SILENT |

Twelve documents: a bundle overview, a working manual, six installation
documents including the four `ANL_` annexes, the three `PRT_` prompts, and the
test and pilot specification. See
[`releases/2026-08-27/README.md`](releases/2026-08-27/README.md) for the
release index, installation sources and known limitations.

The public edition is standalone: no specialist suite component is required in
order to plan, and specialist components attach only as optional adapters.
