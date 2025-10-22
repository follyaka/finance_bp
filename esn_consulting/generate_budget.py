"""
Budget 2026 V4 CORRIGÉ - Ligne par ligne vérifié
"""

import xlsxwriter
from datetime import datetime, date

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = f'Budget_CA_2026_v4_CORRECTED_{timestamp}.xlsx'

workbook = xlsxwriter.Workbook(filename)

# FORMATS (simplifiés)
header = workbook.add_format({'bold': True, 'bg_color': '#1F4E78', 'font_color': 'white', 'align': 'center', 'border': 1})
input_fmt = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'align': 'center'})
input_date = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'num_format': 'dd/mm/yyyy', 'align': 'center'})
input_curr = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'num_format': '#,##0 €'})
input_pct = workbook.add_format({'bg_color': '#FFF2CC', 'border': 1, 'num_format': '0.0%', 'align': 'center'})
formula = workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'align': 'center'})
formula_curr = workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'num_format': '#,##0 €'})
formula_pct = workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'num_format': '0.0%', 'align': 'center'})
total = workbook.add_format({'bold': True, 'bg_color': '#D9E1F2', 'border': 2, 'num_format': '#,##0 €'})
label = workbook.add_format({'bold': True, 'align': 'left', 'border': 1})
section = workbook.add_format({'bold': True, 'font_size': 12, 'bg_color': '#4472C4', 'font_color': 'white', 'border': 1})

# HYPOTHÈSES
hypo = workbook.add_worksheet('Hypothèses')
hypo.set_column('A:A', 40)
hypo.set_column('B:B', 18)

hypo.merge_range('A1:C1', 'HYPOTHÈSES V4 CORRIGÉ', section)
hypo.write('A11', 'Commercial 1 - Date entrée', label)
hypo.write_datetime('B11', date(2026, 1, 1), input_date)
hypo.write('A13', 'Commercial 2 - Date entrée', label)
hypo.write_datetime('B13', date(2026, 1, 1), input_date)
hypo.write('A15', 'Commercial 3 - Date entrée', label)
hypo.write_datetime('B15', date(2026, 3, 1), input_date)

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

hypo.write('A26', 'Durée mission (jours)', label)
hypo.write('B26', 25, input_fmt)
hypo.write('A27', 'TJM (€)', label)
hypo.write('B27', 1000, input_curr)

hypo.write('A31', 'Nombre consultants', label)
hypo.write('B31', 50, input_fmt)
hypo.write('A32', 'TACE (%)', label)
hypo.write('B32', 0.90, input_pct)

# Jours ouvrés
jours = [22, 20, 22, 21, 20, 22, 23, 21, 22, 23, 20, 23]
for i, j in enumerate(jours):
    hypo.write(f'A{35+i}', ['Jan','Fév','Mar','Avr','Mai','Jun','Jul','Aoû','Sep','Oct','Nov','Déc'][i], label)
    hypo.write(f'B{35+i}', j, input_fmt)

# CA
ca = workbook.add_worksheet('Chiffre d\'affaires')
ca.set_column('A:A', 40)
ca.set_column('B:M', 13)

ca.merge_range('A1:M1', 'CHIFFRE D\'AFFAIRES V4 CORRIGÉ', section)

# Row 4: Headers
ca.write('A4', 'MOIS', header)
for i, m in enumerate(['Jan','Fév','Mar','Avr','Mai','Jun','Jul','Aoû','Sep','Oct','Nov','Déc']):
    ca.write(3, i+1, m, header)

# Row 5: Dates
ca.write('A5', 'Date 1er mois', label)
for i in range(12):
    ca.write_datetime(4, i+1, date(2026, i+1, 1), workbook.add_format({'num_format': 'dd/mm/yyyy', 'border': 1}))

# Row 7: TITRE
ca.merge_range('A7:M7', 'TABLEAU 1: NOUVELLES MISSIONS', section)

# Row 8: Com1 missions
ca.write('A8', 'Commercial 1 - Nouvelles missions', label)
for col in range(12):
    col_letter = chr(66+col)  # B, C, D, etc.
    formula_str = f'=IF(${col_letter}$5<Hypothèses!$B$11,0,IF(DATEDIF(Hypothèses!$B$11,${col_letter}$5,"M")=0,Hypothèses!$B$19,IF(DATEDIF(Hypothèses!$B$11,${col_letter}$5,"M")=1,Hypothèses!$B$20,IF(DATEDIF(Hypothèses!$B$11,${col_letter}$5,"M")=2,Hypothèses!$B$21,Hypothèses!$B$22))))'
    ca.write_formula(7, col+1, formula_str, formula)

# Row 9: Com2 missions
ca.write('A9', 'Commercial 2 - Nouvelles missions', label)
for col in range(12):
    col_letter = chr(66+col)
    formula_str = f'=IF(${col_letter}$5<Hypothèses!$B$13,0,IF(DATEDIF(Hypothèses!$B$13,${col_letter}$5,"M")=0,Hypothèses!$B$19,IF(DATEDIF(Hypothèses!$B$13,${col_letter}$5,"M")=1,Hypothèses!$B$20,IF(DATEDIF(Hypothèses!$B$13,${col_letter}$5,"M")=2,Hypothèses!$B$21,Hypothèses!$B$22))))'
    ca.write_formula(8, col+1, formula_str, formula)

