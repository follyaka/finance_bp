# Méthodologie de Calcul CA - Version 2 Corrigée

## Problèmes Identifiés dans la V1

### ❌ Erreur 1: Ramp-up par mois calendaire
**V1 (incorrect)**:
- Janvier = Tous les commerciaux font 2 clients
- Février = Tous les commerciaux font 4 clients
- Mars = Tous les commerciaux font 6 clients

**Problème**: Si un commercial arrive en mars, son M1 devrait être mars (pas janvier)!

**V2 (correct)**:
- Le ramp-up se calcule selon l'**ANCIENNETÉ** du commercial
- Commercial 1 entré le 01/01: Janvier=M1, Février=M2, etc.
- Commercial 3 entré le 01/03: Mars=M1, Avril=M2, etc.

### ❌ Erreur 2: Pas de date d'entrée
**V1**: Impossible de savoir quand chaque commercial a démarré

**V2**: Chaque commercial a une date d'entrée modifiable dans "Hypothèses"

### ❌ Erreur 3: Liens de formules cassés
**V1**: Cellule B23 (et autres) ne tapaient pas au bon endroit

**V2**: Tous les liens sont corrects et tracés avec named ranges

### ❌ Erreur 4: Pas d'arrondi sur factures
**V1**: 20,4 factures signées (impossible!)

**V2**: `ROUNDUP()` → 21 factures signées

### ❌ Erreur 5: Manque de lisibilité
**V1**: Calculs directs sans étapes intermédiaires

**V2**: Lignes intermédiaires pour TJM, Durée, Montant mission

---

## Méthodologie V2: Approche par Missions

### Principe Fondamental

**Dans une société de conseil, le CA = Jours vendus × TJM**

Mais la vraie question est: **Combien de jours sont vendus chaque mois?**

### Approche Retenue: "Mission-Based Revenue"

**Logique**:
1. Les **commerciaux** signent des **missions** (pas juste du CA abstrait)
2. Chaque **mission** = durée × TJM × nb consultants
3. Le **CA mensuel** = somme des missions démarrées ce mois

### Calcul Détaillé

#### Étape 1: Calcul de l'ancienneté de chaque commercial

```excel
Ancienneté Commercial 1 en Janvier = DATEDIF(Date entrée Com1, 01/01/2026, "M") + 1
```

**Exemple**:
- Commercial 1 entré le 01/01/2026
- En janvier: Ancienneté = 1 mois
- En février: Ancienneté = 2 mois
- En mars: Ancienneté = 3 mois

- Commercial 3 entré le 01/03/2026
- En janvier: Ancienneté = 0 (pas encore arrivé)
- En février: Ancienneté = 0 (pas encore arrivé)
- En mars: Ancienneté = 1 mois
- En avril: Ancienneté = 2 mois

#### Étape 2: Application du ramp-up selon ancienneté

```excel
Nouvelles missions =
  SI(Ancienneté = 0, 0,
  SI(Ancienneté = 1, RampupM1,
  SI(Ancienneté = 2, RampupM2,
  SI(Ancienneté = 3, RampupM3,
  RampupM4Plus))))
```

**Exemple Commercial 3** (entré en mars):
- Janvier: 0 missions (pas encore là)
- Février: 0 missions (pas encore là)
- Mars: 2 missions (M1 = ramp-up mois 1)
- Avril: 4 missions (M2 = ramp-up mois 2)
- Mai: 6 missions (M3 = ramp-up mois 3)
- Juin+: 8 missions (M4+ = rythme croisière)

#### Étape 3: Transformation BC → Missions signées

```excel
Total nouvelles missions du mois = Som

me(Com1 + Com2 + Com3)
Missions signées = ROUNDUP(Total × Taux transformation, 0)
```

**Exemple**:
- Total missions = 24
- Taux transformation = 85%
- Calcul: 24 × 85% = 20,4
- **ROUNDUP(20,4) = 21 missions signées**

#### Étape 4: Calcul du CA facturé

**Lignes intermédiaires** (pour lisibilité):
```excel
TJM (référence) = 1 000 €
Durée mission = 25 jours
Montant par mission = TJM × Durée = 25 000 €
```

