from __future__ import annotations

import argparse
import sys
from textwrap import fill
from typing import BinaryIO, cast

from . import generate_barcode
from .data import barcode_types

supported_barcode_types = "Supported barcode types are:\n" + fill(
    ", ".join(sorted(barcode_types)), initial_indent="    ", subsequent_indent="    "
)


def parse_opt(x: str) -> tuple[str, str | bool]:
    if "=" in x:
        return cast(tuple[str, str], tuple(x.split("=", 1)))
    else:
        # binary option
        return (x, True)


def check_scale(value: str) -> int:
    if not value.isnumeric() or int(value) <= 0:
        raise argparse.ArgumentTypeError(
            f'Scale should be a positive integer value. Found "{value}" instead.'
        )
    return int(value)


parser = argparse.ArgumentParser(epilog=supported_barcode_types)
parser.add_argument(
    "-t", "--type", default="qrcode", help="Barcode type (default %(default)s)"
)
parser.add_argument(
    "-f",
    "--format",
    help=(
        "Output format (default is based on file extension, or xbm with no "
        + "output file)"
    ),
)
parser.add_argument("-o", "--output", help="Output file (default is stdout)")
parser.add_argument(
    "-s",
    "--scale",
    type=check_scale,
    default=2,
    help="Factor scaling the output image size (default is 2).",
)
parser.add_argument("data", help="Barcode data")
parser.add_argument(
    "options", nargs="*", type=parse_opt, help="List of BWIPP options (e.g. width=1.5)"
)


def main() -> None:
    args = parser.parse_args()
    type_: str = args.type
    format_: str | None = args.format
    output: str | None | BinaryIO = args.output
    scale: int = args.scale
    data: str = args.data
    options: dict[str, str | bool] = dict(args.options)

    if type_ not in barcode_types:
        parser.error(
            f'Barcode type "{type_}" is not supported. {supported_barcode_types}'
        )

    stdout_binary = sys.stdout.buffer
    if output is None:
        output = stdout_binary

    # PIL needs an explicit format when it doesn't have a filename to guess from
    if output is stdout_binary and format_ is None:
        format_ = "xbm"

    image = generate_barcode(type_, data, options, scale=scale)

    try:
        image.convert("1").save(output, format_)
    except KeyError as e:
        if format_ is not None and e.args[0] == format_.upper():
            parser.error(f"Image format {format_!r} is not supported")
        else:
            raise


if __name__ == "__main__":
    main()
