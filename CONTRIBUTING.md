# Contributing to Statio

Thank you for your interest in contributing to Statio.

Statio is being built with a focus on simple APIs, correct statistical implementations, and clean documentation.

## Development Workflow

1. Fork or clone the repository.
2. Create a feature branch.
3. Write or update tests.
4. Ensure all tests pass using:

```bash
pytest
```

5. Commit with a clear message.
6. Open a Pull Request.

## Coding Principles

- Keep implementations readable.
- Prefer pure Python for core statistical functions.
- Handle edge cases explicitly.
- Add automated tests for every new feature.
- Update documentation when functionality changes.

## Project Structure

- `statio/` — Library source code
- `tests/` — Automated tests
- `docs/` — Documentation
- `README.md` — Project overview

Every statistical function should be implemented together with its corresponding tests before merging.