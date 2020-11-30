# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in equipment_rental/__init__.py
from equipment_rental import __version__ as version

setup(
	name='equipment_rental',
	version=version,
	description='Equipment Rental program',
	author='John',
	author_email='yuntan0@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
