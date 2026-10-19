"""Normalize approved whole card faces for the account carousel.

All photographic edits use ImageMagick; no brand elements are reconstructed.
The gold material edit was produced by the built-in image-generation tool.
"""
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parent.parent
records = json.loads((ROOT/'CARD-ROTATION-V11.json').read_text())
destination = [(0,0),(855,0),(855,539),(0,539)]
for record, name in zip(records,['plus','premium']):
    points=' '.join(f'{s[0]:.6f},{s[1]:.6f} {d[0]},{d[1]}' for s,d in zip(record['source_corners'],destination))
    subprocess.run(['convert',str(ROOT/record['source']),'-alpha','set','-virtual-pixel','edge','-define','distort:viewport=856x540+0+0','-distort','Perspective',points,'+repage',str(ROOT/'dist/assets'/('account-'+name+'-v13.png'))],check=True)
subprocess.run(['convert',str(ROOT/'references/account-cards-v13/gold-edit.png'),'-trim','+repage','-resize','856x540!',str(ROOT/'dist/assets/account-metal-v13.png')],check=True)
