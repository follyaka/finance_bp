"""
Budget 2026 - VERSION AMÉLIORÉE
Ajouts:
- CA cumulé YTD après CA réel mensuel
- CA mensuel moyen après CA total 2026
- Nombre total de missions signées après CA total 2026
"""

import xlsxwriter
from datetime import datetime, date

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'Budget_CA_2026_ENHANCED_{timestamp}.xlsx'

workbook = xlsxwriter.Workbook(filename)

# FORMATS
header = workbook.add_format({'bold': True, 'bg_color': '#1F4E78', 'font_color': 'white', 'align': 'center', 'border': 1})
input_fmt = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'align': 'center'})
input_date = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'num_format': 'dd/mm/yyyy', 'align': 'center'})
input_curr = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'num_format': '#,##0 €'})
input_pct = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'num_format': '0.0%', 'align': 'center'})
formula = workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'align': 'center'})
formula_curr = workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'num_format': '#,##0 €'})
formula_pct = workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'num_format': '0.0%', 'align': 'center'})
total = workbook.add_format({'bold': True, 'bg_color': '#D9E1F2', 'border': 2, 'num_format': '#,##0 €'})
total_orange = workbook.add_format({'bold': True, 'bg_color': '#FFC000', 'border': 2, 'num_format': '#,##0 €', 'font_size': 12})
total_qty = workbook.add_format({'bold': True, 'bg_color': '#D9E1F2', 'border': 2, 'num_format': '#,##0'})
label = workbook.add_format({'bold': True, 'align': 'left', 'border': 1})
section = workbook.add_format({'bold': True, 'font_size': 12, 'bg_color': '#4472C4', 'font_color': 'white', 'border': 1})

# ═══════════════════════════════════════════════════════════════════════════
# HYPOTHÈSES
# ═══════════════════════════════════════════════════════════════════════════
hypo = workbook.add_worksheet('Hypothèses')
hypo.set_column('A:A', 40)
hypo.set_column('B:B', 18)

hypo.merge_range('A1:C1', 'HYPOTHÈSES - Budget 2026', section)

# Dates d'entrée commerciaux
hypo.write('A11', 'Commercial 1 - Date entrée', label)
hypo.write_datetime('B11', date(2026, 1, 1), input_date)
hypo.write('A13', 'Commercial 2 - Date entrée', label)
hypo.write_datetime('B13', date(2026, 1, 1), input_date)
hypo.write('A15', 'Commercial 3 - Date entrée', label)
hypo.write_datetime('B15', date(2026, 3, 1), input_date)

# Ramp-up
hypo.write('A19', 'Ramp-up Mois 1', label)
hypo.write('B19', 2, input_fmt)
hypo.write('A20', 'Ramp-up Mois 2', label)
hypo.write('B20', 4, input_fmt)
hypo.write('A21', 'Ramp-up Mois 3', label)
hypo.write('B21', 6, input_fmt)
hypo.write('A22', 'Ramp-up Mois 4+', label)
hypo.write('B22', 8, input_fmt)
hypo.write('A23', 'Taux transformation', label)
hypo.write('B23', 0.85, input_pct)

# Mission
hypo.write('A26', 'Durée mission (jours)', label)
hypo.write('B26', 25, input_fmt)
hypo.write('A27', 'TJM (€)', label)
hypo.write('B27', 1000, input_curr)

# Consultants
hypo.write('A31', 'Nombre de consultants', label)
hypo.write('B31', 50, input_fmt)
hypo.write('A32', 'TACE', label)
hypo.write('B32', 0.90, input_pct)

# Jours ouvrés
hypo.write('A35', 'JOURS OUVRÉS PAR MOIS', label)
jours = [22, 20, 22, 21, 20, 22, 22, 21, 22, 23, 20, 22]
months = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin',
          'Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
for i, (mois, jrs) in enumerate(zip(months, jours)):
    hypo.write(f'A{36+i}', mois, label)
    hypo.write(f'B{36+i}', jrs, input_fmt)

