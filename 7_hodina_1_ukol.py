


def text_statistics(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            pocet_nenula=0
            pocet_radku=0
            pocet_nejdelsi=0
            pocet_slov=0
            pocet_znaku=0

            for line in file:
                line = line.rstrip()
                if line:
                    pocet_nenula += 1
                pocet_radku += 1
                if len(line) > pocet_nejdelsi:
                    pocet_nejdelsi = len(line)
                pocet_slov += len(line.split())
                pocet_znaku += len(line)
            print(f"Soubor obsahuje {pocet_radku} řádků celkem.")
            print(f"Soubor obsahuje {pocet_nenula} neprázdných řádků.")        
            print(f"Nejdelší řádek má {pocet_nejdelsi} znaků.")
            print(f"Soubor obsahuje {pocet_slov} slov.")
            print(f"Soubor obsahuje {pocet_znaku} znaků celkem.")
            return pocet_nenula, pocet_radku, pocet_nejdelsi, pocet_slov, pocet_znaku
            
    except FileNotFoundError:
        print(f"Soubor {file_path} neexistuje.")
        return 0, 0, 0, 0, 0

file_path = input("Zadej cestu k souboru: ")
if file_path=="":
    file_path="C:\\Users\\uzivatel\\AppData\\Local\\Programs\\Microsoft VS Code\\1ukol.txt"

text_statistics(file_path)