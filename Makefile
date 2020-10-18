build:
	python setup.py sdist bdist_wheel

upload: build
	twine upload dist/*
