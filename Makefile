PYTHON=python3

all: .venv

.venv: setup.py
	@test -d .venv || virtualenv -p $(PYTHON) .venv
	@.venv/bin/pip install -e .
	@touch .venv

clean:
	@rm -rf .venv/ build/ dist/ *.egg-info/
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

test: .venv
	.venv/bin/python tests.py

.PHONY: all clean test
