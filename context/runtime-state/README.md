# 📊 Runtime State — Framework Discovery & Analysis

**Purpose:** Track ongoing discoveries, analysis, and metrics about the framework

**Structure:**
```
context/runtime-state/
├── analysis/
│   └── RPG_NARRATIVE_SERVER_GAP_ANALYSIS.md (Framework gap findings)
├── task-progress/
│   └── [In-progress work]
└── metrics/
    └── [Quality metrics, trends]
```

## 📁 analysis/ — Discoveries & Audits

**Purpose:** Store findings from audits, reverse-dependency checks, and pattern analysis

**What goes here:**
- Framework gap analysis reports
- Pattern extraction from target projects
- Reverse dependency verification
- Architecture compliance trends

**Example:**
- `RPG_NARRATIVE_SERVER_GAP_ANALYSIS.md` - What patterns rpg-narrative-server uses that framework needs to document

**When to create:**
- Quarterly framework audits
- When analyzing new target projects
- When extracting patterns from implementations

---

## 📋 task-progress/ — Active Work

**Purpose:** Track current development tasks and blockers

**What goes here:**
- In-progress features/fixes
- Blockers and dependencies
- Weekly progress snapshots

**When to create:**
- When starting feature work
- When tracking multi-session tasks

---

## 📈 metrics/ — Quality Tracking

**Purpose:** Track framework quality trends over time

**What goes here:**
- Test coverage trends
- Architecture violation rates
- Compliance rates per project
- Documentation completeness %

**When to create:**
- After each major release
- Quarterly reviews

---

## ✅ How This Differs from `.ai/context-aware/`

| Aspect | `/context/runtime-state/` | `.ai/context-aware/` |
|--------|---------------------------|---------------------|
| **Purpose** | Framework discovery | Project-specific runtime |
| **Owner** | SDD framework team | Target project team |
| **Content** | Audit findings, gaps | Task progress, analysis |
| **Frequency** | Quarterly, ad-hoc | During development |
| **Lifespan** | Long-term (reference) | Session-based (ephemeral) |

---

**Authority:** SPEC v2.1 Context Management Standards  
**Updated:** April 19, 2026
