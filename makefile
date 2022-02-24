test:
	pipenv run pytest
mypy:
	pipenv run mypy
lint:
    pipenv run flake8
check:test lint mypy
