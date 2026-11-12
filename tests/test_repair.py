from pathlib import Path
from repair.analyzer import find_duplicates, find_missing
from repair.application import run_fixture
from repair.planner import build_plan
from repair.sources import GapSource


def test_analyzer_and_planner_are_independent():
    data = GapSource().read(str(Path(__file__).parents[1] / "fixtures/gap.json"))
    missing = find_missing(data["expected_keys"], data["actual_keys"])
    duplicates = find_duplicates(data["actual_keys"])
    plan = build_plan(missing, duplicates)
    assert missing == ["2026-11-01T10:05"]
    assert duplicates == ["2026-11-01T10:10"]
    assert plan.safe_backfill is False


def test_application_returns_a_safe_machine_readable_diagnosis():
    result = run_fixture(str(Path(__file__).parents[1] / "fixtures/gap.json"))
    assert result == {"missing": ["2026-11-01T10:05"], "duplicates": ["2026-11-01T10:10"], "safe_backfill": False, "reason": "duplicate keys require reconciliation before backfill"}
