#!/usr/bin/env python3
"""Offline unit tests: provider conversion never invents an unplayed score."""
import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "archive/projects/2026-11-epl-2627-unfolded/scripts"))
from football_data_org import convert_payload, club_name

def fixture(status="FINISHED", hg=2, ag=1):
    return dict(id=1234, status=status, season={"startDate":"2026-08-21"},
                competition={"code":"PL"}, utcDate="2026-08-21T19:00:00Z",
                homeTeam={"name":"Manchester City FC", "shortName":"Man City"},
                awayTeam={"name":"Coventry City FC", "shortName":"Coventry"},
                score={"fullTime":{"home":hg,"away":ag},
                       "winner":"HOME_TEAM" if hg>ag else "AWAY_TEAM" if ag>hg else "DRAW"})
def payload(*matches):
    return {"competition":{"code":"PL"}, "matches":list(matches)}

class ProviderTests(unittest.TestCase):
    def test_aliases_all_twenty(self):
        from football_data_org import ALIASES
        self.assertEqual(len(ALIASES), 20)
        for name, names in ALIASES.items():
            for candidate in names:
                self.assertEqual(club_name({"name":candidate}), name)
    def test_only_finished_and_correct_local_time(self):
        future = fixture("TIMED")
        future["id"] = 1235
        csv_text = convert_payload(payload(fixture(), future))
        self.assertIn("21/08/2026,20:00,Man City,Coventry,2,1,H", csv_text)
        self.assertEqual(csv_text.count("\n"), 2)
    def test_finished_requires_score(self):
        match = fixture()
        match["score"]["fullTime"]["home"] = None
        with self.assertRaises(ValueError):
            convert_payload(payload(match))
    def test_score_winner_must_agree(self):
        match = fixture()
        match["score"]["winner"]="AWAY_TEAM"
        with self.assertRaises(ValueError):
            convert_payload(payload(match))
    def test_refuse_wrong_season_or_league(self):
        match = fixture()
        match["season"]["startDate"]="2025-08-15"
        with self.assertRaises(ValueError):
            convert_payload(payload(match))
        match["season"]["startDate"]="2026-08-21"
        with self.assertRaises(ValueError):
            convert_payload({"competition":{"code":"CL"},"matches":[match]})
    def test_refuse_duplicated_ids_and_unsupported_teams(self):
        match=fixture()
        with self.assertRaises(ValueError):
            convert_payload(payload(match, copy.deepcopy(match)))
        match["homeTeam"]={"name":"Unknown United"}
        with self.assertRaises(ValueError):
            convert_payload(payload(match))
    def test_draw(self):
        text=convert_payload(payload(fixture(hg=0,ag=0)))
        self.assertIn(",0,0,D\n",text)

if __name__=="__main__":
    unittest.main()
