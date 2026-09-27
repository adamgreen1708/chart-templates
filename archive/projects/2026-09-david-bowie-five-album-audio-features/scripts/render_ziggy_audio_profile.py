#!/usr/bin/env python3
from __future__ import annotations

import csv
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

PROJECT = Path(__file__).resolve().parents[1]
INPUT = PROJECT / "data" / "ziggy_audio_features.csv"
OUTPUT = PROJECT / "output" / "ziggy_audio_profile.png"

BG = "#F3F4F6"
BLUE = "#1F8FA8"
RED = "#C44E52"
GREY = "#D9D9D9"
DARK = "#333333"
MID = "#7A7A7A"


def load_rows():
    with INPUT.open(newline="", encoding="utf-8") as fh:
        rows = list(csv.DictReader(fh))
    rows.sort(key=lambda r: int(r["track_position"]))
    return rows


def main():
    rows = load_rows()
    matched = [r for r in rows if r["reccobeats_match_status"] == "matched"]
    if len(matched) < 10:
        raise SystemExit("Not enough audio-feature coverage to render")

    titles = [r["track_title"] for r in rows]
    duration = np.array([float(r["duration_seconds"]) / 60 for r in rows])
    tempo = np.array([float(r["tempo"]) if r["tempo"] else np.nan for r in rows])
    energy = np.array([float(r["energy"]) if r["energy"] else np.nan for r in rows])
    valence = np.array([float(r["valence"]) if r["valence"] else np.nan for r in rows])
    acoustic = np.array([float(r["acousticness"]) if r["acousticness"] else np.nan for r in rows])
    streams = np.array([float(r["spotify_streams"]) if r["spotify_streams"] else 0 for r in rows])
    y = np.arange(len(rows))

    fig = plt.figure(figsize=(12, 10), dpi=190, facecolor=BG)
    gs = fig.add_gridspec(
        1, 4, width_ratios=[6.8, 1.25, 1.25, 1.25],
        left=0.25, right=0.94, top=0.78, bottom=0.15, wspace=0.28
    )
    ax = fig.add_subplot(gs[0,0], facecolor=BG)
    ax_e = fig.add_subplot(gs[0,1], sharey=ax, facecolor=BG)
    ax_v = fig.add_subplot(gs[0,2], sharey=ax, facecolor=BG)
    ax_d = fig.add_subplot(gs[0,3], sharey=ax, facecolor=BG)

    valid_tempo = tempo[np.isfinite(tempo)]
    norm = mpl.colors.Normalize(vmin=float(valid_tempo.min()), vmax=float(valid_tempo.max()))
    cmap = mpl.colors.LinearSegmentedColormap.from_list("tempo", [GREY, BLUE, DARK])
    colours = [cmap(norm(t)) if np.isfinite(t) else GREY for t in tempo]

    bars = ax.barh(y, duration, height=0.62, color=colours, edgecolor="none")
    ax.invert_yaxis()

    top_idx = int(np.argmax(streams))

    for i,(b,r) in enumerate(zip(bars,rows)):
        ax.text(
            b.get_width()+0.06, b.get_y()+b.get_height()/2,
            r["duration_display"], va="center", ha="left",
            fontsize=8.5, color=DARK,
            fontweight="normal"
        )

    ax.set_yticks(y)
    ax.set_yticklabels(titles, fontsize=9.5, color=DARK)

    # A single restrained red dot identifies the album's most-streamed track.
    # x is in axes coordinates and y is in data coordinates, placing the dot
    # between the track label and the plotting area without outlining the bar.
    ax.scatter(
        [-0.025], [y[top_idx]],
        s=42, color=RED, edgecolor="none",
        transform=ax.get_yaxis_transform(),
        clip_on=False, zorder=5
    )
    ax.set_xlim(0, max(duration)*1.18)
    ax.set_xlabel("Track length (minutes)", fontsize=9, color=DARK, labelpad=10)
    ax.grid(axis="x", color="#D5D5D5", linewidth=0.8, alpha=0.75)
    ax.grid(axis="y", visible=False)
    for s in ax.spines.values(): s.set_visible(False)
    ax.tick_params(axis="x", colors=MID, labelsize=8)
    ax.tick_params(axis="y", length=0)

    panels = [
        (ax_e, energy, "Energy"),
        (ax_v, valence, "Valence"),
        (ax_d, acoustic, "Acousticness"),
    ]
    for panel, vals, label in panels:
        panel.axvline(0.5, color="#D0D0D0", linewidth=0.8, zorder=0)
        panel.scatter(vals, y, s=46, color=BLUE, alpha=0.88, zorder=2)
        panel.set_xlim(0,1)
        panel.set_xticks([0,0.5,1])
        panel.set_xticklabels(["0",".5","1"], fontsize=7.5, color=MID)
        panel.set_xlabel(label, fontsize=8.5, color=DARK, labelpad=9)
        panel.tick_params(axis="y", left=False, labelleft=False)
        panel.tick_params(axis="x", length=0)
        panel.grid(False)
        for s in panel.spines.values(): s.set_visible(False)

    # Compact tempo key: horizontal, away from the plotting area.
    cax = fig.add_axes([0.735, 0.812, 0.18, 0.018], facecolor=BG)
    sm = mpl.cm.ScalarMappable(norm=norm, cmap=cmap)
    cb = fig.colorbar(sm, cax=cax, orientation="horizontal")
    cb.outline.set_visible(False)
    cb.set_ticks([float(valid_tempo.min()), float(valid_tempo.max())])
    cb.set_ticklabels([
        f"{valid_tempo.min():.0f}",
        f"{valid_tempo.max():.0f}",
    ])
    cb.ax.tick_params(labelsize=7.5, colors=MID, length=0, pad=2)
    fig.text(0.735, 0.836, "Tempo · BPM", fontsize=8.5, color=DARK, ha="left")

    fig.text(0.07, 0.94, "Inside Ziggy Stardust", fontsize=24, fontweight="bold", color=DARK, ha="left")
    fig.text(
        0.07, 0.895,
        "Track length leads the comparison; bar colour shows tempo. Energy, valence and acousticness add a compact sound profile for each song.",
        fontsize=11, color="#555555", ha="left"
    )
    fig.text(
        0.07, 0.855,
        "Red dot = most-streamed album track in the 25 Sep 2026 snapshot.",
        fontsize=9.5, color=RED, ha="left", fontweight="bold"
    )
    missing = [r["track_title"] for r in rows if r["reccobeats_match_status"] != "matched"]
    if missing:
        fig.text(
            0.07, 0.825,
            "Audio features unavailable for: " + ", ".join(missing) + " · duration retained, feature marks left blank.",
            fontsize=8.5, color=MID, ha="left"
        )

    starman = rows[top_idx]
    fig.text(
        0.07, 0.105,
        f"Most streamed: {starman['track_title']} · {int(float(starman['spotify_streams'])):,} streams",
        fontsize=9, color=DARK, ha="left"
    )
    fig.text(
        0.07, 0.06,
        "Coffeetableviz | Duration: MusicBrainz · Audio features: ReccoBeats · Streams: Spotify/Kworb snapshot 25 Sep 2026",
        fontsize=8.5, color=MID, ha="left"
    )

    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(OUTPUT, facecolor=BG)
    plt.close(fig)
    print(f"Saved {OUTPUT}")


if __name__ == "__main__":
    main()
