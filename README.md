# iFlow GitHub Actions Workflows

This repository contains GitHub Actions workflows for iFlow AI automation.

## Workflows

### iflow-pr.yml
Handles pull request automation including:
- Applying feedback from PR discussions
- Resolving review threads
- Merging PRs when ready

### iflow-docs.yml
Manages documentation synchronization:
- Automatically updates documentation based on code changes
- Maintains a 'doc' branch with latest documentation
- Creates/updates PRs from 'doc' to 'main'

### iflow-orchin.yml
Orchestrator workflow for repository maintenance and innovation:
- Runs on a schedule (weekdays at 02:00 WIB)
- Can be triggered manually or via repository dispatch
- Manages workflows, dependencies, documentation, labels, and innovation tasks
- Has various scopes: workflows, deps, docs, labels, or innovate

## Usage

These workflows run automatically on relevant events. For manual triggering:

- `iflow-pr.yml` can be triggered with a PR number
- `iflow-docs.yml` runs on pushes to main branch
- `iflow-orchin.yml` can be triggered manually with various options (debug, dry_run, scope)

## Configuration

Workflows use the following secrets:
- `GH_TOKEN`: GitHub token for API access
- `IFLOW_API_KEY`: iFlow API key for AI operations

## Permissions

The iFlow Orchestrator requires the following permissions to function properly:
- `actions: write` for workflow management
- `contents: write` for branch/PR operations
- `issues: write` for issue management
- `pull-requests: write` for PR operations
- `security-events: write` for code scanning
- `workflows: write` for CI/CD workflow updates