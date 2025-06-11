# pydanpak

[![codecov](https://codecov.io/gh/bestdan/pydanpak/graph/badge.svg?token=WWMT6WUQGS)](https://codecov.io/gh/bestdan/pydanpak)

A Python package for financial analysis, featuring date-indexed cashflow management.

## Installation

```bash
pip install pydanpak
```

## Development

This project uses UV for dependency management and development tools:

```bash
# Install development dependencies
uv pip install -e ".[dev]"

# Run tests
pytest

# Format code
black pydanpak tests examples
isort pydanpak tests examples
```

## Features

- Date-indexed cashflow management
- Type-safe with Pydantic
- Comprehensive test coverage
