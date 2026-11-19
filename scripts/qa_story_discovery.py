#!/usr/bin/env python3
"""Mechanical story-discovery preflight. Editorial judgement is NOT automatable.

Usage:
    python scripts/qa_story_discovery.py archive/projects/<project>/content/story_review.json

Required JSON structure is documented in docs/editorial_judgement_standard.md.
Numbers are recomputed from CSV files in the repository: no ChatGPT chart rendering.
"""
from __future__ import annotations

import argparse
import csv
import json
import math
import statistics
from pathlib import Path
from urllib.parse import urlparse

REPO = Path(__file__).resolve().parents[1]
ROLES = {"setup", "tension", "reveal"}
CHANNELS = {"x", "y", "position", "length", "size", "colour", "color", "shape",
            "connection", "time", "row", "column", "text"}
OPS = {"mean", "median", "sum", "count", "distinct_count", "max", "min", "percentage"}

class EditorialPreflightError(ValueError):
    """Source, calculation, evidence or design-documentation gate failed."""

def require(cond: bool, msg: str) -> None:
    if not cond:
        raise EditorialPreflightError(msg)

def meaningful(value, field: str, minimum: int = 5) -> str:
    require(isinstance(value, str) and len(value.strip()) >= minimum,
            f"{field}: meaningful nonempty explanation required")
    return value.strip()

def repo_file(raw: str, field: str) -> Path:
    meaningful(raw, field, 3)
    path = (REPO / raw).resolve()
    require(path.is_relative_to(REPO), f"{field}: path escapes repository: {raw}")
    require(path.is_file(), f"{field}: source file missing: {raw}")
    require(path.suffix.lower() == ".csv", f"{field}: expected real CSV data: {raw}")
    return path

