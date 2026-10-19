"""Export an offline HTML copy and ZIP from the current static source."""
from pathlib import Path
import base64, json, re, sys, zipfile
project = Path(__file__).resolve().parent.parent
root = project / 'dist'
out = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else project / 'exports'
out.mkdir(parents=True, exist_ok=True)
assets = {}
source_text = '\n'.join((root / name).read_text() for name in ['index.html', 'app.js', 'styles.css', 'finish.css'])
for p in sorted((root / 'assets').iterdir()):
    if not p.is_file() or p.name not in source_text:
        continue
    mime = {'.png': 'image/png', '.svg': 'image/svg+xml', '.woff2': 'font/woff2', '.ttf':'font/ttf', '.webp':'image/webp'}[p.suffix]
    assets[p.name] = 'data:' + mime + ';base64,' + base64.b64encode(p.read_bytes()).decode()
css = '\n'.join((root / name).read_text() for name in ['styles.css', 'finish.css'])
css = re.sub(r"url\(['\"]?assets/([^'\")]+)['\"]?\)", lambda m: "url('" + assets[m[1]] + "')", css)
js = (root / 'app.js').read_text()
embedded = '  const WHOO_EMBEDDED_ASSETS = ' + json.dumps(assets, separators=(',', ':')) + ';'
assert "  'use strict';" in js
js = js.replace("  'use strict';", "  'use strict';\n" + embedded, 1)
js = re.sub(r'src="assets/\$\{([^}]+)\}"', lambda m: 'src="${WHOO_EMBEDDED_ASSETS[' + m[1] + ']}"', js)
js = re.sub(r'src="assets/([^"$]+)"', lambda m: 'src="${WHOO_EMBEDDED_ASSETS[' + json.dumps(m[1]) + ']}"', js)
html = re.sub(r'href="assets/([^"$]+)"', lambda m: 'href="' + assets[m[1]] + '"', (root / 'index.html').read_text())
html = re.sub(r'<link rel="stylesheet" href="styles\.css(?:\?[^"]*)?">', lambda m: '<style>\n' + css + '\n</style>', html)
html = re.sub(r'<link rel="stylesheet" href="finish\.css(?:\?[^"]*)?">', '', html)
html = re.sub(r'<script src="app\.js(?:\?[^"]*)?" defer></script>', '', html)
html = html.replace('</body>', '<script>\n' + js + '\n</script>\n</body>')
assert 'src="assets/' not in html and 'src="app.js"' not in html and 'href="styles.css"' not in html
standalone = out / 'WHOO-Card-Mobile.html'
standalone.write_text(html)
package = out / 'WHOO-Card-Mobile-Prototype.zip'
with zipfile.ZipFile(package, 'w', zipfile.ZIP_DEFLATED, compresslevel=6) as z:
    for p in sorted(root.rglob('*')):
        if p.is_file():
            if p.parent == root / 'assets' and p.name not in assets:
                continue
            z.write(p, 'WHOO-Card-Mobile/' + str(p.relative_to(root)))
    for name in ['README.md', 'BACKEND-INTEGRATION.md', 'DESIGN-NOTES.md', 'ASSET-PROMPTS.md', 'FONT-LICENSE.txt', 'CARD-FONT-LICENSE.txt', 'CARD-LAYOUT.json', 'MATERIAL-PROMPTS-V6.md', 'REFERENCE-EDITS-V7.md', 'LOGO-REVISION-V8.md', 'PAYMENT-MARK-LICENSE.txt', 'INTRO-REFERENCE-EDITS-V10.md', 'CARD-ROTATION-V11.md', 'CARD-ROTATION-V11.json', 'scripts/rotate-reference-cards-v11.py', 'scripts/prepare-account-cards-v13.py', 'CARD-SELECTOR-V13.md', 'INTRO-STACK-V15.md', 'WALLETS-AND-CHANGENOW-V15.md', 'WALLET-RECOVERY-V16.md', 'HOME-REVAMP-V17.md', 'HOME-REFINEMENTS-V18.md', 'AGENTS.md', 'tests/prototype-checks.cjs', 'scripts/export-prototype.py']:
        z.write(project / name, 'WHOO-Card-Mobile/' + name)
    for p in sorted((project / 'references' / 'card-rotation-v11').glob('*.png')):
        z.write(p, 'WHOO-Card-Mobile/' + str(p.relative_to(project)))
    for p in sorted((project / 'references' / 'account-cards-v13').iterdir()):
        if p.is_file():
            z.write(p, 'WHOO-Card-Mobile/' + str(p.relative_to(project)))
    z.write(standalone, 'WHOO-Card-Mobile/WHOO-Card-Mobile.html')
    report = project / 'VALIDATION.json'
    if report.exists():
        z.write(report, 'WHOO-Card-Mobile/VALIDATION.json')
with zipfile.ZipFile(package) as z:
    assert z.testzip() is None
print(json.dumps({'html': str(standalone), 'zip': str(package), 'html_bytes': standalone.stat().st_size, 'zip_bytes': package.stat().st_size}))
