# 🚀 Phase 5: Functional Testing

**Purpose:** Validate both INTEGRATION and EXECUTION flows work end-to-end  
**Location:** `/tests/phase_5_testing/`  
**Type:** Fake/mock tests (don't modify framework)  
**Duration:** 10-15 minutes

---

## 📋 What is Phase 5?

Phase 5 runs functional tests to ensure both flows are production-ready:

- **INTEGRATION Flow Test:** Simulates creating a new project (5 steps)
- **EXECUTION Flow Test:** Validates framework documentation structure

Both tests are "fake" - they don't modify the actual framework, just verify it works.

---

## 🚀 Quick Start

### Run all Phase 5 tests

```bash
cd /home/sergio/dev/sdd-archtecture

# Run INTEGRATION flow test
python tests/phase_5_testing/test_integration_flow.py

# Run EXECUTION flow test  
python tests/phase_5_testing/test_execution_flow.py

# Or run both
bash tests/phase_5_testing/run_all_tests.sh  # (if script exists)
```

---

## 📊 Test Details

### INTEGRATION Flow Test (`test_integration_flow.py`)

Tests the 5-step INTEGRATION onboarding process:

1. **STEP 1:** Setup project structure
   - Creates: `.github/`, `.vscode/`, `.cursor/`, `scripts/`, `.ai/`
   
2. **STEP 2:** Copy templates  
   - Validates: `INTEGRATION/templates/` has all 8 template files
   
3. **STEP 3:** Configure `.spec.config`
   - Creates: `.spec.config` with `spec_path` pointing to framework
   
4. **STEP 4:** Run validation
   - Creates: `.ai/context-aware/`, `.ai/runtime/`
   
5. **STEP 5:** Commit to git
   - Verifies: All files ready for `git add`

**Expected Result:**
```
✅ STEP 1: Setup structure - PASS
✅ STEP 2: Copy templates - PASS
✅ STEP 3: Configure .spec.config - PASS
✅ STEP 4: Run validation - PASS
✅ STEP 5: Commit to git - PASS

✅ INTEGRATION FLOW: READY FOR PRODUCTION
```

---

### EXECUTION Flow Test (`test_execution_flow.py`)

Tests the 7-phase EXECUTION workflow structure:

1. **Entry Points**
   - `README.md`, `_START_HERE.md`, `NAVIGATION.md`, `INDEX.md`
   
2. **CANONICAL Layer** (immutable authority)
   - Constitution, Rules, Conventions
   - ADRs (6+ decisions)
   - Specifications (definition-of-done, communication, etc.)
   
3. **Guides Layer** (operational)
   - Onboarding guides (11+ files)
   - Operational guides (5+ files)
   - Emergency procedures (6+ files)
   - Reference docs (FAQ, GLOSSARY, etc.)
   
4. **Runtime Layer** (search indices)
   - `search-keywords.md`
   - `spec-canonical-index.md`
   - `spec-guides-index.md`
   
5. **Custom Layer** (project-specific)
   - Project directories in `custom/`
   
6. **Markdown Links**
   - Validates link format in key files
   
7. **AI-First Design**
   - `.ai-index.md`, `README.md`, `.spec.config` at root

**Expected Result:**
```
✅ Entry Points - PASS
✅ CANONICAL Layer - PASS
✅ Guides Layer - PASS
✅ Runtime Layer - PASS
✅ Custom Layer - PASS
✅ Markdown Links - PASS
✅ AI-First Design - PASS

✅ EXECUTION FLOW: READY FOR PRODUCTION
```

---

## 🔍 Understanding Test Output

### Green Checkmarks ✅
Test passed - framework is good

### Red X ❌
Test failed - there's an issue

### Yellow Warning ⚠️
Optional component missing (not critical)

### Examples

```bash
# All good
✅ INTEGRATION FLOW: READY FOR PRODUCTION

# Needs attention  
❌ Entry point missing: _START_HERE.md

# Optional warning
⚠️ FAQ.md (optional guide file)
```

---

## 📈 Pass Criteria

- **INTEGRATION Flow:** All 5 steps must pass (100%)
- **EXECUTION Flow:** 90%+ of checks must pass
  - All critical: entry points, CANONICAL layer, Guides, Runtime
  - Optional: some specification files may be missing

---

## 🔧 Manual Testing (Alternative)

If you prefer to test manually:

### INTEGRATION Flow Manual Test

```bash
# Create a test directory
mkdir /tmp/test-project
cd /tmp/test-project

# Follow INTEGRATION/CHECKLIST.md step-by-step
# - Step 1: Create directories
# - Step 2: Copy templates  
# - Step 3: Edit .spec.config
# - Step 4: Run validation script
# - Step 5: Verify git staging

# Verify success
ls -la .spec.config .ai/context-aware/
```

### EXECUTION Flow Manual Test

```bash
# Start at EXECUTION entry point
cat EXECUTION/_START_HERE.md

# Follow a scenario (e.g., "New Developer")
# Verify you can navigate to key docs

# Test search keywords
grep "PHASE" EXECUTION/docs/ia/runtime/search-keywords.md
```

---

## 📝 Test Results Log

After running tests, results are printed to console. To save them:

```bash
# Save INTEGRATION test results
python tests/phase_5_testing/test_integration_flow.py | tee /tmp/integration_test.log

# Save EXECUTION test results
python tests/phase_5_testing/test_execution_flow.py | tee /tmp/execution_test.log
```

---

## 🚀 Next: Phase 6

Once Phase 5 tests pass ✅:

1. Review test output
2. Fix any failures
3. Re-run tests until all pass
4. Proceed to Phase 6: Final Commit

---

## 🆘 Troubleshooting

### Test fails: "Entry point missing: _START_HERE.md"

**Solution:**
```bash
# Check if file exists
ls EXECUTION/_START_HERE.md

# If missing, it's a structural issue
# Review PHASE_3_4_COMPLETE.md for status
```

### Test fails: "Template not found"

**Solution:**
```bash
# Check INTEGRATION/templates/
ls -la INTEGRATION/templates/

# Verify .spec.config exists
ls INTEGRATION/templates/.spec.config
```

### Python ImportError

**Solution:**
```bash
# Make sure you're running from repo root
cd /home/sergio/dev/sdd-archtecture

# Check Python version (need 3.8+)
python3 --version
```

---

## 📊 Quality Gate

Phase 5 tests are your quality gate before deployment:

✅ Pass all tests → Framework is production-ready  
❌ Failures → Fix issues, re-test

---

**Phase 5: Functional Testing**  
Run tests • Review results • Fix issues • Proceed to Phase 6

Generated: April 19, 2026
