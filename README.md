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

## Usage

These workflows run automatically on relevant events. For manual triggering:

- `iflow-pr.yml` can be triggered with a PR number
- `iflow-docs.yml` runs on pushes to main branch

## Configuration

Workflows use the following secrets:
- `GH_TOKEN`: GitHub token for API access
- `IFLOW_API_KEY`: iFlow API key for AI operations