# AGENTS.md

## Project Purpose
`films.py` is a lightweight Python utility for querying, filtering, and computing IMDb rating statistics over a movie catalog.

## Architecture
- `films.py`: Core data catalog (`movies`), filtering/aggregation functions, and CLI entry point guarded by `if __name__ == "__main__":`.
- `test_films.py`: Standard-library `unittest` suite verifying filtering, averages, edge cases, and acceptance criteria.
- `README.md`: Setup, usage, and verification instructions.

## Environment & Safe Commands
- Runtime: Python 3.x (standard library only; do not add external dependencies).
- Run CLI output: `python films.py`
- Run test suite: `python -m unittest discover -v`
- Check syntax/bytecode compilation: `python -m py_compile films.py test_films.py`

## Coding Conventions
- Keep functions pure: return values (`bool`, `list[dict]`, `float | None`) instead of calling `print()` inside business logic.
- Guard all CLI execution behind `if __name__ == "__main__":` so importing `films` produces no stdout side effects.
- Avoid shadowing Python built-ins (`list`, `sum`, `filter`).
- Use clear type hints and docstrings for public functions.

## Test Expectations
- Every bug fix or structural refactoring must preserve all 5 Acceptance Criteria (`AC-1` through `AC-5`).
- Any behavioral change requires corresponding unit tests in `test_films.py` passing under `python -m unittest discover -v`.

## Forbidden Actions
- **No secrets or PII:** Never commit API keys, credentials, tokens, or personal user data.
- **No production deployments:** Never push, publish, or deploy artifacts to external services or remote servers.
- **No destructive commands:** Never run `rm -rf`, `git reset --hard`, `git push --force`, or delete baseline history.
- **No unreviewed dependency changes:** Do not install third-party packages or introduce external frameworks without explicit human approval.