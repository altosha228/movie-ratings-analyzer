# Movie Ratings Analyzer

A lightweight Python utility for querying, filtering, and computing IMDb rating statistics over a structured movie catalog.

## Requirements & Setup
- **Runtime:** Python 3.12+ (tested on `Python 3.12.11`)
- **Dependencies:** Python standard library only (`typing`, `unittest`). No external packages or virtual environment setup required.

## Repository Structure
- `films.py` — Core movie dataset (`movies`), Strategy-based filtering predicates, rating aggregation functions, and CLI entry point.
- `test_films.py` — Unit test suite built with standard-library `unittest`.
- `AGENTS.md` — Coding conventions, safe commands, and operating boundaries for AI coding assistants.
- `README.md` — Project overview, setup, and verification commands.

## Usage & Verification Commands

Run the default CLI output:
```bash
python films.py