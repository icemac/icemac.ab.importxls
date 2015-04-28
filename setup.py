# -*- coding: utf-8 -*-
# Copyright (c) 2008-2014 Michael Howitz
# See also LICENSE.txt

import os.path
import setuptools

def read(*path_elements):
    return "\n\n" + file(os.path.join(*path_elements)).read()

version = '2.0'
name = 'icemac.ab.importxls'

setuptools.setup(
    name=name,
    version=version,
    description="Import XLS files into icemac.addressbook.",
    long_description=(
        read('README.rst') +
        read('CHANGES.rst')
        ),
    keywords='icemac.addressbook xls excel import',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='http://pypi.python.org/pypi/%s' % name,
    license='ZPL 2.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Paste',
        'Framework :: Zope3',
        'License :: OSI Approved',
        'License :: OSI Approved :: Zope Public License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        ],
    packages=setuptools.find_packages('src'),
    package_dir = {'': 'src'},
    namespace_packages = ['icemac', 'icemac.ab'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'icemac.ab.importer > 0.9',
        'setuptools',
        'xlrd',
        ],
    extras_require = dict(
        test=['zope.testing >= 3.8.0',
              ]),
    )
