test:
	pipenv run pytest
mypy:
	pipenv run mypy
check:test mypy
