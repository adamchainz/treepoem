from __future__ import annotations

import re
import subprocess

from treepoem import _get_ghostscript_binary

GHOSTSCRIPT_VERSION = subprocess.check_output(
    [_get_ghostscript_binary(), "--version"]
).decode("utf-8")
if not re.match(r"9\.\d\d", GHOSTSCRIPT_VERSION):
    print(f"Ghostscript must be version 9.X, have {GHOSTSCRIPT_VERSION}")
    raise SystemExit(1)


def pytest_report_header(config):
    return f"Ghostscript version: {GHOSTSCRIPT_VERSION}"
