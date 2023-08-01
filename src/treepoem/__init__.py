from __future__ import annotations

import io
import os
import shutil
import subprocess
import sys
from binascii import hexlify
from functools import lru_cache
from textwrap import indent
from textwrap import TextWrapper

from PIL import Image

from .data import barcode_types
from .data import BarcodeType

__all__ = ["generate_barcode", "TreepoemError", "BarcodeType", "barcode_types"]

# Inline the BWIPP code rather than using the run operator to execute
# it because the EpsImagePlugin runs Ghostscript with the SAFER flag,
# which disables file operations in the PS code.
BASE_DIR = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
BWIPP_PATH = os.path.join(BASE_DIR, "postscriptbarcode", "barcode.ps")
with open(BWIPP_PATH) as f:
    BWIPP = f.read()

# Error handling from:
# https://github.com/bwipp/postscriptbarcode/wiki/Developing-a-Frontend-to-BWIPP#use-bwipps-error-reporting  # noqa: E501
BBOX_TEMPLATE = """\
%!PS

{bwipp}
/Helvetica findfont 10 scalefont setfont
{scale} {scale} scale
{{
  0 0 moveto
  {data_options_encoder}
  /uk.co.terryburton.bwipp findresource exec
  showpage
}} stopped {{  % "catch" all exceptions
  $error /errorname get dup length string cvs 0 6 getinterval (bwipp.) ne {{
    stop  % Rethrow non-BWIPP exceptions
  }} if
  % Handle BWIPP exceptions, e.g. emit formatted error to stderr
  (%stderr) (w) file
  dup (\nBWIPP ERROR: ) writestring
  dup $error /errorname get dup length string cvs writestring
  dup ( ) writestring
  dup $error /errorinfo get dup length string cvs writestring
  dup (\n) writestring
  dup flushfile
}} if
"""


EPS_TEMPLATE = """\
%!PS-Adobe-3.0 EPSF-3.0
%%HiResBoundingBox: 0 0 {width} {height}
%%Pages: 1
%%LanguageLevel: 2
%%EndComments
%%BeginProlog
{bwipp}
%%EndProlog
%%Page: 1 1
/Helvetica findfont 10 scalefont setfont
{scale} {scale} scale
{translate_x} {translate_y} moveto
{data_options_encoder} /uk.co.terryburton.bwipp findresource exec
showpage
%%Trailer
%%EOF
"""


class TreepoemError(RuntimeError):
    pass


def _get_bbox(
    data_options_encoder: str, scale: int
) -> tuple[float, float, float, float]:
    bbox_code = BBOX_TEMPLATE.format(
        bwipp=BWIPP,
        scale=scale,
        data_options_encoder=indent(data_options_encoder, "  "),
    )
    page_offset = 3000
    gs_process = subprocess.run(
        [
            _ghostscript_binary(),
            "-dSAFER",
            "-dQUIET",
            "-dNOPAUSE",
            "-dBATCH",
            "-sDEVICE=bbox",
            "-c",
            f"<</PageOffset [{page_offset} {page_offset}]>> setpagedevice",
            "-f",
            "-",
        ],
        text=True,
        capture_output=True,
        check=True,
        input=bbox_code,
    )
    err_output = gs_process.stderr.strip()
    # Unfortunately the error-handling in the postscript means that
    # returncode is 0 even if there was an error, but this gives
    # better error messages.
    if gs_process.returncode != 0 or "BWIPP ERROR:" in err_output:
        if err_output.startswith("BWIPP ERROR: "):
            err_output = err_output.replace("BWIPP ERROR: ", "", 1)
        raise TreepoemError(err_output)
    second_line = err_output.split("\n", 2)[1]
    assert second_line.startswith("%%HiResBoundingBox: ")
    numbers = second_line[len("%%HiResBoundingBox: ") :].split(" ")
    assert len(numbers) == 4
    bbx1, bby1, bbx2, bby2 = (float(n) for n in numbers)

    width = bbx2 - bbx1
    height = bby2 - bby1
    translate_x = (page_offset - bbx1) / 2
    translate_y = (page_offset - bby1) / 2
    return width, height, translate_x, translate_y


@lru_cache(maxsize=None)
def _ghostscript_binary() -> str:
    if sys.platform.startswith("win"):
        options = ("gswin32c", "gswin64c", "gs")
    else:
        options = ("gs",)
    for name in options:
        if shutil.which(name) is not None:
            return name
    raise TreepoemError("Cannot determine path to ghostscript, is it installed?")


# Argument passing per:
# https://github.com/bwipp/postscriptbarcode/wiki/Developing-a-Frontend-to-BWIPP#safe-argument-passing  # noqa: E501
def _hexify(data: str | bytes) -> str:
    if isinstance(data, str):
        data = data.encode("utf-8")
    return TextWrapper(subsequent_indent=" ", width=72).fill(
        f"<{hexlify(data).decode('ascii')}>"
    )


def _format_options(options: dict[str, str | bool]) -> str:
    items = []
    for name, value in options.items():
        if isinstance(value, bool):
            if value:
                items.append(name)
        else:
            items.append(f"{name}={value}")
    return " ".join(items)


def _format_data_options_encoder(
    data: str | bytes,
    options: dict[str, str | bool],
    barcode_type: str,
) -> str:
    return (
        f"{_hexify(data)}\n{_hexify(_format_options(options))}\n"
        f"{_hexify(barcode_type)} cvn"
    )


def generate_barcode(
    barcode_type: str,
    data: str | bytes,
    options: dict[str, str | bool] | None = None,
    *,
    scale: int = 2,
) -> Image.Image:
    if barcode_type not in barcode_types:
        raise NotImplementedError(f"unsupported barcode type {barcode_type!r}")
    if options is None:
        options = {}
    if scale < 1:
        raise ValueError("scale must be at least 1")

    data_options_encoder = _format_data_options_encoder(data, options, barcode_type)
    width, height, translate_x, translate_y = _get_bbox(data_options_encoder, scale)
    full_code = EPS_TEMPLATE.format(
        width=width,
        height=height,
        bwipp=BWIPP,
        scale=scale,
        translate_x=translate_x,
        translate_y=translate_y,
        data_options_encoder=data_options_encoder,
    )

    gs_process = subprocess.run(
        [
            _ghostscript_binary(),
            "-dSAFER",
            "-dQUIET",
            "-dNOPAUSE",
            "-dBATCH",
            "-sDEVICE=png16m",
            f"-dDEVICEWIDTHPOINTS={width}",
            f"-dDEVICEHEIGHTPOINTS={height}",
            "-r72",
            "-dTextAlphaBits=4",
            "-dGraphicsAlphaBits=1",
            "-sOutputFile=-",
            "-",
        ],
        capture_output=True,
        check=True,
        input=full_code.encode(),
    )
    return Image.open(io.BytesIO(gs_process.stdout))
