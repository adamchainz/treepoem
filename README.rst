========
Treepoem
========

.. image:: https://img.shields.io/pypi/v/treepoem.svg
           :target: https://pypi.python.org/pypi/treepoem

.. image:: https://img.shields.io/travis/YPlan/treepoem.svg
           :target: https://travis-ci.org/YPlan/treepoem


A cleverly named, but very simple python barcode renderer wrapping the
BWIPP_ library and ``ghostscript`` command line tool. It is also
Python 2.7 and Python 3.3+ compatible.

Install
-------

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

Supported barcode types
-----------------------

It should support more or less everything that is supported by BWIPP_,
but these types are specifically verified in the tests:

* ``qrcode`` - `QR Code`_

* ``azteccode`` - `Aztec Code`_

* ``pdf417`` - PDF417_

* ``interleaved2of5`` - `Interleaved 2 of 5`_

* ``code128`` - `Code 128`_

* ``code39`` - `Code 39`_

The set of supported barcode types is available in ``treepoem.barcode_types``.


Example
-------

.. code-block:: python

   >>> import treepoem
   >>> image = treepoem.generate_barcode(
   ...     barcode_type='qrcode',  # One of the BWIPP supported codes.
   ...     data='barcode payload',
   ...     options={},
   ... )
   >>> image.save('barcode.png')  # This is an instance of `PIL.EpsImagePlugin.EpsImageFile`

A file ``barcode.png`` should appear in your current directory with a QR code.


What's so clever about the name?
--------------------------------

Barcode - Treepoem.

Bark ode.

Tree poem.


.. _BWIPP: https://github.com/bwipp/postscriptbarcode
.. _QR Code: https://github.com/bwipp/postscriptbarcode/wiki/QR-Code
.. _Aztec Code: https://github.com/bwipp/postscriptbarcode/wiki/Aztec-Code
.. _PDF417: https://github.com/bwipp/postscriptbarcode/wiki/PDF417
.. _Interleaved 2 of 5: https://github.com/bwipp/postscriptbarcode/wiki/Interleaved-2-of-5
.. _Code 128: https://github.com/bwipp/postscriptbarcode/wiki/Code-128
.. _Code 39: https://github.com/bwipp/postscriptbarcode/wiki/Code-39
