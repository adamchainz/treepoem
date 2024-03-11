=========
Changelog
=========

* Use |importlib.resources|__ on Python 3.9+, which should allow treepoem to work when installed in different packaging scenarios like with zipimport or PyInstaller apps.

  .. |importlib.resources| replace:: ``importlib.resources``
  __ https://docs.python.org/3/library/importlib.resources.html

  Thanks to HemantShrimali1982 for the initial report in `Issue #273 <https://github.com/adamchainz/treepoem/issues/273>`__.

3.23.0 (2023-08-02)
-------------------

* Fixed text positioning to avoid cropping after upgrade to BWIPP 2023-07-23.

  Thanks to Nico Hein in `PR #496 <https://github.com/adamchainz/treepoem/pull/496>`__.

* Update EPS generation to follow the `BWIPP recommendation <https://github.com/bwipp/postscriptbarcode/wiki/Developing-a-Frontend-to-BWIPP>`__.
  This change improves image quality including anti-aliased text, but slightly changes image dimensions for some barcode types.

  This change also modifies the return type of ``generate_barcode()`` from ``PIL.EpsImagePlugin.EpsImageFile`` to its superclass ``PIL.Image.Image``.
  In most cases, this change will be transparent, as most methods on ``EpsImageFile``, such as ``save()``, are inherited from ``Image``.

  Done with guidance from BWIPP creator Terry Burton in `PR #499 <https://github.com/adamchainz/treepoem/pull/499>`__.

3.22.0 (2023-07-24)
-------------------

* Added ``scale`` parameter to ``generate_barcode()`` and ``-s``/``--scale`` option to the command line.
  Changing the scale changes the pixels in the output image.

3.21.0 (2023-07-24)
-------------------

* Upgrade vendored BWIPP to its 2023-07-23 release.
  This version includes several improvements, including removing borders on some barcode types.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.20.0 (2023-07-10)
-------------------

* Drop Python 3.7 support.

* Upgrade vendored BWIPP to its 2023-07-05 release.
  This version includes a bunch of improvements, including more validation and changing Aztec Code to generate only full-range symbols by default.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.19.0 (2023-06-16)
-------------------

* Support Python 3.12.

3.18.0 (2022-12-31)
-------------------

* Upgrade vendored BWIPP to its 2022-10-19 release.
  This version includes some more validation improvements and small rendering fixes.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.17.0 (2022-08-18)
-------------------

* Upgrade vendored BWIPP to its 2022-07-29 release.
  This version includes:

  * new helper encoders for GS1 Digital Link URIs included in QR Code and Data Matrix symbols
  * improved validation of GS1 syntax data
  * a friendly escape mechanism for ASCII control characters

  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.16.0 (2022-06-21)
-------------------

* Upgrade vendored BWIPP to its 2022-06-10 release.
  This version includes some fixes for the rendering of certain barcode formats.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.15.0 (2022-05-11)
-------------------

* Support Python 3.11.

3.14.0 (2022-01-10)
-------------------

* Drop Python 3.6 support.

3.13.0 (2021-12-21)
-------------------

* Upgrade vendored BWIPP to its 2021-09-28 release.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.12.0 (2021-09-21)
-------------------

* Upgrade vendored BWIPP to its 2021-07-15 release.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.11.0 (2021-08-13)
-------------------

* Add type hints.

3.10.0 (2021-05-10)
-------------------

* Support Python 3.10.

3.9.0 (2021-03-22)
------------------

* Upgrade vendored BWIPP to its 2021-02-06 release.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

* Stop distributing tests to reduce package size.
  Tests are not intended to be run outside of the tox setup in the repository.
  Repackagers can use GitHub's tarballs per tag.

3.8.0 (2020-12-30)
------------------

* Upgrade vendored BWIPP to its 2020-12-28 release.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.7.0 (2020-12-13)
------------------

* Drop Python 3.5 support.
* Support Python 3.9.

3.6.0 (2020-10-11)
------------------

* Upgrade BWIPP from 2020-09-13 to 2020-10-11.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.5.0 (2020-09-21)
------------------

* Upgrade BWIPP from 2020-04-01 to 2020-09-13.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.4.0 (2020-06-21)
------------------

