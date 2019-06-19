import sys
from os import path

import pytest
from PIL import EpsImagePlugin, Image, ImageChops

import treepoem


@pytest.mark.parametrize(
    "barcode_type,barcode_data",
    [
        ("qrcode", "This is qrcode barcode."),
        ("azteccode", "This is azteccode barcode."),
        ("azteccode", b"This is azteccode barcode."),
        ("pdf417", "This is pdf417 barcode."),
        ("interleaved2of5", "0123456789"),
        ("code128", "This is code128 barcode."),
        ("code39", "THIS IS CODE39 BARCODE."),
    ],
)
def test_barcode(barcode_type, barcode_data):
    actual = treepoem.generate_barcode(barcode_type, barcode_data)

    fixture_path = "{dirname}/fixtures/{barcode_type}.png".format(
        dirname=path.dirname(__file__), barcode_type=barcode_type
    )

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


@pytest.fixture
def pretend_windows():
    real_platform = sys.platform
    try:
        sys.platform = "win32"
        yield
    finally:
        sys.platform = real_platform


@pytest.fixture
def pretend_have_windows_ghostscript():
    real_bin = EpsImagePlugin.gs_windows_binary
    try:
        EpsImagePlugin.gs_windows_binary = "gswin32c"
        yield
    finally:
        EpsImagePlugin.gs_windows_binary = real_bin


def test_get_ghostscript_binary_windows(
    pretend_windows, pretend_have_windows_ghostscript
):
    assert treepoem._get_ghostscript_binary() == "gswin32c"


def test_get_ghostscript_binary_windows_missing(pretend_windows):
    with pytest.raises(treepoem.TreepoemError) as excinfo:
        treepoem._get_ghostscript_binary()
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
