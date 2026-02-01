# Skills Reference

## Overview

Skills are codified legal heuristics - functions that encode complex legal logic into executable, auditable code.

---

## Available Skills

### 1. Dead Man Alive Check (`skills/dead_man_alive_check.py`)

**Purpose**: Detect documents signed after the signatory's death.

**Legal Basis**: Indian Evidence Act, 1872, Section 68

**Usage:**
```python
from skills.dead_man_alive_check import detect_posthumous_signatures

result = detect_posthumous_signatures(
    signatory="Goradhanbhai Suthar",
    death_date="2016-03-15",
    document_date="2025-01-10"
)
# Returns: {"is_fraudulent": True, "days_after_death": 3259, "legal_risk": "HIGH"}
```

| Input | Type | Description |
|:---|:---|:---|
| `signatory` | str | Name of deceased person |
| `death_date` | str | YYYY-MM-DD format |
| `document_date` | str | YYYY-MM-DD format |
| `grace_period_days` | int | Default 7 days |

---

### 2. Section 17 Validator (`skills/section_17_validator.py`)

**Purpose**: Check if a property document was properly registered.

**Legal Basis**: Registration Act, 1908, Section 17(1)(b) + Section 49

**Usage:**
```python
from skills.section_17_validator import validate_section_17_compliance

result = validate_section_17_compliance(
    document_type="Relinquishment Deed",
    property_value=750000,
    registration_number=None,
    is_notarized=True
)
# Returns: {"compliant": False, "legal_status": "VOID_AB_INITIO"}
```

**Key Insight**: Notarization does NOT substitute for registration.

---

## Tested On

- 50,000+ pages of legal documents
- 3 active court cases in Gujarat High Court
- Property disputes spanning 2004-2025

---

## Author

**Swetang Gajjar** - Senior AI Engineer | Legal-Tech Specialist
