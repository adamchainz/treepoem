from __future__ import annotations

import shutil
import sys
from os import path
from unittest import mock

import pytest
from PIL import Image, ImageChops

import treepoem


@pytest.mark.parametrize(
    "barcode_type,barcode_data,options",
    [
        ("qrcode", "This is qrcode barcode.", None),
        ("azteccode", "This is azteccode barcode.", None),
        ("azteccode", b"This is azteccode barcode.", None),
        ("pdf417", "This is pdf417 barcode.", None),
        ("interleaved2of5", "0123456789", None),
        ("code128", "This is code128 barcode.", None),
        ("code39", "THIS IS CODE39 BARCODE.", None),
        ("ean13", "012345678912", {"includetext": True}),
    ],
)
def test_barcode(barcode_type, barcode_data, options):
    actual = treepoem.generate_barcode(barcode_type, barcode_data, options)

    fixture_path = f"{path.dirname(__file__)}/fixtures/{barcode_type}.png"

    # Uncomment to rebuild fixtures:
    # actual.save(fixture_path)

    # Trying to prevent a `ResourceWarning`.
    # Bug: https://github.com/python-pillow/Pillow/issues/1144
    # Workaround: https://github.com/python-pillow/Pillow/issues/835
    with open(fixture_path, "rb") as fixture:
        expected = Image.open(fixture)
        bbox = ImageChops.difference(actual, expected).getbbox()
        assert bbox is None

    actual.close()


def test_scale_0():
    with pytest.raises(ValueError) as excinfo:
        treepoem.generate_barcode("code39", "HELLO", scale=0)

    assert str(excinfo.value) == "scale must be at least 1"


def test_scale_1():
    out = treepoem.generate_barcode("code39", "HELLO", scale=1)
    assert out.size == (111, 72)


def test_scale_2():
    out = treepoem.generate_barcode("code39", "HELLO")
    assert out.size == (222, 144)


def test_scale_4():
    out = treepoem.generate_barcode("code39", "HELLO", scale=4)
    assert out.size == (444, 288)


pretend_linux = mock.patch.object(sys, "platform", "linux")
pretend_windows = mock.patch.object(sys, "platform", "win32")


@pytest.fixture
def uncache_ghostscript_binary():
    treepoem._ghostscript_binary.cache_clear()
    yield
    treepoem._ghostscript_binary.cache_clear()


def test_ghostscript_binary_linux(uncache_ghostscript_binary):
    with pretend_linux, mock.patch.object(shutil, "which", return_value=True):
        result = treepoem._ghostscript_binary()
    assert result == "gs"


def test_get_ghostscript_binary_windows(uncache_ghostscript_binary):
    with pretend_windows, mock.patch.object(shutil, "which", return_value=True):
        result = treepoem._ghostscript_binary()
    assert result == "gswin32c"


def test_get_ghostscript_binary_windows_missing(uncache_ghostscript_binary):
    with (
        pretend_windows,
        mock.patch.object(shutil, "which", return_value=None),
        pytest.raises(treepoem.TreepoemError) as excinfo,
    ):
        treepoem._ghostscript_binary()
    assert "Cannot determine path to ghostscript" in str(excinfo.value)


def test_unsupported_barcode_type():
    with pytest.raises(NotImplementedError) as excinfo:
        treepoem.generate_barcode("invalid-barcode-type", "")
    assert "unsupported barcode type" in str(excinfo.value)


def test_barcode_types():
    for code, barcode_type in treepoem.barcode_types.items():
        assert isinstance(code, str)
        assert barcode_type.type_code == code
        assert isinstance(barcode_type.description, str)
