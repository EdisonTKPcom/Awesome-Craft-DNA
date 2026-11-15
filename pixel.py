#!/usr/bin/env python3
"""DNA lab pixel banner for Awesome Craft DNA. Original scene, no brand marks."""
import math
import random
from pathlib import Path

random.seed(21)
P = 8
W = 100
H = 34  # 800x272
out = []


def r(x, y, w, h, c, cls=None, extra=""):
    a = f' class="{cls}"' if cls else ""
    out.append(
        f'<rect x="{x * P}" y="{y * P}" width="{w * P}" height="{h * P}" fill="{c}"{a}{extra}/>'
    )


# 3x5 pixel font
F = {
    "A": ["010", "101", "111", "101", "101"],
    "C": ["011", "100", "100", "100", "011"],
    "D": ["110", "101", "101", "101", "110"],
    "E": ["111", "100", "110", "100", "111"],
    "F": ["111", "100", "110", "100", "100"],
    "N": ["101", "111", "101", "101", "101"],
    "R": ["110", "101", "110", "101", "101"],
    "T": ["111", "010", "010", "010", "010"],
    " ": ["000", "000", "000", "000", "000"],
}

style = """
<style>
.tw{animation:tw 2.4s steps(2) infinite}
.tw2{animation:tw 3.1s steps(2) infinite .8s}
.tw3{animation:tw 1.9s steps(2) infinite 1.4s}
@keyframes tw{0%,100%{opacity:1}50%{opacity:.15}}
.glow{animation:glow 1.6s steps(3) infinite}
.glow2{animation:glow 2s steps(3) infinite .5s}
@keyframes glow{0%,100%{opacity:.35}50%{opacity:1}}
.blink{animation:tw 1s steps(1) infinite}
.hx0{animation:hx 2.4s steps(1) infinite}
.hx1{opacity:0;animation:hx 2.4s steps(1) infinite;animation-delay:-.6s}
.hx2{opacity:0;animation:hx 2.4s steps(1) infinite;animation-delay:-1.2s}
.hx3{opacity:0;animation:hx 2.4s steps(1) infinite;animation-delay:-1.8s}
@keyframes hx{0%,24%{opacity:1}25%,100%{opacity:0}}
.base{animation:base 2s linear infinite}
.base2{animation:base 2s linear infinite .5s}
.base3{animation:base 2s linear infinite 1s}
.base4{animation:base 2s linear infinite 1.5s}
@keyframes base{0%{opacity:0}20%{opacity:1}70%{opacity:1}100%{opacity:0}}
.flow{animation:flow 2.4s steps(1) infinite}
.flow2{animation:flow 2.4s steps(1) infinite .6s}
.flow3{animation:flow 2.4s steps(1) infinite 1.2s}
.flow4{animation:flow 2.4s steps(1) infinite 1.8s}
@keyframes flow{0%,24%{opacity:1}25%,100%{opacity:.15}}
.led{animation:led 1.2s steps(2) infinite}
.led2{animation:led 1.6s steps(2) infinite .4s}
@keyframes led{0%,100%{opacity:1}50%{opacity:.2}}
.read{transform-box:fill-box;transform-origin:left center;animation:read 3.2s ease-in-out infinite}
@keyframes read{0%{transform:scaleX(.15)}70%,100%{transform:scaleX(1)}}
</style>
"""

# Night lab sky
sky = ["#071018", "#0a1424", "#0d1a30", "#102038", "#132440", "#162848", "#1a2e50"]
for i, c in enumerate(sky):
    r(0, i * 4, W, 4, c)

# Sparse lab lights / stars, keep the title band clear
for _ in range(20):
    while True:
        x = random.randrange(W)
        y = random.randrange(10)
        if not (26 <= x <= 74 and y <= 8):
            break
    r(
        x,
        y,
        1,
        1,
        random.choice(["#7dd3fc", "#f9a8d4", "#86efac", "#fff7c2"]),
        random.choice(["tw", "tw2", "tw3"]),
    )

# Title: CRAFT DNA
t = "CRAFT DNA"
tx = (W - len(t) * 4) // 2
ty = 2
for k, ch in enumerate(t):
    for yy, row in enumerate(F[ch]):
        for xx, b in enumerate(row):
            if b == "1":
                r(tx + k * 4 + xx + 0.25, ty + yy + 0.25, 1, 1, "#000", None, ' opacity=".55"')
                r(tx + k * 4 + xx, ty + yy, 1, 1, "#5eead4")

# Rotating pixel double helix (4 phase frames)
CX = 36
Y0 = 10
Y1 = 27
AMP = 5
bases = ["#4ade80", "#f87171", "#60a5fa", "#fbbf24"]  # A, T, C, G
strand_a = "#22d3ee"
strand_b = "#f472b6"


