---
id: RULE-001
title: "All handlers must implement error handling"
type: RULE
criticality: OBRIGATÓRIO
customizable: false
optional: false
category: quality
---

# RULE-001: All handlers must implement error handling

## Description

Every request handler must explicitly handle errors and return appropriate HTTP status codes.

## Specification

1. Try-catch blocks must be present
2. Errors must be logged
3. HTTP status codes must be appropriate
4. User-facing messages must not leak internal details

## Validation

```bash
pytest tests/contracts/test_error_handling.py -v
```

## Related

- ADR-001 (Layer 5: Error Mapping)
- GUARDRAIL-001 (No bare exceptions)