**CA facturé du mois**:
```excel
CA facturé = Missions signées × Montant mission
           = 21 × 25 000 €
           = 525 000 €
```

#### Étape 5: Vérification capacité production

**Capacité théorique**:
```excel
Jours ouvrés = 22
Nb consultants = 50
Capacité théorique = 50 × 22 = 1 100 jours
```

**Capacité facturable**:
```excel
TACE = 90%
Capacité facturable = 1 100 × 90% = 990 jours
CA production MAX = 990 × 1 000 € = 990 000 €
```

#### Étape 6: CA réel

```excel
CA RÉEL = MIN(CA facturé, CA production MAX)
        = MIN(525 000 €, 990 000 €)
        = 525 000 €
```

**Interprétation**:
- Demande commerciale: 525k€
- Capacité production: 990k€
- CA limité par la demande (pas la capacité)
- Taux utilisation: 525k / 990k = 53%

---

## Comparaison V1 vs V2

### Structure Hypothèses

| Élément | V1 | V2 |
|---------|----|----|
| Nb commerciaux | ✓ | ✓ |
| **Date entrée commerciaux** | ❌ | ✅ |
| Ramp-up | ✓ | ✓ |
| Taux transformation | ✓ | ✓ |
| TJM | ✓ | ✓ |
| Durée mission | ✓ | ✓ |
| Nb consultants | ✓ | ✓ |
| TACE | ✓ | ✓ |

### Calcul Ramp-up

| Aspect | V1 | V2 |
|--------|----|----|
| Base calcul | Mois calendaire | **Ancienneté commercial** |
| Commercial arrivé en mars | Fait 6 clients dès mars ❌ | Fait 2 clients en mars (M1) ✅ |
| Formule | Simple mais fausse | Correcte avec DATEDIF |
| Réalisme | Faible | Élevé |

### Calcul CA

| Étape | V1 | V2 |
|-------|----|----|
| Missions signées | 20,4 (décimal) ❌ | 21 (ROUNDUP) ✅ |
| Lignes intermédiaires | Non | **Oui** (TJM, Durée, Montant) |
| Liens formules | Parfois cassés | Tous corrects |
| Lisibilité | Moyenne | Excellente |

### Vérification Capacité

| Aspect | V1 | V2 |
|--------|----|----|
| Lien jours ouvrés | B23 incorrect ❌ | Lien correct ✅ |
| Calcul capacité | Bon | Bon |
| CA final | MIN correct | MIN correct |

---

## Exemples Concrets

### Exemple 1: Commercial 1 (entré 01/01/2026)

| Mois | Ancienneté | Ramp-up | Missions |
|------|------------|---------|----------|
| Jan | 1 | M1 | 2 |
| Fév | 2 | M2 | 4 |
| Mar | 3 | M3 | 6 |
| Avr | 4 | M4+ | 8 |
| Mai | 5 | M4+ | 8 |
| ... | ... | M4+ | 8 |

### Exemple 2: Commercial 3 (entré 01/03/2026)

| Mois | Ancienneté | Ramp-up | Missions |
|------|------------|---------|----------|
| Jan | 0 | - | **0** |
| Fév | 0 | - | **0** |
| Mar | 1 | M1 | **2** |
| Avr | 2 | M2 | **4** |
| Mai | 3 | M3 | **6** |
| Jun | 4 | M4+ | **8** |
| Jul | 5 | M4+ | **8** |

### Exemple 3: Total missions en Mars

**Avant transformation**:
- Com1: 6 missions (M3)
- Com2: 6 missions (M3)
- Com3: 2 missions (M1)
- **Total: 14 missions**

**Après transformation (85%)**:
- 14 × 85% = 11,9
- **ROUNDUP(11,9) = 12 missions signées**

**CA du mois**:
- 12 missions × 25 000€ = **300 000€**

---

## Formules Excel Clés de la V2

### 1. Calcul Ancienneté

```excel
=IF($B$5>=Com1_DateEntree,DATEDIF(Com1_DateEntree,$B$5,"M")+1,0)
```

