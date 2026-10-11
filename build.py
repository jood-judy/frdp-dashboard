"""Regenerate js/dashboard.js from maintainable vanilla-JS source modules.

Usage: python tools/build.py
The resulting bundle runs directly from index.html (file://), with no server.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
JS = ROOT / 'js'
out = "/* FrPD Dashboard browser bundle. Source modules: data.js, charts.js, app.js. */\n'use strict';\n"
for name in ('data.js', 'charts.js', 'app.js'):
    source = (JS / name).read_text(encoding='utf8')
    source = '\n'.join(line for line in source.splitlines() if not line.startswith('import '))
    for token, replacement in (
        ('export const ', 'const '),
        ('export function ', 'function '),
        ('export async function ', 'async function '),
    ):
        source = source.replace(token, replacement)
    out += f'\n/* {name} */\n{source}\n'
(JS / 'dashboard.js').write_text(out, encoding='utf8')
print('Built js/dashboard.js')
