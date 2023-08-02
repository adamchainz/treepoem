from __future__ import annotations

import subprocess
from functools import lru_cache

from treepoem import _ghostscript_binary


@lru_cache(maxsize=None)
def ghostscript_version() -> str:
    return subprocess.run(
        [_ghostscript_binary(), "--version"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()


def pytest_report_header(config):
    return f"Ghostscript version: {ghostscript_version()}"
