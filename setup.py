#!/usr/bin/env python
from setuptools import setup, find_packages

setup(name='shares_count',
      version='1.0',
      author='vlinhart',
      author_email='vladimir.linhart@gmail.com',
      packages=find_packages(),
      include_package_data=True,
      install_requires=['socialshares~=1.0.0'],
      scripts=[],
      dependency_links=[],
      setup_requires=('setuptools',),
      tests_require=[],
      zip_safe=False,
)
