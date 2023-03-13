#!/usr/bin/env python3
'''Use this to install module'''
from os import path
from setuptools import setup, find_namespace_packages

version = '1.0.0'
this_dir = path.abspath(path.dirname(__file__))
with open(path.join(this_dir, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fod-net',
    version=version,
    description='FOD-Net module.',
    author='Rui Zeng',
    author_email='chenyu.wang@sydney.edu.au',
    python_requires='>=3.6',
    license='MIT License',
    install_requires=['easydict'],
    packages=find_namespace_packages(),
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: Unix',
        'Operating System :: MacOS',
        'Operating System :: Microsoft :: Windows :: Windows 10',
    ],
)
