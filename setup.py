#!/usr/bin/env python

import os
import sys
from setuptools import setup

os.system('make rst')
try:
    readme = open('README.rst').read()
except FileNotFoundError:
    # fallback when installing from source package
    readme = ''

setup(
    name='kodetest',
    version=open(os.path.join('kodetest', 'VERSION')).read().strip(),
    description='Tilhørende tester for programmeringsoppgavene på kodeklubben.github.io',
    long_description=readme,
    author='Arve Seljebu',
    author_email='arve.seljebu@gmail.com',
    url='https://github.com/arve0/kodetest',
    packages=[
        'kodetest',
    ],
    package_dir={'kodetest': 'kodetest'},
    package_data={'kodetest': ['VERSION']},
    include_package_data=True,
    install_requires=[
    ],
    license='MIT',
    zip_safe=False,
    keywords='kodetest',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
)
