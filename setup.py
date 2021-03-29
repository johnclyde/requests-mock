#!/usr/bin/env python

from setuptools import setup

setup(
    package_data={"requests_mock": ["py.typed"]},
    setup_requires=['pbr'],
    pbr=True,
)
