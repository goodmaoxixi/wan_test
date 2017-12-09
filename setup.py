# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='WAN Test',
    version='0.0.1',
    description='A WAN test suite',
    long_description=readme,
    author='Guanglin Du; Jia Li',
    author_email='guanglin.du@gmail.com; goodmaoxixi@gmail.com',
    url='https://github.com/goodmaoxixi/wan_test',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite="tests"
)