def helix_points(phase):
    pts = []
    for yi in range(Y0, Y1 + 1):
        ang = (yi - Y0) * (math.pi / 4) + phase
        x1 = CX + AMP * math.cos(ang)
        x2 = CX + AMP * math.cos(ang + math.pi)
        z1 = math.sin(ang)
        z2 = math.sin(ang + math.pi)
        pts.append((yi, x1, x2, z1, z2))
    return pts


for fi, phase in enumerate([0, math.pi / 2, math.pi, 3 * math.pi / 2]):
    cls = f"hx{fi}"
    pts = helix_points(phase)
    # rungs first, then backbones so the closer strand sits on top
    for i, (yi, x1, x2, z1, z2) in enumerate(pts):
        xa, xb = sorted((round(x1), round(x2)))
        if xb - xa >= 2 and i % 2 == 0:
            # base-pair rung
            col = bases[i % 4]
            r(xa + 1, yi, max(1, xb - xa - 1), 1, col, cls)
    # backbones, draw far strand then near strand
    far = []
    near = []
    for yi, x1, x2, z1, z2 in pts:
        far.append((round(x1 if z1 < z2 else x2), yi, strand_a if z1 < z2 else strand_b))
        near.append((round(x1 if z1 >= z2 else x2), yi, strand_a if z1 >= z2 else strand_b))
    for x, yi, col in far + near:
        r(x, yi, 1, 1, col, cls)

# Sequencer on the right (generic box, no badges)
# pedestal / bench
r(64, 25, 30, 2, "#1e293b")
r(65, 26, 28, 1, "#0f172a")
# body
r(68, 12, 22, 14, "#0f172a")
r(68, 12, 22, 1, "#475569")
r(68, 12, 1, 14, "#334155")
r(89, 12, 1, 14, "#020617")
# screen
r(70, 14, 10, 6, "#042f2e")
r(71, 15, 8, 1, "#2dd4bf", "glow")
r(71, 17, 8, 2, "#134e4a")
r(71, 17, 8, 2, "#22d3ee", "read")
# LED row
r(71, 20, 1, 1, "#4ade80", "led")
r(73, 20, 1, 1, "#60a5fa", "led2")
r(75, 20, 1, 1, "#fbbf24", "led")
r(77, 20, 1, 1, "#f87171", "led2")
# flow cell / pore slot
r(82, 14, 6, 10, "#1e293b")
r(83, 15, 4, 8, "#020617")
r(84, 18, 2, 2, "#22d3ee", "glow2")
# bases travelling down the flow cell (staggered)
flow_y = [15, 17, 19, 21]
flow_cls = ["flow", "flow2", "flow3", "flow4"]
flow_col = ["#4ade80", "#f87171", "#60a5fa", "#fbbf24"]
for i, (yy, cls, col) in enumerate(zip(flow_y, flow_cls, flow_col)):
    r(84, yy, 2, 1, col, cls)

# bases approaching the sequencer from the helix (a short conveyor of reads)
conv = [(58, 22), (60, 22), (62, 22), (64, 21), (66, 20)]
conv_cls = ["base", "base2", "base3", "base4", "base"]
for i, ((x, y), cls) in enumerate(zip(conv, conv_cls)):
    r(x, y, 1, 1, flow_col[i % 4], cls)

# Small operator / researcher on the left of the helix (generic figure)
r(16, 20, 2, 2, "#f1c27d")
r(17, 21, 1, 1, "#0f172a")
r(16, 22, 2, 3, "#0f766e")
r(16, 25, 1, 1, "#111827")
r(17, 25, 1, 1, "#111827")
# pipette in hand
r(18, 23, 1, 2, "#64748b")
r(18, 22, 1, 1, "#22d3ee", "glow")

# Bench / lab floor
for x in range(W):
    r(x, 27, 1, 1, "#134e4a" if x % 5 == 0 else "#0f172a")
    for y in range(28, H):
        if (x + y) % 4 == 0:
            r(x, y, 1, 1, "#1e293b")
        else:
            r(x, y, 1, 1, "#0b1220")

# Status bar
out.append(
    f'<text x="{8}" y="{H * P - 8}" font-family="monospace" font-size="12" fill="#5eead4">'
    f"&gt; sequencing open genomes"
    f'<tspan class="blink">_</tspan></text>'
)

svg = (
    f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W * P} {H * P}" '
    f'width="{W * P}" height="{H * P}" shape-rendering="crispEdges">'
    + style
    + "".join(out)
    + "</svg>"
)

dest = Path(__file__).resolve().parent / "assets" / "craft-dna.svg"
dest.write_text(svg)
print(f"wrote {dest} ({dest.stat().st_size} bytes)")
