# Innovation Policies

## Goals
- Encourage experimentation with new CI/CD strategies
- Create reusable components for common tasks
- Automate benchmarking and performance monitoring
- Continuously improve the repository's infrastructure

## Strategies
1. Create experimental workflows prefixed with `exp-` to trial new strategies
2. Wire experimental workflows via `workflow_call` for reusability
3. Create composite actions for common steps to reduce duplication
4. Implement auto-benchmarking for CI time to track improvements
5. Persist learnings in memory and policies files

## Implementation
- New experimental workflows should be created in `.github/workflows/`
- Composite actions should be created in `.github/actions/`
- Performance metrics should be collected and analyzed regularly
- Successful experiments should be integrated into production workflows