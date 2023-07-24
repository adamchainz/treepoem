#!/usr/bin/env python
from __future__ import annotations

import argparse
import os
import subprocess
from collections.abc import Sequence

MODULE_DIR = os.path.dirname(__file__)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("version")
    args = parser.parse_args(argv)
    version: str = args.version

    os.chdir(MODULE_DIR)
    subprocess.run(
        [
            "curl",
            "--location",  # follow redirects
            f"https://github.com/bwipp/postscriptbarcode/releases/download/{version}/postscriptbarcode-monolithic-package-{version}.zip",  # noqa: E501
            "-o",
            "psbc.zip",
        ],
        check=True,
    )
    subprocess.run(
        [
            # fmt: off
            "unzip",
            "-o",  # overwrite existing files
            "psbc.zip",
            "-d", "src/treepoem/postscriptbarcode",
            # exclude:
            "-x", "docs/", "barcode_with_sample.ps",
            # fmt: on
        ],
        check=True,
    )
    os.unlink("psbc.zip")

    return 0


if __name__ == "__main__":
    main()
