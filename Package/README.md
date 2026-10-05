# numimath

[![PyPI Version](https://img.shields.io/badge/version-0.1.0-blue.svg)](https://test.pypi.org/project/numimath/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**`numimath`** is a lightweight, zero-dependency Python library providing basic arithmetic and descriptive statistics helper functions. Built with strict typing and clear error handling for modern Python applications.

---

## Features

- **Arithmetic Helpers**: `add`, `subtract`, `multiply`, `divide` with zero-division protection.
- **Statistical Helpers**: `mean`, `median`, `range_span` with empty sequence validation.
- **Utility Helpers**: `percentage` calculation.
- **Zero External Dependencies**: Pure Python implementation compatible with Python 3.8+.
- **Fully Typed**: Includes comprehensive type hints for IDE autocompletion and static type checkers (`mypy`).

---

## Installation

You can install `numimath` from **TestPyPI** using `pip`:

```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple/ numimath
```

---

## Quickstart & Usage Examples

```python
from numimath import add, divide, mean, median, percentage, range_span

# Basic Arithmetic
print(add(15, 27))          # Output: 42.0
print(divide(100, 4))       # Output: 25.0

# Statistical Analysis
dataset = [12.5, 45.0, 22.1, 89.4, 33.0]

print(mean(dataset))        # Output: 40.4
print(median(dataset))      # Output: 33.0
print(range_span(dataset))  # Output: 76.9

# Percentage Calculation
print(percentage(45, 200))  # Output: 22.5 (%)
```

---

## API Overview

| Function | Signature | Description | Exceptions |
| :--- | :--- | :--- | :--- |
| `add` | `(a: float, b: float) -> float` | Returns `a + b` | None |
| `subtract` | `(a: float, b: float) -> float` | Returns `a - b` | None |
| `multiply` | `(a: float, b: float) -> float` | Returns `a * b` | None |
| `divide` | `(a: float, b: float) -> float` | Returns `a / b` | `ZeroDivisionError` if `b == 0` |
| `mean` | `(numbers: Sequence[float]) -> float` | Returns arithmetic average | `ValueError` if empty |
| `median` | `(numbers: Sequence[float]) -> float` | Returns median value | `ValueError` if empty |
| `percentage` | `(part: float, total: float) -> float` | Returns `(part / total) * 100` | `ZeroDivisionError` if `total == 0` |
| `range_span` | `(numbers: Sequence[float]) -> float` | Returns `max - min` | `ValueError` if empty |

---

## Development & Testing

To set up a local development environment:

```bash
# Clone the repository
git clone https://github.com/I-Josh-pro-grammin/numimath.git
cd numimath

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install in editable mode
pip install -e .

# Run test suite
python -m unittest discover -s tests
```

---

## Building the Package

To build the source distribution and wheel:

```bash
# Ensure build tool is installed
python -m pip install --upgrade build

# Build .tar.gz and .whl artifacts
python -m build
```

This will create a `dist/` directory containing:
- `numimath-0.1.0.tar.gz` (Source Distribution)
- `numimath-0.1.0-py3-none-any.whl` (Wheel)

---

## Publishing to TestPyPI

To upload the package artifacts to TestPyPI using Twine:

```bash
# Ensure twine is installed
python -m pip install --upgrade twine

# Check built artifacts
python -m twine check dist/*

# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*
```

When prompted:
- **Username**: `__token__`
- **Password**: Your TestPyPI API token (`pypi-...`)

---

## License

This project is licensed under the [MIT License](LICENSE).
