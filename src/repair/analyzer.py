from collections import Counter
from typing import Iterable


def find_missing(expected: Iterable[str], actual: Iterable[str]) -> list[str]:
    return sorted(set(expected) - set(actual))


def find_duplicates(actual: Iterable[str]) -> list[str]:
    return sorted(key for key, count in Counter(actual).items() if count > 1)
