# Framework Validation Scripts

**Location:** `/tests/scripts/`  
**Purpose:** Automated validation of SDD framework integrity

---

## 📜 Available Scripts

### Phase 0: Agent Onboarding
**File:** `phase-0-agent-onboarding.py`  
**Purpose:** Set up `.ai/` infrastructure for new agents  
**Run:** `python scripts/phase-0-agent-onboarding.py`  
**Creates:**
- `.ai/context-aware/`
- `.ai/runtime/`
- VALIDATION_QUIZ

### Setup Wizard
**File:** `setup-wizard.py`  
**Purpose:** Interactive setup guide  
**Run:** `python scripts/setup-wizard.py`

### Specification Validator
**File:** `spec_validator.py`  
**Purpose:** Validate framework specifications  
**Run:** `python scripts/spec_validator.py`

### Governance Validation
**File:** `validate_governance.py`  
**Purpose:** Check governance rules compliance  
**Run:** `python scripts/validate_governance.py`

### ADR Validation
**File:** `validate_adrs.py`  
**Purpose:** Validate Architecture Decision Records  
**Run:** `python scripts/validate_adrs.py`

### AI-First Validation
**File:** `validate-ia-first.py`  
**Purpose:** Validate AI-first design principles  
**Run:** `python scripts/validate-ia-first.py`

### Quiz Validation
**File:** `validate_quiz.py`  
**Purpose:** Run VALIDATION_QUIZ  
**Run:** `python scripts/validate_quiz.py`

---

## 🔗 Original Location

Original scripts: `EXECUTION/docs/ia/SCRIPTS/`

Scripts are referenced here for convenience. All scripts should:
- Validate framework integrity
- Not modify framework code
- Report results clearly
- Exit with code 0 (success) or 1 (failure)

---

## 🚀 Running Scripts

```bash
cd /home/sergio/dev/sdd-archtecture

# Phase 0 setup
python tests/scripts/phase-0-agent-onboarding.py

# Full validation
python tests/scripts/spec_validator.py
python tests/scripts/validate_governance.py
python tests/scripts/validate_adrs.py
```

---

## 📊 Script Dependencies

All scripts should:
- Run independently (no external dependencies except Python stdlib)
- Use relative paths from repository root
- Report clear success/failure
- Support --help flag

---

**Framework Validation Scripts**  
Part of Phase 5 testing infrastructure
