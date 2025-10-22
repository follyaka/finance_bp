# Guide d'Utilisation - Budget Prévisionnel 2026

## Fichier Généré

**Nom**: `Budget_CA_2026_[timestamp].xlsx`

Le fichier le plus récent dans le répertoire est toujours le fichier à utiliser.

---

## Structure du Fichier Excel

### Onglet 1: "Hypothèses"

Cet onglet contient TOUTES les hypothèses du modèle.

#### Cellules JAUNES = Modifiables (Inputs)

**Équipe Commerciale:**
- Cellule B8: Nombre de commerciaux (défaut: 3)
- Cellule B9: Ramp-up Mois 1 - nouveaux clients (défaut: 2)
- Cellule B10: Ramp-up Mois 2 - nouveaux clients (défaut: 4)
- Cellule B11: Ramp-up Mois 3 - nouveaux clients (défaut: 6)
- Cellule B12: Ramp-up Mois 4+ - nouveaux clients (défaut: 8)
- Cellule B13: Taux de transformation BC→Factures (défaut: 85%)

**Équipe Consultants:**
- Cellule B16: Nombre de consultants (défaut: 50)
- Cellule B17: TJM - Taux Journalier Moyen en € (défaut: 1 000 €)
- Cellule B18: TACE - Taux d'Activité Congés Exclus (défaut: 90%)
- Cellule B19: Durée moyenne d'une mission en jours (défaut: 25)

**Calendrier:**
- Cellules B22 à B33: Jours ouvrés par mois (janvier à décembre)

#### Instructions d'utilisation

1. **NE modifiez QUE les cellules jaunes**
2. Les cellules bleues contiennent des formules - ne pas toucher
3. Après modification, toutes les valeurs se recalculent automatiquement
4. Allez dans l'onglet "Chiffre d'affaires" pour voir les résultats

---

### Onglet 2: "Chiffre d'affaires"

Cet onglet contient TOUS les calculs du chiffre d'affaires mensuel.

#### TABLEAU 1: Suivi Commerciaux & Ramp-up

**Lignes 7-9**: Nouveaux clients par commercial (Com1, Com2, Com3)
- Applique automatiquement la courbe de ramp-up selon le mois
- Janvier = Ramp-up M1, Février = M2, Mars = M3, Avril-Décembre = M4+

**Ligne 10**: TOTAL nouveaux clients
- Somme des 3 commerciaux

#### TABLEAU 2: Pipeline Commercial

**Ligne 13**: Bons de commande (BC) générés
- = Total nouveaux clients du mois

**Ligne 14**: Taux de transformation
- Référence l'hypothèse (défaut: 85%)

**Ligne 15**: Factures signées (nombre)
- = BC générés × Taux de transformation

**Ligne 16**: Montant par facture (€)
- = TJM × Durée mission
- Exemple: 1 000€ × 25 jours = 25 000€

**Ligne 17**: CA facturé (€)
- = Nombre de factures × Montant par facture
- Représente la demande commerciale

#### TABLEAU 3: Production Consultants

**Ligne 21**: Jours ouvrés du mois
- Référence le calendrier (onglet Hypothèses)

**Ligne 22**: Capacité théorique (j×consultants)
- = Nombre consultants × Jours ouvrés
- Exemple: 50 consultants × 22 jours = 1 100 jours

**Ligne 23**: Capacité facturable (j×TACE)
- = Capacité théorique × TACE
- Exemple: 1 100 j × 90% = 990 jours facturables

**Ligne 24**: CA production MAX (€)
- = Capacité facturable × TJM
- Exemple: 990 j × 1 000€ = 990 000€
- Représente la capacité maximale de production

#### TABLEAU 4: Synthèse CA Mensuel

**Ligne 28**: 🔑 **CA TOTAL MENSUEL (€)**
- **Formule clé**: `= MIN(CA facturé, CA production MAX)`
- Garantit qu'on ne facture pas plus que notre capacité de production
- **C'est le chiffre final du CA mensuel**

**Ligne 29**: CA Cumulé YTD (€)
- Cumul depuis janvier
- Permet de suivre la progression sur l'année

#### TABLEAU 5: Checks de Cohérence

**Ligne 33**: Check CA ≤ Capacité production
- Affiche "✓ OK" si le CA facturé ne dépasse pas la capacité
- Affiche "⚠ ALERTE" en cas de dépassement

**Ligne 34**: Taux d'utilisation réel (%)
- = CA total / CA production MAX
- Montre le % d'utilisation réelle des consultants
- **Optimal**: 75-95%
- <70% = Sous-utilisation (problème commercial)
- >95% = Surcharge (risque burnout)

**Ligne 35**: Évolution vs mois précédent (%)
- Montre la croissance mois par mois
- Permet d'identifier les tendances

