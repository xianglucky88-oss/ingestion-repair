from .pipeline import diagnose
from .sources import GapSource


def run_fixture(fixture: str) -> dict:
    plan = diagnose(GapSource().read(fixture))
    return {"missing": plan.missing, "duplicates": plan.duplicates,
            "safe_backfill": plan.safe_backfill, "reason": plan.reason}
