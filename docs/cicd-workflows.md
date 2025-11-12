# Documentation for CI/CD Workflows

This document provides an overview of the CI/CD workflows used in this repository.

## iFlow - Solve Issue (`iflow-issue.yml`)

This workflow is triggered when a new issue is opened or when a comment containing `/solve` is added to an issue. It uses the iFlow CLI to automatically solve the issue and create a pull request.

## iFlow - Update Documentation (`iflow-docs.yml`)

This workflow runs on every push to the `main` branch. It updates the documentation on the `doc` branch and creates a pull request to merge the changes into `main`.

## iFlow - Apply PR Changes (`iflow-pr.yml`)

This workflow is triggered when a pull request review comment is created or when manually triggered. It applies the changes suggested in the pull request comments.

## iFlow - Repository Maintenance (`iflow-maintenance.yml`)

This workflow runs on a schedule (every weekday at 2:00 AM UTC). It performs repository maintenance tasks such as dependency updates and security audits.

## iFlow Intelijen (`iflow-intelijen.yml`)

This workflow runs on a schedule (every Monday at 3:00 AM UTC) and gathers intelligence about the repository, such as open issues and pull request history. It then creates new issues based on this analysis.

## iFlow - Orchestrator+ (Innovate) (`iflow-orchin.yml`)

This is the main orchestrator workflow that runs on a schedule (weekdays at 02:00 WIB) and can be triggered manually or via repository dispatch. It manages workflows, dependencies, documentation, labels, and innovation tasks, with various scopes available.

## Free VPS Research (`gemini-researcher.yml`)

This workflow runs on a schedule (every Monday at 3:00 AM UTC) and researches free VPS offers, updating the `free-vps.md` file.