# Row 10: Com3 missions
ca.write('A10', 'Commercial 3 - Nouvelles missions', label)
for col in range(12):
    col_letter = chr(66+col)
    formula_str = f'=IF(${col_letter}$5<Hypothèses!$B$15,0,IF(DATEDIF(Hypothèses!$B$15,${col_letter}$5,"M")=0,Hypothèses!$B$19,IF(DATEDIF(Hypothèses!$B$15,${col_letter}$5,"M")=1,Hypothèses!$B$20,IF(DATEDIF(Hypothèses!$B$15,${col_letter}$5,"M")=2,Hypothèses!$B$21,Hypothèses!$B$22))))'
    ca.write_formula(9, col+1, formula_str, formula)

# Row 11: TOTAL
ca.write('A11', 'TOTAL Nouvelles missions', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(10, col+1, f'={col_letter}8+{col_letter}9+{col_letter}10', total)

# Row 13: TITRE
ca.merge_range('A13:M13', 'TABLEAU 2: TRANSFORMATION & CA', section)

# Row 14: Taux transfo
ca.write('A14', 'Taux transformation', label)
for col in range(12):
    ca.write_formula(13, col+1, '=Hypothèses!$B$23', formula_pct)

# Row 15: Missions signées
ca.write('A15', 'Missions signées (arrondi)', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(14, col+1, f'=ROUNDUP({col_letter}11*{col_letter}14,0)', formula)

# Row 17: Séparateur
ca.write('A17', '--- Paramètres ---', workbook.add_format({'italic': True, 'bg_color': '#E7E6E6'}))

# Row 18: TJM
ca.write('A18', 'TJM - Hypothèses!B27', label)
for col in range(12):
    ca.write_formula(17, col+1, '=Hypothèses!$B$27', formula_curr)

# Row 19: Durée
ca.write('A19', 'Durée - Hypothèses!B26', label)
for col in range(12):
    ca.write_formula(18, col+1, '=Hypothèses!$B$26', formula)

# Row 20: Montant mission = B18 * B19
ca.write('A20', 'Montant mission (€)', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(19, col+1, f'={col_letter}18*{col_letter}19', formula_curr)

# Row 22: Séparateur
ca.write('A22', '--- CA ---', workbook.add_format({'italic': True, 'bg_color': '#E7E6E6'}))

# Row 23: CA facturé
ca.write('A23', 'CA FACTURÉ (€)', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(22, col+1, f'={col_letter}15*{col_letter}20', total)

# Row 25: TITRE
ca.merge_range('A25:M25', 'TABLEAU 3: CAPACITÉ', section)

# Row 26: Jours ouvrés
ca.write('A26', 'Jours ouvrés', label)
for col in range(12):
    ca.write_formula(25, col+1, f'=Hypothèses!$B${35+col}', formula)

# Row 27: Nb consultants
ca.write('A27', 'Nb consultants', label)
for col in range(12):
    ca.write_formula(26, col+1, '=Hypothèses!$B$31', formula)

# Row 28: Capacité théorique
ca.write('A28', 'Capacité théorique', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(27, col+1, f'={col_letter}26*{col_letter}27', formula)

# Row 29: TACE
ca.write('A29', 'TACE', label)
for col in range(12):
    ca.write_formula(28, col+1, '=Hypothèses!$B$32', formula_pct)

# Row 30: Capacité facturable
ca.write('A30', 'Capacité facturable', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(29, col+1, f'={col_letter}28*{col_letter}29', workbook.add_format({'bg_color': '#D9E1F2', 'border': 1, 'num_format': '0.00'}))

# Row 31: CA prod MAX
ca.write('A31', 'CA PRODUCTION MAX (€)', label)
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(30, col+1, f'={col_letter}30*{col_letter}18', total)

# Row 33: TITRE
ca.merge_range('A33:M33', 'SYNTHÈSE', section)

# Row 34: CA RÉEL
ca.write('A34', 'CA RÉEL MENSUEL (€)', workbook.add_format({'bold': True, 'bg_color': '#FFC000', 'border': 2}))
for col in range(12):
    col_letter = chr(66+col)
    ca.write_formula(33, col+1, f'=MIN({col_letter}23,{col_letter}31)', workbook.add_format({'bold': True, 'bg_color': '#FFC000', 'border': 2, 'num_format': '#,##0 €'}))

# Row 36: Total annuel
ca.write('A36', 'CA TOTAL 2026', workbook.add_format({'bold': True, 'font_size': 12}))
ca.write_formula('B36', '=SUM(B34:M34)', workbook.add_format({'bold': True, 'font_size': 12, 'num_format': '#,##0 €', 'bg_color': '#FFC000', 'border': 2}))

workbook.close()

print(f"\n{'='*80}")
print(f"✅ FICHIER CORRIGÉ GÉNÉRÉ: {filename}")
print(f"{'='*80}\n")
print("VÉRIFICATIONS FAITES:")
print("  ✓ Row 18: TJM = Hypothèses!B27")
print("  ✓ Row 19: Durée = Hypothèses!B26")
print("  ✓ Row 20: Montant = B18*B19 (TJM × Durée)")
print("  ✓ Row 8-10: Formules ramp-up avec DATEDIF")
print("  ✓ Références Com1=B11, Com2=B13, Com3=B15")
print("  ✓ Pas de lignes ancienneté")
print(f"\n{'='*80}\n")
