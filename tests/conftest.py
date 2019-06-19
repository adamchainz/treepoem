import re
import subprocess
import sys

from treepoem import _get_ghostscript_binary

GHOSTSCRIPT_VERSION = subprocess.check_output(
    [_get_ghostscript_binary(), "--version"]
).decode("utf-8")
if not re.match(r"9\.\d\d", GHOSTSCRIPT_VERSION):
    print("Ghostscript must be version 9.X, have {}".format(GHOSTSCRIPT_VERSION))
    sys.exit(1)


def pytest_report_header(config):
    return "Ghostscript version: {}".format(GHOSTSCRIPT_VERSION)
