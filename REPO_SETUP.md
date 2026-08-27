# GitHub Repository Setup

Recommended initial settings for this public repository.

## Repository

- Visibility: **Public**
- Default branch: `main`
- Wiki: off unless you later need it
- Projects: optional
- Discussions: off initially unless you want a community forum
- Issues: on if you want feedback; otherwise off
- Pull requests: on if collaboration is desired

## Write access

Do not add collaborators with write access unless needed.

Public visibility does not give visitors permission to push directly to the repository.

## Protect `main`

Create a branch ruleset for `main`:

- block force pushes;
- block branch deletion;
- require pull requests before merging if additional writers are ever added;
- optionally require approval before merge;
- optionally require status checks once tests exist.

As sole owner, you can still keep the workflow lightweight.

## Actions

If GitHub Actions are added later:

- keep default token permissions read-only where possible;
- grant write permissions only to the specific job that requires them;
- never place secrets in repository files.

## Public-repository hygiene

Before the first push:

- start from a new clean repository;
- do not copy private Git history;
- grep for credentials, client names, matter IDs and internal paths;
- remove internal repository references;
- confirm that every third-party asset may be redistributed;
- check the rendered README and license notice.

## Licensing

Use CC BY 4.0 for the public textual/prompt/documentation material.

If software code is later introduced, license it separately rather than silently assuming CC BY is the software license.
