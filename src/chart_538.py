import matplotlib.pyplot as plt
import textwrap


def apply_538_template(
    ax,
    fig,
    title="",
    subtitle="",
    source_text="",
    footer_left="",
    vertical_gridlines=False,
):
    # --- Background ---
    fig.patch.set_facecolor("#F3F4F6")
    ax.set_facecolor("#F3F4F6")

    # --- Remove spines ---
    for spine in ["top", "right", "left", "bottom"]:
        ax.spines[spine].set_visible(False)

    # --- Gridlines ---
    ax.grid(axis="y", color="#DADADA", linewidth=1)
    if vertical_gridlines:
        ax.grid(axis="x", color="#E6E6E6", linewidth=0.8)
    else:
        ax.grid(False, axis="x")

    # --- Title ---
    fig.text(
        0.08,
        0.95,
        title,
        fontsize=20,
        fontweight="bold",
        ha="left",
        va="top",
        color="#111111",
    )

    # --- Subtitle (wrapped safely) ---
    wrapped_subtitle = "\n".join(textwrap.wrap(subtitle, width=80))

    fig.text(
        0.08,
        0.90,
        wrapped_subtitle,
        fontsize=12,
        color="#555555",
        ha="left",
        va="top",
    )

    # --- Source / footer ---
    if source_text:
        fig.text(
            0.08,
            0.02,
            source_text,
            fontsize=9,
            color="#666666",
            ha="left",
            va="bottom",
        )

    if footer_left:
        fig.text(
            0.98,
            0.02,
            footer_left,
            fontsize=9,
            color="#666666",
            ha="right",
            va="bottom",
        )

    # --- Tick styling ---
    ax.tick_params(axis="both", which="both", length=0, labelsize=10, colors="#333333")

    # --- Layout spacing (CRITICAL) ---
    plt.subplots_adjust(
        left=0.08,
        right=0.98,
        top=0.82,   # creates space for title + subtitle
        bottom=0.10
    )