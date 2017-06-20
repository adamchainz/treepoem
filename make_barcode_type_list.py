# -*- encoding:utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals
import os

BASE_DIR = os.path.normpath(os.path.abspath(os.path.dirname(__file__)))
BWIPP_PATH = os.path.join(BASE_DIR, 'treepoem', 'postscriptbarcode', 'barcode.ps')
BARCODE_TYPES_PATH = os.path.join(BASE_DIR, 'treepoem', 'barcode_types.py')

with open(BARCODE_TYPES_PATH, "w") as o:
    o.write('# -*- encoding:utf-8 -*-\n')
    o.write('from __future__ import absolute_import, division, print_function, unicode_literals\n\n')
    o.write('# all supported barcode types, extracted from barcode.ps\n')
    o.write('barcode_types = {\n')
    with open(BWIPP_PATH) as f:
        for line in f:
            if line.startswith('% --BEGIN ENCODER ') and line.endswith('--\n'):
                barcode_type = line[:-3].split()[3]
                o.write('    {!r},\n'.format(barcode_type))
    o.write('}\n')
