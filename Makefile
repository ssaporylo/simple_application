#
# Makefile
#

export PATH:=virtualenv/bin:venv/bin:$(PATH)

.PHONY: help
help:
	@echo 'Makefile for Sanic playground'
	@echo ''
	@echo '1. Building:'
	@echo '  make setup         (re)Build your environment and setup project'
	@echo ''
	@echo '2. Testing:'
	@echo '  make test          Run tests and check code with flake8'
	@echo '  make flake         Check code with flake8'
	@echo ''
	@echo '3. Running:'
	@echo '  make run-dev       Run locally using dev server'
	@echo ''

.PHONY: setup
setup: clean
	@echo ' -- Setting up environment'
	sudo apt-get -y install python3-dev python3-pip
	sudo pip3 install virtualenv
	virtualenv -p python3.7 venv
	pip install -e .'[dev,test]'
	@echo ' -- Environment is ready'

.PHONY: clean clean-config
clean: clean-files clean-config

clean-files:
	@rm -rf venv/
	@rm -rf *.egg-info

.PHONY: flake
flake:
	flake8 --exclude=".svn,CVS,.bzr,.hg,.git,__pycache__,.tox,.eggs,*.egg,venv,tests" --ignore=E501

.PHONY: test
test: flake
	py.test tests

.PHONY: coverage
coverage: flake
	coverage run venv/bin/py.test -v --ignore=venv --ignore=/usr tests/
	coverage report --omit=venv/*,/usr/*

.PHONY: run-dev
run-dev:
	python manage.py runserver
