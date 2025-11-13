# CI Optimization Policies

## Workflow Standards

### Permissions Model
All workflows must use least-privilege permissions:
- `actions: read` for inspection-only workflows
- `contents: write` only when creating branches/commits
- `pull-requests: write` only when modifying PRs
- `issues: write` only when creating/modifying issues

### Caching Strategy
- All workflows with build steps must implement caching
- Cache keys must be based on lockfile hashes
- Cache restore should fail gracefully

### Reusable Components
- Common setup steps must be extracted to reusable workflows
- Composite actions should encapsulate complex logic
- Workflows should use `workflow_call` for modularity

## Performance Benchmarks

### Target Metrics
- Average workflow runtime: < 10 minutes
- Cache hit rate: > 80%
- Parallelization efficiency: > 70%

### Monitoring
- Baseline CI performance captured before changes
- After each optimization, capture new baseline
- Report performance impact in PR descriptions