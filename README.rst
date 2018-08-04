========
Treepoem
========

.. image:: https://img.shields.io/pypi/v/treepoem.svg
           :target: https://pypi.python.org/pypi/treepoem

.. image:: https://img.shields.io/travis/adamchainz/treepoem.svg
           :target: https://travis-ci.org/adamchainz/treepoem


A cleverly named, but very simple python barcode renderer wrapping the
BWIPP_ library and ``ghostscript`` command line tool, Python 2.7 and 3.3+
compatible.

------------
Installation
------------

Install from **pip**:

.. code-block:: sh

    pip install treepoem

You'll also need Ghostscript installed. On Ubuntu/Debian this can be installed
with:

.. code-block:: sh

    apt-get install ghostscript

On Mac OS X use:

.. code-block:: sh

    brew install ghostscript

Otherwise refer to your distribution's package manager, though it's likely to
be called ``ghostscript`` too.

---
API
---

``generate_barcode(barcode_type, data, options=None)``
------------------------------------------------------

Generates a barcode and returns it as a PIL image file object (specifically, a
``PIL.EpsImagePlugin.EpsImageFile``).

``barcode_type`` is the name of the barcode type to generate (see below).

``data`` is the string of data to embed in the barcode - the amount that can be
embedded varies by type.

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

----------------------
Command-line interface
----------------------

Treepoem also includes a simple command-line interface to the
functionality of ``generate_barcode``. For example, these commands
will generate two QR codes with identical contents, but different levels
of error correction (see `QR Code Options`_):

.. code-block:: sh

   $ treepoem -o barcode1.png -t qrcode "This is a test" eclevel=H
   $ treepoem -o barcode2.png -t qrcode "^084his is a test" eclevel=L parse

Complete usage instructions are shown with ``treepoem --help``.

--------------------------------
What's so clever about the name?
--------------------------------

Barcode.

Bark ode.

Tree poem.


.. _BWIPP: https://github.com/bwipp/postscriptbarcode
.. _QR Code: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
.. _Aztec Code: https://github.com/bwipp/postscriptbarcode/wiki/Aztec-Code
.. _PDF417: https://github.com/bwipp/postscriptbarcode/wiki/PDF417
.. _Interleaved 2 of 5: https://github.com/bwipp/postscriptbarcode/wiki/Interleaved-2-of-5
.. _Code 128: https://github.com/bwipp/postscriptbarcode/wiki/Code-128
.. _Code 39: https://github.com/bwipp/postscriptbarcode/wiki/Code-39
.. _QR Code Options: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
