# iFlow GitHub Actions Workflows

This repository contains GitHub Actions workflows for iFlow AI automation.

## Workflows

### iflow-issue.yml
Handles issue automation including:
- Automatically solving issues when opened
- Creating pull requests with solutions
- Using iFlow CLI for code analysis and implementation

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

<<<<<<< HEAD
### iflow-maintenance.yml
Repository maintenance workflow:
- Runs on a schedule (every weekday at 2:00 AM UTC)
- Performs dependency updates and security audits
- Applies only non-breaking patch-level updates

### iflow-intelijen.yml
Repository intelligence gathering workflow:
- Runs on a schedule (every Monday at 3:00 AM UTC)
- Gathers data about issues, PRs, and workflow runs
- Creates new issues based on analysis

### gemini-researcher.yml
Automated research workflow for finding free VPS offers:
- Runs on a schedule (weekly on Mondays at 03:00 UTC)
- Can be triggered manually via workflow dispatch
- Uses Google Gemini API to research and compile a list of free VPS providers
- Automatically updates the `free-vps.md` file with current offers
- Includes reliability scoring for each provider

## Documentation

For detailed information about each workflow, see [CI/CD Workflows Documentation](docs/cicd-workflows.md).

=======
>>>>>>> d640226734c64a30066e8e35e6ebec769157a5c2
## Usage

These workflows run automatically on relevant events. For manual triggering:

- `iflow-issue.yml` can be triggered by opening an issue or commenting with `/solve`
- `iflow-pr.yml` can be triggered with a PR number
- `iflow-docs.yml` runs on pushes to main branch
- `iflow-orchin.yml` can be triggered manually with various options (debug, dry_run, scope)

## Configuration

Workflows use the following secrets:
- `GH_TOKEN`: GitHub token for API access
- `IFLOW_API_KEY`: iFlow API key for AI operations
# Free VPS Research

This repository automatically researches and updates a list of free VPS offers using Google Gemini.

## How It Works

1. A GitHub Actions workflow runs weekly to search for free VPS offers.
2. The search results are written to [`free-vps.md`](free-vps.md).
3. The file is automatically committed and pushed if there are changes.

## Contributing

If you'd like to contribute to this project, please submit a pull request with your changes. You can help improve the workflow, add new features, or fix issues. Check the project's issue tracker for ideas on how to contribute.