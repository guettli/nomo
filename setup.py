#!/usr/bin/env python

from distutils.core import setup

setup(name='nomo',
      version='1.0',
      description='nomo: No more coding for simple database applications',
      author='Thomas Güttler',
      author_email='guettli.nomo@thomas-guettler.de',
      url='https://github.com/guettli/nomo/',
      packages=['nomo'],
      install_requires=[
            'Django>=3.1.2',
            'psycopg2',
      ],
      )
