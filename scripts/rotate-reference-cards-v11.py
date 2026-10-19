"""Map each existing complete card face as one plane; never rebuild its contents.

Python reads pixels for edge measurements and computes geometry. ImageMagick
performs the requested whole-face perspective rotation and scene translation.
"""
from pathlib import Path
import hashlib
import json
import math
import subprocess
import sys
import tempfile
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
WORK = Path(sys.argv[1]).resolve() if len(sys.argv)>1 else Path(tempfile.mkdtemp(prefix='whoo-card-rotation-'))
WORK.mkdir(parents=True, exist_ok=True)

def run(*args):
    subprocess.run([str(x) for x in args], check=True)

def corners(path, approximate):
    grey = np.asarray(Image.open(path).convert('L'), dtype=float)
    gy, gx = np.gradient(grey)
    mag = np.hypot(gx, gy)
    ys, xs = np.where(mag > 8)
    points = np.column_stack((xs, ys))
    weights = np.sqrt(mag[ys, xs])
    lines = []
    for i in range(4):
        a, b = np.array(approximate[i]), np.array(approximate[(i+1) % 4])
        direction = b-a
        length = np.linalg.norm(direction)
        direction = direction / length
        normal = np.array([-direction[1], direction[0]])
        along = (points-a) @ direction
        distance = (points-a) @ normal
        selected = (along > .07*length) & (along < .93*length) & (abs(distance) < 12)
        pixels, votes = points[selected], weights[selected]
        angle = math.atan2(normal[1], normal[0])
        best = None
        for theta in np.arange(angle-.045, angle+.045, .0008):
            n = np.array([math.cos(theta), math.sin(theta)])
            rho = np.rint(pixels @ n).astype(int)
            shift = 4000
            bins = np.bincount(rho+shift, weights=votes, minlength=8000)
            k = int(np.argmax(bins))
            if best is None or bins[k] > best[0]:
                best = (bins[k], n, k-shift)
        lines.append((best[1], best[2]))
    result = []
    for i in range(4):
        n1, rho1 = lines[(i-1) % 4]
        n2, rho2 = lines[i]
        p = np.linalg.solve(np.vstack((n1, n2)), [rho1, rho2])
        assert np.linalg.norm(p-np.array(approximate[i])) < 25, (path, i, p)
        result.append(p)
    return np.array(result)

def rounded_mask(quad, size, filename):
    # Inset two pixels to retain the photographed edge and avoid a cut-out seam.
    centre = quad.mean(axis=0)
    quad = np.array([p+(centre-p)/np.linalg.norm(centre-p)*2 for p in quad])
    starts, ends = [], []
    for i, p in enumerate(quad):
        previous, following = quad[(i-1) % 4], quad[(i+1) % 4]
        starts.append(p+(previous-p)/np.linalg.norm(previous-p)*8)
        ends.append(p+(following-p)/np.linalg.norm(following-p)*8)
    fmt = lambda p: f'{p[0]:.4f},{p[1]:.4f}'
    path = 'M '+fmt(starts[0])
    for i in range(4):
        path += ' Q '+fmt(quad[i])+' '+fmt(ends[i])+' L '+fmt(starts[(i+1) % 4])
    path += ' Z'
    run('convert', '-size', f'{size[0]}x{size[1]}', 'xc:black', '-fill', 'white', '-stroke', 'none', '-draw', 'path "'+path+'"', '-alpha', 'off', filename)

specs = [
    dict(name='first', source=ROOT/'references/card-rotation-v11/graphite-layout.png',
         base=ROOT/'references/card-rotation-v11/stack-template.png',
         src=[[79,1128],[524,934],[776,1158],[299,1363]],
         dst=[[201,939],[518,1086],[518,1789],[201,1637]],
         order=[3,0,1,2], lift=220, output='intro-cards-rotated-v11.png'),
    dict(name='second', source=ROOT/'references/card-rotation-v11/platinum-layout.png',
         base=ROOT/'references/card-rotation-v11/phone-template.png',
         src=[[257,1128],[758,1212],[778,1554],[255,1464]],
         dst=[[363,967],[653,1051],[660,1562],[364,1495]],
         order=[1,2,3,0], lift=0, output='intro-wallet-card-rotated-v11.png')
]
records = []
for spec in specs:
    src = corners(spec['source'], spec['src'])
    outline = corners(spec['base'], spec['dst'])
    dst = outline[spec['order']]
    size = Image.open(spec['base']).size
    points = ' '.join(f'{s[0]:.6f},{s[1]:.6f} {d[0]:.6f},{d[1]:.6f}' for s,d in zip(src,dst))
    plane, mask, layer, merged = [WORK/(spec['name']+'-'+suffix+'.png') for suffix in ['plane','mask','layer','merged']]
    run('convert', spec['source'], '-alpha', 'set', '-virtual-pixel', 'transparent',
        '-define', f'distort:viewport={size[0]}x{size[1]}+0+0',
        '-distort', 'Perspective', points, '+repage', plane)
    rounded_mask(outline, size, mask)
    run('convert', plane, mask, '-compose', 'CopyOpacity', '-composite', layer)
    run('convert', spec['base'], layer, '-compose', 'Over', '-composite', merged)
    output = ROOT/'dist/assets'/spec['output']
    if spec['lift']:
        run('convert', merged, '-virtual-pixel', 'edge', '-define',
            f'distort:viewport={size[0]}x{size[1]}+0+0', '-distort',
            'AffineProjection', f'1,0,0,1,0,-{spec["lift"]}', '+repage', output)
    else:
        run('cp', merged, output)
    records.append(dict(scene=spec['name'], source=str(spec['source'].relative_to(ROOT)),
        source_sha256=hashlib.sha256(spec['source'].read_bytes()).hexdigest(),
        source_corners=src.tolist(), target_corners=dst.tolist(),
        scene_lift_pixels=spec['lift'], output=spec['output']))
(ROOT/'CARD-ROTATION-V11.json').write_text(json.dumps(records, indent=2)+'\n')
print(json.dumps(records))
