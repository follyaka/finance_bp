# PROMPT FINAL - Budget Prévisionnel 2026 ESN/Consulting

## 📝 Input Utilisateur (Prompt Original)

```
Je veux créer un budget prévisionnel 2026 pour une société de conseil (ESN)
avec une approche bottom-up.

ÉQUIPE COMMERCIALE:
- 3 commerciaux
- Ramp-up progressif basé sur leur ancienneté individuelle:
  * Mois 1 : 2 clients
  * Mois 2 : 4 clients
  * Mois 3 : 6 clients
  * Mois 4+ : 8 clients
- Taux de transformation BC → Factures : 85%
- Chaque commercial a sa propre date d'entrée :
  * Commercial 1 : 01/01/2026
  * Commercial 2 : 01/01/2026
  * Commercial 3 : 01/03/2026 (arrive en mars)

ÉQUIPE CONSULTANTS:
- 50 consultants
- TJM : 1 000€
- TACE : 90%
- Durée mission moyenne : 25 jours

STRUCTURE EXCEL:
- 2 onglets : "Hypothèses" et "Chiffre d'affaires"
- 100% formules dynamiques (aucune valeur en dur)
- Références explicites (=Hypothèses!$B$XX), PAS de named ranges
- Formatage professionnel M&A/PE/TS :
  * Cellules jaunes pour inputs modifiables
  * Cellules bleues pour formules calculées
  * Headers bleu foncé

CALCULS:
- Ramp-up basé sur ANCIENNETÉ (DATEDIF), pas sur mois calendaire
- ROUNDUP sur missions signées (pas de décimales)
- CA réel = MIN(CA facturé commercial, CA production MAX)
- Lignes intermédiaires pour lisibilité (TJM, Durée, Montant)

INDICATEURS CLÉS SOUHAITÉS:
- CA réel mensuel
- CA cumulé YTD juste en dessous du CA réel mensuel
- CA total 2026
- CA mensuel moyen en dessous de CA total 2026
- Nombre total de missions signées en dessous du CA mensuel moyen

CONTRAINTES TECHNIQUES:
- Utiliser xlsxwriter (Python)
- Tester automatiquement avec openpyxl SANS ouvrir le fichier
- Structure par secteur : tout dans dossier esn_consulting/
- Anciennes versions dans esn_consulting/old/
- Racine propre : uniquement CLAUDE.md et README.md

QUALITÉ:
- Contrôler le fichier 3-4 fois avant livraison
- Tests automatisés obligatoires
- Documentation complète (README, GUIDE_UTILISATION, METHODOLOGIE)
- Conformité standards M&A/PE/TS
```

---

## 🎯 Output Obtenu

### ✅ Fichier Excel Final

**Budget_CA_2026_FINAL.xlsx** (version améliorée avec indicateurs supplémentaires)

**Onglet "Hypothèses" (Inputs jaunes):**
- Dates d'entrée des 3 commerciaux (B11, B13, B15)
- Ramp-up M1, M2, M3, M4+ (B19-B22)
- Taux transformation 85% (B23)
- Durée mission 25 jours (B26)
- TJM 1000€ (B27)
- Nombre consultants 50 (B31)
- TACE 90% (B32)
- Jours ouvrés par mois (B36-B47)

**Onglet "Chiffre d'affaires" (Formules bleues):**

**TABLEAU 1 - NOUVELLES MISSIONS:**
- Row 8-10 : Missions par commercial (formules DATEDIF basées sur ancienneté)
- Row 11 : TOTAL nouvelles missions

**TABLEAU 2 - TRANSFORMATION & CA:**
- Row 14 : Taux transformation
- Row 15 : Missions signées (ROUNDUP)
- Row 18 : TJM (=Hypothèses!$B$27)
- Row 19 : Durée (=Hypothèses!$B$26)
- Row 20 : Montant mission (=B18*B19)
- Row 23 : CA FACTURÉ

**TABLEAU 3 - CAPACITÉ:**
- Row 26 : Jours ouvrés
- Row 27 : Nb consultants
- Row 28 : Capacité théorique
- Row 29 : TACE
- Row 30 : Capacité facturable
- Row 31 : CA PRODUCTION MAX

