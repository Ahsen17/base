# Makefile for Python backend project

# Default target
.PHONY: all
all: help

# Variables
PROJECT_NAME := base
VENV := .venv
PYTHON := $(VENV)/bin/python
UV := uv
RUFF := $(VENV)/bin/ruff

# Setup virtual environment
.PHONY: venv
venv:
	$(UV) venv

# Install dependencies
.PHONY: install
install: clean venv
	$(UV) sync --all-packages

# Run tests
.PHONY: test
test:
	$(PYTHON) -m pytest

# Run database migrations (if applicable)
.PHONY: migrate
migrate:
	$(PYTHON) -m alembic upgrade head

# Generate new migration files (if applicable)
.PHONY: makemigrations
makemigrations:
	$(PYTHON) -m alembic revision --autogenerate -m "$(m)"

# Clean build artifacts
.PHONY: clean
clean:
	rm -rf $(VENV)
	rm -rf .ruff_cache
	find . -type d -name "__pycache__" -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete

# Lint code
.PHONY: lint
lint:
	$(RUFF) check --fix

# Help message
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install     - Install dependencies"
	@echo "  test        - Run tests"
	@echo "  migrate     - Run database migrations"
	@echo "  makemigrations - Generate new migration files"
	@echo "  clean       - Clean build artifacts"
	@echo "  lint        - Lint code"
	@echo "  help        - Show this help message"