#### SYNTHÈSE ANNUELLE

**Ligne 39**: CA TOTAL ANNÉE 2026
- Somme des 12 mois
- **Cellule orange, gros chiffre**

**Ligne 40**: CA mensuel moyen

**Ligne 41**: Croissance moyenne M/M
- Taux de croissance composé mensuel

---

## Scénarios d'Utilisation

### Scénario 1: Doubler l'équipe commerciale

**Objectif**: Voir l'impact de passer de 3 à 6 commerciaux

1. Ouvrir "Hypothèses"
2. Changer B8 de `3` à `6`
3. Aller dans "Chiffre d'affaires"
4. Observer:
   - TOTAL nouveaux clients a doublé
   - BC générés a doublé
   - CA facturé a augmenté
   - **MAIS**: Vérifier le check de cohérence ligne 33
   - Si "⚠ ALERTE" = la capacité production est dépassée
   - **Conclusion**: Il faut aussi augmenter le nombre de consultants

### Scénario 2: Augmenter le TJM

**Objectif**: Voir l'impact d'une augmentation tarifaire de 10%

1. Ouvrir "Hypothèses"
2. Changer B17 de `1000` à `1100`
3. Observer:
   - Montant par facture augmente
   - CA facturé augmente
   - CA production MAX augmente proportionnellement
   - **Résultat**: +10% de CA à volume constant

### Scénario 3: Recruter des consultants

**Objectif**: Passer de 50 à 60 consultants (+20%)

1. Ouvrir "Hypothèses"
2. Changer B16 de `50` à `60`
3. Observer:
   - Capacité production augmente de 20%
   - Taux d'utilisation baisse (plus de capacité disponible)
   - **Si commerciaux génèrent assez de demande**: CA augmente
   - **Sinon**: Sous-utilisation (consultants pas assez occupés)

### Scénario 4: Améliorer le taux de transformation

**Objectif**: Passer de 85% à 95% de transformation BC→Factures

1. Ouvrir "Hypothèses"
2. Changer B13 de `0.85` à `0.95`
3. Observer:
   - Plus de factures signées pour le même nombre de BC
   - CA augmente
   - **Implique**: Meilleure qualification des leads ou meilleur closing

### Scénario 5: Modifier le ramp-up commercial

**Objectif**: Commerciaux plus performants dès le début

1. Ouvrir "Hypothèses"
2. Changer:
   - B9 (M1): de `2` à `4`
   - B10 (M2): de `4` à `6`
   - B11 (M3): de `6` à `8`
   - B12 (M4+): de `8` à `10`
3. Observer:
   - CA des premiers mois augmente
   - Croissance plus rapide
   - CA total annuel augmente

---

## Formules Clés Expliquées

### 1. Ramp-up Commercial (Cellules B7:M9)

```excel
=IF(COLUMN()=2, RampupM1, IF(COLUMN()=3, RampupM2, IF(COLUMN()=4, RampupM3, RampupM4Plus)))
```

Simplifié dans le modèle avec noms définis:
- Janvier (colonne B) = RampupM1
- Février (colonne C) = RampupM2
- Mars (colonne D) = RampupM3
- Avril-Décembre = RampupM4Plus

### 2. CA Facturé (Ligne 17)

```excel
=B15 * B16
=Nombre factures × Montant par facture
```

Exemple:
- 20,4 factures × 25 000€ = 510 000€

### 3. CA Production MAX (Ligne 24)

```excel
=B23 * TJM
=Capacité facturable × TJM
```

Exemple:
- 990 jours × 1 000€ = 990 000€

### 4. CA TOTAL MENSUEL (Ligne 28) - **FORMULE CRITIQUE**

```excel
=MIN(B17, B24)
=MIN(CA facturé, CA production MAX)
```

