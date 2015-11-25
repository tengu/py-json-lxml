
all:

register:
	python setup.py sdist register

upload:
	python setup.py sdist upload

test_% :
	python test.py Test.$@


install:
	sudo install -m0644 json_lxml.py /usr/local/lib/python2.7/dist-packages/