* Upgrade BWIPP from 2019-11-08 to 2020-04-01.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.3.1 (2020-02-04)
------------------

* Update allowed barcode list to add missing types from new versions of BWIPP.

3.3.0 (2019-12-21)
------------------

* Upgrade BWIPP from 2019-08-05 to 2019-11-08.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/src/treepoem/postscriptbarcode/CHANGES>`__.

3.2.0 (2019-12-19)
------------------

* Upgrade BWIPP from 2019-04-24 to 2019-08-05.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

* Converted setuptools metadata to configuration file.
  This meant removing the ``__version__`` attribute from the package.

  If you want to inspect the installed version, use ``importlib.metadata.version("treepoem")`` (`docs <https://docs.python.org/3.8/library/importlib.metadata.html#distribution-versions>`__ / `backport <https://pypi.org/project/importlib-metadata/>`__).

* Update Python support to 3.5-3.8.

3.1.0 (2019-06-25)
------------------

* Update Python support to 3.5-3.7, as 3.4 has reached its end of life.

* Upgrade BWIPP from 2017-07-27 to 2019-04-24.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

3.0.0 (2019-05-08)
------------------

* Drop Python 2 support, only Python 3.4+ is supported now.

* Upgrade BWIPP from 2017-05-20 to 2018-07-27.
  This version has a few bug fixes and performance improvements.
  You can read its changelog in the vendored copy in the `treepoem repo <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

2.0.0 (2018-08-04)
------------------

* Support binary barcode data - if ``bytes`` (``str`` on Python 2) is passed
  as data, it's not encoded. This has introduced a dependency on ``six``. This
  may be backwards incompatible, depending on what type of data you're passing
  in on Python 2.
* Make ``treepoem.barcode_types`` a ``dict`` mapping the BWIPP encoder
  names to a custom type containing a human-readable ``description``. This is
  backwards incompatible if you're relying on ``barcode_types`` which
  previously was a ``set`` of the encoder names.
* Upgrade BWIPP from 2017-10-19 to 2018-05-20. This has a few bug fixes and
  performance improvements. You can read its changelog in the vendored copy in
  the `treepoem repo
  <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

1.4.1 (2018-05-01)
------------------

* Fix formatting bug in CLI output.

1.4.0 (2018-05-01)
------------------

* Make the ``options`` argument to ``generate_barcode`` optional.
* Add a CLI ``treepoem``.
* Upgrade BWIPP from 2017-07-10 to 2017-10-19. This has a few bug fixes and
  performance improvements. You can read its changelog in the vendored copy in
  the `treepoem repo
  <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

1.3.2 (2017-10-22)
------------------

* Upgrade BWIPP from 2017-07-10 to 2017-10-19. This has a few bug fixes. You
  can read its changelog in the vendored copy in the `treepoem repo
  <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

1.3.1 (2017-08-24)
------------------

* Upgrade BWIPP from 2017-06-20 to 2017-07-10. This has a few bug fixes. You
  can read its changelog in the vendored copy in the `treepoem repo
  <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

1.3.0 (2017-06-21)
------------------

* Upgrade BWIPP from 2015-11-24 to 2017-06-20. This has a number of bug fixes,
  and supports more barcode types. It has also changed the pixel-for-pixel
  output of some formats, although they still encode the same information -
  notably QR codes, which are tested in ``treepoem``\'s test suite. You can
  read its changelog in the `vendored copy in the treepoem repo
  <https://github.com/adamchainz/treepoem/blob/main/treepoem/postscriptbarcode/CHANGES>`__.

1.2.0 (2017-06-21)
------------------

* Add ``treepoem.barcode_types``, a set of all the names of supported barcode
  types, and error if asked to generate a barcode of an unknown type.

1.1.0 (2017-04-13)
------------------

* Support Windows.

1.0.1 (2016-03-30)
------------------

* Add the missing ``BWIPP`` files.

1.0.0 (2016-03-23)
------------------

* Use ``$PATH`` to find ``gs`` binary.
* Rename ``PostscriptError`` to ``TreepoemError``.
* Add basic ``setup.py``.
* Setup Travis CI build.
* Setup Tox
