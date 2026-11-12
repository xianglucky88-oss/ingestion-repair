import json
from pathlib import Path
from typing import Any


class GapSource:
    """只负责读取断层诊断输入。"""

    def read(self, path: str) -> dict[str, Any]:
        value = json.loads(Path(path).read_text(encoding="utf-8"))
        if not isinstance(value, dict):
            raise ValueError("gap fixture must contain an object")
        return value
