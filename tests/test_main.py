from __future__ import annotations

import sys

import pytest

from treepoem.__main__ import main


def test_help(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["treepoem", "--help"])
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 0
    out, err = capsys.readouterr()
    assert "Supported barcode types are: auspost," in out
    assert err == ""


def test_simple(tmp_path, monkeypatch):
    test_png = tmp_path / "test.png"
    monkeypatch.setattr(sys, "argv", ["treepoem", "-o", str(test_png), "barcodedata"])
    main()
    assert test_png.exists()


def test_stdout(monkeypatch, capsys):
    monkeypatch.setattr(sys, "argv", ["treepoem", "barcodedata"])
    main()
    out, err = capsys.readouterr()
    print(out)
    print(err)
    out_lines = out.splitlines()
    assert out_lines[:3] == [
        # xbm format
        "#define im_width 84",
        "#define im_height 84",
        "static char im_bits[] = {",
    ]
    assert err == ""


def test_stdout_with_format(monkeypatch, capfdbinary):
    monkeypatch.setattr(sys, "argv", ["treepoem", "-f", "png", "barcodedata"])
    main()
    out, err = capfdbinary.readouterr()
    assert out.startswith(b"\x89PNG")  # PNG magic bytes
    assert err == b""


def test_unsupported_barcode_type(tmp_path, monkeypatch, capsys):
    test_png = tmp_path / "test.png"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "treepoem",
            "-t",
            "invalid-barcode-type",
            "-o",
            str(test_png),
            "barcodedata",
        ],
    )
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
    assert not test_png.exists()
    out, err = capsys.readouterr()
    assert out == ""
    assert (
        'Barcode type "invalid-barcode-type" is not supported. Supported '
        + "barcode types are:"
    ) in err


def test_unsupported_file_format(tmp_path, monkeypatch, capsys):
    test_png = tmp_path / "test.png"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "treepoem",
            "-f",
            "invalid-image-format",
            "-o",
            str(test_png),
            "barcodedata",
        ],
    )
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
    assert not test_png.exists()
    out, err = capsys.readouterr()
    assert out == ""
    assert "Image format 'invalid-image-format' is not supported" in err


def test_scale(tmpdir, monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["treepoem", "-o", str(tmpdir.join("test.png")), "--scale", "4", "barcodedata"],
    )
    main()
    assert tmpdir.join("test.png").check(exists=True)


def test_unsupported_scale(tmpdir, monkeypatch, capsys):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "treepoem",
            "-o",
            str(tmpdir.join("test.png")),
            "-s",
            "unsupported-scale",
            "barcodedata",
        ],
    )
    with pytest.raises(SystemExit) as excinfo:
        main()
    assert excinfo.value.code == 2
    assert tmpdir.join("test.bin").check(exists=False)
    out, err = capsys.readouterr()
    assert out == ""
    assert (
        'Scale should be a positive integer value. Found "unsupported-scale" instead.'
        in err
    )
