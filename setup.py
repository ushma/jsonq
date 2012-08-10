#!/usr/bin/python
# -*- coding: utf-8 -*-

from setuptools import setup
import jsonq

setup(
    name='jsonq',
    version=jsonq.__version__,
    description=jsonq.__doc__.strip(),
    long_description=open('README.rst').read(),
    author=jsonq.__author__,
    author_email='ushma.bhatt.3@gmail.com',
    url='',
    packages=['jsonq'],
    entry_points={
        'console_scripts': [
            'jsonq = jsonq.__main__:main',
        ],
    },
    license=open('LICENSE').read(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Utilities'
    ]
)


