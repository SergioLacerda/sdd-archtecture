---
id: ADR-001
title: "Clean Architecture 8-Layer Pattern"
type: DECISION
criticality: OBRIGATÓRIO
customizable: false
optional: false
category: architecture
---

# ADR-001: Clean Architecture 8-Layer Pattern

## Status
- **Accepted** ✅
- Proposed: 2025-06-15
- Accepted: 2025-06-20

## Context

**Problem**: The system needed clear separation between business logic, adaptation, and infrastructure.

## Decision

**Implement 8-layer Clean Architecture**:

```
Layer 8: Controllers & Interfaces (HTTP, CLI)
Layer 7: DTOs & Serialization (Pydantic models)
Layer 6: Adapters (Implementation of ports)
Layer 5: Error Mapping (Domain → HTTP)
Layer 4: Use Cases (Orchestration)
Layer 3: Ports (Abstraction, interfaces)
Layer 2: Domain (Business logic)
Layer 1: Entities (Domain models)
```

## Consequences

- ✅ Consistency across all features
- ✅ Easy to spot violations
- ⚠️ More layers = more indirection
