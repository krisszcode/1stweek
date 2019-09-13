elso_ora = int(input("ora:"))
elso_perc = int(input("perc:"))
elso_masodperc = int(input("masodperc:"))
masodik_ora = int(input("ora:"))
masodik_perc = int(input("perc:"))
masodik_masodperc = int(input("masodperc:"))
if elso_ora > masodik_ora:
    eredm_ora = elso_ora - masodik_ora
else: eredm_ora = masodik_ora - elso_ora
if elso_perc > masodik_perc:
    eredm_perc = elso_perc - masodik_perc
else: eredm_perc = masodik_perc - elso_perc
if elso_masodperc > masodik_masodperc:
    ered_masodperc = elso_masodperc - masodik_masodperc
else: ered_masodperc = masodik_masodperc - elso_masodperc

eredm = eredm_ora * 60 * 60 + eredm_perc * 60 + ered_masodperc
print(eredm)