# Fraud Detection Skills Library

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**Codified Legal Heuristics for AI-Powered Compliance Auditing**

A collection of specialized forensic analysis functions that encode complex legal logic into executable code.

## 🎯 Available Skills

| Skill | Legal Principle | Use Case |
|:---|:---|:---|
| `dead_man_alive_check.py` | Temporal Entity Resolution | Property fraud, Will contests |
| `section_17_validator.py` | Registration Act 1908, Section 17 | Real estate transactions |

## 🚀 Quick Start

```python
from skills.dead_man_alive_check import detect_posthumous_signatures

result = detect_posthumous_signatures(
    signatory="Goradhanbhai Suthar",
    death_date="2016-03-15",
    document_date="2025-01-10"
)

print(result)
# {"is_fraudulent": True, "days_after_death": 3259, "legal_risk": "HIGH"}
```

## 👤 Author

**Swetang Gajjar** - Senior AI Engineer | Legal-Tech Specialist

- LinkedIn: [@gajjarswetang](https://linkedin.com/in/gajjarswetang)
