# Python Calculator

A calculator that adds, subtracts, multiplies, and divides two numbers.
Division by zero raises ValueError.

## Project initialization

This project was initialized with:

```bash
uv init --name calculator
```

Notebook support was added with:

```bash
uv add --dev ipykernel
```

These steps are already complete.

## Setup after downloading

Install uv, then open a terminal in the project folder and run:

```bash
uv sync
```

In VS Code, install the Python and Jupyter extensions.
Open the class notebook and select this project's `.venv` as its kernel.

## Project files

- pyproject.toml: project settings and dependencies.
- .python-version: project's Python version.
- uv.lock: recorded dependency versions.
- src/calculator/calculator.py: the four calculator functions.
- src/calculator/__init__.py: exposes the functions and contains the starter entry point.
- Class notebook (.ipynb): predictions, tests, results, and reflections.
- .gitignore: excludes the environment and generated cache files from Git.

## Using the calculator

In the notebook, run:

```python
from src.calculator import add

print(add(2, 3))
```

Expected output: 5.

## Running the tests

Restart the notebook kernel, then click Run All.

The TODO 3 cell checks normal calculations, negative numbers,
decimals, zero, and division by zero.

Expected final output:

```text
Division by zero correctly rejected.
All assertions passed.
```

## Design choice

Division by zero raises ValueError so an invalid calculation
cannot produce a misleading result.

## Separate test file

Run this command from the project folder:

```bash
uv run python -m tests.test_calculator
```

Expected output:

```text
Division by zero correctly rejected.
All assertions passed.
```
