import codecs
import io
import os
import subprocess
import sys

from PIL import EpsImagePlugin

from .data import BarcodeType, barcode_types

__all__ = ["generate_barcode", "TreepoemError", "BarcodeType", "barcode_types"]

BASE_DIR = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
BWIPP_PATH = os.path.join(BASE_DIR, "postscriptbarcode", "barcode.ps")

BASE_PS = """\
{bwipp}

/Helvetica findfont 10 scalefont setfont
gsave
2 2 scale
10 10 moveto

{code}
/uk.co.terryburton.bwipp findresource exec
grestore

showpage
"""

# Error handling from:
# https://github.com/bwipp/postscriptbarcode/wiki/Developing-a-Frontend-to-BWIPP#use-bwipps-error-reporting  # noqa: B950
BBOX_TEMPLATE = (
    """\
%!PS

errordict begin
/handleerror {{
  $error begin
  errorname dup length string cvs 0 6 getinterval (bwipp.) eq {{
    (%stderr) (w) file
    dup (\nBWIPP ERROR: ) writestring
    dup errorname dup length string cvs writestring
    dup ( ) writestring
    dup errorinfo dup length string cvs writestring
    dup (\n) writestring
    dup flushfile end quit
  }} if
  end //handleerror exec
}} bind def
end

"""
    + BASE_PS
)

EPS_TEMPLATE = (
    """\
%!PS-Adobe-3.0 EPSF-3.0
{bbox}

"""
    + BASE_PS
)


class TreepoemError(RuntimeError):
    pass


# Inline the BWIPP code rather than using the run operator to execute
# it because the EpsImagePlugin runs Ghostscript with the SAFER flag,
# which disables file operations in the PS code.
def _read_file(file_path):
    with open(file_path) as f:
        return f.read()


BWIPP = _read_file(BWIPP_PATH)


def _get_bbox(code):
    full_code = BBOX_TEMPLATE.format(bwipp=BWIPP, code=code)
    ghostscript = _get_ghostscript_binary()
    gs_process = subprocess.Popen(
        [ghostscript, "-sDEVICE=bbox", "-dBATCH", "-dSAFER", "-"],
        universal_newlines=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    _, err_output = gs_process.communicate(full_code)
    err_output = err_output.strip()
    # Unfortunately the error-handling in the postscript means that
    # returncode is 0 even if there was an error, but this gives
    # better error messages.
    if gs_process.returncode != 0 or "BWIPP ERROR:" in err_output:
        if err_output.startswith("BWIPP ERROR: "):
            err_output = err_output.replace("BWIPP ERROR: ", "", 1)
        raise TreepoemError(err_output)
    return err_output


def _get_ghostscript_binary():
    binary = "gs"

    if sys.platform.startswith("win"):
        binary = EpsImagePlugin.gs_windows_binary
        if not binary:
            raise TreepoemError(
                "Cannot determine path to ghostscript, is it installed?"
            )

    return binary


def _encode(data):
    if isinstance(data, str):
        data = data.encode("utf-8")
    return codecs.encode(data, "hex_codec").decode("ascii")


def _format_options(options):
    items = []
    for name, value in options.items():
        if isinstance(value, bool):
            if value:
                items.append(name)
        else:
            items.append("{}={}".format(name, value))
    return " ".join(items)


def _format_code(barcode_type, data, options):
    return "<{data}> <{options}> <{barcode_type}> cvn".format(
        data=_encode(data),
        options=_encode(_format_options(options)),
        barcode_type=_encode(barcode_type),
    )


def generate_barcode(barcode_type, data, options=None):
    if barcode_type not in barcode_types:
        raise NotImplementedError("unsupported barcode type {!r}".format(barcode_type))
    if options is None:
        options = {}
    code = _format_code(barcode_type, data, options)
    bbox_lines = _get_bbox(code)
    full_code = EPS_TEMPLATE.format(bbox=bbox_lines, bwipp=BWIPP, code=code)
    return EpsImagePlugin.EpsImageFile(io.BytesIO(full_code.encode("utf8")))
