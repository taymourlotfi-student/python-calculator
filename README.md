# Python Calculator

A calculator with four operations: add, subtract, multiply, and divide.

## Setup

Open a terminal in the project folder and run:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install ipykernel
```

Open the class notebook in VS Code and select `.venv` as its kernel.
VS Code needs the Python and Jupyter extensions to run the notebook.

## Usage

The functions are in `src/calculator.py`.

Example:

```python
from src.calculator import add

print(add(2, 3))
```

Expected output: `5`.

## Tests

Run the TODO 3 cell in the class notebook.
It checks normal calculations, negative numbers, decimals, zero,
and division by zero.

Division by zero must raise a ValueError.
