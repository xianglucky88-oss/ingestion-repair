from collections.abc import Iterable
from .analyzer import find_duplicates, find_missing
from .planner import RepairPlan, build_plan


def diagnose(data: dict) -> RepairPlan:
    """编排分析器和计划器；不把结构异常误判为可安全补采。"""
    expected = data.get("expected_keys")
    actual = data.get("actual_keys")
    if not isinstance(expected, list) or not isinstance(actual, list):
        raise ValueError("expected_keys and actual_keys must be lists")
    if any(not isinstance(key, str) or not key for key in expected + actual):
        raise ValueError("diagnostic keys must be non-empty strings")
    missing = find_missing(expected, actual)
    duplicates = find_duplicates(actual)
    return build_plan(missing, duplicates)
