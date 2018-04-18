PYTHON_VERSION=python3

clean:
	pip uninstall -y algorithms || true
	rm -rf .venv

validate:
	virtualenv -p ${PYTHON_VERSION} .venv
	. .venv/bin/activate
	pip install -r requirements.txt

compile:
	pip install .

test:
	python setup.py test

.PHONY: clean validate compile test package deploy