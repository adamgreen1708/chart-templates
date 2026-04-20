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
    ax.grid(axis="x", color="#E6E6E6", linewidth=0.8)

    # Respect config if vertical gridlines explicitly disabled
    if not vertical_gridlines:
        ax.grid(False, axis="x")
        ax.grid(axis="y", color="#DADADA", linewidth=1)

    # --- Title ---
    fig.text(
        0.09,
        0.94,
        title,
        fontsize=20,
        fontweight="bold",
        ha="left",
        va="top",
        color="#111111",
    )

    # --- Subtitle (wrapped safely) ---
    wrap_width = max(60, int(fig.get_figwidth() * 9))
    wrapped_subtitle = "\n".join(textwrap.wrap(subtitle, width=wrap_width))

    fig.text(
        0.09,
        0.895,
        wrapped_subtitle,
        fontsize=12,
        color="#555555",
        ha="left",
        va="top",
    )

    # --- Footer ---
    if footer_left:
        fig.text(
            0.09,
            0.045,
            footer_left,
            fontsize=9,
            color="#666666",
            ha="left",
            va="bottom",
        )

    if source_text:
        fig.text(
            0.91,
            0.045,
            source_text,
            fontsize=9,
            color="#666666",
            ha="right",
            va="bottom",
        )

    # --- Tick styling ---
    ax.tick_params(
        axis="both",
        which="both",
        length=0,
        labelsize=10,
        colors="#333333",
    )

    # --- Layout spacing ---
    # More generous and more even whitespace around the full chart
    plt.subplots_adjust(
        left=0.09,
        right=0.91,
        top=0.80,
        bottom=0.16,
    )