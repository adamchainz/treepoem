import os
import re

from setuptools import find_packages, setup


def get_version(filename):
    with open(filename, 'r') as fp:
        contents = fp.read()
    return re.search(r"__version__ = ['\"]([^'\"]+)['\"]", contents).group(1)


version = get_version(os.path.join('treepoem', '__init__.py'))

with open('README.rst', 'r') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst', 'r') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

setup(
    name='treepoem',
    version=version,
    description="Barcode rendering for Python 2 and 3 supporting QRcode, "
                "Aztec, PDF417, I25, Code128, Code39 and many more types.",
    long_description=readme + '\n\n' + history,
    author="Christian Muirhead",
    author_email='xtian@babbageclunk.com',
    maintainer="Adam Johnson",
    maintainer_email='me@adamj.eu',
    url='https://github.com/adamchainz/treepoem',
    packages=find_packages(exclude=['tests', 'tests.*']),
    package_dir={
        'treepoem': 'treepoem',
    },
    entry_points={'console_scripts': ['treepoem=treepoem.__main__:main']},
    include_package_data=True,
    install_requires=[
        'Pillow',
    ],
    python_requires='>=3.5',
    license="MIT",
    zip_safe=False,
    keywords='barcode bwipp postscript ghostscript qr qrcode aztec azteccode pdf417 interleaved2of5 i25 code128 code39',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
