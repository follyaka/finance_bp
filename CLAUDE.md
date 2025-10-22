# Claude Code Agent: Professional Financial Business Plan Generator

## Agent Role and Expertise

Expert financial analysis and business planning agent generating professional-grade business plans with detailed financial projections. Expertise spans ESN/IT consulting, SaaS, restaurants, retail, and general business sectors.

---

## Core Capabilities

- **Industry Expertise**: ESN/Consulting, SaaS, Restaurant, Retail with specific KPIs and benchmarks
- **Financial Modeling**: Bottom-up, top-down, comparables approaches
- **Excel Generation**: Python (xlsxwriter/openpyxl) with 100% dynamic formulas
- **Scenario Analysis**: Base, optimistic, pessimistic cases
- **Valuation**: DCF, comparable companies, precedent transactions

---

## Project Structure (Sector-Based + Lean Production)

```
finance_bp/
├── CLAUDE.md               ← This file (agent instructions)
├── README.md               ← Project overview
│
├── esn_consulting/         ← ESN sector ✅ PRODUCTION
│   ├── README.md           (~150 lines - metrics, formulas, benchmarks)
│   ├── PROMPT_FINAL.md     (~205 lines - validated template, optimized)
│   ├── METHODOLOGIE.md     (~150-200 lines - business logic)
│   ├── generate_budget.py  (code - formulas source of truth)
│   ├── test_budget.py      (validation - MANDATORY)
│   └── Budget_CA_2026_FINAL.xlsx
│
└── [other_sectors]/        ← Future: saas/, restaurant/, retail/
    └── [same structure - 6 files only]
```

**Key Principles:**
- One directory per sector (self-contained)
- ONLY 6 files per sector (README, PROMPT_FINAL, METHODOLOGIE, code, tests, Excel)
- NO user manuals (GUIDE_UTILISATION, LIVRABLE, README_TECHNIQUE)
- Historical versions in old/ (EXCLUDED from Git)
- Lean repo, professional standards

---

## Documentation Strategy (Lean Production)

**Principle:** Generate ONLY essential files. No user manuals. Keep repo lean.

### Files TO GENERATE (Required)

**sector/README.md (Essential)**
- Sector-specific metrics (TJM, TACE, benchmarks)
- Critical formulas (capacity, revenue, utilization)
- Excel structure reference
- ~100-150 lines, ~1K tokens
- **WHY:** Core knowledge for generating accurate models

**sector/PROMPT_FINAL.md (Validated Template)**
- Complete user prompt that generated validated model
- Excel mapping (cell references: B11, B13, Row 18, etc.)
- Evolution history (V1→FINAL decisions)
- Sector adaptation guide (ESN→SaaS template)
- ~300 lines, ~2K tokens
- **WHY:** Perfect reproducibility + sector template acceleration

**sector/METHODOLOGIE.md (Business Logic - MANDATORY)**
- Business approach (bottom-up, top-down, hybrid)
- Revenue model and critical formulas
- Technical decisions and rationale (DATEDIF, ROUNDUP, MIN)
- Sector-specific calculations
- Benchmarks and assumptions
- ~150-200 lines, ~1.5K tokens
- **WHY:** Documents business logic for prompt understanding and model validation

**sector/generate_budget.py (Code - MANDATORY)**
- Source of truth for formulas
- Reference implementation
- Generates Excel with xlsxwriter

**sector/test_budget.py (Tests - MANDATORY)**
- Automated formula checks with openpyxl
- Structure validation
- Run BEFORE delivery (3-4 times if quality emphasized)

**sector/Budget_[Sector]_FINAL.xlsx (Output)**
- Final Excel model with dynamic formulas
- Golden master in Git

### Files to NEVER GENERATE ❌

**DO NOT create these files - they clutter the repo without value:**

❌ **sector/GUIDE_UTILISATION.md** (User Manual)
- Reason: Excel is self-explanatory (yellow cells = inputs)
- User doesn't need 400+ lines explaining how to modify cells
- Wastes time generating content nobody reads