**SYNTHÈSE:**
- Row 34 : **CA RÉEL MENSUEL** (=MIN(CA facturé, CA prod MAX))
- Row 35 : **💰 CA CUMULÉ YTD** (cumul progressif) ← ✨ NOUVEAU
- Row 37 : **🎯 CA TOTAL 2026**
- Row 38 : **📊 CA MENSUEL MOYEN** (=B37/12) ← ✨ NOUVEAU
- Row 39 : **📦 TOTAL MISSIONS SIGNÉES** (=SUM(B15:M15)) ← ✨ NOUVEAU

---

### ✅ Validation & Tests

**Tests automatisés passés (8/8):**
```
✓ B18 → Hypothèses!B27 (TJM)
✓ B19 → Hypothèses!B26 (Durée)
✓ B20 = B18*B19 (Montant)
✓ Ramp-up Com1 DATEDIF + B11
✓ Ramp-up Com3 DATEDIF + B15
✓ CA cumulé YTD
✓ CA mensuel moyen
✓ Total missions signées
```

**Conformité M&A/PE/TS:**
- ✓ Séparation inputs/formulas/outputs
- ✓ Références explicites (=Hypothèses!$B$XX)
- ✓ Audit trail traçable
- ✓ Tests automatisés avant livraison

---

## 🔄 Évolutions par Version

### V1 → V2
- ❌ Problème : Ramp-up basé sur mois calendaire (tous les commerciaux démarraient en janvier)
- ✅ Solution : Ajout dates d'entrée + formules DATEDIF

### V2 → V3
- ❌ Problème : Named ranges cachaient les références réelles
- ✅ Solution : Suppression named ranges, références explicites uniquement

### V3 → V4
- ❌ Problème : Structure trop complexe (2 lignes par commercial)
- ✅ Solution : Simplification à 1 ligne par commercial, calcul direct

### V4 → V4 CORRECTED
- ❌ Problème : Erreurs d'indexation (B19→B27 au lieu de B26)
- ✅ Solution : Vérification ligne par ligne, correction indexation

### V4 CORRECTED → FINAL (ENHANCED)
- ✨ Ajout : CA cumulé YTD (row 35)
- ✨ Ajout : CA mensuel moyen (row 38)
- ✨ Ajout : Total missions signées (row 39)

---

## 🎓 Leçons Clés

### 1. Named Ranges vs Références Explicites
❌ `=TJM` (cache référence) → ✅ `=Hypothèses!$B$27` (transparent)

### 2. Ramp-up par Ancienneté
❌ Mois calendaire → ✅ `DATEDIF(DateEntrée, MoisActuel, "M")`

### 3. Indexation Excel
❌ Row 18 = index 18 → ✅ Row 18 = index 17 (index = row - 1)

### 4. Tests Obligatoires
❌ Livrer sans tester → ✅ `python test_budget.py` AVANT livraison

### 5. Organisation
❌ Fichiers à la racine → ✅ Dossier par secteur (esn_consulting/, saas/)

---

## 💡 Adaptation Autres Secteurs

**ESN → SaaS :**
- TJM (€1000) → ARPU ($100/mo)
- TACE (90%) → Churn (5%/mo)
- Missions → Subscriptions
- CA = Missions × TJM → MRR = Customers × ARPU

**ESN → Restaurant :**
- TJM → Average Ticket
- TACE → Table Turnover
- Consultants → Tables/Seats
- CA = Missions × TJM → Revenue = Covers × Avg Ticket

**Principes conservés :**
✓ Références explicites
✓ Tests automatisés
✓ Organisation par secteur
✓ Documentation (README, PROMPT_FINAL, METHODOLOGIE)

---

**Date de création :** 21 octobre 2025
**Dernière mise à jour :** 22 octobre 2025
**Statut :** ✅ Production Ready
**Version :** OPTIMIZED (réduit de 295 → 205 lignes, -30%)
**Tests :** ✅ 8/8 passés
**Conformité :** ✅ Standards M&A/PE/TS
