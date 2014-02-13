
all:

register:
	python setup.py sdist register

upload:
	python setup.py sdist upload
