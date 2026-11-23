from datetime import datetime
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
def add(text):

    try:
        with open(file_path, "a",encoding="utf-8") as file:
             file.write(f"{timestamp} | {text}\n")
             
             return("text",text,"byl přidán do",file_path) 
             
    except FileNotFoundError:
            print(f"Soubor {file_path} neexistuje.")
            return        

def list():
    try:
         with open(file_path,"r",encoding="utf-8") as file:
              content = file.read()
              if content.strip() == "":
                  return("soubor je prázdný")
              else:
                  return content
    except FileNotFoundError:
            print(f"Soubor {file_path} neexistuje.")
            return 

def search():
    try:
             with open(file_path,"r",encoding="utf-8") as file:
                    content = file.read()
                    if content.strip() == "":
                        return("soubor je prázdný")
                    else:
                        hledany_text = input("Zadej hledaný text: ")
                        if hledany_text in content:
                            return(f"Hledaný text '{hledany_text}' byl nalezen.")
                        else:
                            return(f"Hledaný text '{hledany_text}' nebyl nalezen.")
        except FileNotFoundError:
                print(f"Soubor {file_path} neexistuje.")
                return

file_path="C:\\Users\\uzivatel\\Desktop\\Škola\\základy programování\\journal.txt"


print("v souboru je:",list())
spustit=input("Chceš přidat poznámku? (Y/n): ")
if spustit == "Y":
    print(add(input("Zadej poznámku:")))
