#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
setup stdgif.

Copyright (c) 2016 Tyler Cipriani <tyler@tylercipriani.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from setuptools import setup, find_packages

setup(name='stdgif',
      version='0.1.0',
      description='Display gifs it the terminal with ANSI-escape sequences',
      author='Tyler Cipriani',
      author_email='tyler@tylercipriani.com',
      license='GNU GPLv3',
      url='https://github.com/thcipriani/stdgif',
      packages=find_packages(),
      install_requires=[line.strip() for line in open('requirements.txt')],
      classifiers=[('License :: OSI Approved :: '
                    'GNU General Public License v3 (GPLv3)'),
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python',
                   'Programming Language :: Python :: 2',
                   'Programming Language :: Python :: 2.7'],
      keywords='gif ansi ascii',
      entry_points={
          'console_scripts': [
              'stdgif=stdgif.stdgif:main'
          ]
      })
