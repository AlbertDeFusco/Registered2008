from setuptools import find_packages, setup
from version import find_version

setup(
    name = 'registered2008',
    version = find_version('registered2008', '__init__.py'),
    packages = find_packages()
)
