from dataclasses import dataclass


@dataclass(frozen=True)
class RepairPlan:
    missing: list[str]
    duplicates: list[str]
    safe_backfill: bool
    reason: str


def build_plan(missing: list[str], duplicates: list[str]) -> RepairPlan:
    if duplicates:
        return RepairPlan(missing, duplicates, False, "duplicate keys require reconciliation before backfill")
    if not missing:
        return RepairPlan([], [], False, "no missing keys")
    return RepairPlan(missing, [], True, "missing keys are unique and eligible for review")
