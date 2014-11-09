all: venv

venv: .venv/bin/activate

.venv/bin/activate: requirements.txt
	test -d .venv || virtualenv-2.7 --no-site-packages --distribute .venv
	. .venv/bin/activate; pip install -r requirements.txt
	touch .venv/bin/activate

clean:
	rm -f *.pyc
	rm -rf .venv

test: venv
	.venv/bin/python tests.py
