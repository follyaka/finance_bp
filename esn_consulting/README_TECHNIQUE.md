# Budget Prévisionnel 2026 - Société de Conseil

## Description

Modèle financier professionnel conforme aux standards M&A/PE/Transaction Services pour le calcul du chiffre d'affaires d'une société de conseil avec approche bottom-up.

## Fichiers générés

- **Budget_CA_2026_[timestamp].xlsx** - Fichier Excel principal
- **generate_budget_2026.py** - Script de génération
- **validate_budget.py** - Script de validation

## Structure du modèle

### Onglet 1: Hypothèses

Toutes les cellules **JAUNES** sont modifiables (inputs):

#### Équipe Commerciale
- Nombre de commerciaux: **3**
- Ramp-up progressif:
  - Mois 1 (Janvier): 2 nouveaux clients/commercial
  - Mois 2 (Février): 4 nouveaux clients/commercial
  - Mois 3 (Mars): 6 nouveaux clients/commercial
  - Mois 4+ (Avril-Décembre): 8 nouveaux clients/commercial
- Taux de transformation BC → Factures: **85%**

#### Équipe Consultants
- Nombre de consultants: **50**
- TJM (Taux Journalier Moyen): **1 000 €**
- TACE (Taux d'Activité Congés Exclus): **90%**
- Durée moyenne mission: **25 jours**

#### Calendrier
- Jours ouvrés par mois (modifiable)

### Onglet 2: Chiffre d'affaires

Tous les calculs sont effectués par **FORMULES** (pas de valeurs en dur).

#### Tableau 1: Suivi Commerciaux & Ramp-up
- Nombre de nouveaux clients par commercial et par mois
- Total consolidé

#### Tableau 2: Pipeline Commercial
- Bons de commande (BC) générés
- Application du taux de transformation
- Calcul du nombre de factures signées
- Montant par facture (TJM × Durée mission)
- **CA facturé** (nombre factures × montant)

#### Tableau 3: Production Consultants
- Capacité théorique (consultants × jours ouvrés)
- Capacité facturable (× TACE)
- **CA production MAX** (capacité × TJM)

#### Tableau 4: Synthèse CA Mensuel
- **CA TOTAL MENSUEL**: MIN(CA facturé, CA production MAX)
  - Garantit qu'on ne facture pas plus que la capacité de production
- CA Cumulé YTD (Year-To-Date)

#### Checks de Cohérence
- Vérification CA ≤ Capacité production
- Taux d'utilisation réel des consultants
- Évolution mois par mois
- Synthèse annuelle

## Formules clés

Toutes les formules utilisent des **références de cellules** et des **noms définis**:

```excel
# Named ranges
NbCommerciaux = Hypothèses!$B$8
TJM = Hypothèses!$B$17
TACE = Hypothèses!$B$18
DureeMission = Hypothèses!$B$19
```

### Exemples de formules

**Ramp-up par mois:**
```excel
=IF(MONTH(date)=1, RampupM1, IF(MONTH(date)=2, RampupM2, ...))
```

**CA facturé:**
```excel
=NbFactures * (TJM * DureeMission)
```

**Capacité production:**
```excel
=NbConsultants * JoursOuvrés * TACE * TJM
```

**CA total:**
```excel
=MIN(CAFacturé, CAProductionMAX)
```

## Standards de formatage

### Couleurs (conforme M&A/PE)
- **Headers**: Bleu foncé (#1F4E78), texte blanc, gras
- **Inputs**: Jaune clair (#FFF2CC) - cellules modifiables
- **Formules**: Bleu clair (#D9E1F2) - cellules calculées
- **Totaux**: Bordure épaisse (2px)

### Formats numériques
- Montants: `#,##0 €` (séparateurs de milliers)
- Pourcentages: `0.0%` (1 décimale)
- Nombres: Format standard avec séparateurs

## Utilisation

### 1. Générer un nouveau fichier

```bash
python generate_budget_2026.py
```

Crée: `Budget_CA_2026_YYYYMMDD_HHMMSS.xlsx`

### 2. Valider le modèle

```bash
python validate_budget.py
```

Vérifie:
- Structure des onglets
- Cohérence des hypothèses
- Présence des formules
- Calculs CA
- Capacité production
- Formatage

### 3. Modifier les hypothèses

1. Ouvrir le fichier Excel
2. Aller dans l'onglet "Hypothèses"
3. Modifier uniquement les cellules **JAUNES**
4. Tous les calculs se mettent à jour automatiquement
5. Vérifier l'onglet "Chiffre d'affaires"

## Exemples de scénarios

### Scénario 1: Augmenter les commerciaux
- Changer `Nombre de commerciaux` de 3 à 5
- → Plus de BC générés
- → Plus de factures signées
- → CA augmente (dans la limite de la capacité production)

### Scénario 2: Augmenter le TJM
- Changer `TJM` de 1000€ à 1200€
- → Montant par facture augmente
- → CA facturé augmente
- → CA production MAX augmente proportionnellement

### Scénario 3: Augmenter les consultants
- Changer `Nombre de consultants` de 50 à 60
- → Capacité production augmente
- → Permet de supporter plus de CA si les commerciaux génèrent assez de factures

### Scénario 4: Modifier le taux de transformation
- Changer `Taux transformation` de 85% à 75%
- → Moins de factures signées pour le même nombre de BC
- → CA diminue

## Checks de cohérence automatiques

Le modèle intègre des validations automatiques:

### 1. CA ≤ Capacité production
```
✓ OK  : CA facturé ne dépasse pas la capacité
⚠ ALERTE : CA demandé > capacité disponible
```

### 2. Taux d'utilisation
Affiche le % d'utilisation réel des consultants:
- <70% → Sous-utilisation (optimiser commercial)
- 70-95% → Zone optimale
- >95% → Risque de surcharge

### 3. Évolution M/M
Montre la croissance mois par mois pour détecter:
- Pics anormaux
- Stagnation
- Décroissance

## Logique métier implémentée

### Ramp-up commercial
Le modèle simule la montée en charge progressive:
- **Mois 1-3**: Phase d'apprentissage (2 → 4 → 6 clients)
- **Mois 4+**: Rythme de croisière (8 clients/mois)

### Transformation BC → Factures
Taux < 100% car:
- Certains BC ne se concrétisent pas
- Délais de signature
- Annulations possibles

### Contrainte de capacité
```
CA réel = MIN(Demande commerciale, Capacité production)
```

Simule la réalité:
- On ne peut pas facturer plus que ce qu'on peut produire
- Permet d'identifier les goulots d'étranglement

## Évolutions possibles

### Version future: Ajouter
- [ ] Saisonnalité (coefficients mensuels)
- [ ] Plusieurs types de missions (TJM différents)
- [ ] Coûts et marges (P&L complet)
- [ ] Trésorerie (délais de paiement)
- [ ] Scénarios (optimiste/pessimiste/réaliste)
- [ ] Graphiques (évolution CA, utilisation consultants)
- [ ] Dashboard exécutif (KPIs visuels)

## Support

Pour toute question ou modification:
1. Consulter les commentaires dans les cellules Excel
2. Vérifier la structure des formules
3. Utiliser le script de validation
4. Modifier uniquement les cellules jaunes

## Conformité Transaction Services

Le modèle respecte les standards professionnels:
- ✓ Audit trail complet (chaque calcul est traçable)
- ✓ Séparation inputs/calculs/outputs
- ✓ Formules uniquement (pas de valeurs en dur)
- ✓ Formatage professionnel
- ✓ Checks de cohérence intégrés
- ✓ Documentation complète
- ✓ Nommage des cellules clés
- ✓ Protection des formules (inputs seulement déverrouillés)

---

**Version**: 1.0
**Date**: 2026
**Conforme**: Standards M&A/PE/Transaction Services
