from pathlib import Path

# Vytvoření a zápis do souboru
with open("1ukol.txt", "w", encoding="utf-8") as file:
    file.write("ahoj.\n")
    

# Zjištění přesné cesty
cesta = Path("1ukol.txt").resolve()
print("SOUBOR JE ZDE:", cesta)