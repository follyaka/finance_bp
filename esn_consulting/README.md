# ESN/Consulting - Budget Prévisionnel

## 📊 Modèle Financier Société de Conseil

Modèle de budget prévisionnel professionnel conforme aux standards M&A/PE/Transaction Services pour sociétés de conseil (ESN/IT Consulting).

---

## 📦 Fichiers Production

- **Budget_CA_2026_FINAL.xlsx** - Modèle Excel validé (100% formules dynamiques)
- **generate_budget.py** - Générateur du modèle Excel
- **test_budget.py** - Tests automatisés (validation sans ouvrir Excel)
- **validate_budget.py** - Validation de cohérence
- **show_summary.py** - Affichage du résumé
- **inspect_formulas.py** - Inspection des formules

---

## 📊 Métriques Clés ESN

| Métrique | Valeur Standard |
|----------|-----------------|
| **TJM** (Taux Journalier Moyen) | 1000€ |
| **TACE** (Taux Activité Congés Exclus) | 90% |
| **Durée mission moyenne** | 25 jours |
| **Taux transformation BC→Factures** | 85% |
| **Ramp-up commerciaux** | M1: 2, M2: 4, M3: 6, M4+: 8 missions |

---

## 🔢 Formules Essentielles

### Capacité et Production

```excel
Capacité théorique = Nb_Consultants × Jours_Ouvrés
Capacité facturable = Capacité_théorique × TACE
CA Production MAX = Capacité_facturable × TJM
```

### CA Réel

```excel
CA Réel = MIN(CA_Facturé_Commercial, CA_Production_MAX)
```

### Taux d'Utilisation

```excel
Taux_Utilisation = CA_Réel / CA_Production_MAX
```

### Ramp-up Commercial (Ancienneté Individuelle)

```excel
Ancienneté_Mois = DATEDIF(Date_Entrée_Commercial, Date_Mois_Actuel, "M")
Missions = SI(Ancienneté=0, 0, SI(Ancienneté=1, M1, SI(Ancienneté=2, M2, SI(Ancienneté=3, M3, M4+))))
```

---

## 📈 Benchmarks Secteur

| Métrique | Cible |
|----------|-------|
| **Utilisation consultants** | 75-85% |
| **Marge brute** | 40-60% |
| **Marge nette** | 8-15% |
| **Revenue/consultant** | 200K€/an |
| **DSO** (Days Sales Outstanding) | 45-75 jours |

---

## 🎯 Structure Excel

### Onglet "Hypothèses" (Inputs)

Cellules **jaunes** = modifiables

**Équipe Commerciale:**
- Nombre de commerciaux (B8)
- Dates d'entrée (B11, B13, B15)
- Ramp-up M1-M4+ (B19-B22: 2, 4, 6, 8 missions)
- Taux transformation (B23: 85%)

**Équipe Consultants:**
- Nombre de consultants (B31)
- TJM (B27: 1000€)
- TACE (B32: 90%)
- Durée mission (B26: 25 jours)

**Calendrier:**
- Jours ouvrés par mois (B36-B47)

### Onglet "Chiffre d'affaires" (Calculs)

Cellules **bleues** = formules (ne pas modifier)

**Tableau 1:** Suivi commerciaux & ramp-up (Row 8-11)
**Tableau 2:** Pipeline commercial & CA facturé (Row 14-23)
**Tableau 3:** Capacité production consultants (Row 26-31)
**Tableau 4:** CA total mensuel = MIN(demande, capacité) (Row 34-39)

---

## ✅ Caractéristiques du Modèle

- ✅ 100% formules dynamiques (aucune valeur en dur)
- ✅ Références explicites (`=Hypothèses!$B$XX`, **PAS de named ranges**)
- ✅ Ramp-up basé sur ancienneté individuelle (DATEDIF)
- ✅ ROUNDUP sur unités discrètes (missions, factures)
- ✅ Lignes intermédiaires pour lisibilité (TJM, Durée, Montant)
- ✅ Tests automatisés (openpyxl)
- ✅ Conforme standards M&A/PE/TS

---

## 🧪 Validation

Le modèle est validé automatiquement :

```bash
python test_budget.py Budget_CA_2026_FINAL.xlsx
```

**Tests critiques :**
- ✓ Références explicites (pas de named ranges)
- ✓ Formules correctes (TJM, Durée, Montant)
- ✓ Ramp-up avec DATEDIF et dates d'entrée individuelles
- ✓ CA cumulé YTD, CA mensuel moyen, Total missions

---

## 📖 Standards M&A/PE/TS

Ce modèle respecte 100% les standards professionnels :

- ✓ Séparation inputs/calculs/outputs
- ✓ Formules avec références cellules explicites
- ✓ Audit trail complet et traçable
- ✓ Formatage professionnel (couleurs standards)
- ✓ Documentation des assumptions
- ✓ Checks de cohérence intégrés

---

**Version:** FINAL (Octobre 2025)
**Statut:** ✅ Production Ready
**Tests:** ✅ 8/8 passés
**Conformité:** ✅ Standards M&A/PE/TS
