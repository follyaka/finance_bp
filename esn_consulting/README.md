# ESN/Consulting - Budget Prévisionnel

## 📊 Modèle Financier Société de Conseil

Modèle de budget prévisionnel professionnel conforme aux standards M&A/PE/Transaction Services pour sociétés de conseil (ESN/IT Consulting).

---

## 📦 Fichiers Disponibles

### ✅ Version Finale (Production Ready)

- **Budget_CA_2026_FINAL.xlsx** - Modèle Excel validé et prêt à utiliser
  - 2 onglets : Hypothèses + Chiffre d'affaires
  - 100% formules dynamiques avec références explicites
  - Testé et validé (tous les tests passent ✅)

### 🐍 Scripts Python

- **generate_budget.py** - Générateur du modèle Excel (version corrigée)
- **test_budget.py** - Tests automatisés (validation sans ouvrir Excel)
- **validate_budget.py** - Validation de cohérence du modèle
- **show_summary.py** - Affichage du résumé du budget
- **inspect_formulas.py** - Inspection des formules Excel

### 📖 Documentation

- **GUIDE_UTILISATION.md** - Guide utilisateur complet (421 lignes)
- **METHODOLOGIE.md** - Méthodologie détaillée pour ESN
- **LIVRABLE.md** - Récapitulatif de livraison
- **README_TECHNIQUE.md** - Documentation technique

### 📁 Anciennes Versions

Dossier `old/` contient toutes les versions de développement (V1 à V4) pour référence historique.

---

## 🚀 Utilisation Rapide

### 1. Générer un nouveau budget

```bash
python generate_budget.py
```

### 2. Tester un fichier existant

```bash
python test_budget.py Budget_CA_2026_FINAL.xlsx
```

### 3. Afficher le résumé

```bash
python show_summary.py
```

---

## 📊 Spécificités ESN/Consulting

### Métriques Clés

- **TJM** (Taux Journalier Moyen) : 1000€
- **TACE** (Taux Activité Congés Exclus) : 90%
- **Durée mission moyenne** : 25 jours
- **Ramp-up commerciaux** : 2 → 4 → 6 → 8 missions (M1-M4+)
- **Taux transformation** : 85%

### Formules Essentielles

```excel
Capacité facturable = Nb_Consultants × Jours_Ouvrés × TACE
CA Production MAX = Capacité_facturable × TJM
CA Réel = MIN(CA_Facturé_Commercial, CA_Production_MAX)
Taux_Utilisation = CA_Réel / CA_Production_MAX
```

### Benchmarks Secteur

| Métrique | Cible |
|----------|-------|
| **Utilisation consultants** | 75-85% |
| **Marge brute** | 40-60% |
| **Marge nette** | 8-15% |
| **Revenue/consultant** | 200K€/an |
| **DSO** | 45-75 jours |

---

## ✅ Caractéristiques du Modèle

- ✅ 100% formules dynamiques (aucune valeur en dur)
- ✅ Références explicites (`=Hypothèses!$B$XX`)
- ✅ Ramp-up basé sur ancienneté individuelle (DATEDIF)
- ✅ ROUNDUP sur unités discrètes (missions, factures)
- ✅ Lignes intermédiaires pour lisibilité (TJM, Durée, Montant)
- ✅ Tests automatisés (openpyxl)
- ✅ Conforme standards M&A/PE/TS

---

## 🎯 Structure Excel

### Onglet "Hypothèses" (Inputs)

Cellules **jaunes** = modifiables par l'utilisateur

- **Équipe Commerciale**
  - Nombre de commerciaux (3)
  - Dates d'entrée (B11, B13, B15)
  - Ramp-up M1-M4+ (2, 4, 6, 8 missions)
  - Taux transformation (85%)

- **Équipe Consultants**
  - Nombre de consultants (50)
  - TJM (1000€)
  - TACE (90%)
  - Durée mission (25 jours)

- **Calendrier**
  - Jours ouvrés par mois (12 valeurs)

### Onglet "Chiffre d'affaires" (Calculs)

Cellules **bleues** = formules (ne pas modifier)

- **Tableau 1** : Suivi commerciaux & ramp-up
- **Tableau 2** : Pipeline commercial & CA facturé
- **Tableau 3** : Capacité production consultants
- **Tableau 4** : CA total mensuel = MIN(demande, capacité)

---

## 🧪 Tests et Validation

Le modèle a été testé et validé automatiquement :

```
✅ TOUS LES TESTS PASSENT (5/5)

  ✓ B18 → Hypothèses!B27 (TJM)
  ✓ B19 → Hypothèses!B26 (Durée)
  ✓ B20 = B18*B19 (Montant)
  ✓ B8 ramp-up Com1 avec DATEDIF et B11
  ✓ B10 ramp-up Com3 avec DATEDIF et B15
```

---

## 📚 Documentation Complète

Pour une compréhension approfondie, consulter :

1. **[GUIDE_UTILISATION.md](GUIDE_UTILISATION.md)** - Guide pas-à-pas
2. **[METHODOLOGIE.md](METHODOLOGIE.md)** - Approche mission-based validée
3. **[LIVRABLE.md](LIVRABLE.md)** - Récapitulatif de livraison

---

## 🔧 Développement

### Générer une nouvelle version

```python
python generate_budget.py
```

### Tester avant livraison (OBLIGATOIRE)

```python
python test_budget.py Budget_CA_2026_FINAL.xlsx
```

**IMPORTANT:** Ne jamais livrer un fichier sans avoir exécuté les tests !

---

## 📖 Standards M&A/PE/TS

Ce modèle respecte 100% les standards M&A/PE/Transaction Services :

- ✓ Séparation inputs/calculs/outputs
- ✓ Formules avec références cellules explicites
- ✓ Audit trail complet et traçable
- ✓ Formatage professionnel
- ✓ Documentation des assumptions
- ✓ Checks de cohérence intégrés

---

## 🎓 Leçons Apprises

Voir la section **"CRITICAL LESSONS LEARNED"** dans [../CLAUDE.md](../CLAUDE.md) pour :

- ⚠️ Validation obligatoire avant livraison
- 🎯 5 erreurs critiques à éviter
- 📋 Template de script de test
- 🔄 Workflow correct
- 💡 Pro tips

---

## 📞 Support

Pour toute question sur ce modèle ESN/Consulting, consulter :

- [GUIDE_UTILISATION.md](GUIDE_UTILISATION.md) - Guide utilisateur
- [METHODOLOGIE.md](METHODOLOGIE.md) - Méthodologie détaillée
- [../CLAUDE.md](../CLAUDE.md) - Instructions agent global

---

**Version:** V4 CORRECTED (21 octobre 2025)
**Statut:** ✅ Production Ready
**Tests:** ✅ 5/5 passés
**Conformité:** ✅ Standards M&A/PE/TS
