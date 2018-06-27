.. :changelog:

-------
History
-------

.. Insert new release notes below this line

* Upgrade BWIPP from 2017-10-19 to 2018-05-20. This has a few bug fixes and
  performance improvements. You can read its changelog in the vendored copy in
  the `treepoem repo
  <https://github.com/YPlan/treepoem/blob/master/treepoem/postscriptbarcode/CHANGES>`__.

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
  <https://github.com/YPlan/treepoem/blob/master/treepoem/postscriptbarcode/CHANGES>`__.

1.3.2 (2017-10-22)
------------------

* Upgrade BWIPP from 2017-07-10 to 2017-10-19. This has a few bug fixes. You
  can read its changelog in the vendored copy in the `treepoem repo
  <https://github.com/YPlan/treepoem/blob/master/treepoem/postscriptbarcode/CHANGES>`__.

1.3.1 (2017-08-24)
------------------

* Upgrade BWIPP from 2017-06-20 to 2017-07-10. This has a few bug fixes. You
  can read its changelog in the vendored copy in the `treepoem repo
  <https://github.com/YPlan/treepoem/blob/master/treepoem/postscriptbarcode/CHANGES>`__.

1.3.0 (2017-06-21)
------------------

* Upgrade BWIPP from 2015-11-24 to 2017-06-20. This has a number of bug fixes,
  and supports more barcode types. It has also changed the pixel-for-pixel
  output of some formats, although they still encode the same information -
  notably QR codes, which are tested in ``treepoem``\'s test suite. You can
  read its changelog in the `vendored copy in the treepoem repo
  <https://github.com/YPlan/treepoem/blob/master/treepoem/postscriptbarcode/CHANGES>`__.

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
