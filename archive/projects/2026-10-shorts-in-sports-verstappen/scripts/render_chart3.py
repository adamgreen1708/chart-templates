"""Render the seven-race Max Verstappen comeback chart from verified selected_comebacks.csv.

Editorial highlight: among these seven qualifying races, both Sao Paulo 2024 and Belgium 2022
were wins. Sao Paulo's net +16 positions is the larger winning recovery (+13 for Belgium).
"""
from pathlib import Path
import csv
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

ROOT = Path(__file__).resolve().parent
with (ROOT / 'selected_comebacks.csv').open(encoding='utf-8-sig', newline='') as handle:
    races = list(csv.DictReader(handle))
for r in races:
    r['starting_grid'] = int(r['starting_grid'])
    r['classified_finish'] = int(r['classified_finish'])
    r['net_positions_gained'] = int(r['net_positions_gained'])
    assert r['starting_grid'] - r['classified_finish'] == r['net_positions_gained']

winners = [r for r in races if r['classified_finish'] == 1]
assert len(races) == 7 and len(winners) == 2
assert {(r['race'], r['net_positions_gained']) for r in winners} == {
    ('São Paulo · 2024', 16), ('Belgium · 2022', 13)
}

bg, blue, red = '#F3F4F6', '#1F8FA8', '#C44E52'
ink, sub, greyline, grey_dot, grid = '#111111', '#555555', '#B7C4CC', '#A8B5BE', '#D2D7DB'
fig = plt.figure(figsize=(8, 8), dpi=200, facecolor=bg)

header = fig.text(0.09, 0.947, 'COFFEETABLEVIZ  /  SHORTS IN SPORTS',
                  fontsize=12.2, color='#777777', fontweight='bold', va='top')
title = fig.text(0.09, 0.862, 'P17 to P1: the standout comeback',
                 fontsize=23.2, color=ink, fontweight='bold', va='top')
subtitle = fig.text(0.09, 0.797,
                    'All seven 2015–2025 Grands Prix with 13+ net places gained.\n'
                    'Two ended in a win. São Paulo gained 16 places; Belgium gained 13.',
                    fontsize=12.9, color=sub, va='top', linespacing=1.32)

ax = fig.add_axes([0.41, 0.213, 0.46, 0.52], facecolor=bg)
ax.set_xlim(20.5, 0.5)  # P1 on the right
ax.set_ylim(-0.68, len(races)-0.28)
ax.invert_yaxis()
for spine in ax.spines.values():
    spine.set_visible(False)
ax.set_yticks([])
ax.set_xticks([20, 15, 10, 5, 1])
ax.set_xticklabels(['P20', 'P15', 'P10', 'P5', 'P1'], fontsize=12, color=sub)
ax.tick_params(axis='x', length=0, pad=7)
for x in [20, 15, 10, 5, 1]:
    ax.axvline(x, lw=0.85, color=grid, zorder=0)

# Ensure y rows in figure coordinates match the chart exactly.
fig.canvas.draw()
fig_y = lambda yy: fig.transFigure.inverted().transform(ax.transData.transform((10, yy)))[1]
texts = [header, title, subtitle]
for i, r in enumerate(races):
    start, finish, gain = r['starting_grid'], r['classified_finish'], r['net_positions_gained']
    focus = r['race'] == 'São Paulo · 2024'
    row_y = fig_y(i)
    c = red if focus else blue

    # Race labels, separate gain column; no overlap with the plot labels.
    texts.append(fig.text(0.328, row_y, r['race'], ha='right', va='center',
                          fontsize=14.2, color=red if focus else ink,
                          weight='bold' if focus else 'normal'))
    texts.append(fig.text(0.398, row_y, f'+{gain}', ha='right', va='center',
                          fontsize=14.5, color=red if focus else ink, weight='bold'))

    ax.plot([start, finish], [i, i], lw=5.2 if focus else 4.0,
            color=red if focus else greyline, solid_capstyle='round', zorder=2)
    ax.scatter([start], [i], s=92, color=grey_dot, edgecolor=bg, linewidth=1.2, zorder=4)
    ax.scatter([finish], [i], s=140 if focus else 104, color=c,
               edgecolor=bg, linewidth=1.2, zorder=5)

    # Simple compact position labels (no Start/Finish prefixes).
    texts.append(ax.annotate(f'P{start}', xy=(start, i), xytext=(0, 9), textcoords='offset points',
                             ha='center', va='bottom', fontsize=8.9, color='#777777', zorder=6))
    texts.append(ax.annotate(f'P{finish}', xy=(finish, i),
                             xytext=(-3 if finish <= 2 else 0, -11), textcoords='offset points',
                             ha='right' if finish <= 2 else 'center', va='top',
                             fontsize=10.0, weight='bold' if focus else 'normal', color=c, zorder=6))

    if focus:
        texts.append(ax.text(9.25, i-0.32, 'Biggest winning recovery',
                             fontsize=9.8, color=red, weight='bold', ha='left', va='center'))

legend = fig.text(0.09, 0.151, '● Grey: starting grid    ● Blue/red: classified finish',
                  fontsize=12.5, color=sub)
source = fig.text(0.09, 0.116,
                  'Net change ≠ overtakes. Source: The Data Taylor; F1/FIA checks.',
                  fontsize=10.9, color=sub)
fig.add_artist(Line2D([0.09, 0.91], [0.100, 0.100], transform=fig.transFigure,
                      color='#D0D0D0', lw=0.9))
foot_l = fig.text(0.09, 0.075, 'COFFEETABLEVIZ', fontsize=13, color=ink, weight='bold')
foot_r = fig.text(0.91, 0.075, 'THE DATA TAYLOR  /  3 OF 3', ha='right', fontsize=12, color=sub)
texts.extend([legend, source, foot_l, foot_r])

# Conservative visual QA: no title/subtitle/plot or annotation text overruns canvas.
fig.canvas.draw()
renderer = fig.canvas.get_renderer()
canvas = fig.bbox
for item in texts:
    bbox = item.get_window_extent(renderer)
    assert bbox.x0 >= 8 and bbox.x1 <= canvas.x1-8, f'horizontal clipping: {item.get_text()}'
    assert bbox.y0 >= 8 and bbox.y1 <= canvas.y1-8, f'vertical clipping: {item.get_text()}'

for ext in ('png', 'svg'):
    out = ROOT / f'03_verstappen_comeback_races.{ext}'
    fig.savefig(out, dpi=200, facecolor=bg)
    print(out)
plt.close(fig)
