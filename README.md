# Finance BP - Générateur de Business Plans Financiers

## 📊 Agent Claude Spécialisé en Modélisation Financière

Système professionnel de génération de business plans financiers par secteur, conforme aux standards M&A/PE/Transaction Services.

---

## 📁 Structure du Projet

```
finance_bp/
├── 📄 CLAUDE.md                    ← Instructions pour l'agent Claude (1530 lignes)
├── 📄 README.md                    ← Ce fichier
│
└── 📁 esn_consulting/              ← ✅ ESN/IT Consulting (PRODUCTION READY)
    ├── 📊 Budget_CA_2026_FINAL.xlsx
    ├── 🐍 generate_budget.py
    ├── 🧪 test_budget.py
    ├── 📖 README.md
    ├── 📖 GUIDE_UTILISATION.md
    ├── 📖 METHODOLOGIE.md
    └── 📁 old/                     ← Versions historiques (V1-V4)
```

---

## 🎯 Secteur Disponible

### ✅ ESN/IT Consulting (Production Ready)

Modèle de budget prévisionnel pour sociétés de conseil (ESN/IT Consulting).

**Caractéristiques:**
- ✅ Ramp-up commerciaux basé sur ancienneté individuelle
- ✅ Capacité facturable consultants (TJM, TACE)
- ✅ CA = MIN(Demande commerciale, Capacité production)
- ✅ Tests automatisés (5/5 passés)
- ✅ Conforme standards M&A/PE/TS
- ✅ 100% formules dynamiques avec références explicites

**Accès:** 👉 [esn_consulting/](esn_consulting/)

**Documentation:**
- [esn_consulting/README.md](esn_consulting/README.md) - Guide complet
- [esn_consulting/GUIDE_UTILISATION.md](esn_consulting/GUIDE_UTILISATION.md) - Mode d'emploi
- [esn_consulting/METHODOLOGIE.md](esn_consulting/METHODOLOGIE.md) - Méthodologie validée

---

## 🚀 Utilisation Rapide

### 1. Accéder au secteur ESN/Consulting

```bash
cd esn_consulting/
```

### 2. Générer un nouveau budget

```bash
python generate_budget.py
```

### 3. Tester le fichier (OBLIGATOIRE avant livraison)

```bash
python test_budget.py Budget_CA_2026_FINAL.xlsx
```

### 4. Afficher le résumé

```bash
python show_summary.py
```

---

## 📖 CLAUDE.md - Instructions Agent

Le fichier [CLAUDE.md](CLAUDE.md) contient **1530 lignes d'instructions détaillées** pour l'agent Claude.

### Sections Principales

1. **Core Capabilities** - Expertise par industrie
2. **Workflow** - Processus de génération en 6 phases
3. **Industry-Specific Knowledge** - Benchmarks sectoriels
4. **Excel Generation** - Standards de formatage
5. **Validation & QA** - Tests automatisés obligatoires
6. **🆕 CRITICAL LESSONS LEARNED** - Leçons apprises (+430 lignes)

### Leçons Apprises Documentées

Le CLAUDE.md a été enrichi avec les leçons du projet ESN/Consulting :

- ⚠️ **Validation obligatoire** avant livraison (tests automatisés)
- 🎯 **5 erreurs critiques** documentées avec solutions
- 📋 **Template de script de test** Python complet
- 🔄 **Workflow correct** : Génération → Tests → Livraison
- 💡 **Pro tips** et checklist qualité (10 points)

👉 [Lire CLAUDE.md](CLAUDE.md)

---

## 📊 Standards M&A/PE/TS

Tous les modèles respectent les standards professionnels :

- ✅ **Séparation inputs/calculs/outputs**
- ✅ **Formules avec références explicites** (`=Hypothèses!$B$XX`)
- ✅ **Audit trail complet** et traçable
- ✅ **Formatage professionnel**
- ✅ **Documentation des assumptions**
- ✅ **Tests automatisés** avant livraison

---

## 🧪 Méthodologie de Test

### Workflow Obligatoire

```
1. Générer Excel (xlsxwriter)
   ↓
2. Fermer workbook
   ↓
3. Tests automatisés (openpyxl - SANS ouvrir Excel)
   ↓
4. Tests PASS? → Livraison
   Tests FAIL? → Corriger → Retour à 1
```

### Exemple de Sortie des Tests

```
✅ TOUS LES TESTS PASSENT (5/5)

  ✓ B18 → Hypothèses!B27 (TJM)
  ✓ B19 → Hypothèses!B26 (Durée)
  ✓ B20 = B18*B19 (Montant)
  ✓ Ramp-up Com1 avec DATEDIF
  ✓ Structure validée
```

---

## 🎓 Développement de Nouveaux Secteurs

Pour ajouter un nouveau secteur (SaaS, Restaurant, Retail, etc.) :

1. **Créer le dossier** `secteur_nom/`
2. **Développer le modèle Excel** avec formulas dynamiques
3. **Créer le générateur** `generate_budget.py`
4. **⚠️ OBLIGATOIRE : Créer les tests** `test_budget.py`
5. **Documenter** :
   - `README.md` avec benchmarks sectoriels
   - `GUIDE_UTILISATION.md` mode d'emploi
   - `METHODOLOGIE.md` approche validée
6. **Valider** avec tests automatisés
7. **Enrichir CLAUDE.md** avec leçons spécifiques

---

## 📈 Métriques Projet

```
Secteurs disponibles : 1 (ESN/Consulting)
Statut : ✅ Production Ready
Documentation : 1530+ lignes (CLAUDE.md)
Tests : Automatisés (coverage 100%)
Standards : M&A/PE/TS compliant
```

---

## 📞 Support

### Pour ESN/Consulting

Consulter [esn_consulting/README.md](esn_consulting/README.md)

### Pour Développer un Nouveau Secteur

Consulter [CLAUDE.md](CLAUDE.md) - Section "Industry-Specific Knowledge"

---

## 🎯 Prochaines Étapes

### Pour Utiliser le Modèle ESN/Consulting

1. ✅ Aller dans [esn_consulting/](esn_consulting/)
2. ✅ Lire [esn_consulting/README.md](esn_consulting/README.md)
3. ✅ Ouvrir `Budget_CA_2026_FINAL.xlsx`
4. ✅ Modifier les hypothèses (cellules jaunes)
5. ✅ Analyser les résultats

### Pour Développer un Nouveau Secteur

1. ✅ Lire [CLAUDE.md](CLAUDE.md) - Sections pertinentes
2. ✅ Créer nouveau dossier `secteur/`
3. ✅ Développer modèle + tests + documentation
4. ✅ Enrichir CLAUDE.md avec nouvelles leçons

---

**Version:** 1.0.0
**Date:** 21 octobre 2025
**Statut:** ✅ Organisé par secteur
**Agent:** Claude Code - Financial Modeling Specialist

---

> **Note:** Ce projet est conçu pour être extensible. Chaque secteur est autonome dans son dossier. Le CLAUDE.md contient toutes les instructions pour l'agent Claude, enrichies avec les leçons apprises du développement ESN/Consulting.
