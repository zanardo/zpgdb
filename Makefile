PYTHON=python3

.PHONY: all
all: .venv

.venv/ok:
	$(PYTHON) -m venv .venv
	.venv/bin/pip install -U pip wheel
	touch .venv/ok

.venv: .venv/ok setup.py
	.venv/bin/pip install -e .
	touch .venv

.PHONY: clean
clean:
	@rm -rf .venv/ build/ dist/ *.egg-info/
	@find . -type f -name '*.pyc' -delete
	@find . -type d -name '__pycache__' -delete

.PHONY: test
test: .venv
	.venv/bin/python tests.py
