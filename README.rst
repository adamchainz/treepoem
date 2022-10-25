========
Treepoem
========

.. image:: https://img.shields.io/github/actions/workflow/status/adamchainz/treepoem/main.yml?branch=main&style=for-the-badge
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

Python 3.8 to 3.12 supported.

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
Improve your skills with `one of my books <https://adamj.eu/books/>`__.

----

API
===

``generate_barcode(barcode_type: str, data: str | bytes, options: dict[str, str | bool] | None=None, scale: int = 2) -> EpsImageFile``
----------------------------------------------------------------------------------------------------------------------

Generates a barcode and returns it as a PIL image file object (specifically, a
``PIL.EpsImagePlugin.EpsImageFile``).

``barcode_type`` is the name of the barcode type to generate (see below).

``data`` is a ``str`` or ``bytes`` of data to embed in the barcode - the amount
that can be embedded varies by type.

``options`` is a dictionary of strings-to-strings of extra options to be passed
to BWIPP_, as per its docs.

For example, this generates a QR code image, and saves it to a file using
standard PIL ``Image.save()``:

.. code-block:: pycon

   >>> import treepoem
   >>> image = treepoem.generate_barcode(
   ...     barcode_type="qrcode",  # One of the BWIPP supported codes.
   ...     data="barcode payload",
   ... )
   >>> image.convert("1").save("barcode.png")

If your barcode image is monochrome, with no additional text or
coloring, converting the ``Image`` object to monochrome as shown above
(``image.convert('1')``) will likely reduce its file size.

``barcode_types: dict[str, BarcodeType]``
-----------------------------------------

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

1. Run ``./download_bwipp.py`` with the version of BWIPP to download.
2. Run ``./make_data.py`` to update the barcode types that treepoem knows about.
3. Add a note in ``CHANGELOG.rst`` about the upgrade, adapting from the previous one.
4. Commit and make a pull request, `adapting from previous examples <https://github.com/adamchainz/treepoem/pulls?utf8=%E2%9C%93&q=is%3Apr+is%3Aclosed+upgrade+bwipp>`__.

.. _BWIPP: https://github.com/bwipp/postscriptbarcode
.. _QR Code: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
.. _Aztec Code: https://github.com/bwipp/postscriptbarcode/wiki/Aztec-Code
.. _PDF417: https://github.com/bwipp/postscriptbarcode/wiki/PDF417
.. _Interleaved 2 of 5: https://github.com/bwipp/postscriptbarcode/wiki/Interleaved-2-of-5
.. _Code 128: https://github.com/bwipp/postscriptbarcode/wiki/Code-128
.. _Code 39: https://github.com/bwipp/postscriptbarcode/wiki/Code-39
.. _QR Code Options: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
