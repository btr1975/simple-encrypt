# Makefile for project needs
# Author: Ben Trachtenberg
# Version: 1.0.4
#

.PHONY: info app-run coverage pylint pytest pdf gh-pages build

info:
	@echo "make options"
	@echo "    build     To build a distribution"
	@echo "    coverage  To run coverage and display ASCII and output to htmlcov"
	@echo "    pylint    To run pylint"
	@echo "    pytest    To run pytest with verbose option"
	@echo "    pdf       To create PDF Docs"


build:
	@python -m build

coverage:
	@pytest --cov --cov-report=html -vvv

pylint:
	@pylint simple_encrypt/

pytest:
	@pytest --cov -vvv

pdf:
	@sphinx-build -b rinoh ./docs ./docs/_build/pdf


