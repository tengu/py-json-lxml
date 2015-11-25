from setuptools import setup
    
setup(
    name = "json-lxml",
    py_modules = ["json_lxml"],
    scripts = ["json_lxml.py"],
    version = "0.1.4",
    license = "LGPL",
    platforms = ['POSIX', 'Windows'],
    install_requires=["lxml"],
    description = "Convert JSON to lxml.etree so that xpath can be applied.",
    author = "karasuyamatengu",
    author_email = "karasuyamatengu@gmail.com",
    url = "https://github.com/tengu/py-json-lxml",
    keywords = ["json", "xpath", "lxml"],
    classifiers = [
        "License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
        "Operating System :: POSIX :: Linux", # debian, to be specific
        "Programming Language :: Python",
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Topic :: Utilities",
        ],
    #long_description = """"""
    )