**Explication**:
- Si date du mois ≥ date entrée commercial → calcule l'ancienneté
- Sinon → 0 (commercial pas encore arrivé)
- DATEDIF(...,"M")+1 = nombre de mois révolus + 1

### 2. Application Ramp-up

```excel
=IF(B7=0,0,
  IF(B7=1,RampupM1,
  IF(B7=2,RampupM2,
  IF(B7=3,RampupM3,
  RampupM4Plus))))
```

**Explication**:
- Si ancienneté = 0 → 0 missions
- Si ancienneté = 1 → RampupM1 (ex: 2)
- Si ancienneté = 2 → RampupM2 (ex: 4)
- Si ancienneté = 3 → RampupM3 (ex: 6)
- Sinon (≥4) → RampupM4Plus (ex: 8)

### 3. Arrondi Supérieur

```excel
=ROUNDUP(B14*B15,0)
```

**Explication**:
- B14 = Total missions (ex: 24)
- B15 = Taux transformation (ex: 85%)
- 24 × 0,85 = 20,4
- ROUNDUP(20,4, 0) = 21

### 4. Montant Mission

```excel
=B20*B21
```

Avec lignes intermédiaires:
- B20 = TJM (lié à Hypothèses)
- B21 = Durée mission (lié à Hypothèses)
- Résultat visible et traçable

### 5. Lien Jours Ouvrés (corrigé)

```excel
=Hypothèses!$B$34
```

Pour janvier (calendrier commence ligne 34 dans Hypothèses)

### 6. CA Réel

```excel
=MIN(B24,B31)
```

- B24 = CA facturé
- B31 = CA production MAX
- Prend le minimum des deux

---

## Validation de la Méthodologie

### ✅ Est-ce la bonne méthode pour calculer le CA d'une société de conseil?

**OUI**, sous réserve que:

1. **Les missions sont de durée standard** (ex: toutes ~25 jours)
   - Si très variable → il faudrait un onglet "Catalogue missions"

2. **Les missions démarrent le mois où elles sont signées**
   - Si décalage temporel → il faudrait gérer date signature vs date démarrage

3. **Le TJM est homogène**
   - Si TJM varie beaucoup (junior/senior) → il faudrait segmenter

4. **On ne suit pas le stock de missions en cours**
   - Cette version calcule les **nouvelles** missions chaque mois
   - Pour un suivi plus fin → il faudrait un backlog de missions

### 📊 Pour Quelle Taille d'Entreprise?

**Optimal pour**:
- Société de conseil de 10 à 100 consultants
- Missions relativement standardisées
- Cycle de vente court (signature → démarrage < 1 mois)
- Budget prévisionnel (pas de suivi opérationnel)

**Limites pour**:
- Très grosses ESN (>500 consultants) → besoin d'un ERP
- Missions très longues (>6 mois) → besoin de suivi projet par projet
- TJM très variables → besoin de segmentation

---

## Améliorations Futures Possibles

### Court Terme
- [ ] Ajouter un coefficient de saisonnalité
- [ ] Gérer le décalage signature → démarrage mission
- [ ] Suivre le nombre de consultants en intercontrat

### Moyen Terme
- [ ] Onglet "Backlog missions" (stock de missions en cours)
- [ ] Plusieurs profils de missions (TJM différents)
- [ ] Churn missions (% de missions qui s'arrêtent avant terme)

### Long Terme
- [ ] Suivi mission par mission (date début, date fin, consultants affectés)
- [ ] Forecast dynamique basé sur le pipeline CRM
- [ ] Intégration coûts salariaux → calcul marge

---

## Conclusion

La **Version 2** corrige tous les problèmes identifiés:

✅ Date d'entrée des commerciaux → ramp-up réaliste
✅ Ancienneté calculée avec DATEDIF
✅ Arrondi supérieur sur missions signées
✅ Liens de formules corrects
✅ Lignes intermédiaires pour lisibilité
✅ Approche par missions (conforme à la réalité conseil)

**La méthodologie est correcte** pour un budget prévisionnel de société de conseil avec missions standardisées.

Le modèle est maintenant **professionnel, réaliste et conforme aux standards Transaction Services**.
