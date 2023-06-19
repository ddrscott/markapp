.PHONY: dist

test:
	poetry run pytest

dist: test
	python setup.py sdist bdist_wheel

publish: dist
	twine upload dist/*