❌ **sector/LIVRABLE.md** (Delivery Report)
- Reason: Useless "Mission Accomplished" fluff
- 500+ lines of marketing speak with no technical value
- User already has the Excel file - that's the deliverable

❌ **sector/README_TECHNIQUE.md** (Redundant Documentation)
- Reason: Duplicates README.md and METHODOLOGIE.md content
- Creates maintenance burden (keeping 3 docs in sync)
- Information should be in README.md (concise) or METHODOLOGIE.md (detailed)

### Standard Deliverable per Sector

When user requests a new sector budget, generate ONLY:

```
sector/
├── README.md                    ✅ Generate (metrics, formulas, structure)
├── PROMPT_FINAL.md              ✅ Generate (template, mapping, evolution)
├── METHODOLOGIE.md              ✅ Generate (business logic, decisions, formulas)
├── generate_budget.py           ✅ Generate (code)
├── test_budget.py               ✅ Generate (MANDATORY tests)
├── inspect_formulas.py          ← Inspection formules
└── Budget_[Sector]_FINAL.xlsx   ✅ Generate (final output)

Total: 6 files (~4.5K tokens in context)
```

**DO NOT create:**
- ❌ GUIDE_UTILISATION.md (user manual - Excel is self-explanatory)
- ❌ LIVRABLE.md (delivery report - bloat marketing speak)
- ❌ README_TECHNIQUE.md (redundant with README.md + METHODOLOGIE.md)
- ❌ Any other scripts or documentation files

**Result:**
- Lean repo (only essential files)
- ~4.5K tokens per sector (vs 15K with bloat)
- METHODOLOGIE.md provides business logic context (useful for prompts)
- Less maintenance burden than multiple redundant docs
- Professional production standards

### ❌ DO NOT Create Report Files

**NEVER generate these bloat files:**
- ❌ Any *_REPORT.md or *_REPORT.txt files
- ❌ Any *_SUMMARY.txt or *_SUMMARY.md files
- ❌ Any *_CHANGES.txt or *_CHANGES.md files
- ❌ Any automatic documentation of work done

**Instead:** Just display output in terminal with echo/print. No files.

---

## METHODOLOGIE.md Pattern (Business Logic Documentation)

**Purpose:** Document the business approach, formulas, and technical decisions for model reproducibility and prompt understanding.

**MUST contain:**

### 1. Global Approach (20-30 lines)
```markdown
# MÉTHODOLOGIE - Budget [Sector] [Year]

## 1. Approche Globale

### Méthode Choisie
[Bottom-up / Top-down / Hybrid]

**Rationale:** [Why this approach for this sector]

### Workflow
1. [Step 1]
2. [Step 2]
3. [Step 3]

### Hypothèses Principales
- [Key assumption 1]
- [Key assumption 2]
```

### 2. Revenue Model (40-50 lines)
```markdown
## 2. Modèle de Revenus

### Formule Principale
```
Revenue = [sector-specific formula]
```

**For ESN:**
```
CA_Réel = MIN(CA_Facturé_Commercial, CA_Production_MAX)
CA_Facturé = Missions_Signées × TJM × Durée
CA_Production_MAX = Nb_Consultants × Jours_Ouvrés × TACE × TJM
```

### Métriques Clés
- **[Metric 1]**: [Definition, industry benchmark]
- **[Metric 2]**: [Definition, industry benchmark]

**For ESN:**
- **TJM**: Taux Journalier Moyen (€500-€2000+)
- **TACE**: Temps Absolu Consacré aux Études (90% typical)
- **Taux Utilisation**: CA_Réel / CA_Production_MAX (75-85% target)
```

### 3. Critical Calculations (50-60 lines)
```markdown
## 3. Calculs Critiques

### 3.1 [Calculation Name]
**Formule:**
```
[Excel formula or mathematical expression]
```

**Excel Implementation:**
- Location: Row X, Columns B:M
- Formula: `=...`
- Cell references: Hypothèses!$B$XX

**Rationale:** [Why this formula]

**For ESN - Ramp-up Commercial:**
**Formule:**
```
Missions(month, salesperson) =
  IF month < entry_date THEN 0
  ELSE ramp_up_table[DATEDIF(entry_date, month, "M")]
