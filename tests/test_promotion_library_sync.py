"""Tests for idempotent, approval-first promotion inventory sync."""
import csv
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from sync_promotion_library import EVENT_FIELDS, INDEX_FIELDS, read_csv, sync  # noqa: E402


class PromotionSyncTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for d in ("site/_posts", "site/_data_lens", "site/_blockbuster_quotes",
                  "site/resources/chart-guide", "data/promotion"):
            (self.root / d).mkdir(parents=True, exist_ok=True)
        self._seed_csv(
            "data/promotion/content_index.csv",
            INDEX_FIELDS,
            [{
                "id": "article_existing", "type": "article", "title": "Existing story",
                "category": "Design", "source_path": "site/_posts/existing.md",
                "priority": "P1", "evergreen_class": "evergreen",
                "hook_seed": "Carefully edited hook", "freshness_gate": "Keep this note",
            }],
        )
        self._seed_csv("data/promotion/blockbuster_events.csv", EVENT_FIELDS, [])
        (self.root / "site/_posts/existing.md").write_text(
            '---\ntitle: "Existing story"\ncategory: Design\n---\nBody\n', encoding="utf-8"
        )

    def _seed_csv(self, relative, fields, rows):
        with (self.root / relative).open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    def test_new_items_append_once_and_preserve_editorial_notes(self):
        (self.root / "site/_posts/2026-10-21-new-story.md").write_text(
            '---\ntitle: "A new story: with a colon"\ncategory: Society\n---\nHello\n',
            encoding="utf-8",
        )
        (self.root / "site/_data_lens/2026-10-21-a-small-detail.md").write_text(
            '---\ntitle: "A small detail."\ndate: 2026-10-21\n---\n', encoding="utf-8"
        )
        (self.root / "site/resources/chart-guide/index.html").write_text(
            '---\ntitle: "Chart guide"\n---\n', encoding="utf-8"
        )
        new_content, new_events = sync(self.root, write=False)
        self.assertEqual(3, len(new_content))
        self.assertEqual([], new_events)
        self.assertEqual("REVIEW", new_content[0]["priority"])
        sync(self.root, write=True)
        self.assertEqual(([], []), sync(self.root, write=True))
        rows = read_csv(self.root / "data/promotion/content_index.csv", INDEX_FIELDS)
        self.assertEqual(4, len(rows))
        self.assertEqual("Carefully edited hook", rows[0]["hook_seed"])
        self.assertEqual("Keep this note", rows[0]["freshness_gate"])
        self.assertTrue(all(x["priority"] == "REVIEW" for x in rows[1:]))
        self.assertIn("A new story: with a colon", [x["title"] for x in rows])

    def test_new_blockbuster_gets_no_forced_story_link(self):
        (self.root / "site/_blockbuster_quotes/2026-10-21-test-film.md").write_text(
            '---\ndate: 2026-10-21\nfilm: "Test Film"\n'
            'performer: "Example Performer"\nconnection_type: "birthday of performer"\n---\n',
            encoding="utf-8",
        )
        _, new_events = sync(self.root, write=True)
        self.assertEqual(1, len(new_events))
        self.assertEqual("2026-10-21", new_events[0]["original_date"])
        self.assertEqual("10-21", new_events[0]["month_day"])
        self.assertEqual("", new_events[0]["matched_content_ids"])
        self.assertEqual(([], []), sync(self.root, write=False))

    def test_missing_blockbuster_date_fails_closed(self):
        (self.root / "site/_blockbuster_quotes/2026-10-21-invalid.md").write_text(
            '---\nfilm: "Undated"\n---\n', encoding="utf-8"
        )
        with self.assertRaisesRegex(ValueError, "needs ISO date"):
            sync(self.root, write=True)


if __name__ == "__main__":
    unittest.main()
