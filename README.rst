========
Treepoem
========

.. image:: https://img.shields.io/github/workflow/status/adamchainz/treepoem/CI/master?style=for-the-badge
   :target: https://github.com/adamchainz/treepoem/actions?workflow=CI

.. image:: https://img.shields.io/pypi/v/treepoem.svg?style=for-the-badge
   :target: https://pypi.org/project/treepoem/

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg?style=for-the-badge
   :target: https://github.com/psf/black

.. image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white&style=for-the-badge
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit

A cleverly named, but very simple python barcode renderer wrapping the
BWIPP_ library and ``ghostscript`` command line tool.

Installation
============

Install from **pip**:

.. code-block:: sh

    python -m pip install treepoem

Python 3.5 to 3.9 supported.

You'll also need Ghostscript installed. On Ubuntu/Debian this can be installed
with:

.. code-block:: sh

    apt-get install ghostscript

On Mac OS X use:

.. code-block:: sh

    brew install ghostscript

Otherwise refer to your distribution's package manager, though it's likely to
be called ``ghostscript`` too.

There's a known issue with rendering on Ghostscript 9.22+ where images are
smeared. See
`GitHub Issue #124 <https://github.com/adamchainz/treepoem/issues/124>`_ and
its associated links for more details. Ghostscript merged a fix in version
9.26 and common barcodes seem to work from then on, though still with some
smearing.

You can check your Ghostscript version with:

.. code-block:: sh

    gs --version

----

**Working on a Django project?**
Check out my book `Speed Up Your Django Tests <https://gumroad.com/l/suydt>`__ which covers loads of best practices so you can write faster, more accurate tests.

----

API
===

``generate_barcode(barcode_type, data, options=None)``
------------------------------------------------------

Generates a barcode and returns it as a PIL image file object (specifically, a
``PIL.EpsImagePlugin.EpsImageFile``).

``barcode_type`` is the name of the barcode type to generate (see below).

``data`` is a ``str`` (Python 2 ``unicode``) or ``bytes`` (Python 2 ``bytes``)
of data to embed in the barcode - the amount that can be embedded varies by
type.

``options`` is a dictionary of strings-to-strings of extra options to be passed
to BWIPP_, as per its docs.

For example, this generates a QR code image, and saves it to a file using
standard PIL ``Image.save()``:

.. code-block:: python

   >>> import treepoem
   >>> image = treepoem.generate_barcode(
   ...     barcode_type='qrcode',  # One of the BWIPP supported codes.
   ...     data='barcode payload',
   ... )
   >>> image.convert('1').save('barcode.png')

If your barcode image is monochrome, with no additional text or
coloring, converting the ``Image`` object to monochrome as shown above
(``image.convert('1')``) will likely reduce its file size.

``barcode_types``
-----------------

This is a ``dict`` of the ~100 names of the barcode types that the vendored
version of BWIPP_ supports: its keys are ``str``\s of the barcode type encoder
names, and the values are instances of ``BarcodeType``.

``BarcodeType``
---------------

A class representing meta information on the types. It has two attributes:

* ``type_code`` - the value needed for the ``barcode_type`` argument of
  ``generate_barcode()`` to use this type.

* ``description`` - the human level description of the type
  which has two ``str``.

Only these common types are used in the test suite:

* ``qrcode`` - `QR Code`_

* ``azteccode`` - `Aztec Code`_

* ``pdf417`` - PDF417_

* ``interleaved2of5`` - `Interleaved 2 of 5`_

* ``code128`` - `Code 128`_

* ``code39`` - `Code 39`_

Command-line interface
======================

Treepoem also includes a simple command-line interface to the
functionality of ``generate_barcode``. For example, these commands
will generate two QR codes with identical contents, but different levels
of error correction (see `QR Code Options`_):

.. code-block:: sh

   $ treepoem -o barcode1.png -t qrcode "This is a test" eclevel=H
   $ treepoem -o barcode2.png -t qrcode "^084his is a test" eclevel=L parse

Complete usage instructions are shown with ``treepoem --help``.

What's so clever about the name?
================================

Barcode.

Bark ode.

Tree poem.

Updating BWIPP
==============

For development of treepoem, when there's a new BWIPP release:

1. Download the latest monolithic zip file from https://github.com/bwipp/postscriptbarcode/releases
2. Unzip the files into `src/treepoem/postscriptbarcode`
3. Remove the unneded `docs` subdirectory.
4. Run `make_data.py` from the root of the repo to update the barcode types that treepoem knows about.
5. Add a CHANGELOG note about the upgrade.
6. Commit and make a pull request, for examples see https://githugb.com/adamchainz/treepoem/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+upgrade+bwipp

.. _BWIPP: https://github.com/bwipp/postscriptbarcode
.. _QR Code: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
.. _Aztec Code: https://github.com/bwipp/postscriptbarcode/wiki/Aztec-Code
.. _PDF417: https://github.com/bwipp/postscriptbarcode/wiki/PDF417
.. _Interleaved 2 of 5: https://github.com/bwipp/postscriptbarcode/wiki/Interleaved-2-of-5
.. _Code 128: https://github.com/bwipp/postscriptbarcode/wiki/Code-128
.. _Code 39: https://github.com/bwipp/postscriptbarcode/wiki/Code-39
.. _QR Code Options: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