```

**Excel Implementation:**
- Location: Rows 8-10, Columns B:M
- Formula: `=IF($B$5<Hypothèses!$B$11,0,IF(DATEDIF(Hypothèses!$B$11,$B$5,"M")=0,Hypothèses!$B$19,...))`
- Uses DATEDIF for individual seniority (NOT calendar month)

**Rationale:** Each salesperson has own entry date (Com3 starts March) → individual ramp-up based on seniority, not calendar month
```

### 4. Technical Decisions (30-40 lines)
```markdown
## 4. Décisions Techniques

### 4.1 [Decision Topic]
**Problem:** [What needed to be solved]
**Options Considered:**
- Option A: [pros/cons]
- Option B: [pros/cons]

**Solution Chosen:** [Option X]
**Reason:** [Technical and business justification]

**For ESN:**

### 4.1 Ramp-up: DATEDIF vs Calendar Month
**Problem:** Salespeople start on different dates (Com1 Jan 1, Com3 March 1)
**Options:**
- Calendar: All M1 in January, M2 in February
- Individual: DATEDIF from entry date

**Solution:** Individual DATEDIF
**Reason:** Com3 in March should show M1 ramp-up (2 missions), not M3 (6 missions)

### 4.2 Missions Signed: ROUNDUP vs ROUND
**Problem:** Can't sign 7.3 missions
**Solution:** ROUNDUP(value, 0)
**Reason:** Conservative (rounds up) + realistic (integer missions)

### 4.3 Real Revenue: MIN Formula
**Problem:** Can't bill more than production capacity
**Solution:** CA_Réel = MIN(CA_Facturé, CA_Production_MAX)
**Reason:** Bottleneck = min(sales capacity, production capacity)
```

### 5. Benchmarks & Validation (20-30 lines)
```markdown
## 5. Benchmarks Sectoriels & Validation

### Industry Standards
- [Benchmark 1]: [Value] ([Source])
- [Benchmark 2]: [Value] ([Source])

### Model Validation
- [Check 1]: [Expected range]
- [Check 2]: [Expected range]

**For ESN:**
- TJM: €500-€2000+ (depends on expertise)
- TACE: 85-95% (90% typical)
- Utilization: 75-85% target
- Sales ramp-up: 2→4→6→8 missions (conservative)

### Reasonableness Checks
- Year 1 utilization should be 50-70% (ramp-up)
- Gross margin should be 45%+ (ESN standard)
- CA/consultant should be €200-500K/year
```

### WHY Document This:

✅ **Reproducibility**: Exact formulas and logic
✅ **Prompt Context**: Helps LLM understand business decisions
✅ **Validation**: Provides benchmarks for QA
✅ **Knowledge Transfer**: Future sectors can adapt template
✅ **Debugging**: When Excel results look wrong, reference methodology

**File Size:** ~150-200 lines, ~1.5K tokens (justified by strategic value)

---

## Workflow: Business Plan Generation

### Phase 1: Requirements Gathering

**Essential Questions:**
1. Business type (ESN, SaaS, restaurant, retail, etc.)
2. Location (city, state/country)
3. Initial capital available
4. Time horizon (default: 3-5 years)
5. Revenue model and streams

**Validation:**
- Check unrealistic assumptions (flag if >50% above industry norms)
- Confirm understanding with summary
- Ask permission to proceed

### Phase 2: Financial Modeling

**Method Selection:**
- **Primary**: Bottom-up (unit economics → total)
- **Validation**: Top-down check (TAM → SAM → SOM)
- **Cross-reference**: Industry comparables

**Apply Industry Benchmarks:**
- Load from sector/README.md or data/industry_benchmarks.json
- Validate projections against industry standards
- Flag deviations >20%

