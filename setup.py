#!/usr/bin/env python
# -*- encoding: utf-8 -*-


# http://docs.django-cms.org/en/develop/how_to/install.html
from setuptools import setup

setup(
    name='mycms',
    version='1.0',
    description='OpenShift App',
    author='Ken Cochrane',
    author_email='example@example.com',
    url='http://www.python.org/sigs/distutils-sig/',
    install_requires=['Django>=1.8',
                      'django-classy-tags>=0.6.2',
                      'django-treebeard==3.0',
                      'django-sekizai>=0.82',
                      'djangocms-admin-style',
                      'html5lib>=0.9999999',
                      'PIL==1.1.7',
                      'django-cms==3.2',
                      'south>=1.0.2',
                      'MySQL-python>=1.2.5'
                      ],
)
