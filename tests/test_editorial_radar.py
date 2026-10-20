"""Regression tests for the prospective monthly editorial radar."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from render_editorial_radar import (  # noqa: E402
    EVENTS_PATH, FIELDS, read_events, render_month, months_from,
)
from datetime import date


class EditorialRadarTests(unittest.TestCase):
    def sample(self, **overrides):
        row = {
            "id": "test-event", "target_date": "2027-01-14", "date_precision": "day",
            "original_date": "1977-01-14", "event_type": "album_anniversary",
            "subject": "Example album", "milestone_years": "50",
            "territory": "UK original album release", "source_urls": "https://example.com/source",
            "source_note": "Use independently checked evidence before publication",
            "story_mode": "new", "priority": "A", "proposed_headline": "One title",
            "research_question": "What changed?", "data_plan": "Verified track metadata",
            "existing_content_path": "", "status": "candidate",
            "blockbuster_alignment": "No forced connection",
        }
        row.update(overrides)
        return row

    def read_fixture(self, records):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "events.csv"
            with path.open("w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=FIELDS)
                writer.writeheader()
                writer.writerows(records)
            return read_events(path)

    def test_anniversary_date_and_ordinal(self):
        self.assertEqual([self.sample()], self.read_fixture([self.sample()]))
        page = render_month("2027-01", [self.sample()])
        self.assertIn("**14 Jan** — Example album (50 years)", page)
        self.assertIn("17 Dec 2026", page)  # 28-day lead time

    def test_birthday_is_turns_not_invalid_ordinal(self):
        b = self.sample(id="birthday", original_date="1943-01-14",
                        event_type="artist_birthday", milestone_years="84")
        self.assertIn("turns 84", render_month("2027-01", [b]))

    def test_month_only_never_claims_first_day(self):
        row = self.sample(id="month", target_date="2026-11-01",
                          original_date="1996-11", date_precision="month",
                          milestone_years="30", event_type="album_release")
        self.read_fixture([row])
        page = render_month("2026-11", [row])
        self.assertIn("November (date unconfirmed)", page)
        self.assertNotIn("**1 Nov**", page)

    def test_date_mismatch_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "differ"):
            self.read_fixture([self.sample(original_date="1977-01-15")])

    def test_wrong_milestone_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "inconsistent"):
            self.read_fixture([self.sample(milestone_years="49")])

    def test_months_cross_year_boundaries(self):
        self.assertEqual(
            ["2026-11", "2026-12", "2027-01"],
            months_from(date(2026, 11, 1), 3)
        )

    def test_seed_and_month_tables_have_expected_counts(self):
        events = read_events(EVENTS_PATH)
        counts = {m: len([e for e in events if e["target_date"].startswith(m)])
                  for m in ("2026-11", "2026-12", "2027-01")}
        self.assertEqual({"2026-11": 8, "2026-12": 7, "2027-01": 4}, counts)


if __name__ == "__main__":
    unittest.main()