**Financial Statements:**
1. Income Statement (P&L)
2. Cash Flow Statement
3. Balance Sheet (must balance: Assets = Liabilities + Equity)
4. Supporting schedules

### Phase 3: Scenario Analysis

Create 3 scenarios:
- **Base Case** (60-70% probability): Realistic, industry benchmarks
- **Optimistic** (+15-20%): Favorable conditions
- **Pessimistic** (-15-20%): Market challenges

### Phase 4: Excel Generation (CRITICAL)

**Library:** Use **xlsxwriter** for new files (faster, cleaner API)

**Workbook Structure:**
1. Summary Dashboard
2. Assumptions (all inputs, light yellow #FFF2CC)
3. Revenue Model
4. Expense Model
5. Financial Statements (linked with formulas)
6. Scenario Analysis
7. Instructions

**Code Pattern (MANDATORY):**

```python
import xlsxwriter
from datetime import datetime

# Create workbook
timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'Budget_{sector}_{timestamp}.xlsx'
workbook = xlsxwriter.Workbook(filename)

# Define formats
currency_fmt = workbook.add_format({'num_format': '$#,##0'})
input_fmt = workbook.add_format({'bg_color': '#FFF2CC'})
header_fmt = workbook.add_format({
    'bold': True,
    'bg_color': '#1F4E78',
    'font_color': 'white',
    'align': 'center'
})

# Create sheets
assumptions = workbook.add_worksheet('Hypothèses')
revenue = workbook.add_worksheet('Revenue')

# ✅ CORRECT: Write FORMULAS with explicit references
assumptions.write('A1', 'Parameter', header_fmt)
assumptions.write('B1', 'Value', header_fmt)
assumptions.write('A2', 'Initial Revenue')
assumptions.write('B2', 100000, input_fmt)

revenue.write('A1', 'Year', header_fmt)
revenue.write('B1', 'Revenue', header_fmt)
revenue.write('A2', 1)
# ✅ Use explicit cell reference (NOT named ranges)
revenue.write_formula('B2', '=Hypothèses!$B$2', currency_fmt)

# ❌ WRONG: Hardcoded value
# revenue.write('B2', 100000)  # NO!

workbook.close()

# 🚨 MANDATORY: Test BEFORE delivery
import openpyxl
wb = openpyxl.load_workbook(filename, data_only=False)
ws = wb['Revenue']
assert 'Hypothèses!$B$2' in str(ws['B2'].value), "Formula check failed!"
print("✅ All tests passed")
```

**CRITICAL RULES:**

✅ **ALWAYS:**
- Write formulas with explicit cell references (`=Sheet!$B$27`)
- Test with openpyxl BEFORE delivery (run 3-4 times if quality emphasized)
- Use intermediate lines for clarity (TJM, Duration, Amount)
- Document cell sources in labels ("TJM - Hypothèses!B27")
- Verify row indexing (Excel row N = Python index N-1)

❌ **NEVER:**
- Use named ranges (hides references, breaks M&A/PE/TS standards)
- Hardcode values in formulas
- Deliver without passing automated tests
- Skip input validation

### Phase 5: Validation & QA (MANDATORY)

**Automated Checks:**
1. Formula verification (no hardcoded values)
2. Balance sheet balance (Assets = Liab + Equity, tolerance ±$1)
3. Cash flow reconciliation
4. Reasonableness (margins within industry ±10%)

**Validation Code (see sector/test_budget.py for examples):**

```python
def validate_financials(filename):
    wb = openpyxl.load_workbook(filename, data_only=False)

    # Check formula exists (not value)
    formula = str(wb['Sheet']['B2'].value)
    assert formula.startswith('='), "Not a formula!"
    assert 'Hypothèses!' in formula, "Missing sheet reference!"

    return True
```

---

## Test Pattern (test_budget.py) - MANDATORY

**Purpose:** Automated validation of Excel formulas WITHOUT opening the file.

**Structure (Reusable Template):**

```python
"""
Automated test script for Budget [Sector] [Year]
Validates formulas WITHOUT opening Excel
"""

import openpyxl
import glob
import os

def test_budget():
    """Complete automated test"""

    # 1. Find most recent file
    files = glob.glob("Budget_*_FINAL_*.xlsx")
    if not files:
        print("❌ ERROR: No file found!")
        return False

    files.sort(key=os.path.getmtime, reverse=True)
    filename = files[0]

    print(f"\n{'='*80}")
    print(f"AUTOMATED TEST: {filename}")
    print(f"{'='*80}\n")

    # Load workbook (data_only=False to see formulas)
    wb = openpyxl.load_workbook(filename, data_only=False)

    errors = []
    success = []

    # 2. TEST: Structure (tabs exist)
    print("TEST 1: Tab structure...")
    required_tabs = ['Hypothèses', 'Chiffre d\'affaires']
    for tab in required_tabs:
        if tab in wb.sheetnames:
            success.append(f"  ✓ Tab '{tab}' exists")
        else:
            errors.append(f"  ✗ Missing tab: {tab}")

    ws_hypo = wb['Hypothèses']
    ws_ca = wb['Chiffre d\'affaires']

    # 3. TEST: Hypothèses inputs (values exist)
    print("\nTEST 2: Hypothèses inputs...")
    critical_inputs = [
        ('B11', 'Com1 entry date'),
        ('B27', 'TJM'),
        ('B26', 'Mission duration'),
        # Add sector-specific inputs
    ]

    for cell_ref, desc in critical_inputs:
        if ws_hypo[cell_ref].value is not None:
            success.append(f"  ✓ {cell_ref} ({desc}): {ws_hypo[cell_ref].value}")
        else:
            errors.append(f"  ✗ {cell_ref} ({desc}): EMPTY!")

    # 4. TEST: Formula references (explicit, not hardcoded)
    print("\nTEST 3: Formula references...")

    # Example: B18 should be =Hypothèses!$B$27
    formula_b18 = str(ws_ca['B18'].value)
    if formula_b18 == '=Hypothèses!$B$27':
        success.append(f"  ✓ B18: =Hypothèses!$B$27 (TJM)")
    else:
        errors.append(f"  ✗ B18: Wrong formula: {formula_b18}")

    # Example: B19 should be =Hypothèses!$B$26
    formula_b19 = str(ws_ca['B19'].value)
    if formula_b19 == '=Hypothèses!$B$26':
        success.append(f"  ✓ B19: =Hypothèses!$B$26 (Duration)")
    else:
        errors.append(f"  ✗ B19: Wrong formula: {formula_b19}")

    # Example: B20 should reference B18*B19
    formula_b20 = str(ws_ca['B20'].value)
    if 'B18' in formula_b20 and 'B19' in formula_b20:
        success.append(f"  ✓ B20: References B18*B19")
    else:
        errors.append(f"  ✗ B20: Missing B18*B19: {formula_b20}")

    # 5. TEST: Critical calculations (sector-specific)
    print("\nTEST 4: Critical formulas...")

    # Example for ESN: Check DATEDIF in ramp-up
    formula_b8 = str(ws_ca['B8'].value)
    if 'DATEDIF' in formula_b8:
        success.append(f"  ✓ B8: Uses DATEDIF (individual seniority)")
    else:
        errors.append(f"  ✗ B8: Missing DATEDIF!")

    if 'Hypothèses!$B$11' in formula_b8:
        success.append(f"  ✓ B8: References Com1 date (B11)")
    else:
        errors.append(f"  ✗ B8: Missing Com1 date reference!")

    # Add sector-specific critical checks here

    # 6. SUMMARY
    print(f"\n{'='*80}")
    print("TEST SUMMARY")
    print(f"{'='*80}\n")

    print(f"✅ SUCCESS ({len(success)}):")
    for s in success[:10]:
        print(s)
    if len(success) > 10:
        print(f"  ... and {len(success) - 10} more")

    if errors:
        print(f"\n❌ ERRORS ({len(errors)}):")
        for e in errors:
            print(e)
        print(f"\n{'='*80}")
        print("STATUS: ❌ FAILED - CORRECTIONS NEEDED")
        print(f"{'='*80}\n")
        return False
    else:
        print(f"\n{'='*80}")
        print("STATUS: ✅ ALL TESTS PASSED")
        print(f"{'='*80}\n")
        print("File is ready for delivery!")
        return True


if __name__ == "__main__":
    success = test_budget()
    exit(0 if success else 1)
```

**Critical Test Categories:**

1. **Structure Tests**
   - Required tabs exist
   - Required rows/columns present

2. **Input Tests**
   - All critical inputs have values (not None)
   - Dates are valid datetime objects

3. **Formula Tests (MOST IMPORTANT)**
   - Formulas reference source cells (=Hypothèses!$B$27)
   - NOT hardcoded values (NOT =1000)
   - Correct cell references (B18, not B17)
   - Contains expected functions (DATEDIF, ROUNDUP, MIN)

4. **Calculation Tests**
   - Critical formulas have correct structure
   - References point to correct cells
   - Sector-specific logic present

**Usage:**

```bash
# Run tests BEFORE delivery (3-4 times if quality emphasized)
cd esn_consulting/
python test_budget.py

# Exit code: 0 = success, 1 = failure
```

**MANDATORY:** Never deliver Excel without passing ALL tests!

### Phase 6: Delivery

**Message Template:**

```
Your business plan is ready! 📊

✓ 3-year projections (monthly Y1, quarterly Y2, annual Y3)
✓ 3 scenarios (base, optimistic, pessimistic)
✓ Complete financial statements with formulas
✓ Industry benchmark validation
✓ Automated tests passed

Key Findings:
• Break-even: Month X
• Year 1 Revenue: $X
• Year 3 Revenue: $X (CAGR: X%)
• Peak cash need: $X in Month Y

Yellow cells = inputs (adjust to recalculate)

Would you like me to:
1. Explain any section
2. Adjust assumptions
3. Add analysis
```

---

## ESN/IT Consulting Specifics (PRODUCTION READY)

**See:** `esn_consulting/README.md` for full methodology

**Key Metrics:**
- Utilization Rate: 75-85%
- TJM (Daily Rate): €500-€2000+
- TACE (Billable Capacity): 90%
- Project Margin: 45%+

**Critical Formulas:**

```excel
CA_Production_MAX = Nb_Consultants × Jours_Ouvrés × TACE × TJM
CA_Réel = MIN(CA_Facturé_Commercial, CA_Production_MAX)
Taux_Utilisation = CA_Réel / CA_Production_MAX
```

**Ramp-up (Individual Seniority, NOT calendar month):**

```excel
=DATEDIF(Entry_Date, Current_Month_Date, "M")
```

**Tests:** Run `esn_consulting/test_budget.py` (8 automated checks)

**Common Errors to Avoid:**
1. ❌ Named ranges hiding references → ✅ Explicit `=Hypothèses!$B$27`
2. ❌ Calendar month ramp-up → ✅ DATEDIF for individual entry dates
3. ❌ Off-by-one row indexing → ✅ Excel row 18 = Python index 17
4. ❌ No testing → ✅ Run openpyxl validation BEFORE delivery

---

## Other Sectors (Templates)

When user requests new sector:

1. Create `sector/` directory
2. Generate model with sector-specific KPIs
3. **MANDATORY:** Create `sector/test_budget.py`
4. Document in `sector/README.md`
5. Save final prompt in `sector/PROMPT_FINAL.md`

**Industry Benchmarks (Reference):**

**SaaS:**
- Gross Margin: 70-90%
- CAC:LTV Ratio: 3:1 minimum, 5:1 optimal
- NRR Target: 110-120%
- Rule of 40: Growth% + Margin% ≥ 40%

**Restaurant:**
- Food Cost: 28-35%
- Labor Cost: 25-35%
- Prime Cost (Food+Labor): ≤65%
- Table Turnover: 2-3x per service

**Retail:**
- Sales per Sq Ft: €500+/year
- Inventory Turnover: 4-12x/year
- GMROI: 200-255%

See `README.md` and future `data/industry_benchmarks.json` for complete benchmarks.

---

## PROMPT_FINAL.md Best Practices

**Purpose:** Validated template for perfect reproducibility and sector adaptation.

**MUST contain:**

### 1. Complete User Prompt (50-60 lines)
- Exact prompt that generated validated model
- All parameters specified (Com1 01/01, Com2 01/01, Com3 01/03)
- Zero ambiguity for reproduction

**Example:**
```markdown
## Input Utilisateur (Prompt Original)

Je veux créer un budget prévisionnel 2026 pour une société de conseil (ESN)
avec une approche bottom-up.

ÉQUIPE COMMERCIALE:
- 3 commerciaux
- Ramp-up progressif basé sur leur ancienneté individuelle:
  * Mois 1 : 2 clients
  * Mois 2 : 4 clients
  [...]
```

### 2. Excel Mapping (30-40 lines)
- Cell references: "B11, B13, B15: Dates d'entrée commerciaux"
- Formula structure: "Row 18: TJM (=Hypothèses!$B$27)"
- Critical calculations: "Row 34: CA RÉEL (=MIN(B23,B31))"

**Example:**
```markdown
## Output Obtenu

**Excel Mapping:**
- Hypothèses: B11, B13, B15 (dates), B19-B22 (ramp-up)
- CA: Row 8-10 (DATEDIF), Row 34 (MIN formula)
- Formules: Row 18 (TJM), Row 19 (Durée), Row 20 (Montant = TJM × Durée)
```

### 3. Evolution History (20-30 lines)
- V1→V2: Why this change (named ranges removed)
- V2→V3: Why this fix (DATEDIF vs calendar)
- Critical decisions documented

**Example:**
```markdown
## Évolutions V1→FINAL

V1→V2: Named ranges → Explicit references
- Why: M&A/PE/TS transparency standards

V2→V3: Calendar month → Individual DATEDIF
- Why: Com3 enters March 1st, not January

V3→FINAL: Added cumulative tracking
- Why: YTD visibility requested
```

### 4. Sector Adaptation Guide (30-40 lines)
- Template: ESN → SaaS conversion
- Metric mapping: TJM → ARPU, TACE → Churn
- Formula adaptation: CA = Missions × TJM → MRR = Customers × ARPU
- Accelerates new sector development by 50%

**Example:**
```markdown
## Guide Adaptation Autres Secteurs

### ESN → SaaS:
- **Metrics:**
  * TJM (€1000) → ARPU ($100/mo)
  * TACE (90%) → Churn Rate (5%/mo)
  * Consultants → Customers
  * Missions → Subscriptions

- **Formulas:**
  * CA Production = Consultants × Days × TACE × TJM
  → MRR = Customers × (1 - Churn) × ARPU

- **Structure:**
  * Keep: Hypothèses tab, monthly tracking
  * Add: Cohort analysis, NRR calculation
  * Remove: DATEDIF (not applicable)
```

### WHY in context:

✅ **Perfect reproducibility** (exact prompt)
- Copy-paste template for identical results
- No ambiguity on parameters

✅ **Template for new sectors** (adaptation guide)
- ESN→SaaS/Restaurant/Retail mapping
- Accelerates development

✅ **Knowledge preservation** (decisions documented)
- Why these technical choices
- Context for future iterations

✅ **Cost justified:** +2K tokens for strategic value
- Alternative: Recreate from scratch each time
- ROI: Time saved > token cost

**File structure example:**
```markdown
# PROMPT FINAL - Budget ESN 2026

## Input Utilisateur (Prompt Original)
[Complete prompt with all parameters]

## Output Obtenu
**Excel Mapping:**
[Cell references and formula locations]

## Évolutions V1→FINAL
V1→V2: [Changes and rationale]
V2→V3: [Changes and rationale]

## Guide Adaptation Autres Secteurs
ESN → SaaS: [Metric and formula mappings]
ESN → Restaurant: [Metric and formula mappings]
```

---

## Quality Standards

**Pre-Delivery Checklist:**
- [ ] All formulas use explicit cell references
- [ ] Balance sheet balances
- [ ] Cash flow reconciles
- [ ] Automated tests pass (openpyxl)
- [ ] Input cells have data validation
- [ ] Industry benchmarks applied
- [ ] 3 scenarios generated
- [ ] Instructions tab included
- [ ] File named with timestamp

**Test Command:**
```bash
cd sector/
python test_budget.py Budget_FINAL.xlsx
```

---

## Critical Lessons Learned (ESN/Consulting)

### ⚠️ MANDATORY Pre-Delivery Validation

**BEFORE delivering ANY Excel:**
1. Test programmatically with openpyxl (WITHOUT opening in Excel)
2. Verify ALL critical formula references
3. Check row indexing (row 18 = index 17)
4. Run tests 3-4 times if user emphasizes quality
5. Never deliver without passing all tests

### Common Errors (AVOID):

**Error 1: Named Ranges Hiding References**
❌ `workbook.define_name('TJM', '=Hypothèses!$B$27')`
✅ `worksheet.write_formula('B18', '=Hypothèses!$B$27')`

**Error 2: Calendar Month vs Individual Seniority**
❌ All salespeople use same calendar month
✅ Use `DATEDIF(Entry_Date, Month_Date, "M")` for individual ramp-up

**Error 3: Off-by-One Row Indexing**
❌ `ws.write_formula(18, 1, '...')` writes to row 19!
✅ `ws.write_formula(17, 1, '...')` writes to row 18 (index = row - 1)

**Error 4: Not Testing Before Delivery**
❌ Generate and deliver immediately
✅ Generate → Test with openpyxl → Validate → Deliver

**Error 5: Overly Complex Structure**
❌ Two rows per entity (Ancienneté + Missions)
✅ One row per entity (DATEDIF calculates inline)

See `esn_consulting/README.md` for sector-specific methodology.
For detailed evolution history, refer to `esn_consulting/PROMPT_FINAL.md`.

---

## Commands

```bash
# Generate business plan (interactive)
cd sector/
python generate_budget.py

# Validate with automated tests
python test_budget.py Budget_FINAL.xlsx

# Inspect formulas
python inspect_formulas.py Budget_FINAL.xlsx

# Show summary
python show_summary.py Budget_FINAL.xlsx
```

---

## Dependencies

```bash
pip install xlsxwriter openpyxl pandas numpy
```

---

## Final Notes

This agent generates **professional, investor-ready business plans** with:
1. **Accuracy**: Validated formulas and industry benchmarks
2. **Transparency**: Explicit references (M&A/PE/TS standards)
3. **Quality**: Automated testing before delivery
4. **Adaptability**: Seamless handling of different sectors
5. **Professionalism**: Production-grade Excel workbooks

**Remember:** You're creating strategic planning tools for critical business decisions. Quality and accuracy are paramount. Never compromise on financial statement integrity or testing.

---

**For extended documentation, examples, and sector templates:**
- See sector-specific README.md files
- Refer to PROMPT_FINAL.md for working prompts
- Check existing generate_budget.py for code patterns
- Reference full CLAUDE_FULL_ARCHIVE.md if needed (archive only)

---

*Last updated: 2025-10-22*
*Version: ULTRA-OPTIMIZED*
*Changes:*
*- Added METHODOLOGIE.md pattern (business logic documentation)*
*- Added test_budget.py pattern (reusable test template)*
*- Updated file generation rules (6 files: +METHODOLOGIE, -bloat)*
*- Optimized PROMPT_FINAL.md (295→205 lines, -30%)*
*- Total: 974 lines (vs 2114 original, -54% reduction)*
