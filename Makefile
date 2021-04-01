all: help

help:
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "ℹ️ Available commands ℹ️"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"
	@echo "⭐️ update-requirements : Runs the pip-compile (from pip-tools) to fix the version of each dependency"
	@echo "⭐️ clean               : Remove all cache and test related files"
	@echo "⭐️ install             : Use the pip to install all dependencies"
	@echo "―――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――"

clean:
	@rm -f ./.coverage
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

update-requirements:
	@pip-compile requirements.txt

install:
	@pip install -r requirements.txt