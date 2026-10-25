def preved_teplotu(cislo,jednotka,pozadovana_jednotka):
    if jednotka == "C":
        if pozadovana_jednotka == "F":
            return cislo * 9/5 + 32
        if pozadovana_jednotka == "K":
            return cislo + 273.15
    elif jednotka == "F":
        if pozadovana_jednotka == "C":
            return (cislo - 32) * 5/9
        if pozadovana_jednotka == "K":
            return (cislo - 32) * 5/9 + 273.15
    elif jednotka == "K":
        if pozadovana_jednotka == "C":
            return cislo - 273.15
        if pozadovana_jednotka == "F":
            return (cislo - 273.15) * 9/5 + 32
    else:        
       return("None")
       exit()

print(preved_teplotu(100, "C", "F"))   # 212.0
print(preved_teplotu(0, "K", "C"))     # -273.15
print(preved_teplotu(-40, "C", "F"))   # -40.0
print(preved_teplotu(20, "C", "X"))    # None    