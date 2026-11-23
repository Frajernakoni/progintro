import os
import time

NUMBER_OF_LINES=10
DEFAULT_FILE="data.txt"

filepath= ""

while not filepath:
    filepath = input("Jaký soubor se má otevřít?")
    if not filepath:
        filepath=DEFAULT_FILE 
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
            print("soubor nalezen")
    time.sleep(2)        
    except FileNotFoundError:
    
        print("soubor nenalezen zkuste znov")
        filepath= ""
print("soubor otevřen")

time.sleep(2)

while True:
    os.system("cls")
    print(f"Super editor: {filepath}")
    with open(filepath, "r", encoding="utf-8") as file:
        content = file.read()

        clean_lines=[]
        for idx, line in enumerate(content.split("\n"), start=1):
            if line:
                clean_lines.append(f"{str(idx).rjust(5)}: {line}")
        for clean_line in clean_lines[-NUMBER_OF_LINES:]:
            print(clean_line)        

    
    new_line = input("Přidej nový řádek: ")
    if new_line.startswith("\\"):
        if new_line== "\\exit":
            print("program byl ukončen uzivatelem")
            break
        elif new_line == "\\clear":
            with open(filepath, "w", encoding="utf-8") as file:
                file.write("")
    else:        
        with open(filepath, "a", encoding="utf-8") as file:
            file.write(new_line + "\n")