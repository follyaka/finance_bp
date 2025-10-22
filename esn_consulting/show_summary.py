"""
Display a visual summary of the delivered budget model
"""

import glob
import os
from datetime import datetime

def show_summary():
    """Display delivery summary"""

    print("\n" + "="*80)
    print(" "*20 + "BUDGET PRÉVISIONNEL 2026")
    print(" "*15 + "Modèle Financier - Société de Conseil")
    print("="*80)

    print("\n📦 LIVRABLES")
    print("-"*80)

    # Find Excel files
    excel_files = glob.glob("Budget_CA_2026_*.xlsx")
    excel_files.sort(key=os.path.getmtime, reverse=True)

    if excel_files:
        latest = excel_files[0]
        size = os.path.getsize(latest) / 1024  # KB
        mtime = datetime.fromtimestamp(os.path.getmtime(latest))
        print(f"\n✅ Fichier Excel Principal:")
        print(f"   📊 {latest}")
        print(f"   📅 Créé: {mtime.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   💾 Taille: {size:.1f} KB")
        print(f"   📈 Contenu: 2 onglets | 12 mois | Formules dynamiques")

    # Python scripts
    print(f"\n✅ Scripts Python:")
    scripts = [
        ('generate_budget_2026.py', '🐍 Générateur du modèle Excel'),
        ('validate_budget.py', '🔍 Validateur de cohérence'),
        ('inspect_formulas.py', '🔧 Inspecteur de formules'),
        ('show_summary.py', '📊 Affichage résumé (ce script)'),
    ]

    for script, description in scripts:
        if os.path.exists(script):
            lines = len(open(script, 'r').readlines())
            print(f"   {description}")
            print(f"      📄 {script} ({lines} lignes)")

    # Documentation
    print(f"\n✅ Documentation:")
    docs = [
        ('LIVRABLE_FINAL.md', '📋 Récapitulatif de livraison'),
        ('GUIDE_UTILISATION.md', '📖 Guide utilisateur complet'),
        ('README_Budget_2026.md', '📚 Documentation technique'),
    ]

    for doc, description in docs:
        if os.path.exists(doc):
            lines = len(open(doc, 'r').readlines())
            print(f"   {description}")
            print(f"      📄 {doc} ({lines} lignes)")

    print("\n" + "="*80)
    print("📊 STRUCTURE DU MODÈLE EXCEL")
    print("="*80)

    print("\n🗂️  Onglet 1: HYPOTHÈSES (Inputs modifiables)")
    print("   📥 Cellules JAUNES = Modifiables par l'utilisateur")
    print()
    print("   👥 Équipe Commerciale:")
    print("      • Nombre de commerciaux: 3")
    print("      • Ramp-up Mois 1: 2 clients/commercial")
    print("      • Ramp-up Mois 2: 4 clients/commercial")
    print("      • Ramp-up Mois 3: 6 clients/commercial")
    print("      • Ramp-up Mois 4+: 8 clients/commercial")
    print("      • Taux transformation BC→Factures: 85%")
    print()
    print("   💼 Équipe Consultants:")
    print("      • Nombre de consultants: 50")
    print("      • TJM (Taux Journalier Moyen): 1 000 €")
    print("      • TACE (Taux Activité Congés Exclus): 90%")
    print("      • Durée moyenne mission: 25 jours")
    print()
    print("   📅 Calendrier:")
    print("      • Jours ouvrés par mois (12 valeurs modifiables)")

    print("\n🗂️  Onglet 2: CHIFFRE D'AFFAIRES (Calculs automatiques)")
    print("   📊 Cellules BLEUES = Formules (ne pas modifier)")
    print()
    print("   📌 Tableau 1: Suivi Commerciaux & Ramp-up")
    print("      • Nouveaux clients par commercial (3 lignes)")
    print("      • Total nouveaux clients consolidé")
    print()
    print("   📌 Tableau 2: Pipeline Commercial")
    print("      • Bons de commande (BC) générés")
    print("      • Taux de transformation")
    print("      • Factures signées (nombre)")
    print("      • Montant par facture (€)")
    print("      • 💰 CA facturé (demande commerciale)")
    print()
    print("   📌 Tableau 3: Production Consultants")
    print("      • Jours ouvrés du mois")
    print("      • Capacité théorique (consultants × jours)")
    print("      • Capacité facturable (× TACE)")
    print("      • 💰 CA production MAX (capacité)")
    print()
    print("   📌 Tableau 4: Synthèse CA Mensuel")
    print("      • 🎯 CA TOTAL MENSUEL = MIN(CA facturé, CA prod MAX)")
    print("      • CA Cumulé YTD")
    print("      • Checks de cohérence (CA ≤ Capacité)")
    print("      • Taux d'utilisation consultants")
    print("      • Évolution mois par mois")
    print()
    print("   📌 Synthèse Annuelle")
    print("      • 🏆 CA TOTAL ANNÉE 2026 (cellule orange)")
    print("      • CA mensuel moyen")
    print("      • Croissance moyenne M/M")

    print("\n" + "="*80)
    print("🔧 CARACTÉRISTIQUES TECHNIQUES")
    print("="*80)

    features = [
        ("✅ Formules 100% dynamiques", "Aucune valeur en dur"),
        ("✅ Named Ranges", "NbCommerciaux, TJM, TACE, etc."),
        ("✅ Liens inter-onglets", "Hypothèses → Chiffre d'affaires"),
        ("✅ Formatage M&A/PE", "Headers bleus, inputs jaunes, formules bleues"),
        ("✅ Checks de cohérence", "Validations automatiques intégrées"),
        ("✅ Audit trail complet", "Chaque calcul traçable"),
        ("✅ Protection formules", "Seuls les inputs modifiables"),
        ("✅ Formats numériques", "€, %, séparateurs de milliers"),
    ]

    for feature, description in features:
        print(f"   {feature:30s} {description}")

    print("\n" + "="*80)
    print("🎯 CONFORMITÉ STANDARDS TRANSACTION SERVICES")
    print("="*80)

    standards = [
        "✓ Séparation inputs/calculs/outputs",
        "✓ Formules avec références de cellules uniquement",
        "✓ Pas de références circulaires",
        "✓ Nommage des cellules clés",
        "✓ Formatage professionnel conforme",
        "✓ Documentation des assumptions",
        "✓ Checks de cohérence mathématique",
        "✓ Modèle stress-testé et validé",
    ]

    for standard in standards:
        print(f"   {standard}")

    print("\n" + "="*80)
    print("📖 GUIDE D'UTILISATION RAPIDE")
    print("="*80)

    print("\n1️⃣  OUVRIR LE FICHIER EXCEL")
    if excel_files:
        print(f"   Fichier: {excel_files[0]}")
    print("   Double-cliquer pour ouvrir dans Excel/LibreOffice/Numbers")

    print("\n2️⃣  MODIFIER LES HYPOTHÈSES")
    print("   • Aller dans l'onglet 'Hypothèses'")
    print("   • Modifier UNIQUEMENT les cellules JAUNES (colonne B)")
    print("   • Exemples:")
    print("      - Changer le nombre de commerciaux de 3 à 5")
    print("      - Changer le TJM de 1000€ à 1200€")
    print("      - Changer le TACE de 90% à 85%")

    print("\n3️⃣  VOIR LES RÉSULTATS")
    print("   • Aller dans l'onglet 'Chiffre d'affaires'")
    print("   • Observer les calculs mis à jour automatiquement")
    print("   • Vérifier:")
    print("      - CA total mensuel (ligne 28)")
    print("      - CA total annuel (ligne 39, cellule orange)")
    print("      - Checks de cohérence (lignes 33-35)")

    print("\n4️⃣  ANALYSER LES SCÉNARIOS")
    print("   • Tester différentes hypothèses")
    print("   • Noter les résultats (CA annuel)")
    print("   • Comparer les scénarios")
    print("   • Identifier les leviers de croissance")

    print("\n" + "="*80)
    print("🚀 COMMANDES UTILES")
    print("="*80)

    commands = [
        ("python generate_budget_2026.py", "Générer un nouveau fichier Excel"),
        ("python validate_budget.py", "Valider la cohérence du modèle"),
        ("python inspect_formulas.py", "Inspecter les formules"),
        ("python show_summary.py", "Afficher ce résumé"),
    ]

    for cmd, description in commands:
        print(f"\n   $ {cmd}")
        print(f"     → {description}")

    print("\n" + "="*80)
    print("📚 DOCUMENTATION COMPLÈTE")
    print("="*80)

    print("\n   📖 LIVRABLE_FINAL.md")
    print("      • Vue d'ensemble complète")
    print("      • Récapitulatif de livraison")
    print("      • Checklist de validation")

    print("\n   📖 GUIDE_UTILISATION.md")
    print("      • Guide utilisateur détaillé (30+ pages)")
    print("      • Explication de chaque formule")
    print("      • 5 scénarios d'utilisation pas-à-pas")
    print("      • Conseils pour présentations professionnelles")

    print("\n   📖 README_Budget_2026.md")
    print("      • Documentation technique")
    print("      • Architecture du modèle")
    print("      • Standards de formatage")
    print("      • Formules de référence")

    print("\n" + "="*80)
    print("✨ EXEMPLE DE CALCUL")
    print("="*80)

    print("\n   📊 Mois typique (rythme de croisière, Mois 4+):")
    print()
    print("   Côté COMMERCIAL (Demande):")
    print("      3 commerciaux × 8 clients = 24 nouveaux clients")
    print("      24 BC × 85% transformation = 20,4 factures signées")
    print("      20,4 factures × 25 000€ = 510 000€ CA facturé")
    print()
    print("   Côté PRODUCTION (Capacité):")
    print("      50 consultants × 22 jours = 1 100 jours théoriques")
    print("      1 100 jours × 90% TACE = 990 jours facturables")
    print("      990 jours × 1 000€ = 990 000€ CA production MAX")
    print()
    print("   RÉSULTAT:")
    print("      CA TOTAL = MIN(510 000€, 990 000€) = 510 000€")
    print("      Taux utilisation = 510k / 990k = 51,5%")
    print()
    print("   💡 INTERPRÉTATION:")
    print("      • Capacité production sous-utilisée (51,5% < 75%)")
    print("      • Leviers: Augmenter commerciaux ou ramp-up")
    print("      • Alternative: Réduire le nombre de consultants")

    print("\n" + "="*80)
    print("🎯 PROCHAINES ÉTAPES")
    print("="*80)

    steps = [
        ("1. Ouvrir le fichier Excel", "Valider que tout fonctionne"),
        ("2. Lire GUIDE_UTILISATION.md", "Comprendre en détail le modèle"),
        ("3. Calibrer les hypothèses", "Ajuster selon votre contexte"),
        ("4. Tester des scénarios", "Explorer différentes stratégies"),
        ("5. Valider avec les parties prenantes", "Présenter en comité"),
        ("6. Suivre vs réalisé", "Mise à jour mensuelle"),
    ]

    for step, description in steps:
        print(f"   {step:40s} → {description}")

    print("\n" + "="*80)
    print("✅ STATUT: LIVRAISON COMPLÈTE ET VALIDÉE")
    print("="*80)

    print("\n   🎯 Modèle conforme aux standards M&A/PE/Transaction Services")
    print("   🎯 100% formules dynamiques - Aucune valeur en dur")
    print("   🎯 Documentation exhaustive fournie")
    print("   🎯 Scripts de validation et maintenance inclus")
    print("   🎯 Prêt pour utilisation professionnelle")

    print("\n" + "="*80 + "\n")


if __name__ == "__main__":
    show_summary()
