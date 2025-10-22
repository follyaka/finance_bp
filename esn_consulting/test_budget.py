"""
Script de test automatique du Budget V4
Vérifie les formules SANS ouvrir Excel
"""

import openpyxl
import glob
import os
from datetime import date

def test_budget_v4():
    """Test automatique complet du modèle V4"""

    # Trouver le fichier V4 le plus récent
    files = glob.glob("Budget_CA_2026_v4_FINAL_*.xlsx")
    if not files:
        print("❌ ERREUR: Aucun fichier V4 trouvé!")
        return False

    files.sort(key=os.path.getmtime, reverse=True)
    filename = files[0]

    print(f"\n{'='*80}")
    print(f"TEST AUTOMATIQUE: {filename}")
    print(f"{'='*80}\n")

    wb = openpyxl.load_workbook(filename, data_only=False)  # data_only=False pour voir les formules

    errors = []
    warnings = []
    success = []

    # ========================
    # TEST 1: Structure Hypothèses
    # ========================
    print("TEST 1: Vérification onglet Hypothèses...")

    ws_hypo = wb['Hypothèses']

    # Vérifier les cellules clés
    tests_hypo = [
        ('B11', 'Com1 date entrée'),
        ('B13', 'Com2 date entrée'),
        ('B15', 'Com3 date entrée'),
        ('B19', 'Ramp-up M1'),
        ('B20', 'Ramp-up M2'),
        ('B21', 'Ramp-up M3'),
        ('B22', 'Ramp-up M4+'),
        ('B23', 'Taux transformation'),
        ('B26', 'Durée mission'),
        ('B27', 'TJM'),
        ('B31', 'Nb consultants'),
        ('B32', 'TACE'),
    ]

    for cell_ref, description in tests_hypo:
        cell = ws_hypo[cell_ref]
        if cell.value is not None:
            success.append(f"  ✓ {cell_ref} ({description}): {cell.value}")
        else:
            errors.append(f"  ✗ {cell_ref} ({description}): VIDE!")

    # ========================
    # TEST 2: Formules Ramp-up
    # ========================
    print("\nTEST 2: Vérification formules ramp-up...")

    ws_ca = wb["Chiffre d'affaires"]

    # Test formule Commercial 1, Janvier (B7)
    cell_b7 = ws_ca['B7']
    formula_b7 = cell_b7.value if isinstance(cell_b7.value, str) else str(cell_b7.value)

    if formula_b7 and formula_b7.startswith('='):
        # Vérifier que la formule contient les bonnes références
        checks = [
            ('Hypothèses!$B$11' in formula_b7, 'Référence date Com1'),
            ('Hypothèses!$B$19' in formula_b7, 'Référence Ramp M1'),
            ('Hypothèses!$B$20' in formula_b7, 'Référence Ramp M2'),
            ('Hypothèses!$B$21' in formula_b7, 'Référence Ramp M3'),
            ('Hypothèses!$B$22' in formula_b7, 'Référence Ramp M4+'),
            ('DATEDIF' in formula_b7, 'Utilise DATEDIF'),
            ('$B$4' in formula_b7, 'Référence date du mois'),
        ]

        for condition, desc in checks:
            if condition:
                success.append(f"  ✓ B7: {desc}")
            else:
                errors.append(f"  ✗ B7: Manque {desc}")

        # Afficher la formule pour vérification visuelle
        print(f"\n  Formule B7 (Com1, Jan):")
        print(f"  {formula_b7[:100]}...")

    else:
        errors.append(f"  ✗ B7: Pas de formule trouvée!")

    # Test formule Commercial 3, Mars (D9) - doit donner 2 missions
    cell_d9 = ws_ca['D9']
    formula_d9 = cell_d9.value if isinstance(cell_d9.value, str) else str(cell_d9.value)

    if formula_d9 and formula_d9.startswith('='):
        if 'Hypothèses!$B$15' in formula_d9:
            success.append(f"  ✓ D9: Référence date Com3 (B15)")
        else:
            errors.append(f"  ✗ D9: Ne référence PAS B15 pour Com3!")

        print(f"\n  Formule D9 (Com3, Mars):")
        print(f"  {formula_d9[:100]}...")

    # ========================
    # TEST 3: Références Cellules Critiques
    # ========================
    print("\nTEST 3: Vérification références critiques...")

    # B20 (Montant mission janvier) - DOIT pointer vers B18*B19
    cell_b20 = ws_ca['B20']
    formula_b20 = cell_b20.value if isinstance(cell_b20.value, str) else str(cell_b20.value)

    if formula_b20 and formula_b20.startswith('='):
        if 'B18' in formula_b20 and 'B19' in formula_b20:
            success.append(f"  ✓ B20: Pointe vers B18*B19 (TJM*Durée)")
            print(f"\n  Formule B20: {formula_b20}")
        else:
            errors.append(f"  ✗ B20: Ne pointe PAS vers B18*B19!")
            print(f"\n  ❌ Formule B20: {formula_b20}")

    # B18 (TJM janvier) - DOIT être =Hypothèses!$B$27
    cell_b18 = ws_ca['B18']
    formula_b18 = cell_b18.value if isinstance(cell_b18.value, str) else str(cell_b18.value)

    if formula_b18 == '=Hypothèses!$B$27':
        success.append(f"  ✓ B18: =Hypothèses!$B$27 (TJM)")
    else:
        errors.append(f"  ✗ B18: Formule incorrecte: {formula_b18}")

    # B19 (Durée janvier) - DOIT être =Hypothèses!$B$26
    cell_b19 = ws_ca['B19']
    formula_b19 = cell_b19.value if isinstance(cell_b19.value, str) else str(cell_b19.value)

    if formula_b19 == '=Hypothèses!$B$26':
        success.append(f"  ✓ B19: =Hypothèses!$B$26 (Durée)")
    else:
        errors.append(f"  ✗ B19: Formule incorrecte: {formula_b19}")

    # ========================
    # TEST 4: Liens Jours Ouvrés
    # ========================
    print("\nTEST 4: Vérification jours ouvrés...")

    # B27 (Jours ouvrés janvier) - DOIT être =Hypothèses!$B$35
    cell_b27 = ws_ca['B27']
    formula_b27 = cell_b27.value if isinstance(cell_b27.value, str) else str(cell_b27.value)

    if formula_b27 == '=Hypothèses!$B$35':
        success.append(f"  ✓ B27: =Hypothèses!$B$35 (Jours ouvrés Jan)")
    else:
        errors.append(f"  ✗ B27: Formule incorrecte: {formula_b27}")

    # C27 (Jours ouvrés février) - DOIT être =Hypothèses!$B$36
    cell_c27 = ws_ca['C27']
    formula_c27 = cell_c27.value if isinstance(cell_c27.value, str) else str(cell_c27.value)

    if formula_c27 == '=Hypothèses!$B$36':
        success.append(f"  ✓ C27: =Hypothèses!$B$36 (Jours ouvrés Fév)")
    else:
        errors.append(f"  ✗ C27: Formule incorrecte: {formula_c27}")

    # ========================
    # TEST 5: Structure Tableau 1
    # ========================
    print("\nTEST 5: Structure Tableau 1...")

    # Vérifier qu'il n'y a PAS de lignes "ancienneté"
    label_b6 = ws_ca['A6'].value
    label_b7 = ws_ca['A7'].value
    label_b8 = ws_ca['A8'].value
    label_b9 = ws_ca['A9'].value

    if 'Ancienneté' in str(label_b7):
        errors.append(f"  ✗ Ligne 7 contient 'Ancienneté' - DOIT être supprimée!")
    else:
        success.append(f"  ✓ Pas de ligne 'Ancienneté' (simplifié)")

    if 'Commercial 1 - Nouvelles missions' in str(label_b7):
        success.append(f"  ✓ Ligne 7: Commercial 1 - Nouvelles missions")
    else:
        errors.append(f"  ✗ Ligne 7: Label incorrect: {label_b7}")

    # ========================
    # RÉSUMÉ
    # ========================
    print(f"\n{'='*80}")
    print("RÉSUMÉ DES TESTS")
    print(f"{'='*80}\n")

    print(f"✅ SUCCÈS ({len(success)}):")
    for s in success[:10]:  # Afficher les 10 premiers
        print(s)
    if len(success) > 10:
        print(f"  ... et {len(success) - 10} autres")

    if warnings:
        print(f"\n⚠️  AVERTISSEMENTS ({len(warnings)}):")
        for w in warnings:
            print(w)

    if errors:
        print(f"\n❌ ERREURS ({len(errors)}):")
        for e in errors:
            print(e)
        print(f"\n{'='*80}")
        print("STATUT: ❌ ÉCHEC - CORRECTIONS NÉCESSAIRES")
        print(f"{'='*80}\n")
        return False
    else:
        print(f"\n{'='*80}")
        print("STATUT: ✅ TOUS LES TESTS PASSÉS")
        print(f"{'='*80}\n")
        print("Le fichier est prêt à être livré!")
        return True


if __name__ == "__main__":
    success = test_budget_v4()
    exit(0 if success else 1)
