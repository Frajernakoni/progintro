
birth_number=input("Zadej rodné číslo ve tvaru RRMMDD/XXXX:",)
def normalize(birth_number):
    birth_number=birth_number.replace("/", "")
    return birth_number
def is_valid(birth_number):
    if len(birth_number)==10 and int(birth_number)%11 ==0 and birth_number[2:4] in ["01","02","03","04","05","06","07","08","09","10","11","12","51","52","53","54","55","56","57","58","59","60","61","62"]:
        return True
    else:
        return False
def gender(birth_number):
    month = int(birth_number[2:4])

    if month > 50:
        return "Žena"
    else:
        return "Muž"
def birth_date(birth_number):
    year = int(birth_number[0:2])
    month = int(birth_number[2:4])
    day = int(birth_number[4:6])
    if month > 50:
        month -= 50
    if year < 54:
        year += 2000
    else:
        year += 1900
    return f"{day:02d}.{month:02d}.{year}"
birth_number = normalize(birth_number)
print("Rodné číslo:", birth_number,end="")
print(" Platnost:", is_valid(birth_number),end="")
print(" Pohlaví:", gender(birth_number),end="")
print(" Datum narození:", birth_date(birth_number),end="")