def data_rows(path: Path):
    with path.open(encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        require(reader.fieldnames, f"{path}: missing CSV header")
        rows = list(reader)
    require(rows, f"{path}: empty dataset")
    return rows, set(reader.fieldnames)

def selected(rows: list[dict], columns: set, condition: dict | None, tag: str):
    if condition is None:
        return rows
    require(isinstance(condition, dict) and set(condition) == {"column", "equals"},
            f"{tag}: filter must be {{column, equals}}")
    col = condition["column"]
    require(col in columns, f"{tag}: filter field missing: {col}")
    result = [row for row in rows if row[col] == str(condition["equals"])]
    require(result, f"{tag}: filter matched no source rows")
    return result

def number(value, tag: str):
    try:
        out = float(str(value).replace(",", ""))
    except (TypeError, ValueError):
        raise EditorialPreflightError(f"{tag}: not a numeric source value: {value!r}")
    require(math.isfinite(out), f"{tag}: non-finite numerical value")
    return out

def calculate(audit: dict) -> float:
    tag = f"evidence {audit.get('id', '?')}"
    rows, columns = data_rows(repo_file(audit.get("file", ""), tag))
    rows = selected(rows, columns, audit.get("filter"), tag)
    op = audit.get("operation")
    require(op in OPS, f"{tag}: unsupported calculation {op!r}")
    if op == "count":
        return float(len(rows))
    field = audit.get("column")
    require(field in columns, f"{tag}: missing metric column {field!r}")
    if op == "distinct_count":
        return float(len({r[field] for r in rows}))
    values = [number(row[field], f"{tag}/{field}") for row in rows]
    if op == "mean":
        return statistics.fmean(values)
    if op == "median":
        return statistics.median(values)
    if op == "sum":
        return sum(values)
    if op == "max":
        return max(values)
    if op == "min":
        return min(values)
    # Share of a source total, explicitly *not* people unless source grain is people.
    require(op == "percentage", f"{tag}: invalid operation")
    all_rows, _ = data_rows(repo_file(audit["file"], tag))
    denom = selected(all_rows, columns, audit.get("denominator_filter"), tag + "/denominator")
    total = sum(number(row[field], f"{tag}/denominator") for row in denom)
    require(total != 0, f"{tag}: zero denominator")
    return 100 * sum(values) / total

def validate_annotation(a: dict, chart_rows: list[dict], columns: set, chart_id: str) -> None:
    tag = f"chart {chart_id} annotation"
    meaningful(a.get("label", ""), tag + " label")
    rule = a.get("rule")
    require(isinstance(rule, dict), f"{tag}: explicit selection rule is required")
    kind = rule.get("kind")
    require(kind in {"max", "min", "editorial", "event", "threshold"},
            f"{tag}: unsupported annotation selection {kind!r}")
    meaningful(a.get("why_labelled", ""), tag + " justification", 15)
    if kind in {"editorial", "event", "threshold"}:
        meaningful(rule.get("criterion", ""), tag + " criterion", 15)
        return
    metric, key, target = rule.get("metric"), rule.get("identity_column"), rule.get("selected_identity")
    require(metric in columns and key in columns and target not in (None, ""),
            f"{tag}: rank rule needs existing metric, identity_column and selected_identity")
    group = selected(chart_rows, columns, rule.get("filter"), tag)
    vals = [number(r[metric], tag) for r in group]
    extremum = max(vals) if kind == "max" else min(vals)
    winners = [r for r in group if number(r[metric], tag) == extremum]
    require(len(winners) == 1, f"{tag}: rank tie must be resolved explicitly")
    require(str(winners[0][key]) == str(target),
            f"{tag}: selected {target!r} is not source-derived {kind} for {metric} "
            f"(actual {winners[0][key]!r})")

def validate(doc: dict) -> dict:
    require(isinstance(doc, dict), "Root must be a JSON object")
    meaningful(doc.get("project", ""), "project")
    source = doc.get("source", {})
    require(isinstance(source, dict), "source must be an object")
    for key in ("dataset", "snapshot", "grain", "coverage"):
        meaningful(source.get(key, ""), f"source.{key}")
    require(isinstance(source.get("limitations"), list) and source["limitations"],
            "source.limitations must name actual research limits")
    for item in source["limitations"]:
        meaningful(item, "source limitation", 10)
    meaningful(doc.get("central_question", ""), "central_question", 15)
    meaningful(doc.get("editorial_takeaway", ""), "editorial_takeaway", 20)

    audits = doc.get("evidence")
    require(isinstance(audits, list) and audits, "evidence list is required")
    evidence_ids = set()
    calc_checked = 0
    for e in audits:
        require(isinstance(e, dict), "Evidence entries must be objects")
        ident = meaningful(e.get("id", ""), "evidence id", 2)
        require(ident not in evidence_ids, f"Duplicate evidence id {ident!r}")
        evidence_ids.add(ident)
        if e.get("kind") == "calculation":
            expected = number(e.get("expected"), f"expected {ident}")
            actual = calculate(e)
            tolerance = number(e.get("tolerance", 0.00001), f"tolerance {ident}")
            require(tolerance >= 0 and math.isclose(actual, expected, rel_tol=0, abs_tol=tolerance),
                    f"evidence {ident}: expected {expected}, recomputed {actual}, tolerance {tolerance}")
            calc_checked += 1
        elif e.get("kind") == "source":
            url = meaningful(e.get("url", ""), f"evidence {ident} URL", 10)
            require(urlparse(url).scheme == "https" and bool(urlparse(url).netloc),
                    f"evidence {ident}: verified-source URL must use https")
            meaningful(e.get("claim", ""), f"evidence {ident} claim", 10)
            meaningful(e.get("checked_on", ""), f"evidence {ident} checked_on", 8)
        else:
            raise EditorialPreflightError(f"evidence {ident}: unsupported kind")
    require(calc_checked > 0, "At least one verified CSV-derived calculation is required")

    def check_evidence(ids, tag):
        require(isinstance(ids, list) and ids, f"{tag}: evidence_ids must not be empty")
        require(set(ids).issubset(evidence_ids), f"{tag}: unknown evidence IDs {set(ids)-evidence_ids}")

    candidates = doc.get("candidates")
    require(isinstance(candidates, list) and len(candidates) >= 3,
            "At least 3 genuinely competing story routes must be documented")
    ids = [c.get("id") for c in candidates]
    require(len(set(ids)) == len(ids), "Candidate IDs must be unique")
    preferred = doc.get("preferred_candidate")
    require(preferred in ids, "preferred_candidate must name one considered route")
    for c in candidates:
        tag = f"candidate {c.get('id', '?')}"
        for field in ("claim", "why_interesting", "why_audience_cares", "weakness", "visual_direction"):
            meaningful(c.get(field, ""), f"{tag}.{field}", 12)
        check_evidence(c.get("evidence_ids"), tag)
        if c["id"] != preferred:
            meaningful(c.get("rejection_reason", ""), f"{tag}.rejection_reason", 15)
    require(len({c["visual_direction"].strip().lower() for c in candidates}) >= 3,
            "Candidate routes are only reworded versions of the same visual idea")

    charts = doc.get("charts")
    require(isinstance(charts, list) and charts, "At least one editorial chart is required")
    require(len(charts) <= 6, "Six+ charts require a separate editorial exception")
    if len(charts) == 3:
        require([c.get("role") for c in charts] == ["setup", "tension", "reveal"],
                "Three-chart arc must establish → complicate → reveal")
    else:
        meaningful(doc.get("chart_count_reason", ""), "chart_count_reason", 20)
    colors, takeaways = {}, set()
    total_labels = 0
    for idx, c in enumerate(charts, 1):
        tag = f"chart {idx}"
        for key in ("id", "role", "title", "question", "claim", "new_information",
                    "why_this_form", "alternative_form", "why_not_alternative", "scale_disclosure"):
            meaningful(c.get(key, ""), f"{tag}.{key}", 2 if key == "id" else 4 if key == "role" else 12)
        require(c["role"] in ROLES, f"{tag}: role must be setup/tension/reveal")
        require(c["new_information"] not in takeaways, f"{tag}: repeated takeaway")
        takeaways.add(c["new_information"])
        check_evidence(c.get("evidence_ids"), tag)
        file = repo_file(c.get("data_file", ""), f"{tag} data_file")
        rows, columns = data_rows(file)
        enc = c.get("encoding")
        require(isinstance(enc, list) and enc, f"{tag}: explain at least one visual encoding")
        for item in enc:
            require(isinstance(item, dict) and item.get("channel") in CHANNELS,
                    f"{tag}: invalid visual channel")
            meaningful(item.get("meaning", ""), f"{tag} encoding meaning", 8)
            if item.get("field") not in (None, ""):
                require(item["field"] in columns, f"{tag}: encoding field missing: {item['field']}")
        labels = c.get("annotations", [])
        require(isinstance(labels, list), f"{tag}: annotations must be a list")
        for a in labels:
            validate_annotation(a, rows, columns, c["id"])
            total_labels += 1
        for role in c.get("color_roles", []):
            key = meaningful(role.get("role", ""), f"{tag} color role")
            val = meaningful(role.get("hex", ""), f"{tag} color hex")
            require(val.startswith("#") and len(val) == 7 and
                    all(ch in "0123456789abcdefABCDEF" for ch in val[1:]),
                    f"{tag}: invalid hexadecimal colour {val}")
            if key in colors:
                require(colors[key] == val.lower(), f"{tag}: semantic colour {key!r} changed")
            colors[key] = val.lower()

    contract = doc.get("render_contract")
    require(isinstance(contract, dict), "render_contract must be documented")
    require(contract.get("system") == "github",
            "All data chart rendering (including drafts) MUST be in GitHub")
    meaningful(contract.get("renderer", ""), "render_contract.renderer", 10)
    require("ChatGPT" not in contract["renderer"], "ChatGPT must not render numerical charts")
    print(f"PASS | {doc['project']} | {len(candidates)} story candidates, "
          f"{len(charts)} distinct chart roles, {calc_checked} numeric audits, "
          f"{total_labels} audited annotation selections")
    print("NOTE: Mechanical validation cannot verify editorial ingenuity, truth of external "
          "sources, legal use or pixel legibility. Human GitHub-artifact review remains mandatory.")
    return {"candidates": len(candidates), "charts": len(charts), "numeric_audits": calc_checked}

def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path, help="JSON manifest checked against real repo CSVs")
    args = parser.parse_args(argv)
    try:
        with args.manifest.open(encoding="utf-8") as f:
            doc = json.load(f)
        validate(doc)
    except (OSError, json.JSONDecodeError, EditorialPreflightError) as exc:
        parser.exit(1, f"FAIL | {exc}\n")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
