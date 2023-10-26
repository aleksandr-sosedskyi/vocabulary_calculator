.PHONY: install check format

RUN := poetry run
SCRIPT_MODULE := script

ALL_MODULES := $(SCRIPT_MODULE)

# Setup project
install:
	poetry install
	$(RUN) python -m spacy download en_core_web_sm
	$(RUN) pre-commit install

# Run CI checks
ci: format test check  

# Run all static checks
check:
	poetry check
	$(RUN) mypy $(ALL_MODULES)
	$(RUN) flake8 $(ALL_MODULES)
	$(RUN) black --diff --check $(ALL_MODULES)
	$(RUN) isort --check $(ALL_MODULES)

# Format code
format:
	$(RUN) black $(ALL_MODULES)
	$(RUN) isort $(ALL_MODULES)

# Run tests
test:
	$(RUN) pytest
