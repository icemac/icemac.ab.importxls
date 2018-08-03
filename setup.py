# -*- coding: utf-8 -*-
import os.path
import setuptools


def read(*path_elements):
    """Read a file."""
    with open(os.path.join(*path_elements)) as f:
        return f.read()

version = '2.4'
name = 'icemac.ab.importxls'

setuptools.setup(
    name=name,
    version=version,
    description="Import XLS files into icemac.addressbook.",
    long_description="\n\n".join([
        read('README.rst'),
        read('CHANGES.rst')
    ]),
    keywords='icemac.addressbook xls excel import',
    author='Michael Howitz',
    author_email='icemac@gmx.net',
    url='https://pypi.org/project/%s' % name,
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Zope3',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
    ],
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    namespace_packages=['icemac', 'icemac.ab'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'icemac.ab.importer >= 1.0',
        'setuptools',
        'xlrd',
    ],
    extras_require=dict(
        test=['zope.testing >= 3.8.0',
              ]),
)
