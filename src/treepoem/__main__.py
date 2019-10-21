import argparse
import sys
from textwrap import fill

from . import generate_barcode
from .data import barcode_types

supported_barcode_types = "Supported barcode types are:\n" + fill(
    ", ".join(sorted(barcode_types)), initial_indent="    ", subsequent_indent="    "
)


def parse_opt(x):
    if "=" in x:
        return x.split("=", 1)
    else:
        # binary option
        return [x, True]


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
parser.add_argument("data", help="Barcode data")
parser.add_argument(
    "options", nargs="*", type=parse_opt, help="List of BWIPP options (e.g. width=1.5)"
)


def main():
    args = parser.parse_args()

    if args.type not in barcode_types:
        parser.error(
            'Barcode type "{}" is not supported. {}'.format(
                args.type, supported_barcode_types
            )
        )

    try:
        stdout_binary = sys.stdout.buffer
    except AttributeError:
        stdout_binary = sys.stdout  # Python 2

    if args.output is None:
        args.output = stdout_binary

    # PIL needs an explicit format when it doesn't have a filename to guess from
    if args.output is stdout_binary and args.format is None:
        args.format = "xbm"

    image = generate_barcode(args.type, args.data, dict(args.options))

    try:
        image.convert("1").save(args.output, args.format)
    except KeyError as e:
        if e.args[0] == args.format.upper():
            parser.error('Image format "{}" is not supported'.format(args.format))
        else:
            raise


if __name__ == "__main__":
    main()
