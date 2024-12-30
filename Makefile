.PHONY: install test test-coverage lint selfcheck check build

# Install dependencies
install:
	poetry install

# Run tests
test:
	poetry run pytest

# Run tests with coverage report
test-coverage:
	poetry run pytest --cov=gendiff --cov-report=xml:coverage.xml

# Run linter
lint:
	poetry run flake8 gendiff

# Perform self-checks
selfcheck:
	poetry check

# Perform all checks: selfcheck, tests, and lint
check: selfcheck test lint

# Build the package after passing all checks
build: check
	poetry build