# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import os

version = '0.0.1'

setup(
    name='bugsystem',
    version=version,
    description='Bug Tracking System',
    author='Nishta',
    author_email='anandh.nishta@gmail.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=("frappe",),
)
