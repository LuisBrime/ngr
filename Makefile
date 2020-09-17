SHELL := bash
PATH := ./venv/bin:${PATH}
PYTHON = python3.8
PROJECT = ngr
isort = isort $(PROJECT) tests
black = black -S -l 79 --target-version py38 $(PROJECT) $(PROJECT)/api/* tests


.PHONY: all
all: test

venv:
		$(PYTHON) -m venv --prompt $(PROJECT) venv
		pip install -qU pip

.PHONY: install
install:
		pip install -qU -r requirements.txt

.PHONY: install-dev
install-dev: install
		pip install -qU -r requirements-dev.txt
	
.PHONY: test
test: clean install-dev lint
		pytest

.PHONY: format
format:
		$(isort)
		$(black)

.PHONY: lint
lint:
		flake8 $(PROJECT) tests
		$(isort) --check-only
		$(black) --check

.PHONY: clean
clean:
		rm -rf `find . -name __pycache__`
		rm -rf `find . -type f -name '*.py[co]' `
		rm -rf `find . -type f -name '*~' `
		rm -rf `find . -type f -name '.*~' `
		rm -rf .cache
		rm -rf .pytest_cache
		rm -rf build
		rm -rf dist
