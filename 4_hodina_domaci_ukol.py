i=1
pocet=0
maxi=0
maximum=0

while i!=0:
    vstup=input("Číslo (Enter pro ukončení): ")
    if vstup=="":
        break
    pocet+=1
    maxi+=int(vstup)
    if int(vstup) > maximum:
        maximum = int(vstup)
print("Počet:", pocet)
print("Maximum:", maximum)