#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import codecs
from setuptools import setup


def read(fname):
    file_path = os.path.join(os.path.dirname(__file__), fname)
    return codecs.open(file_path, encoding="utf-8").read()


setup(
    name="pytest-drop-dup-tests",
    author="Bruno Oliveira",
    author_email="nicoddemus@gmail.com",
    maintainer="Bruno Oliveira",
    maintainer_email="nicoddemus@gmail.com",
    license="MIT",
    url="https://github.com/nicoddemus/pytest-drop-dup-tests",
    description="A Pytest plugin to drop duplicated tests during collection",
    long_description=read("README.rst"),
    py_modules=["pytest_drop_dup_tests"],
    setup_requires="setuptools_scm",
    use_scm_version=True,
    install_requires=["pytest>=2.7"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Framework :: Pytest",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
    entry_points={"pytest11": ["drop-dup-tests = pytest_drop_dup_tests",],},
)
