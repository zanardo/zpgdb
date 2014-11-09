.PHONY: all clean test clean-setuptools

all: venv

venv: .venv/bin/activate

.venv/bin/activate: requirements.txt
	test -d .venv || virtualenv-2.7 --no-site-packages --distribute .venv
	. .venv/bin/activate; pip install -r requirements.txt
	touch .venv/bin/activate

clean-setuptools:
	rm -rf dist zpgdb.egg-info build

clean: clean-setuptools
	rm -rf *.pyc .venv

test: venv
	.venv/bin/python tests.py
