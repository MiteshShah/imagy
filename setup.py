# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import imagy

deps = ['watchdog','path.py']

setup(
    name='imagy',
    version=imagy.__version__,
    description='A daemon to automatically handle image optimization',
    author='Dominik Dabrowski',
    author_email='dominik@silberrock.com',
    url='https://github.com/doda/imagy',
    license=open('LICENSE').read(),
    long_description=open('README.rst').read(),
    packages=find_packages(),
    package_data={'': ['README.rst','LICENSE']},
    install_requires=deps,
    entry_points={
        "console_scripts": ['imagy=imagy.cl:main']
        },
)

