# -*- coding: utf-8 -*-

from setuptools import setup

from zpgdb import __VERSION__

setup(
    name = "zpgdb",
    version = __VERSION__,
    py_modules = ['zpgdb'],
    install_requires = ['psycopg2==2.5.5'],
    package_data = {
        '': ['README.md', 'COPYING']
    },
    author = 'Antonio Zanardo',
    author_email = 'zanardo@gmail.com',
    description = 'Library for simple PostgreSQL connection and transaction management',
    license = 'BSD',
    keywords = 'postgresql database transaction connection',
    url = 'https://github.com/zanardo/zpgdb',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Database',
    ],
)