# ═══════════════════════════════════════════════════════════════════════════
# CHIFFRE D'AFFAIRES
# ═══════════════════════════════════════════════════════════════════════════
ca = workbook.add_worksheet("Chiffre d'affaires")
ca.set_column('A:A', 35)
ca.set_column('B:M', 15)

# Titre
ca.merge_range('A1:M1', 'CHIFFRE D\'AFFAIRES 2026 - VERSION AMÉLIORÉE', section)

# Headers mois (row 4 = index 3)
ca.write('A4', 'MOIS', header)
for i, mois in enumerate(['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 'Jul', 'Aoû', 'Sep', 'Oct', 'Nov', 'Déc']):
    ca.write(3, i+1, mois, header)

# Row 5 (index 4): Dates 1er du mois pour DATEDIF
ca.write('A5', 'Date 1er mois', label)
for i in range(12):
    ca.write_datetime(4, i+1, date(2026, i+1, 1), formula)

# ═══════════════════════════════════════════════════════════════════════════
# TABLEAU 1: NOUVELLES MISSIONS
# ═══════════════════════════════════════════════════════════════════════════
ca.write('A7', 'TABLEAU 1: NOUVELLES MISSIONS', section)

# Row 8-10 (index 7-9): Commerciaux avec ramp-up DATEDIF
commerciaux = [
    (8, 'Commercial 1 - Nouvelles missions', 'B11'),
    (9, 'Commercial 2 - Nouvelles missions', 'B13'),
    (10, 'Commercial 3 - Nouvelles missions', 'B15')
]

for row_num, desc, ref_cell in commerciaux:
    ca.write(f'A{row_num}', desc, label)
    for col in range(12):
        col_letter = chr(66 + col)  # B, C, D, ...
        formula_str = (
            f'=IF(${col_letter}$5<Hypothèses!${ref_cell},0,'
            f'IF(DATEDIF(Hypothèses!${ref_cell},${col_letter}$5,"M")=0,Hypothèses!$B$19,'
            f'IF(DATEDIF(Hypothèses!${ref_cell},${col_letter}$5,"M")=1,Hypothèses!$B$20,'
            f'IF(DATEDIF(Hypothèses!${ref_cell},${col_letter}$5,"M")=2,Hypothèses!$B$21,'
            f'Hypothèses!$B$22))))'
        )
        ca.write_formula(row_num-1, col+1, formula_str, formula)

# Row 11 (index 10): TOTAL nouvelles missions
ca.write('A11', 'TOTAL Nouvelles missions', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(10, col+1, f'={col_letter}8+{col_letter}9+{col_letter}10', total_qty)

# ═══════════════════════════════════════════════════════════════════════════
# TABLEAU 2: TRANSFORMATION & CA
# ═══════════════════════════════════════════════════════════════════════════
ca.write('A13', 'TABLEAU 2: TRANSFORMATION & CA', section)

# Row 14 (index 13): Taux transformation
ca.write('A14', 'Taux transformation', label)
for col in range(12):
    ca.write_formula(13, col+1, '=Hypothèses!$B$23', formula_pct)

# Row 15 (index 14): Missions signées (ROUNDUP)
ca.write('A15', 'Missions signées (arrondi)', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(14, col+1, f'=ROUNDUP({col_letter}11*{col_letter}14,0)', total_qty)

# Row 17-20: Paramètres mission
ca.write('A17', '--- Paramètres ---', section)

# Row 18: TJM
ca.write('A18', 'TJM - Hypothèses!B27', label)
for col in range(12):
    ca.write_formula(17, col+1, '=Hypothèses!$B$27', formula_curr)

# Row 19: Durée
ca.write('A19', 'Durée - Hypothèses!B26', label)
for col in range(12):
    ca.write_formula(18, col+1, '=Hypothèses!$B$26', formula)

# Row 20: Montant mission
ca.write('A20', 'Montant mission (€)', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(19, col+1, f'={col_letter}18*{col_letter}19', formula_curr)

# Row 22-23: CA
ca.write('A22', '--- CA ---', section)

# Row 23: CA FACTURÉ
ca.write('A23', 'CA FACTURÉ (€)', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(22, col+1, f'={col_letter}15*{col_letter}20', total)

# ═══════════════════════════════════════════════════════════════════════════
# TABLEAU 3: CAPACITÉ
# ═══════════════════════════════════════════════════════════════════════════
ca.write('A25', 'TABLEAU 3: CAPACITÉ', section)

# Row 26: Jours ouvrés
ca.write('A26', 'Jours ouvrés', label)
for col in range(12):
    ca.write_formula(25, col+1, f'=Hypothèses!$B${36+col}', formula)

# Row 27: Nb consultants
ca.write('A27', 'Nb consultants', label)
for col in range(12):
    ca.write_formula(26, col+1, '=Hypothèses!$B$31', formula)

# Row 28: Capacité théorique
ca.write('A28', 'Capacité théorique', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(27, col+1, f'={col_letter}27*{col_letter}26', formula)

# Row 29: TACE
ca.write('A29', 'TACE', label)
for col in range(12):
    ca.write_formula(28, col+1, '=Hypothèses!$B$32', formula_pct)

# Row 30: Capacité facturable
ca.write('A30', 'Capacité facturable', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(29, col+1, f'={col_letter}28*{col_letter}29', formula)

# Row 31: CA PRODUCTION MAX
ca.write('A31', 'CA PRODUCTION MAX (€)', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(30, col+1, f'={col_letter}30*{col_letter}18', total)

# ═══════════════════════════════════════════════════════════════════════════
# SYNTHÈSE
# ═══════════════════════════════════════════════════════════════════════════
ca.write('A33', 'SYNTHÈSE', section)

# Row 34: CA RÉEL MENSUEL
ca.write('A34', 'CA RÉEL MENSUEL (€)', label)
for col in range(12):
    col_letter = chr(66 + col)
    ca.write_formula(33, col+1, f'=MIN({col_letter}23,{col_letter}31)', total)

# ✨ AJOUT 1: Row 35 - CA CUMULÉ YTD (Year-to-Date)
ca.write('A35', '💰 CA CUMULÉ YTD (€)', label)
for col in range(12):
    if col == 0:
        # Janvier = B34
        ca.write_formula(34, 1, '=B34', total_orange)
    else:
        # Mois suivants = cumul précédent + mois actuel
        col_letter = chr(66 + col)
        prev_col_letter = chr(66 + col - 1)
        ca.write_formula(34, col+1, f'={prev_col_letter}35+{col_letter}34', total_orange)

# Row 37: CA TOTAL 2026
ca.write('A37', '🎯 CA TOTAL 2026', label)
ca.write_formula('B37', '=SUM(B34:M34)', total_orange)

# ✨ AJOUT 2: Row 38 - CA MENSUEL MOYEN
ca.write('A38', '📊 CA MENSUEL MOYEN', label)
ca.write_formula('B38', '=B37/12', total)

# ✨ AJOUT 3: Row 39 - NOMBRE TOTAL DE MISSIONS SIGNÉES
ca.write('A39', '📦 TOTAL MISSIONS SIGNÉES', label)
ca.write_formula('B39', '=SUM(B15:M15)', total_qty)

# ═══════════════════════════════════════════════════════════════════════════
# FERMETURE
# ═══════════════════════════════════════════════════════════════════════════
workbook.close()

print("═"*80)
print("✅ FICHIER GÉNÉRÉ AVEC SUCCÈS")
print("═"*80)
print(f"📊 Fichier: {filename}")
print()
print("📈 NOUVEAUX ÉLÉMENTS AJOUTÉS:")
print("   ✨ Row 35: CA CUMULÉ YTD (€) - Cumul du CA mois par mois")
print("   ✨ Row 38: CA MENSUEL MOYEN - Moyenne du CA sur 12 mois")
print("   ✨ Row 39: TOTAL MISSIONS SIGNÉES - Somme de toutes les missions")
print()
print("📍 EMPLACEMENT DES NOUVEAUTÉS:")
print("   • CA cumulé YTD : Juste après CA réel mensuel (row 34 → 35)")
print("   • CA mensuel moyen : Après CA total 2026 (row 37 → 38)")
print("   • Total missions : Après CA mensuel moyen (row 38 → 39)")
print("═"*80)