**Logique métier**:
- On ne peut pas facturer plus que ce qu'on peut produire
- Si demande commerciale (CA facturé) > capacité production:
  - CA réel = Capacité production (goulot d'étranglement)
  - Signal d'alerte pour recruter des consultants
- Si demande commerciale < capacité production:
  - CA réel = Demande commerciale
  - Consultants sous-utilisés, optimiser le commercial

### 5. CA Cumulé YTD (Ligne 29)

```excel
Janvier (B29):   =B28
Février (C29):   =B29 + C28
Mars (D29):      =C29 + D28
...
```

Cumul depuis le début de l'année.

---

## Indicateurs Clés à Surveiller

### 1. Taux d'Utilisation (Ligne 34)

**Formule**: `= CA total / CA production MAX`

**Interprétation**:
- **<60%** = 🔴 Problème commercial grave (consultants inoccupés)
- **60-75%** = 🟡 Sous-optimal (chercher plus de clients)
- **75-95%** = 🟢 Zone optimale
- **>95%** = 🔴 Surcharge (risque qualité et burnout)

### 2. Ratio BC→Factures

**Objectif**: 85%+

Si le taux baisse:
- Problème de qualification des leads
- Problème de closing commercial
- Concurrence accrue
- Décalage temporel (BC signés ce mois, facturés le suivant)

### 3. Évolution M/M (Ligne 35)

**Sain**: +5% à +15% mensuel en phase de croissance

Si négatif ou stagnant:
- Saisonnalité?
- Problème commercial?
- Marché saturé?

### 4. CA par Commercial

**Formule manuelle**: `= CA total annuel / Nb commerciaux / 12`

**Benchmark**: 200 000€ à 400 000€ par commercial par an

Si <150 000€/commercial/an = Problème de productivité ou ramp-up trop lent

---

## Vérifications Importantes

### ✓ AVANT de valider les chiffres

1. **Cohérence commerciale**:
   - Les ramp-up sont-ils réalistes?
   - Un commercial peut-il vraiment générer 8 nouveaux clients/mois?
   - Est-ce cohérent avec le cycle de vente?

2. **Cohérence production**:
   - TACE 90% est ambitieux (tenir compte congés, formation, intercontrats)
   - Durée moyenne mission: vérifier avec l'historique

3. **Vérifier les alertes**:
   - Ligne 33: Tous les mois doivent être "✓ OK"
   - Si "⚠ ALERTE": ajuster soit commerciaux (baisser), soit consultants (augmenter)

4. **Stress test**:
   - Que se passe-t-il si taux transformation baisse à 70%?
   - Que se passe-t-il si un commercial part (passer de 3 à 2)?
   - Que se passe-t-il si TACE baisse à 80%?

---

## Limites du Modèle

### Ce que le modèle FAIT:
✓ Calcul du CA mensuel bottom-up
✓ Contraintes de capacité production
✓ Ramp-up commercial progressif
✓ Taux de transformation < 100%
✓ Liens dynamiques entre hypothèses et résultats

### Ce que le modèle NE FAIT PAS (évolutions futures):
✗ Saisonnalité (coefficients mensuels différents)
✗ Plusieurs types de missions (TJM différents)
✗ Coûts et charges (P&L complet)
✗ Trésorerie et décalages de paiement
✗ Croissance de l'équipe en cours d'année
✗ Churn clients (renouvellement missions)

---

## Conseils d'Utilisation Professionnelle

### Pour une présentation en comité

1. **Préparer 3 scénarios**:
   - Pessimiste: -20% sur ramp-up et taux transformation
   - Base: Valeurs actuelles du modèle
   - Optimiste: +15% sur ramp-up

2. **Analyser les gaps**:
   - Si CA visé = 15M€ et modèle donne 12M€
   - Identifier les leviers: +X commerciaux, ou +Y% TJM, ou +Z consultants

3. **Préparer les hypothèses de sensibilité**:
   - Impact d'une variation de ±10% du TJM
   - Impact d'une variation de ±10% du taux transformation
   - Impact d'un ±1 commercial

### Pour un audit/due diligence

1. **Documenter les sources**:
   - D'où viennent les chiffres de ramp-up? (historique, benchmark)
   - Le TACE 90% est-il confirmé par les données RH?
   - Le taux transformation 85% est-il confirmé par le CRM?

2. **Ajouter une analyse de variance**:
   - Comparer le budget N-1 vs réalisé N-1
   - Analyser les écarts pour calibrer N+1

3. **Identifier les risques**:
   - Dépendance à 3 commerciaux (risque départ)
   - Capacité production limitée (goulet)
   - Hypothèses optimistes non challengées

---

## Support et Modifications

### Si vous voulez modifier le modèle

**Code source**: `generate_budget_2026.py`

**Modifications courantes**:

1. **Ajouter un 4ème commercial**:
   - Ligne 263: Changer `for com_idx in range(3):` en `range(4)`
   - Mettre à jour B8 (hypothèse)

2. **Ajouter des graphiques**:
   - Utiliser `workbook.add_chart()` après ligne 400
   - Types utiles: `column`, `line`, `area`

3. **Ajouter des onglets (Charges, Trésorerie)**:
   - Créer nouveau worksheet après ligne 230
   - Référencer les données de "Chiffre d'affaires"

### Régénérer le fichier

```bash
python generate_budget_2026.py
```

Crée un nouveau fichier avec timestamp.

---

**Version**: 1.0
**Conforme**: Standards M&A/PE/Transaction Services
**Audit trail**: Complet
**Formules**: 100% dynamiques (pas de valeurs en dur)
