# Use Bash shell in Make instead of the default sh
SHELL := /bin/bash

.PHONY: install-poetry install-precommit all

install: install-poetry install-precommit

# Install Poetry
install-poetry: check-poetry
	@echo "Poetry is already installed."
	@command -v poetry > /dev/null 2>&1 || (echo "Installing Poetry..." && curl -sSL https://install.python-poetry.org | python3 -)

# Install pre-commit hooks
install-precommit: check-poetry
	@echo "Installing pre-commit hooks..."
	@poetry run pre-commit install

# Help command to display commands
help:
	@echo "Available commands:"
	@echo "  install-poetry    Install Poetry if it's not installed"
	@echo "  install-precommit Install pre-commit hooks using Poetry"
	@echo "  install               Run all setups (Poetry & pre-commit)"
