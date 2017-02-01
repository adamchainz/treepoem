#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
from setuptools import find_packages, setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `__init__.py`.
    """
    init_py = open(os.path.join(package, '__init__.py')).read()
    return re.search("__version__ = ['\"]([^'\"]+)['\"]", init_py).group(1)


version = get_version('treepoem')


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    'Pillow',
]

setup(
    name='treepoem',
    version=version,
    description="Barcode rendering for Python 2 and 3 supporting QRcode, "
                "Aztec, PDF417, I25, Code128, Code39 and many more types.",
    long_description=readme + '\n\n' + history,
    author="Christian Muirhead",
    author_email='xtian@babbageclunk.com',
    maintainer="Julius Seporaitis",
    maintainer_email="julius@yplanapp.com",
    url='https://github.com/YPlan/treepoem',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_dir={
        'treepoem': 'treepoem',
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT",
    zip_safe=False,
    keywords='barcode bwipp postscript ghostscript qr qrcode aztec azteccode pdf417 interleaved2of5 i25 code128 code39',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
