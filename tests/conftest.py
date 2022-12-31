from __future__ import annotations

import subprocess

from treepoem import _get_ghostscript_binary

GHOSTSCRIPT_VERSION = subprocess.check_output(
    [_get_ghostscript_binary(), "--version"]
).decode("utf-8")


def pytest_report_header(config):
    return f"Ghostscript version: {GHOSTSCRIPT_VERSION}"
