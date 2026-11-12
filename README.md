# 采集数据断层诊断与安全补采工具

按单一职责拆分为：`sources.py` 读取输入，`analyzer.py` 计算缺失和重复，`planner.py` 决定补采安全性，`pipeline.py` 编排，`application.py` 负责组装，`cli.py` 负责输出。

默认只读取本地 fixture，不访问真实数据源；核心验证覆盖缺失识别、重复识别和不安全补采阻断。

## 外部依赖类型与版本

- Python 3.11+
- pytest 8.3.x（开发/测试）
