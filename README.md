# 🏛️ SDD Framework v3.0

**Specification-Driven Development with Autonomous Governance**

![Status](https://img.shields.io/badge/v3.0-✅%20Production-brightgreen?style=flat-square)
![Tests](https://img.shields.io/badge/Tests-124%2F124%20✅-brightgreen?style=flat-square)

---

## ⚡ Quick Start (Choose Your Role)

### 👨‍💻 **I'm a Developer**
```bash
# 1. Read the governance rules (5 min)
cat .sdd-core/HONEST-CRITIQUE-CONSTITUTION.md

# 2. Follow the 7-phase workflow
cat .sdd-core/spec/guides/onboarding/AGENT_HARNESS.md

# 3. Run tests to verify setup
python3 run-all-tests.py --fail-fast
```

### 🤖 **I'm an AI Agent**
```bash
# 1. Your complete guide
cat .ai-index.md

# 2. Verify your context
python3 -c "print('✅ Ready for autonomous development')"
```

### 📦 **I'm Adding a Project to SDD**
```bash
# 1. Follow the integration checklist (30 min)
cat .sdd-integration/CHECKLIST.md

# 2. Execute 5 steps
cd /path/to/new/project
# See: .sdd-integration/STEP_1.md through STEP_5.md
```

### 🔧 **I'm Using the CLI**
```bash
# Show governance configuration
python3 -m sdd_cli governance load

# Validate integrity
python3 -m sdd_cli governance validate

# Generate agent seed templates
python3 -m sdd_cli governance generate
```

---

## 📚 Documentation (Detailed References)

**For complete documentation, see [docs/INDEX.md](./docs/INDEX.md)**

| Document | Purpose | Time |
|----------|---------|------|
| [.ai-index.md](.ai-index.md) | AI agent entry point | 15 min |
| [.sdd-core/_START_HERE.md](.sdd-core/_START_HERE.md) | Developer entry point | 5 min |
| [.sdd-integration/README.md](.sdd-integration/README.md) | Add projects | 10 min |
| [docs/TEST_RUNNER_GUIDE.md](./docs/TEST_RUNNER_GUIDE.md) | Run all tests | 10 min |
| [docs/CHANGELOG.md](./docs/CHANGELOG.md) | Version history | varies |

---

## 🎯 Your Scenarios

### Testing

**Run all tests from root (7 layers):**
```bash
# Quick check (stop on first failure)
python3 run-all-tests.py --fail-fast

# Full validation with details
python3 run-all-tests.py --verbose

# List test layers
python3 run-all-tests.py --list-layers

# Test specific layer
python3 run-all-tests.py --layer "Wizard"
```

**See:** [docs/TEST_RUNNER_GUIDE.md](./docs/TEST_RUNNER_GUIDE.md) for complete guide

### CLI Commands

**Load governance:**
```bash
python3 -m sdd_cli governance load
```

**Validate integrity:**
```bash
python3 -m sdd_cli governance validate
```

**Generate templates:**
```bash
python3 -m sdd_cli governance generate
```

### Development Workflow

**You have a task → Follow 7 phases:**

```
PHASE 0: Setup (.ai infrastructure) — 20-30 min, one time
PHASE 1: Lock to rules — 15 min
PHASE 2: Check execution state — 5 min
PHASE 3: Choose PATH (bug/feature/complex/multi) — 5 min
PHASE 4: Load context — 10-20 min
PHASE 5: Implement (TDD) — 1-8 hours
PHASE 6: Validate (tests + done criteria) — 15 min
PHASE 7: Checkpoint (document + PR) — 10 min
```

**Details:** [.sdd-core/spec/guides/onboarding/AGENT_HARNESS.md](.sdd-core/spec/guides/onboarding/AGENT_HARNESS.md)

---

## 🏗️ What's Inside

### Core Framework
- ✅ **4 immutable mandates** (CORE governance)
- ✅ **151 customizable guidelines** (CLIENT governance)
- ✅ **SHA-256 fingerprinting** (integrity validation)
- ✅ **7-phase wizard** (fully operational)

### Status
- ✅ **124/124 tests passing** (100% coverage)
- ✅ **CLI ready** (Typer framework)
- ✅ **Documentation complete** (150+ files)
- ✅ **Production-ready**

### Entry Points
- [.sdd-core/](.sdd-core/) — Development workflow
- [.sdd-integration/](.sdd-integration/) — Add projects
- [.sdd-wizard/](.sdd-wizard/) — Runtime artifacts
- [.sdd-compiler/](.sdd-compiler/) — Compiler source

---

## 🔗 Key Files

| File | Use When |
|------|----------|
| [.sdd-core/HONEST-CRITIQUE-CONSTITUTION.md](.sdd-core/HONEST-CRITIQUE-CONSTITUTION.md) | Need governance rules |
| [.sdd-core/spec/guides/onboarding/AGENT_HARNESS.md](.sdd-core/spec/guides/onboarding/AGENT_HARNESS.md) | Implementing a feature |
| [.sdd-core/spec/CANONICAL/decisions/](.sdd-core/spec/CANONICAL/decisions/) | Understand architecture |
| [.sdd-core/NAVIGATION.md](.sdd-core/NAVIGATION.md) | Find documentation |
| [docs/TEST_RUNNER_GUIDE.md](./docs/TEST_RUNNER_GUIDE.md) | Run tests |

---

## 📞 Help

- **Developer:** [.sdd-core/_START_HERE.md](.sdd-core/_START_HERE.md)
- **AI Agent:** [.ai-index.md](.ai-index.md)
- **Adding Project:** [.sdd-integration/README.md](.sdd-integration/README.md)
- **Tests:** [docs/TEST_RUNNER_GUIDE.md](./docs/TEST_RUNNER_GUIDE.md)
- **Emergency:** [.sdd-core/spec/guides/emergency/](.sdd-core/spec/guides/emergency/)

---

## ✅ Status

| Component | Status | Tests |
|-----------|--------|-------|
| Governance Pipeline | ✅ Complete | 13/13 |
| Compiler | ✅ Complete | 15/15 |
| Integration | ✅ Complete | 15/15 |
| Deployment | ✅ Complete | 16/16 |
| Wizard | ✅ Complete | 41/41 |
| CLI | ✅ Complete | 24/24 |
| **Total** | **✅ Ready** | **124/124** |

---

**SDD Framework v3.0** — Production Ready  
**Last Updated:** April 22, 2026  
**License:** MIT
