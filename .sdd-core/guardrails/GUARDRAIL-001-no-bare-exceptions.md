---
id: GUARDRAIL-001
title: "No bare exceptions in production code"
type: GUARDRAIL
criticality: ALERTA
customizable: true
optional: false
category: quality
---

# GUARDRAIL-001: No bare exceptions in production code

## Description

Bare `except:` or `except Exception:` clauses are forbidden in source code (except in tests).
Must catch specific exceptions.

## Implementation

```python
# ❌ BAD
try:
    result = dangerous_operation()
except:
    print("Error!")

# ✅ GOOD
try:
    result = dangerous_operation()
except ValueError as e:
    logger.error(f"Invalid value: {e}")
    raise CustomError(f"Could not process: {e}") from e
```

## Exceptions

- Tests may use bare `except` if needed
- Shell scripts may use catch-all

## Validation

```bash
grep -r "except:\|except Exception:" src/ && exit 1
pytest tests/quality/test_bare_exceptions.py -v
```

## Criticality

- OBRIGATÓRIO: In user-facing APIs
- ALERTA: In internal utilities
- OPCIONAL: In batch jobs
