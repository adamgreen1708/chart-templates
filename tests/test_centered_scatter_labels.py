"""Opt-in, backward-compatible in-dot labels for scatter matrices."""
import unittest

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from src import render_538


class CenteredScatterLabelsTest(unittest.TestCase):
    def setUp(self):
        self.original_config = render_538.CHART_CONFIG
        self.fig, self.ax = plt.subplots()

    def tearDown(self):
        render_538.CHART_CONFIG = self.original_config
        plt.close(self.fig)

    def test_iso_country_labels_use_semantic_contrast(self):
        render_538.CHART_CONFIG = {
            "render_profile": "social_square",
            "x_col": "Year",
            "y_col": "RaceRow",
            "series_col": None,
            "highlight_points": [{"Group": "Outside"}],
            "label_strategy": "all",
            "label_style": {
                "enabled": True, "label_col": "CountryISO2",
                "position": "center", "fontsize": 12, "fontweight": "bold",
                "color": "#20303A", "highlight_color": "#FFFFFF",
            },
        }
        rows = [
            {"Year": 2000, "RaceRow": 3, "Group": "Outside", "CountryISO2": "JP"},
            {"Year": 2001, "RaceRow": 3, "Group": "Kenya/Ethiopia", "CountryISO2": "KE"},
        ]
        render_538._plot_labels(self.ax, rows)
        labels = self.ax.texts
        self.assertEqual([a.get_text() for a in labels], ["JP", "KE"])
        self.assertEqual([a.get_horizontalalignment() for a in labels], ["center", "center"])
        self.assertEqual([a.get_position() for a in labels], [(0, 0), (0, 0)])
        self.assertEqual([a.get_color() for a in labels], ["#FFFFFF", "#20303A"])
        self.assertEqual([a.get_fontweight() for a in labels], ["bold", "bold"])

    def test_legacy_right_labels_do_not_change_placement(self):
        render_538.CHART_CONFIG = {
            "render_profile": "social_square",
            "x_col": "Year", "y_col": "RaceRow",
            "highlight_points": [],
            "label_style": {"enabled": True, "label_col": "Code", "position": "right"},
        }
        render_538._plot_labels(
            self.ax, [{"Year": 2000, "RaceRow": 3, "Code": "GB"}]
        )
        label = self.ax.texts[0]
        self.assertEqual(label.get_text(), "GB")
        self.assertEqual(label.get_position(), (6, 0))
        self.assertEqual(label.get_horizontalalignment(), "left")


if __name__ == "__main__":
    unittest.main()
