#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
# created_on: 2022-11-10 18:23

"""Setup."""


import os
import sys

from setuptools import find_packages, setup


__author__ = "Toran Sahu <toran.sahu@yahoo.com>"
__license__ = "Distributed under terms of the MIT license"

REPO_DIR = os.path.abspath(os.path.dirname(__file__))
ABOUT_FILE = os.path.join(REPO_DIR, "__about__.py")
REQ_FILE = os.path.join(REPO_DIR, "requirements.txt")
VERSION_FILE = os.path.join(REPO_DIR, "VERSION")
VERSION = open(VERSION_FILE).read()

# Package metadata
about = {}
with open(ABOUT_FILE, "r") as f:
    exec(f.read(), about)

# get the dependencies and installs
with open(REQ_FILE, encoding="utf-8") as f:
    requires = []
    for line in f:
        req = line.split("#", 1)[0].strip()
        if req and not req.startswith("--"):
            requires.append(req)

# get long description
with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name=about['__title__'],
    version=VERSION,
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about['__github__'],
    license=about['__license__'],
    packages=find_packages(exclude=["tests"]),
    install_requires=requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        'Topic :: Internet :: WWW/HTTP :: Indexing/Search',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Archiving :: Packaging',
        "Topic :: Text Processing",
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Natural Language :: English",
    ],
    keywords=[
        "util",
        "utils",
        "pyutil",
        "pyutils",
    ],
)


# Shorthand to publish the package `$ python setup.py publish`
if sys.argv[-2:] == ["--test", "publish"]:
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload --repository-url https://test.pypi.org/legacy/ dist/*")
    sys.exit()
elif sys.argv[-1] == "publish":
    os.system("python setup.py sdist bdist_wheel")
    os.system("twine upload dist/*")
    # os.system("twine upload --repository-url https://upload.pypi.org/legacy/ dist/*")
    sys.exit()
